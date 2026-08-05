<p align="center">
  <img src="assets/profile-banner.svg" width="100%" alt="Khairul Fawwaz — Embedded Systems, Edge AI and Automation">
</p>

<p align="center">
  <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection"><img src="https://img.shields.io/badge/FEATURED_PROJECT-ACOUSTIC_EDGE_AI-2dd4bf?style=for-the-badge&labelColor=07111f" alt="Featured project: Acoustic Edge AI"></a>
  <a href="https://www.linkedin.com/in/khairulfawwaz"><img src="https://img.shields.io/badge/LINKEDIN-LET'S_CONNECT-38bdf8?style=for-the-badge&labelColor=07111f" alt="Connect on LinkedIn"></a>
</p>

### Engineering reliable intelligence at the edge.

I'm a **Mechatronic Engineering graduate from Universiti Sains Malaysia (USM)** focused on embedded software, signal processing, Edge AI, and automation. I enjoy the point where hardware meets intelligence: capturing real-world signals, turning them into useful features, deploying compact models, and making the complete system behave reliably in real time.

My work spans **embedded C/C++**, RTOS-based firmware, sensor integration, TinyML, IoT connectivity, and hardware–software debugging. Here, I document the systems I build and the engineering lessons behind them.

---

## Featured engineering work

<table>
  <tr>
    <td width="58%" valign="top">
      <h3>AI-Powered Acoustic Event Detection</h3>
      <p>An embedded Edge AI system that classifies six domestic sound categories directly on a <strong>Renesas RA8P1 Titan Board</strong>—without cloud inference.</p>
      <p>The firmware captures microphone audio, extracts MFCC, delta, and delta-delta features, runs an INT8 convolutional neural network with TensorFlow Lite for Microcontrollers, and produces confidence-gated real-time alerts.</p>
      <p><code>Embedded C/C++</code> <code>RT-Thread</code> <code>CMSIS-DSP</code> <code>TinyML</code> <code>TFLM</code></p>
      <p><a href="https://github.com/KhaiFaw/ai-acoustic-event-detection"><strong>Explore the firmware and technical breakdown →</strong></a></p>
    </td>
    <td width="42%" align="center" valign="middle">
      <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection">
        <img src="https://raw.githubusercontent.com/KhaiFaw/ai-acoustic-event-detection/main/docs/images/system-pipeline.png" width="100%" alt="Acoustic event detection system pipeline">
      </a>
    </td>
  </tr>
</table>

| On-device classes | Feature pipeline | Model footprint | Evaluation |
|:---:|:---:|:---:|:---:|
| **6** sound categories | **39 × 61** MFCC-derived features | **114.4 KB** INT8 model | **87.5%** on a small board-recorded test split |

> The project demonstrates the full embedded ML path: data capture, DSP, model deployment, memory-aware inference, confidence handling, and live device output.

---

## Engineering toolkit

| Area | Technologies and capabilities |
|---|---|
| **Embedded systems** | C, C++, microcontrollers, RTOS concepts, firmware architecture, peripheral and sensor integration |
| **Edge AI & DSP** | TensorFlow Lite Micro, TinyML, CNNs, MFCC feature extraction, CMSIS-DSP, quantized inference |
| **Connectivity** | MQTT, UART, LTE AT commands, Wi-Fi, OTA update workflows |
| **Automation** | PLC Ladder Logic, control systems, MATLAB/Simulink |
| **Development** | RT-Thread Studio, VS Code, Keil µVision, Git/GitHub, Python |

<p>
  <img src="https://img.shields.io/badge/C-Embedded_firmware-2dd4bf?style=flat-square&labelColor=07111f" alt="C">
  <img src="https://img.shields.io/badge/C%2B%2B-Real--time_systems-38bdf8?style=flat-square&labelColor=07111f" alt="C++">
  <img src="https://img.shields.io/badge/RTOS-RT--Thread-0ea5e9?style=flat-square&labelColor=07111f" alt="RT-Thread">
  <img src="https://img.shields.io/badge/TinyML-On--device_AI-818cf8?style=flat-square&labelColor=07111f" alt="TinyML">
  <img src="https://img.shields.io/badge/DSP-MFCC_%2B_CMSIS-6366f1?style=flat-square&labelColor=07111f" alt="Digital signal processing">
  <img src="https://img.shields.io/badge/IoT-MQTT_%2B_LTE-f59e0b?style=flat-square&labelColor=07111f" alt="IoT connectivity">
</p>

---

## Experience

### Embedded Systems Intern · Innowave LLC

- Developed and optimized microcontroller-based embedded systems.
- Integrated sensors and supported hardware–firmware debugging.
- Worked with MQTT, LTE communication, and OTA update workflows.
- Built practical experience connecting physical devices to reliable software services.

### Bachelor of Mechatronic Engineering · Universiti Sains Malaysia

A multidisciplinary foundation spanning electronics, embedded programming, control, automation, mechanical systems, and intelligent system design.

---

## Other engineering work

| Project | Engineering focus |
|---|---|
| **Legged line-following robot** | Arduino-based sensing, locomotion, and closed-loop path following |
| **Hand-hygiene monitoring system** | PLC-controlled automation and process monitoring |
| **Height-measurement device** | RISC-V and 8052 embedded implementation |
| **FPGA passcode alarm** | Digital logic, state-based control, and hardware implementation |
| **Personal contact directory** | C++ file-based CRUD application and structured data handling |

These projects are being cleaned up and documented for future public releases.

---

## What I'm working toward

- Building production-minded embedded and Edge AI systems.
- Improving real-time firmware architecture, testing, and documentation.
- Publishing more engineering projects and technical write-ups.
- Exploring graduate and entry-level opportunities in embedded systems, Edge AI, automation, and related engineering roles.

---

## Let's connect

If you're working on embedded intelligence, real-time firmware, IoT, or automation, I'd be glad to connect.

<p>
  <a href="https://www.linkedin.com/in/khairulfawwaz"><strong>LinkedIn</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/KhaiFaw/ai-acoustic-event-detection"><strong>Featured project</strong></a>
</p>

<sub>Building systems that sense, decide, and act.</sub>
