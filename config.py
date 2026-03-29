"""Windsurf AIコーディング完全ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Windsurf AIコーディング完全ガイド"
BLOG_DESCRIPTION = "大規模コードベース向けAIコードエディタWindsurfの使い方・Cascade機能・Cursor比較を毎日更新。"
BLOG_URL = "https://musclelove-777.github.io/windsurf-guide"
BLOG_TAGLINE = "Windsurf AIコードエディタを最大限活用するための日本語情報サイト"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/windsurf-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Windsurf 使い方",
    "Windsurf 料金・プラン",
    "Windsurf vs Cursor",
    "Windsurf 最新ニュース",
    "Cascade機能",
    "Windsurf テクニック",
    "AIコードエディタ比較",
    "Windsurf 活用事例",
]

THEME = {
    "primary": "#00d4aa",
    "accent": "#0088ff",
    "gradient_start": "#00d4aa",
    "gradient_end": "#0088ff",
    "dark_bg": "#0a1a1a",
    "dark_surface": "#142828",
    "light_bg": "#f0fffc",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Windsurf Pro": [
        {"service": "Windsurf Pro", "url": "https://windsurf.com/pricing", "description": "Windsurf Proプランに登録する"},
    ],
    "Cursor": [
        {"service": "Cursor", "url": "https://cursor.com", "description": "Cursorを試してみる"},
    ],
    "VS Code拡張": [
        {"service": "VS Code Marketplace", "url": "https://marketplace.visualstudio.com", "description": "VS Code拡張機能"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAIコーディング講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAIコーディング関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAIコーディング関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8103
