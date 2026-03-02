# Helper - Home Health Monitoring App

A privacy-first home monitoring application that uses audio wave analysis to detect potential health emergencies without violating privacy.

## 🎯 Features

- **Clean, Pastel UI** - Beautiful interface with soft colors
- **Household Member Tracking** - Monitor family members in real-time
- **Room Location Display** - Know where each person is
- **Health Status Indicator** - Quick visual status of household health
- **Privacy-First Audio Analysis** - Detects patterns from audio (future feature)

## 📱 Building the APK

### Quick Build:
```bash
# Create project zip
zip -r helper.zip main.py buildozer.spec requirements.txt

# Upload to Codemagic (https://codemagic.io)
# 1. Sign up
# 2. Upload helper.zip
# 3. Select Android platform
# 4. Build Debug
# 5. Download APK
# 6. Install on Android phone
```

### Local Build (macOS/Linux with Android SDK):
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build APK
buildozer android debug
```

## 🛠️ Development

### Running on Desktop:
```bash
source venv/bin/activate
python main.py
```

### Project Structure:
- `main.py` - Kivy app with full UI
- `buildozer.spec` - Build configuration
- `requirements.txt` - Python dependencies
- `.github/workflows/build.yml` - CI/CD configuration

## 🎨 Design

**Color Palette:**
- Primary: Pastel Blue (#D9EBF7)
- Secondary: Pastel Purple (#EDDAF3)
- Success: Pastel Green (#D9F2D9)
- Accent: Pastel Pink (#FAE0E8)
- Text: Dark Gray (#4D4D58)

## 📦 Requirements

- Python 3.8+
- Kivy 2.3.0+
- Android SDK (for local builds)

## 🚀 Roadmap

- [x] Clean UI Design
- [x] Member Display Cards
- [ ] Audio Wave Capture
- [ ] Stroke Detection Algorithm
- [ ] Real-time Alerts
- [ ] Cloud Sync
- [ ] Multi-room Support
- [ ] Historical Data Tracking

## 📜 License

MIT License
