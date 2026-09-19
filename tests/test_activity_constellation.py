import importlib.util
from datetime import date, timedelta
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

spec = importlib.util.spec_from_file_location(
    'constellation', Path(__file__).resolve().parents[1] / 'scripts/render_activity_constellation.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
NS = {'s': 'http://www.w3.org/2000/svg'}


class ActivityTests(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 9, 19)
        self.activity = {self.today - timedelta(days=2): (1, 1),
                         self.today - timedelta(days=1): (5, 2), self.today: (20, 4)}
        self.root = ET.fromstring(module.render('KhaiFaw', self.today, self.activity))
        self.cells = self.root.findall('.//s:rect[@data-date]', NS)

    def test_only_real_contribution_days_animate(self):
        self.assertEqual(len(self.cells), 371)
        for cell in self.cells:
            self.assertEqual(cell.find('s:animate', NS) is not None, int(cell.attrib['data-count']) > 0)

    def test_same_week_days_light_separately_in_date_order(self):
        arrivals = []
        for cell in self.cells:
            animation = cell.find('s:animate', NS)
            if animation is not None:
                times = [float(v) for v in animation.attrib['keyTimes'].split(';')]
                self.assertEqual(times, sorted(times))
                arrivals.append(times[1])
        self.assertEqual(len(arrivals), 3)
        self.assertTrue(all(a < b for a, b in zip(arrivals, arrivals[1:])))

    def test_count_controls_brightness_and_halo_monotonically(self):
        values = [module.contribution_light(n, 40) for n in range(41)]
        luminances = [sum(int(color[i:i+2], 16) * weight for i, weight in
                          zip((1, 3, 5), (.2126, .7152, .0722))) for color, _ in values]
        self.assertTrue(all(a < b for a, b in zip(luminances, luminances[1:])))
        self.assertTrue(all(a[1] < b[1] for a, b in zip(values, values[1:])))

    def test_cursor_arrivals_match_cell_reveal_times(self):
        cursor = self.root.find('.//s:rect[@id="day-cursor"]/s:animate', NS)
        arrivals = set(cursor.attrib['keyTimes'].split(';'))
        for cell in self.cells:
            animation = cell.find('s:animate', NS)
            if animation is not None:
                self.assertIn(animation.attrib['keyTimes'].split(';')[1], arrivals)
                colors = animation.attrib['values'].split(';')
                self.assertEqual(colors[0], colors[-1])
                self.assertEqual(colors[2], colors[3])  # Remains lit until global fade.

    def test_empty_calendar_stays_dark(self):
        root = ET.fromstring(module.render('Empty', self.today, {}))
        self.assertEqual(len(root.findall('.//s:rect[@data-date]/s:animate', NS)), 0)
        self.assertIn('0 contributions', root.find('s:desc', NS).text)

    def test_dense_year_has_nonoverlapping_arrivals_and_hold(self):
        days = [(self.today - timedelta(days=370-i), 1, 1) for i in range(371)]
        arrivals, fade_start, duration = module.scan_timeline(days)
        self.assertTrue(all(b - a > .04 for a, b in zip(arrivals, arrivals[1:])))
        self.assertGreater(fade_start - arrivals[-1], 2.4)
        self.assertLess(duration, 25)

    def test_future_days_are_not_lit_and_reduced_motion_exists(self):
        future = self.today + timedelta(days=1)
        root = ET.fromstring(module.render('Test', self.today, {future: (99, 4)}))
        self.assertEqual(len(root.findall('.//s:rect[@data-date]/s:animate', NS)), 0)
        self.assertIn('prefers-reduced-motion', root.find('.//s:style', NS).text)


if __name__ == '__main__':
    unittest.main()
