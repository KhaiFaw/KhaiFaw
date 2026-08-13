<p align="center">
  <img src="assets/portfolio-constellation.gif" width="100%" alt="Animated engineering constellation representing embedded systems, Edge AI, automation, IoT, and software">
</p>

<p align="center">
  <a href="https://github.com/KhaiFaw/manufacturing-sql-yield-dashboard"><img src="https://img.shields.io/badge/EXPLORE-MANUFACTURING_ANALYTICS-f2c94c?style=for-the-badge&labelColor=07111f" alt="Explore the manufacturing analytics project"></a>
  <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection"><img src="https://img.shields.io/badge/EXPLORE-EMBEDDED_EDGE_AI-52dcff?style=for-the-badge&labelColor=07111f" alt="Explore the embedded Edge AI project"></a>
  <a href="https://github.com/KhaiFaw/mybudget-windows"><img src="https://img.shields.io/badge/EXPLORE-MYBUDGET_WINDOWS-8b8cff?style=for-the-badge&labelColor=07111f" alt="Explore the MyBudget Windows app"></a>
</p>

<p align="center">
  <img src="assets/signal-to-software.svg" width="100%" alt="From physical systems to intelligent software: an animated signal journey from sensing through processing and inference to delivery">
</p>

I'm a **Mechatronic Engineering graduate from Universiti Sains Malaysia (USM)** who builds where hardware, software, data, and intelligence meet. My work moves between real-time firmware, signal processing, on-device machine learning, connected devices, manufacturing analytics, automation, and native application development.

I care about the full engineering path: understanding the physical signal or production data, choosing a practical architecture, working within real constraints, and leaving behind a system that can be tested, explained, and improved.

---

## Selected work

<table>
  <tr>
    <td width="44%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/manufacturing-sql-yield-dashboard">
        <img src="https://raw.githubusercontent.com/KhaiFaw/manufacturing-sql-yield-dashboard/main/docs/screenshots/Yield%20Overview.png" width="100%" alt="Manufacturing test yield Power BI dashboard">
      </a>
    </td>
    <td width="56%" valign="top">
      <h3>01 / Manufacturing data intelligence</h3>
      <p>An end-to-end production-test analytics system that turns <strong>8,000 deliberately messy tester records</strong> into validated manufacturing insights and an interactive Power BI dashboard.</p>
      <p>PostgreSQL preserves the raw source, cleans and quarantines records, enforces a normalized production model, and exposes reusable analytics views for yield, Pareto, station performance, and trend analysis.</p>
      <p><code>PostgreSQL</code> <code>Advanced SQL</code> <code>Power BI</code> <code>Python</code> <code>Docker</code></p>
      <p><a href="https://github.com/KhaiFaw/manufacturing-sql-yield-dashboard"><strong>Explore the data model, SQL analysis, and dashboards →</strong></a></p>
    </td>
  </tr>
</table>

| Test records | First-pass yield | Analytics contract | PBIR validation |
|:---:|:---:|:---:|:---:|
| **8,000** | **94.48%** | **4** reusable views | **0** errors |

<br>

<table>
  <tr>
    <td width="56%" valign="top">
      <h3>02 / On-device acoustic intelligence</h3>
      <p>A complete embedded Edge AI pipeline that recognizes six domestic sound categories directly on a <strong>Renesas RA8P1 Titan Board</strong>—without cloud inference.</p>
      <p>The firmware captures microphone audio, extracts MFCC, delta, and delta-delta features, runs an INT8 convolutional neural network through TensorFlow Lite for Microcontrollers, and produces confidence-gated alerts in real time.</p>
      <p><code>Embedded C/C++</code> <code>RT-Thread</code> <code>CMSIS-DSP</code> <code>TinyML</code> <code>TFLM</code></p>
      <p><a href="https://github.com/KhaiFaw/ai-acoustic-event-detection"><strong>Explore the firmware and technical breakdown →</strong></a></p>
    </td>
    <td width="44%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection">
        <img src="https://raw.githubusercontent.com/KhaiFaw/ai-acoustic-event-detection/main/docs/images/system-pipeline.png" width="100%" alt="Acoustic event detection system pipeline">
      </a>
    </td>
  </tr>
</table>

| Sound classes | Feature pipeline | Model footprint | Board-recorded evaluation |
|:---:|:---:|:---:|:---:|
| **6** | **39 × 61** MFCC-derived features | **114.4 KB** INT8 model | **87.5%** on a small test split |

<br>

<table>
  <tr>
    <td width="44%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/mybudget-windows">
        <img src="https://raw.githubusercontent.com/KhaiFaw/mybudget-windows/main/docs/screenshots/mybudget-dashboard-light.png" width="100%" alt="MyBudget Windows dashboard">
      </a>
    </td>
    <td width="56%" valign="top">
      <h3>03 / Local-first Windows software</h3>
      <p><strong>MyBudget</strong> is a native Windows monthly budget planner designed around private, PC-local data. It handles planning, transactions, recurring income and bills, savings goals, investments, reporting, backup, and CSV exchange.</p>
      <p>The codebase separates UI, budget rules, and persistence; uses exact decimal money calculations; and includes data-preserving SQLite migrations plus automated verification.</p>
      <p><code>C# 14</code> <code>.NET 10</code> <code>WinUI 3</code> <code>MVVM</code> <code>SQLite</code></p>
      <p><a href="https://github.com/KhaiFaw/mybudget-windows"><strong>See the architecture, screenshots, and verified build →</strong></a></p>
    </td>
  </tr>
</table>

| Native screens | Automated tests | Data model | Cloud dependency |
|:---:|:---:|:---:|:---:|
| **8** | **105** | Local SQLite | **None** |

---

## Engineering range

| Domain | What I build with |
|---|---|
| **Embedded systems** | C, C++, microcontrollers, RTOS concepts, firmware architecture, peripheral and sensor integration |
| **Edge AI & signal processing** | TensorFlow Lite Micro, TinyML, CNNs, MFCC feature extraction, CMSIS-DSP, quantized inference |
| **Manufacturing analytics** | PostgreSQL, advanced SQL, Power BI, data modeling, quality validation, yield and failure analysis |
| **Automation & control** | PLC Ladder Logic, control systems, MATLAB, Simulink |
| **Connected devices** | MQTT, UART, LTE AT commands, Wi-Fi, OTA update workflows |
| **Application software** | C#, .NET, WinUI 3, XAML, MVVM, SQLite, Python |

<p>
  <img src="https://img.shields.io/badge/PostgreSQL-Manufacturing_data-4169e1?style=flat-square&labelColor=07111f" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQL-Yield_%2B_Pareto-0f766e?style=flat-square&labelColor=07111f" alt="Advanced SQL">
  <img src="https://img.shields.io/badge/Power_BI-Engineering_dashboards-f2c94c?style=flat-square&labelColor=07111f" alt="Power BI">
  <img src="https://img.shields.io/badge/C-Embedded_firmware-52dcff?style=flat-square&labelColor=07111f" alt="C">
  <img src="https://img.shields.io/badge/C%2B%2B-Real--time_systems-38bdf8?style=flat-square&labelColor=07111f" alt="C++">
  <img src="https://img.shields.io/badge/C%23-Native_Windows-8b8cff?style=flat-square&labelColor=07111f" alt="C sharp">
  <img src="https://img.shields.io/badge/RTOS-RT--Thread-0ea5e9?style=flat-square&labelColor=07111f" alt="RT-Thread">
  <img src="https://img.shields.io/badge/TinyML-On--device_AI-818cf8?style=flat-square&labelColor=07111f" alt="TinyML">
  <img src="https://img.shields.io/badge/DSP-MFCC_%2B_CMSIS-6366f1?style=flat-square&labelColor=07111f" alt="Digital signal processing">
  <img src="https://img.shields.io/badge/IoT-MQTT_%2B_LTE-66e3cf?style=flat-square&labelColor=07111f" alt="IoT connectivity">
  <img src="https://img.shields.io/badge/.NET-WinUI_3-9b8cff?style=flat-square&labelColor=07111f" alt=".NET and WinUI 3">
</p>

---

## Experience & foundation

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Embedded Systems Intern</h3>
      <p><strong>Innowave LLC</strong></p>
      <ul>
        <li>Developed and optimized microcontroller-based embedded systems.</li>
        <li>Integrated sensors and supported hardware–firmware debugging.</li>
        <li>Worked with MQTT, LTE communication, and OTA update workflows.</li>
        <li>Connected physical devices to dependable software services.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>Bachelor of Mechatronic Engineering</h3>
      <p><strong>Universiti Sains Malaysia</strong></p>
      <p>A multidisciplinary foundation across electronics, embedded programming, control, automation, mechanical systems, and intelligent system design.</p>
      <p>That mix still shapes how I work: system-first, evidence-led, and comfortable crossing hardware–software boundaries.</p>
    </td>
  </tr>
</table>

### Earlier engineering builds

| System | Engineering focus |
|---|---|
| **Legged line-following robot** | Arduino sensing, locomotion, and closed-loop path following |
| **Hand-hygiene monitoring system** | PLC-controlled automation and process monitoring |
| **Height-measurement device** | RISC-V and 8052 embedded implementation |
| **FPGA passcode alarm** | Digital logic, state-based control, and hardware implementation |

---

## Current trajectory

- Building production-minded embedded and Edge AI systems.
- Applying SQL and Power BI to manufacturing yield, failure, and process data.
- Strengthening real-time firmware architecture, testing, and documentation.
- Expanding into well-structured application software and AI-assisted engineering workflows.
- Publishing project evidence—not just finished screenshots, but architecture, constraints, verification, and lessons learned.

---

## Connect

I'm open to graduate and entry-level opportunities across embedded systems, Edge AI, manufacturing analytics, automation, IoT, and adjacent software engineering.

<p>
  <a href="mailto:khairulfaw@gmail.com"><strong>Email</strong></a>
  &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/khairulfawwaz"><strong>LinkedIn</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/KhaiFaw?tab=repositories"><strong>Repositories</strong></a>
</p>

<sub>Sense precisely. Model clearly. Decide locally. Build reliably.</sub>

<br>

---

<p align="center">
  <img src="https://raw.githubusercontent.com/KhaiFaw/KhaiFaw/activity-output/activity-constellation.svg" width="100%" alt="KhaiFaw activity constellation: an animated public GitHub contribution calendar">
</p>
