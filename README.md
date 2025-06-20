
# Fetcherr 🦊

Fetcherr is a command-line tool written in Python to ***fetch*** and organize content from the [Kemono](https://kemono.su/) API.  
It allows you to retrieve detailed information about creators and their posts, with a clean and modular architecture. And even downloading! (Is it interesting?)

> **Note:** This tool is meant for educational and archival purposes only. Respect all terms of service and copyrights.

## 🔧 Features

- 🔍 Get detailed info of any creator
- 📥 Download and parse creator posts
- 🔁 Refresh the creators database
- ⚙️ Configurable with `kemono.yml` file (mostly)
## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/SlackerBahadir/fetcherr.git
cd fetcherr
pip install -r requirements.txt
```
## 🚀 Usage

Usage: python main.py [OPTIONS]

**Options:**
- **--info** - Get detailed info of a creator.
- **--refresh** - Refresh creators.json file.
- **-g**, **--getposts** TEXT - Get posts from the selected creator.
- **--creator** TEXT - Set creator name or ID to be used with **--info**, **--installall** and **--getposts**
- **--installall** - Download all posts of selected creator.
- **--help** - Show this message and exit.

## Examples

```bash
python main.py --creator "SlackerBahadir" --info
```
## ⚠️ Known Issues

- If you receive an SSLError, it's likely due to censorship in your country or workplace.
Try using a VPN or [zapret](https://github.com/bol-van/zapret).
## 🗂 Project Structure

```css
fetcherr/
├── fetcherr/ # Fetcher related utilities and core functions
│   ├── download_posts.py
│   └── kemono_yaml_loader.py
├── kemono/ # Kemono related utilities and configuration
│   ├── kemono.yml # API configuration
│   └── utils/ # Core utilities for kemono API
│       ├── creator_info.py
│       ├── get_posts_of_creator_by_name_or_id.py
│       └── recent_posts.py
├── LICENSE
├── main.py # CLI Program
├── README.md
└── requirements.txt
```

## 👨‍💻 Author
by **SlackerBahadir**

Github: [@SlackerBahadir](https://github.com/SlackerBahadir)

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/) — steal responsibly.