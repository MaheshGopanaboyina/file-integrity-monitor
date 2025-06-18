# file-integrity-monitor
# 🔐 File Integrity Monitor

A simple Python tool to monitor a directory and detect file changes using SHA-256 hashing.

---

## 📁 Monitored Directory

By default, the script monitors:


You can change this by modifying the `MONITORED_DIR` variable in the script.

---

## ⚙️ How It Works

- Calculates SHA-256 hashes of files in the directory.
- Saves the current file hashes to `file_hashes.json`.
- Compares current hashes with the stored ones.
- Detects and prints:
  - 🆕 New files
  - ✏️ Modified files
  - ❌ Deleted files

---

## 🧪 Sample Output


---

## 🚀 Getting Started

### 1. Clone or download the repository

```bash
git clone https://github.com/your-username/file-integrity-monitor.git
cd file-integrity-monitor
mkdir monitored_files
python3 file_integrity_monitor.py
