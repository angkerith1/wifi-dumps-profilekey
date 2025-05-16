# 🌐 WiFi Profile Extractor | CODE BY @RITHCYBER-TEAM

![App Screenshot](https://i.imgur.com/JQ6Zfz9.png) <!-- Replace with your actual screenshot -->

A professional tool to extract saved WiFi profiles and passwords on Windows systems (requires admin rights).

[![GitHub release](https://img.shields.io/github/release/yourusername/wifi-profile-extractor.svg)](https://github.com/yourusername/wifi-profile-extractor/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)]()

## ✨ Features

- 🕵️‍♂️ Extract all saved WiFi profiles
- 🔑 Reveal WiFi passwords (admin required)
- 💾 Export results to TXT/CSV
- 🎨 Animated background support
- 🛡️ UAC-aware (auto-admin request)
- 📱 Responsive UI with modern design

## 📦 Installation

### Option 1: Download Pre-built EXE
1. Download the latest release from [Releases page](https://github.com/yourusername/wifi-profile-extractor/releases)
2. Run `WiFiProfileExtractor.exe` (right-click → "Run as administrator")

### Option 2: Build from Source
```bash
# Clone repository
git clone https://github.com/angkerith1/wifi-dumps-profilekey.git
cd wifi-dumps-profilekey

# Install dependencies
pip install -r requirements.txt

# Build executable
pyinstaller --onefile --windowed --icon=assets/icon.ico wifi.py
