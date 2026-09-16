# Digital Twin — Cybersecurity Risk Predictor

[![Team](https://img.shields.io/badge/Team-Morningstar-06b6d4.svg)](#)
[![Researchers](https://img.shields.io/badge/Researchers-Rushil%20S%20%26%20Nikitha%20H%20S-10b981.svg)](#)
[![Client--Side](https://img.shields.io/badge/Architecture-Zero--Backend%20%7C%20100%25%20Client--Side-8b5cf6.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-amber.svg)](#)

A modern, high-performance, single-page web application that models an individual's digital cyber risk profile ("Digital Twin") across four primary attack surfaces. Featuring an interactive, hardware-accelerated **animated spider/radar chart** and a real-time **What-If Remediation Simulator**.

---

## Authors & Branding
- **Team**: Morningstar
- **Researchers**: Rushil S & Nikitha H S
- **App Title**: Digital Twin — Cybersecurity Risk Predictor

---

## Key Features

### 1. Risk Profile Form (Collapsible Telemetry)
Four security surfaces covering 14 critical cybersecurity vectors:
- **Accounts**:
  - Password reuse across services *(Weight: 8, Risky: Yes)*
  - Two-Factor Authentication (2FA) enabled *(Weight: 9, Risky: No)*
  - Uses breached passwords *(Weight: 10, Risky: Yes)*
  - Email handle reused across sensitive/public sites *(Weight: 5, Risky: Yes)*
- **Devices**:
  - OS auto-updates active *(Weight: 8, Risky: No)*
  - Antivirus / EDR protection active *(Weight: 6, Risky: No)*
  - Full-disk BitLocker/FileVault encryption *(Weight: 7, Risky: No)*
  - Screen auto-lock with PIN/biometrics *(Weight: 7, Risky: No)*
- **Networks**:
  - Frequent public Wi-Fi usage *(Weight: 6, Risky: Yes)*
  - VPN used on public Wi-Fi *(Weight: 8, Risky: No)*
  - Router default admin password changed *(Weight: 9, Risky: No)*
- **Apps**:
  - Apps and browsers updated regularly *(Weight: 7, Risky: No)*
  - Software downloaded strictly from official sources *(Weight: 8, Risky: No)*
  - Periodic review of app permissions *(Weight: 5, Risky: No)*

### 2. Weighted Scoring Engine
- **Category Risk Score**:
  $$\text{Category Score} = \left( \frac{\sum \text{Active Risk Weights in Category}}{\sum \text{Total Category Weights}} \right) \times 100$$
- **Overall Risk Score**:
  $$\text{Overall Score} = \left( \frac{\sum_{\text{all}} \text{Active Risk Weights}}{\sum_{\text{all}} \text{Total Possible Weights}} \right) \times 100$$
- **Risk Bands**:
  - `0 - 30`: **Low Risk** (Emerald Green, Hardened posture)
  - `31 - 60`: **Medium Risk** (Amber Yellow, Moderate exposure)
  - `61 - 100`: **High Risk** (Rose Red, Critical threat surface)

### 3. Animated Spider / Radar Chart
- Visualizes the 4 distinct attack surface vectors in 360-degree space.
- Concentric coordinate rings at 25%, 50%, 75%, and 100%.
- Interactive coordinate vertices with dynamic color feedback based on risk severity.
- **Dual Contours during Simulation**: Shows both baseline contour (ghost red dashed line) and the simulated improved contour (glowing emerald polygon) shrinking toward center.

### 4. Top Vulnerabilities Panel
- Automatically highlights the **top 3 highest-weighted active risks** configured by the user.
- Shows actionable 1-line remediation advice (e.g. enabling 2FA, changing breached credentials).

### 5. "What-If" Simulator (Core Demo Feature)
- Beside each vulnerability in the Top Vulnerabilities list, a **"⚡ Simulate Fix"** toggle lets the user test what happens when that fix is implemented.
- The radar chart smoothly morphs inward and the overall score counter rolls down in real time.
- Clicking **"Apply Fixes"** saves the simulated posture directly to the live form.

### 6. Persona Quick Presets
- **🚨 High Risk Target**: Simulates a user with breached passwords, disabled 2FA, and open public Wi-Fi habits.
- **⚠️ Typical Remote Worker**: Common modern habits with moderate risk.
- **🛡️ Cyber Fortress**: Hardened security posture across all categories.
- **🔄 Reset**: Returns to base baseline.

---

## How to Run

### Method 1: Instant In-Browser (No dependencies required)
Simply double-click [`index.html`](file:///c:/Users/nikitha/luci/index.html) or open it directly in Google Chrome, Microsoft Edge, or Firefox.

```powershell
Start-Process chrome.exe "c:\Users\nikitha\luci\index.html"
```

### Method 2: Python Local Server
If Python is installed:
```powershell
python server.py
```
This serves the application on `http://localhost:8000` with live API telemetry and automatically launches your default browser.

---

## Connecting to Git & GitHub

To initialize or push this repository to GitHub:

```powershell
# 1. Initialize Git repository
git init

# 2. Stage and commit all files
git add .
git commit -m "Initial commit: Digital Twin Cybersecurity Risk Predictor by Morningstar"

# 3. Connect to your GitHub repository (replace with your repo URL)
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 4. Push to remote
git push -u origin main
```

---

## Project Structure
```
c:\Users\nikitha\luci\
├── index.html       # Complete Single-Page Application (HTML + Tailwind + SVG Radar Engine)
├── server.py        # Python local server & health API
├── .gitignore       # Git ignore rules
└── README.md        # Documentation and presentation guide
```
