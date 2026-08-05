<p align="center">
  <img src="assets/portfolio-constellation.gif" width="100%" alt="Animated engineering constellation representing embedded systems, Edge AI, automation, IoT, and software">
</p>

<p align="center">
  <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection"><img src="https://img.shields.io/badge/EXPLORE-EMBEDDED_EDGE_AI-52dcff?style=for-the-badge&labelColor=07111f" alt="Explore the embedded Edge AI project"></a>
  <a href="https://github.com/KhaiFaw/mybudget-windows"><img src="https://img.shields.io/badge/EXPLORE-MYBUDGET_WINDOWS-8b8cff?style=for-the-badge&labelColor=07111f" alt="Explore the MyBudget Windows app"></a>
  <a href="https://www.linkedin.com/in/khairulfawwaz"><img src="https://img.shields.io/badge/CONNECT-LINKEDIN-66e3cf?style=for-the-badge&labelColor=07111f" alt="Connect with Khairul Fawwaz on LinkedIn"></a>
</p>

### From physical systems to intelligent software.

I'm a **Mechatronic Engineering graduate from Universiti Sains Malaysia (USM)** who builds where hardware, software, and intelligence meet. My work moves between real-time firmware, signal processing, on-device machine learning, connected devices, automation, and native application development.

I care about the full engineering path: understanding the physical signal, choosing a practical architecture, working within real constraints, and leaving behind a system that can be tested, explained, and improved.

---

## Selected work

<table>
  <tr>
    <td width="56%" valign="top">
      <h3>01 / On-device acoustic intelligence</h3>
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
      <h3>02 / Local-first Windows software</h3>
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
| **Automation & control** | PLC Ladder Logic, control systems, MATLAB, Simulink |
| **Connected devices** | MQTT, UART, LTE AT commands, Wi-Fi, OTA update workflows |
| **Application software** | C#, .NET, WinUI 3, XAML, MVVM, SQLite, Python |

<p>
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
- Strengthening real-time firmware architecture, testing, and documentation.
- Expanding into well-structured application software and AI-assisted engineering workflows.
- Publishing project evidence—not just finished screenshots, but architecture, constraints, verification, and lessons learned.

---

## Connect

I'm open to graduate and entry-level opportunities across embedded systems, Edge AI, automation, IoT, and adjacent software engineering.

<p>
  <a href="mailto:khairulfaw@gmail.com"><strong>Email</strong></a>
  &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/khairulfawwaz"><strong>LinkedIn</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/KhaiFaw?tab=repositories"><strong>Repositories</strong></a>
</p>

<sub>Sense precisely. Decide locally. Build reliably.</sub>
