<p align="center">
  <img src="assets/portfolio-constellation.gif" width="100%" alt="Khairul Fawwaz — Engineering intelligence. Animated constellation connecting firmware, Edge AI, automation, IoT and software.">
</p>

<p align="center">
  <strong>Mechatronic Engineering graduate · Universiti Sains Malaysia</strong><br>
  Building where physical systems, software and intelligence meet.
</p>

<p align="center">
  <a href="#01--on-device-acoustic-intelligence"><img src="https://img.shields.io/badge/01-FLAGSHIP_FYP-52dcff?style=for-the-badge&amp;labelColor=07111f" alt="01 — Explore my flagship acoustic FYP"></a>
  <a href="#02--pc-platform-validation"><img src="https://img.shields.io/badge/02-PLATFORM_VALIDATION-66e3cf?style=for-the-badge&amp;labelColor=07111f" alt="02 — PC platform validation"></a>
  <a href="#03--manufacturing-data-intelligence"><img src="https://img.shields.io/badge/03-DATA_INTELLIGENCE-f2c94c?style=for-the-badge&amp;labelColor=07111f" alt="03 — Manufacturing data intelligence"></a>
  <a href="#04--local-first-windows-software"><img src="https://img.shields.io/badge/04-NATIVE_SOFTWARE-a78bfa?style=for-the-badge&amp;labelColor=07111f" alt="04 — Native Windows software"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/khairulfawwaz">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://github.com/KhaiFaw?tab=repositories">All repositories</a>
</p>

<p align="center">
  <img src="assets/signal-to-software.svg" width="100%" alt="From physical systems to intelligent software — an animated journey through sensing, processing, inference and delivery">
</p>

I'm **Fawwaz**, a Mechatronic Engineering graduate from **USM**. I work across microcontroller firmware, signal processing, on-device machine learning and practical engineering software. I enjoy connecting the pieces: a physical signal, a constrained device, a useful interface—and a clear way to test the result.

My **final-year acoustic detection project** is the starting point. The projects below extend that foundation into platform validation, manufacturing analytics and native Windows applications.

## Selected work

### 01 / On-device acoustic intelligence

<table>
  <tr>
    <td width="56%" valign="top">
      <h3>Listening at the edge.</h3>
      <p><strong>Final-year project · Embedded Edge AI</strong></p>
      <p>Recognising six domestic sound categories directly on a <strong>Renesas RA8P1 Titan Board</strong>, without cloud inference.</p>
      <p>Microphone capture → MFCC, delta and delta-delta features → INT8 CNN → confidence-gated alerts. An application-layer firmware snapshot connects signal processing with on-device inference and a later LCD extension.</p>
      <p><code>C/C++</code> <code>RT-Thread</code> <code>CMSIS-DSP</code> <code>TFLM</code></p>
      <p><a href="https://github.com/KhaiFaw/ai-acoustic-event-detection"><strong>Explore the FYP →</strong></a><br>
      <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection/blob/main/firmware/src/hal_entry.c">Core firmware</a> · <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection/blob/main/docs/images/confusion-matrix.png">Evaluation figure</a></p>
    </td>
    <td width="44%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection/blob/main/docs/images/system-pipeline.png"><img src="assets/acoustic-signal.svg" width="100%" alt="Animated FYP architecture: microphone capture, MFCC features, INT8 inference and confidence-gated alerts. Illustration, not live data."></a>
      <p><sub>THE FLAGSHIP / SIGNAL → DECISION</sub></p>
    </td>
  </tr>
</table>

| Sound classes | Feature input | Embedded model | Historical board evaluation |
|:---:|:---:|:---:|:---:|
| **6** | **39 × 61** | **114.39 KiB** · INT8 | **14 / 16** windows |

<sub>Embedded prototype. The small historical split demonstrates feasibility, not broad reliability. A model-quantization correction is under <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection/pull/1">draft review</a> and still needs board validation.</sub>

<br><br>

### 02 / PC platform validation

<table>
  <tr>
    <td width="44%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/pc-platform-validation-toolkit/blob/main/examples/measured/report.md"><img src="https://raw.githubusercontent.com/KhaiFaw/pc-platform-validation-toolkit/main/docs/images/measured-report.png" width="100%" alt="Real PC validation report with explicit PASS, WARN and SKIP outcomes"></a>
      <p><sub>ACTIVE BUILD / REQUIREMENTS → EVIDENCE</sub></p>
    </td>
    <td width="56%" valign="top">
      <h3>Test the system. Keep the evidence.</h3>
      <p><strong>Functional MVP · Continued development</strong></p>
      <p>A requirements-based CLI for bounded CPU, memory and temporary-storage checks, capability discovery and telemetry.</p>
      <p>Preserves runs in SQLite and JSON, Markdown and HTML reports. Compatible baselines support regression comparisons; a labelled fault-injection demo exercises the failure path.</p>
      <p><code>Python</code> <code>C++20</code> <code>pytest</code> <code>SQLite</code></p>
      <p><a href="https://github.com/KhaiFaw/pc-platform-validation-toolkit"><strong>Inspect the toolkit →</strong></a><br>
      <a href="https://github.com/KhaiFaw/pc-platform-validation-toolkit/blob/main/docs/final-verification.md">Verification scope</a> · <a href="https://github.com/KhaiFaw/pc-platform-validation-toolkit/blob/main/examples/measured/report.md">Measured report</a> · <a href="https://github.com/KhaiFaw/pc-platform-validation-toolkit/blob/main/examples/injected/report.md">Failure demo</a></p>
    </td>
  </tr>
</table>

| Automated tests | CI platforms | Captured run | Development stage |
|:---:|:---:|:---:|:---:|
| **66** | **Windows + Ubuntu** | **7 PASS · 1 WARN · 1 SKIP** | **0.1.0.dev0** |

<sub>Missing native or sensor capabilities are reported explicitly. Captured results describe one local run, not hardware certification or a benchmark ranking.</sub>

<br><br>

### 03 / Manufacturing data intelligence

<table>
  <tr>
    <td width="56%" valign="top">
      <h3>From tester data to engineering insight.</h3>
      <p><strong>SQL + Power BI · Synthetic-data demonstration</strong></p>
      <p>Turn <strong>8,000 deliberately messy synthetic tester records</strong> into a validated PostgreSQL model and an interactive Power BI dashboard.</p>
      <p>Preserve the raw source, clean and quarantine records, then expose reusable views for yield trends, failure analysis and station performance.</p>
      <p><code>PostgreSQL</code> <code>SQL</code> <code>Power BI</code> <code>Python</code></p>
      <p><a href="https://github.com/KhaiFaw/manufacturing-sql-yield-dashboard"><strong>Explore the analysis →</strong></a><br>
      <a href="https://github.com/KhaiFaw/manufacturing-sql-yield-dashboard/blob/main/docs/screenshots/Yield%20Overview.png">Dashboard</a> · <a href="https://github.com/KhaiFaw/manufacturing-sql-yield-dashboard/blob/main/docs/verification.md">Data verification</a></p>
    </td>
    <td width="44%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/manufacturing-sql-yield-dashboard/blob/main/docs/screenshots/Yield%20Overview.png"><img src="https://raw.githubusercontent.com/KhaiFaw/manufacturing-sql-yield-dashboard/main/docs/screenshots/Yield%20Overview.png" width="100%" alt="Power BI yield overview dashboard using synthetic manufacturing test data"></a>
      <p><sub>DATA SYSTEMS / RAW RECORDS → INSIGHT</sub></p>
    </td>
  </tr>
</table>

| Synthetic records | Pass / fail | Analytics views | Verification |
|:---:|:---:|:---:|:---:|
| **8,000** | **7,558 / 442** | **4** | **Fresh load + rerun** |

<sub>Generated scenarios, not production-factory results. Dashboard images are real Power BI captures of this synthetic fixture.</sub>

<br><br>

### 04 / Local-first Windows software

<table>
  <tr>
    <td width="44%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/mybudget-windows"><img src="https://raw.githubusercontent.com/KhaiFaw/mybudget-windows/main/docs/screenshots/mybudget-dashboard-light.png" width="100%" alt="MyBudget native Windows dashboard displaying synthetic example finances"></a>
      <p><sub>SUPPORTING PROJECT / LOGIC → EXPERIENCE</sub></p>
    </td>
    <td width="56%" valign="top">
      <h3>MyBudget. Your data stays local.</h3>
      <p><strong>Native Windows application · Released</strong></p>
      <p>A monthly budget planner with exact decimal calculations and local SQLite storage. Covers planning, transactions, recurring income, goals and reports.</p>
      <p>Separates the interface, domain rules and persistence, with automated tests and data-preserving migrations.</p>
      <p><code>C#</code> <code>.NET</code> <code>WinUI 3</code> <code>SQLite</code></p>
      <p><a href="https://github.com/KhaiFaw/mybudget-windows"><strong>Explore MyBudget →</strong></a><br>
      <a href="https://github.com/KhaiFaw/mybudget-windows/releases/tag/v1.0.2">Release</a> · <a href="https://github.com/KhaiFaw/mybudget-windows/blob/main/docs/verification.md">Verification</a></p>
    </td>
  </tr>
</table>

| Documented tests | Release | Persistence | Cloud dependency |
|:---:|:---:|:---:|:---:|
| **105** | **v1.0.2** | **Local SQLite** | **None** |

<sub>Source-available under PolyForm Strict; unsigned portable build. Screenshots use synthetic finances.</sub>

---

## Engineering range

| Layer | What I work with |
|:---|:---|
| **Sense & control** | Microcontrollers, sensor integration, C/C++, RT-Thread, peripheral interfaces |
| **Process & infer** | MFCC features, CMSIS-DSP, TinyML, TensorFlow Lite Micro, INT8 inference |
| **Test & explain** | Python, pytest, bounded workloads, telemetry, CI, inspectable reports |
| **Model & visualise** | PostgreSQL, SQL, Power BI, data validation, yield and failure analysis |
| **Build & deliver** | C#, .NET, WinUI 3, SQLite, structured application layers |

<p align="center">
  <img src="https://img.shields.io/badge/C%2FC%2B%2B-Embedded-52dcff?style=flat-square&amp;labelColor=07111f" alt="C/C++ embedded systems">
  <img src="https://img.shields.io/badge/TinyML-Edge_AI-a78bfa?style=flat-square&amp;labelColor=07111f" alt="TinyML Edge AI">
  <img src="https://img.shields.io/badge/Python-Validation-66e3cf?style=flat-square&amp;labelColor=07111f" alt="Python validation">
  <img src="https://img.shields.io/badge/SQL-Power_BI-f2c94c?style=flat-square&amp;labelColor=07111f" alt="SQL and Power BI">
  <img src="https://img.shields.io/badge/C%23-WinUI_3-9b8cff?style=flat-square&amp;labelColor=07111f" alt="C sharp and WinUI 3">
</p>

## How I build

**Understand the signal. Design around the constraints. Make the result inspectable.**

I like working across the hardware–software boundary: keeping the data path clear, testing failure cases, and documenting what a result does—and does not—establish. My current focus is stronger FYP verification and repeatable evidence workflows across my projects.

## Let's connect

Open to **graduate and early-career opportunities** in embedded software, Edge AI, test automation and engineering systems.

<p>
  <a href="https://www.linkedin.com/in/khairulfawwaz"><strong>LinkedIn ↗</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/KhaiFaw?tab=repositories"><strong>All repositories ↗</strong></a>
</p>

<sub>Sense precisely. Model clearly. Decide locally. Build reliably.</sub>

<br><br>

<p align="center">
  <img src="https://raw.githubusercontent.com/KhaiFaw/KhaiFaw/activity-output/activity-constellation.svg" width="100%" alt="Animated activity constellation based on KhaiFaw's public GitHub contributions, with travelling signals and illuminated contribution nodes">
</p>

<p align="center">
  <a href="https://github.com/KhaiFaw/KhaiFaw/blob/activity-output/PLAY.md"><strong>▶ Play animation</strong></a><br>
  <sub>Opens the animated view, even with reduced motion enabled. No browser settings changed.</sub><br>
  <sub>Public contributions · Refreshed weekly · Each node represents a day of building.</sub>
</p>
