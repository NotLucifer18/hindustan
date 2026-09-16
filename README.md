# Digital Twin — Cybersecurity Risk Predictor
### Morningstar Cyber Command Center

[![Theme](https://img.shields.io/badge/Theme-Black%20%26%20Red%20Cyber%20Command-ff1a40.svg)](#)
[![Team](https://img.shields.io/badge/Team-Morningstar-dc2626.svg)](#)
[![Researchers](https://img.shields.io/badge/Researchers-Rushil%20S%20%26%20Nikitha%20H%20S-10b981.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-5--Page%20Zero--Backend%20SPA-101420.svg)](#)

An aggressive, high-contrast **Black & Red** cyber-warfare dashboard that models an individual's digital risk profile ("Digital Twin") across four defensive surfaces. Built with hardware-accelerated **animated SVG spider charts**, interactive weighted risk telemetry, and a real-time **What-If Cyber Remediation Simulator**.

---

## Authors & Branding
- **Organization**: Morningstar Cyber Labs
- **Researchers**: Rushil S & Nikitha H S
- **App Title**: Digital Twin — Cybersecurity Risk Predictor

---

## 5 Specialized Cyber Command Pages

### 1. 📊 Executive Overview
- Giant Blood-Red Digital Score Gauge (0–100) with dynamic rolling counter and threat level indicator.
- Interactive High-Contrast SVG Spider/Radar Chart with crimson glowing contours.
- Category summary cards (Accounts, Devices, Networks, Apps) with mini progress bars.
- Quick persona presets (🚨 High Risk Target, ⚠️ Typical User, 🛡️ Cyber Fortress, 🔄 Reset).

### 2. ⚙️ Risk Profile Telemetry (14 Controls)
- Detailed breakdown across 4 defensive surfaces with collapsible accordions:
  - **Accounts**: Password reuse (w:8), 2FA enabled (w:9), breached passwords (w:10), email reused (w:5).
  - **Devices**: OS updates (w:8), antivirus installed (w:6), disk encryption (w:7), screen lock (w:7).
  - **Networks**: Public Wi-Fi usage (w:6), VPN on public Wi-Fi (w:8), router default password changed (w:9).
  - **Apps**: Regular app updates (w:7), official app stores only (w:8), app permissions review (w:5).
- High-visibility red/green binary toggle switches with threat weights (1-10) and live category risk badges.

### 3. ⚡ "What-If" Cyber Remediation Simulator (The Core Demo Moment)
- Dedicated simulation workstation:
  - Side-by-side comparative posture view: **Current Baseline Risk vs. Hardened Posture**.
  - Top 3 highest-weighted vulnerabilities with live **"⚡ Simulate Fix"** toggles.
  - Global **"⚡ Simulate All Fixes"** action button.
  - Live animated SVG radar chart displaying dual contours (baseline red dashed ghost contour vs. morphing green simulated contour).
  - Dynamic score reduction readout (e.g. `▼ -38 pts (-45%)`).
  - **"Apply Fixes to Profile"** button to commit changes permanently.

### 4. 🎯 Threat Intelligence Matrix
- Deep technical breakdown of 4 real-world adversary attack vectors:
  1. **Credential Stuffing & Takeover** (T1110 - Breach dump botnets).
  2. **Ransomware & Zero-Day Endpoint Exploits** (T1204 - Privilege escalation).
  3. **Man-In-The-Middle (MITM) & Wi-Fi Eavesdropping** (T1557 - Evil Twin, DNS poisoning).
  4. **Supply Chain & Malicious App Extraction** (T1195 - Trojanized torrents).
- Dynamic threat rating based on current user inputs with key defensive controls.

### 5. 📑 Audit & Compliance Report
- Official Executive Cyber Risk Audit Certificate with digital seal and timestamp.
- Evaluated layer breakdown table and active risk list.
- One-click **Copy Executive Summary** (formatted markdown clipboard export).
- One-click **Export JSON Telemetry** file download.
- Printable certificate layout (`window.print()`).

---

## How to Run

### Method 1: Instant In-Browser
Open [`index.html`](file:///c:/Users/nikitha/luci/index.html) in your browser:
```powershell
Start-Process "c:\Users\nikitha\luci\index.html"
```

### Method 2: Python Local Server
```powershell
python server.py
```
Serves the application on `http://localhost:8000` with health telemetry API and auto-opens your browser.

---

## Git Repository & Remote

This repository is connected to:
`https://github.com/NotLucifer18/hindustan.git`

To push to GitHub:
```powershell
cd c:\Users\nikitha\luci
git push -u origin main
```
