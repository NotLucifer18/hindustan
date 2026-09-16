# Digital Twin — Cybersecurity Threat & Risk Predictor
### Morningstar Cybersecurity Defense Labs

[![Interface](https://img.shields.io/badge/Interface-Enterprise%20SOC%20Command%20Center-ff2244.svg)](#)
[![Team](https://img.shields.io/badge/Organization-Morningstar%20Cyber%20Labs-141822.svg)](#)
[![Researchers](https://img.shields.io/badge/Lead%20Researchers-Rushil%20S%20%26%20Nikitha%20H%20S-10b981.svg)](#)
[![Controls](https://img.shields.io/badge/Security%20Controls-24%20Vectors%20(MITRE%20Mapped)-3b4660.svg)](#)

A high-performance, engineering-grade Security Operations Center (SOC) dashboard that models an individual's digital cyber risk profile across 24 critical threat vectors. Built with **hardware-accelerated animated SVG spider charts**, real-world **MITRE ATT&CK matrix mappings**, and a multi-bundle **What-If Attack Surface Remediation Simulator**.

---

## Authors & Organization
- **Organization**: Morningstar Cybersecurity Defense Labs
- **Researchers**: Rushil S & Nikitha H S
- **System**: Digital Twin — Cybersecurity Threat & Risk Predictor

---

## 24 Security Controls Across 4 Defensive Surfaces

### Surface 1: Identity & Credential Hygiene (Accounts)
1. **Password Reuse Across Accounts** *(Weight: 8, MITRE T1110.004)*
2. **Two-Factor Authentication (2FA/MFA)** *(Weight: 9, MITRE T1078)*
3. **Known Breached Credentials in Active Use** *(Weight: 10, MITRE T1110.003)*
4. **Primary Email Reused for Public Signups** *(Weight: 5, MITRE T1589.002)*
5. **Dedicated Password Vault Utilization** *(Weight: 7, MITRE T1555.003)*
6. **Predictable Security Question Hygiene** *(Weight: 4, MITRE T1586.002)*

### Surface 2: Endpoint Integrity & Physical Security (Devices)
7. **Automated OS Patching within 14 Days** *(Weight: 8, MITRE T1068)*
8. **Real-Time Antivirus / EDR Active** *(Weight: 6, MITRE T1204.002)*
9. **Full-Disk Storage Encryption (BitLocker/FileVault)** *(Weight: 7, MITRE T1005)*
10. **Screen Lock Timeout (< 3 Mins) with Biometrics** *(Weight: 7, MITRE T1200)*
11. **Automated 3-2-1 Encrypted Backups** *(Weight: 8, MITRE T1486)*
12. **Remote Wipe & Device Localization** *(Weight: 5, MITRE T1082)*

### Surface 3: Perimeter, Connectivity & Gateway Surface (Networks)
13. **Frequent Public Wi-Fi Usage** *(Weight: 6, MITRE T1557.002)*
14. **Encrypted VPN Active on Untrusted Networks** *(Weight: 8, MITRE T1040)*
15. **Home Router Default Admin Password Changed** *(Weight: 9, MITRE T1078.001)*
16. **Encrypted DNS (DoH / DoT / NextDNS)** *(Weight: 6, MITRE T1584.008)*
17. **Segmented Guest Subnet for Smart/IoT Devices** *(Weight: 7, MITRE T1046)*
18. **Universal Plug and Play (UPnP) Disabled** *(Weight: 7, MITRE T1599)*

### Surface 4: Application, Browser & Supply Chain Hygiene (Apps)
19. **Browsers & Software Updated Automatically** *(Weight: 7, MITRE T1190)*
20. **Software Strictly Installed from Official Sources** *(Weight: 8, MITRE T1195.002)*
21. **Routine Review of Application Permissions** *(Weight: 5, MITRE T1548)*
22. **Browser Extension Audit (Pruned Dormant Addons)** *(Weight: 6, MITRE T1176)*
23. **Developer Mode / Sideloading Disabled** *(Weight: 8, MITRE T1204.002)*
24. **Office Document Macro Execution Blocked** *(Weight: 7, MITRE T1204.002)*

---

## 6 Specialized SOC Command Pages

1. **Executive Overview**: High-resolution composite risk gauge (0–100), animated SVG spider chart, 4-layer progress telemetry, and target persona presets (*Critical Target, Typical Remote, Hardened Fortress*).
2. **Risk Controls (24 Vectors)**: Detailed audit accordions with binary switches, weight badges, and MITRE IDs.
3. **What-If Simulator (Core Demo)**:
   - Quick Remediation Bundles: *Max Impact (Top 3)*, *Zero-Cost Quick Wins (< 5 mins)*, *Total Perimeter Hardening*.
   - Actionable execution playbooks with time-to-fix estimates, user friction levels, and MITRE mitigations.
   - Dual-contour live spider chart morphing with real-time score drops.
4. **MITRE ATT&CK Matrix**: Cyber Kill Chain progression tracking, threat actor profiles (*Initial Access Brokers, Ransomware Syndicates, AiTM Eavesdroppers, Infostealers*), and live simulated global campaign feed.
5. **Audit & Compliance**: Official attestation certificate, domain evaluation table, markdown clipboard copy, and JSON telemetry export.
6. **OSINT & Social Media Privacy Scanner**:
   - **Dual-Mode Input**: Accepts public URLs/handles (GitHub, LinkedIn, X, Instagram) OR uploaded/drag-and-dropped profile/settings screenshots.
   - **Computer Vision & OCR Simulation**: Extracts text bounding boxes for visible emails, unverified GPG keys, and insecure 2FA radio toggles (SMS).
   - **ML Heuristic Feature Scoring**: Calculates PII Exposure, 2FA/Signature gaps, email scraping surface, and cross-platform handle correlation.
   - **Digital Twin Direct Sync**: One-click sync that injects OSINT findings directly into the 24 telemetry vectors.

---

## Complete Technology Stack & Architecture

| Layer | Technology | Technical Purpose & Details |
| :--- | :--- | :--- |
| **Frontend Framework** | **Modern Vanilla ES6+ SPA** | Zero external JS framework dependencies; lightweight, instantaneous execution, 100% in-memory state preservation without latency. |
| **Styling & Design System** | **Tailwind CSS + Custom Carbon Tokens** | SOC dark mode theme (`#06070a` canvas, `#141822` panels, `#ff2244` tactical crimson, `#10b981` emerald), glassmorphic backdrops, crisp 1px borders. |
| **Visualization & Charts** | **Hardware-Accelerated Scalable Vector Graphics (SVG)** | Mathematical dynamic polygon geometry for 4-axis radar/spider risk models with cubic-bezier morphing transitions. |
| **OSINT & Vision ML Pipeline** | **Client-Side Heuristic Classification & OCR Bounding Box Engine** | Passive multi-vector scoring (T1589, T1586, T1078), token entropy evaluation, regex birth-year deduction, and visual bounding box overlays. |
| **Cybersecurity Knowledge Base** | **MITRE ATT&CK Enterprise Matrix (v14)** | Full mapping of 24 personal attack vectors to enterprise tactics: Initial Access, Execution, Persistence, Privilege Escalation, Credential Access, Lateral Movement, Exfiltration. |
| **Server & Runtime** | **Python 3.12 Standard Library (`http.server`)** | High-reliability zero-dependency daemon (`main.py`) with native multi-threading, custom request routing, and `/api/health` heartbeat. |
| **Data Synchronization** | **Client-Side In-Memory JSON State Store** | Real-time reactive updates propagating between OSINT findings, What-If simulator, and Executive Overview with zero remote data leakage. |

---

## How to Run

```powershell
cd c:\Users\nikitha\luci
python main.py
```
Serves on `http://localhost:8000` with live telemetry API and auto-opens your browser.
