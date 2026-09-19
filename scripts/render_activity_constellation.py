#!/usr/bin/env python3
"""Render a public GitHub contribution calendar as an animated engineering constellation."""

from __future__ import annotations

import argparse
import html
import re
import urllib.request
from datetime import date, timedelta
from pathlib import Path


WIDTH = 1200
HEIGHT = 326
GRID_X = 54
GRID_Y = 110
CELL = 11
GAP = 5
WEEKS = 53
DAYS = 7

LEVEL_COLORS = {
    0: "#111c2b",
    1: "#22637b",
    2: "#4b93a5",
    3: "#79c6d2",
    4: "#c9fbff",
}


def fetch_public_contributions(username: str, start: date, end: date) -> dict[date, tuple[int, int]]:
    """Read only the contribution data already visible on the public profile."""
    result: dict[date, tuple[int, int]] = {}
    cell_pattern = re.compile(
        r'<td\b(?P<attrs>[^>]*\bdata-date="(?P<date>\d{4}-\d{2}-\d{2})"[^>]*)></td>'
        r'\s*<tool-tip\b[^>]*>(?P<label>.*?)</tool-tip>',
        re.IGNORECASE | re.DOTALL,
    )

    for year in range(start.year, end.year + 1):
        url = (
            f"https://github.com/users/{username}/contributions"
            f"?from={year}-01-01&to={year}-12-31"
        )
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": f"{username}-activity-constellation",
                "Accept": "text/html",
            },
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            markup = response.read().decode("utf-8")

        for match in cell_pattern.finditer(markup):
            day = date.fromisoformat(match.group("date"))
            if not start <= day <= end:
                continue
            level_match = re.search(r'\bdata-level="([0-4])"', match.group("attrs"))
            level = int(level_match.group(1)) if level_match else 0
            label = html.unescape(re.sub(r"<[^>]+>", "", match.group("label"))).strip()
            count_match = re.search(r"([\d,]+)\s+contributions?", label, re.IGNORECASE)
            count = int(count_match.group(1).replace(",", "")) if count_match else 0
            result[day] = (count, level)

    return result


def streaks(days: list[tuple[date, int, int]]) -> tuple[int, int]:
    longest = 0
    run = 0
    for _, count, _ in days:
        if count:
            run += 1
            longest = max(longest, run)
        else:
            run = 0

    current = 0
    for _, count, _ in reversed(days):
        if count:
            current += 1
        else:
            break
    return longest, current


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def contribution_light(count: int, maximum: int) -> tuple[str, float]:
    """Count-based, monotonically brighter RGB and halo strength; zero stays dark."""
    if count <= 0:
        return LEVEL_COLORS[0], 0.0
    strength = count / max(maximum, count)
    low, high = (24, 83, 110), (201, 251, 255)
    rgb = tuple(round(a + (b - a) * strength) for a, b in zip(low, high))
    return '#' + ''.join(f'{value:02x}' for value in rgb), 0.12 + 0.78 * strength


def scan_timeline(days: list[tuple[date, int, int]]) -> tuple[list[float], float, float]:
    """Visit every date chronologically, slowing down on contribution days."""
    active = sum(count > 0 for _, count, _ in days)
    dwell = min(0.55, 18.0 / max(active, 1))
    elapsed = 0.35
    arrivals = []
    for _, count, _ in days:
        arrivals.append(elapsed)
        elapsed += dwell if count else 0.014
    fade_start = elapsed + 2.4  # Hold the completed constellation before resetting.
    return arrivals, fade_start, fade_start + 0.8


def render(username: str, today: date, activity: dict[date, tuple[int, int]]) -> str:
    sunday_offset = (today.weekday() + 1) % 7
    current_week = today - timedelta(days=sunday_offset)
    start = current_week - timedelta(weeks=WEEKS - 1)

    days: list[tuple[date, int, int]] = []
    for offset in range((today - start).days + 1):
        day = start + timedelta(days=offset)
        count, level = activity.get(day, (0, 0))
        days.append((day, count, level))

    total = sum(count for _, count, _ in days)
    active_days = sum(1 for _, count, _ in days if count)
    longest, current = streaks(days)

    month_labels: list[tuple[int, str]] = []
    last_month = None
    for column in range(WEEKS):
        week_start = start + timedelta(weeks=column)
        probe = week_start + timedelta(days=3)
        if probe.month != last_month:
            month_labels.append((column, probe.strftime("%b").upper()))
            last_month = probe.month

    maximum = max((count for _, count, _ in days), default=0)
    arrivals, fade_start, duration = scan_timeline(days)
    dark = LEVEL_COLORS[0]
    cells: list[str] = []
    static_cells: list[str] = []
    halos: list[str] = []
    for column in range(WEEKS):
        for row in range(DAYS):
            day = start + timedelta(weeks=column, days=row)
            count, level = activity.get(day, (0, 0)) if day <= today else (0, 0)
            x = GRID_X + column * (CELL + GAP)
            y = GRID_Y + row * (CELL + GAP)
            color, strength = contribution_light(count, maximum)
            label = f"{count} contribution{'s' if count != 1 else ''} on {day.isoformat()}"
            animation = ""
            if count:
                arrival = arrivals[column * DAYS + row]
                times = ';'.join(f'{t / duration:.6f}' for t in
                                 (0, arrival, arrival + 0.04, fade_start, duration))
                animation = (
                    f'<animate attributeName="fill" values="{dark};{dark};{color};{color};{dark}" '
                    f'keyTimes="{times}" dur="{duration:.6f}s" repeatCount="indefinite"/>'
                )
                halos.append(
                    f'<rect x="{x - 2}" y="{y - 2}" width="{CELL + 4}" height="{CELL + 4}" '
                    f'rx="4" fill="{color}" filter="url(#glow)" opacity="0">'
                    f'<animate attributeName="opacity" values="0;0;{strength:.6f};{strength:.6f};0" '
                    f'keyTimes="{times}" dur="{duration:.6f}s" repeatCount="indefinite"/></rect>'
                )
            cells.append(
                f'<g><title>{esc(label)}</title>'
                f'<rect data-date="{day}" data-count="{count}" x="{x}" y="{y}" '
                f'width="{CELL}" height="{CELL}" rx="2" fill="{dark}">{animation}</rect></g>'
            )
            static_cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{color}"/>'
            )

    # One subtle outline visits individual cells, not weekly column averages.
    positions = [(GRID_X + (i // DAYS) * (CELL + GAP) - 2,
                  GRID_Y + (i % DAYS) * (CELL + GAP) - 2) for i in range(len(days))]
    cursor_times = ';'.join(f'{t / duration:.6f}' for t in [0, *arrivals, duration])
    cursor_positions = [positions[0], *positions, positions[-1]]
    cursor_x = ';'.join(str(x) for x, _ in cursor_positions)
    cursor_y = ';'.join(str(y) for _, y in cursor_positions)

    labels = "".join(
        f'<text x="{GRID_X + column * (CELL + GAP)}" y="{GRID_Y - 17}" class="month">{label}</text>'
        for index, (column, label) in enumerate(month_labels)
        if GRID_X + column * (CELL + GAP) < 910
        and (index + 1 == len(month_labels) or month_labels[index + 1][0] - column >= 3)
    )

    current_text = f"{current} day{'s' if current != 1 else ''}" if current else "ready"
    title = f"{username.upper()} / ACTIVITY CONSTELLATION"
    description = (
        f"Animated public contribution calendar for {username}: {total} contributions, "
        f"{active_days} active days, longest streak {longest} days. "
        "Days are visited in chronological order; only contribution days light up. "
        "More contributions produce brighter cubes. The completed grid holds, then resets."
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">{esc(title)}</title>
  <desc id="desc">{esc(description)}</desc>
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07111f"/>
      <stop offset="0.58" stop-color="#081525"/>
      <stop offset="1" stop-color="#0b1020"/>
    </linearGradient>
    <linearGradient id="signal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#22d3ee" stop-opacity="0"/>
      <stop offset="0.45" stop-color="#38bdf8"/>
      <stop offset="0.76" stop-color="#a78bfa"/>
      <stop offset="1" stop-color="#fde68a" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#38bdf8" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#67e8f9" stop-opacity="0.16"/>
      <stop offset="1" stop-color="#38bdf8" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="core">
      <stop offset="0" stop-color="#f8fdff"/>
      <stop offset="0.22" stop-color="#67e8f9"/>
      <stop offset="0.58" stop-color="#38bdf8" stop-opacity="0.5"/>
      <stop offset="1" stop-color="#38bdf8" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-200%" y="-200%" width="400%" height="400%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="microgrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M24 0H0V24" fill="none" stroke="#163047" stroke-width="0.7" opacity="0.28"/>
    </pattern>
    <style>
      text {{ font-family: "Segoe UI", Inter, Arial, sans-serif; }}
      .eyebrow {{ fill:#67e8f9; font-size:12px; font-weight:700; letter-spacing:2.4px; }}
      .headline {{ fill:#edf8ff; font-size:23px; font-weight:700; letter-spacing:0.4px; }}
      .sub {{ fill:#86a6ba; font-size:12px; letter-spacing:0.6px; }}
      .month {{ fill:#66869c; font-size:10px; font-weight:600; letter-spacing:1px; }}
      .metric {{ fill:#eaf8ff; font-size:21px; font-weight:700; }}
      .metric-label {{ fill:#6f91a7; font-size:9px; font-weight:600; letter-spacing:1.1px; }}
      .footer {{ fill:#9bb7c8; font-size:12px; }}
      .mono {{ fill:#5b7f97; font-family: Consolas, monospace; font-size:9px; letter-spacing:1px; }}
      .static-grid {{ display:none; }}
      @media (prefers-reduced-motion: reduce) {{
        .animated-grid, .orbital-motion {{ display:none; }}
        .static-grid {{ display:inline; }}
      }}
    </style>
  </defs>

  <rect x="1" y="1" width="{WIDTH - 2}" height="{HEIGHT - 2}" rx="22" fill="url(#panel)" stroke="#1e3b51"/>
  <rect x="1" y="1" width="{WIDTH - 2}" height="{HEIGHT - 2}" rx="22" fill="url(#microgrid)" opacity="0.38"/>
  <path d="M28 78H1172" stroke="#19364b" stroke-width="1"/>

  <g transform="translate(54 31)">
    <rect width="34" height="34" rx="9" fill="#0b2033" stroke="#38bdf8"/>
    <path d="M10 23V11M10 17L18 10M10 17L19 25M23 10h3" fill="none" stroke="#67e8f9" stroke-width="2.4" stroke-linecap="round"/>
    <circle cx="27" cy="9" r="2.2" fill="#fde68a"/>
  </g>
  <text x="103" y="43" class="eyebrow">{esc(username.upper())} / PUBLIC BUILD SIGNAL</text>
  <text x="103" y="65" class="headline">ACTIVITY CONSTELLATION</text>

  <g transform="translate(870 28)">
    <text x="0" y="19" class="metric">{total}</text>
    <text x="0" y="36" class="metric-label">CONTRIBUTIONS</text>
    <path d="M88 2V42" stroke="#1a3c54"/>
    <text x="108" y="19" class="metric">{active_days}</text>
    <text x="108" y="36" class="metric-label">ACTIVE DAYS</text>
    <path d="M184 2V42" stroke="#1a3c54"/>
    <text x="204" y="19" class="metric">{longest}</text>
    <text x="204" y="36" class="metric-label">LONGEST STREAK</text>
  </g>

  {labels}
  <g class="static-grid">{"".join(static_cells)}</g>
  <g class="animated-grid">
    {"".join(halos)}
    {"".join(cells)}
    <rect id="day-cursor" x="{positions[0][0]}" y="{positions[0][1]}" width="{CELL + 4}" height="{CELL + 4}"
          rx="3" fill="none" stroke="#68899e" stroke-width="0.8" opacity="0.65">
      <animate attributeName="x" values="{cursor_x}" keyTimes="{cursor_times}" calcMode="discrete" dur="{duration:.6f}s" repeatCount="indefinite"/>
      <animate attributeName="y" values="{cursor_y}" keyTimes="{cursor_times}" calcMode="discrete" dur="{duration:.6f}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.65;0.65;0;0" keyTimes="0;{(fade_start - 2.4) / duration:.6f};{(fade_start - 2.2) / duration:.6f};1" dur="{duration:.6f}s" repeatCount="indefinite"/>
    </rect>
  </g>

  <g class="orbital-motion" transform="translate(965 106)">
    <circle cx="86" cy="52" r="49" fill="none" stroke="#19425d" stroke-width="1"/>
    <circle cx="86" cy="52" r="36" fill="none" stroke="#216286" stroke-width="1" stroke-dasharray="3 7">
      <animateTransform attributeName="transform" type="rotate" from="0 86 52" to="360 86 52" dur="18s" repeatCount="indefinite"/>
    </circle>
    <path d="M29 79L86 52L137 21M45 17L86 52L143 77" fill="none" stroke="#245b7b" stroke-width="1"/>
    <circle cx="29" cy="79" r="3" fill="#38bdf8"/>
    <circle cx="45" cy="17" r="3" fill="#a78bfa"/>
    <circle cx="137" cy="21" r="3" fill="#fde68a"/>
    <circle cx="143" cy="77" r="3" fill="#67e8f9"/>
    <circle cx="86" cy="52" r="27" fill="url(#core)" opacity="0.85">
      <animate attributeName="r" values="23;29;23" dur="3.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.58;0.95;0.58" dur="3.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="86" cy="52" r="5" fill="#f8fdff"/>
    <text x="86" y="119" text-anchor="middle" class="mono">SYSTEM / {esc(current_text.upper())}</text>
  </g>

  <path d="M54 245H1146" stroke="#19364b" stroke-width="1"/>
  <text x="54" y="278" class="footer">One day at a time. More contributions, brighter cubes.</text>
  <text x="54" y="298" class="mono">{esc(start.isoformat())}  →  {esc(today.isoformat())}</text>

  <g transform="translate(821 270)">
    <text x="0" y="10" class="mono">LOW → HIGH COUNT</text>
    <rect x="128" y="0" width="11" height="11" rx="3" fill="{LEVEL_COLORS[0]}"/>
    <rect x="146" y="0" width="11" height="11" rx="3" fill="{LEVEL_COLORS[1]}"/>
    <rect x="164" y="0" width="11" height="11" rx="3" fill="{LEVEL_COLORS[2]}"/>
    <rect x="182" y="0" width="11" height="11" rx="3" fill="{LEVEL_COLORS[3]}"/>
    <rect x="200" y="0" width="11" height="11" rx="3" fill="{LEVEL_COLORS[4]}"/>
  </g>
</svg>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--date", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()

    sunday_offset = (args.date.weekday() + 1) % 7
    current_week = args.date - timedelta(days=sunday_offset)
    start = current_week - timedelta(weeks=WEEKS - 1)
    activity = fetch_public_contributions(args.user, start, args.date)
    svg = render(args.user, args.date, activity)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
