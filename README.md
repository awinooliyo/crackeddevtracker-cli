# 🧠 CrackTracker CLI

Terminal-based productivity tracker for cracked devs who want to track logs, streaks, goals, and builds right from the command line.

---

## 🚀 Features

- ✅ Add encrypted daily logs
- 🔥 Track your log streaks and consistency
- 🎯 Manage long-term goals
- 🧱 Build time-boxed dev projects
- 🖥️ View everything in a terminal dashboard
- 💾 Local SQLite DB + optional AES encryption
- 🧠 AI Suggestions (soon!)

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/cracktracker-cli
cd cracktracker-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## 📦 Commands

### 🔐 Vault (Optional if you enable encryption)
```bash
crack vault unlock   # Set or enter your master password
crack vault lock     # Lock vault session
```

### ✅ Daily Logs
```bash
crack add log "Refactored FastAPI routes"
crack log all
```

### 🔥 Streak Tracker
```bash
crack streaks show
```

### 🎯 Goals
```bash
crack goals add "Master Django ORM"
crack goals list
crack goals done 2
```

### 🧱 Builds
```bash
crack build new "Write CLI Parser" --days 4
crack build list
```

### 🖥️ Dashboard
```bash
crack dashboard show
```
Shows logs for today, current streak, top goals, and active builds.

### 🧪 Init DB
```bash
crack init db
```
Creates the SQLite tables if not already created.

---

## 📁 Project Structure

```
cracktracker/
├── commands/
│   ├── add.py
│   ├── log.py
│   ├── streaks.py
│   ├── goals.py
│   ├── build.py
│   └── dashboard.py
├── utils/
│   └── crypto.py (optional for AES)
├── db.py
├── main.py
└── data/
    └── crackeddevtracker.db
```

---

## ✅ Upcoming Features
- `crack export readme` → auto-generate logs/summary for GitHub
- `crack ai suggest` → daily dev challenge from OpenAI
- TUI mode with live dashboard
- Config system (`crack config set`)

---

## 🧠 License
MIT

---

## 👨‍💻 Built by a cracked dev for cracked devs.
Stay sharp, log daily, and keep stacking streaks 🧱

