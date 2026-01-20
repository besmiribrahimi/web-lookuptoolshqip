# 🔍 Termux Web Lookup

> **Terminal-based web search engine** | Search the web directly from your command line like a hacker! 🚀

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-orange?style=flat-square)

</div>

---

## ✨ Features

- 🌐 **Web Search** - Search from terminal instantly
- 🔎 **Multi-Engine** - Google & DuckDuckGo support
- 🎨 **Rich UI** - Beautiful colored terminal output
- ⚡ **Fast & Lightweight** - Instant results
- 📝 **Web Scraping** - Extract data from web
- 🔄 **Command History** - Remember your searches
- 🎯 **Quick Lookups** - One-command searches

---

## 📦 Project Structure

```
termux-web-lookup/
│
├── 📁 src/
│   ├── 🐍 __init__.py           Package initialization
│   ├── 🚀 main.py               Main entry point & REPL
│   ├── 🔍 search.py             Search engine wrapper
│   ├── 🕷️  scraper.py            Web scraping utilities
│   ├── 🎨 ui.py                 Terminal UI components
│   └── ⚙️  commands.py            Command parser & handler
│
├── 📄 requirements.txt           Dependencies
├── 📖 README.md                 This file
└── 📁 .github/

```

## 🚀 Quick Start

### ⬇️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/besmiribrahimi/web-lookuptoolshqip.git
cd termux-web-lookup

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the app
python src/main.py
```

### 💻 Usage

```bash
python src/main.py
```

Then type commands:
```
termux-lookup> search python tutorials
termux-lookup> google machine learning
termux-lookup> duckduckgo privacy
termux-lookup> help
termux-lookup> exit
```

---

## 🎯 Commands

| Command | Description | Example |
|---------|-------------|---------|
| 🔍 `search` | Generic web search (Google) | `search python tutorials` |
| 🔴 `google` | Search using Google | `google best code editor` |
| 🦆 `duckduckgo` | Privacy-focused search | `duckduckgo proxies` |
| 📚 `define` | Word definitions | `define algorithm` |
| ❓ `help` | Show all commands | `help` |
| 🚪 `exit`/`quit` | Close application | `exit` |

---

## 📦 Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| **requests** | HTTP requests | `2.31.0` |
| **beautifulsoup4** | Web scraping | `4.12.2` |
| **rich** | Terminal formatting & colors | `13.7.0` |
| **urwid** | Advanced terminal UI | `2.4.2` |
| **python-dotenv** | Environment config | `1.0.0` |

---

## 🛠️ Development

### 🚧 Upcoming Features

- 🌤️ **Weather Lookup** - Get weather by city
- 📰 **News Aggregation** - Latest news headlines
- 💱 **Currency Conversion** - Real-time rates
- 🌍 **IP Lookup** - Get info from IP address
- 📖 **Dictionary** - Advanced definitions
- 🤓 **Stack Overflow Search** - Find code solutions

### 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📄 License

<div align="center">

**MIT License** - Feel free to use this project for personal or commercial use.

[View License](LICENSE)

</div>

---

## 👨‍💻 Author

Created with ❤️ by the Besmir IBrahmi

<div align="center">

⭐ If you found this useful, please star the repository! ⭐

</div>


