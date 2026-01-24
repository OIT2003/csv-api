# CSV Analysis API & Portfolio Demo

FastAPI + Docker + nginx + HTTPS による CSV 分析・可視化 API の
**実行可能ポートフォリオ**です。

------------------------------------------------------------------------

## 🔗 Demo

-   ポートフォリオトップ\
    https://www.oit2003.com/

-   CSV API 実行画面\
    https://www.oit2003.com/csv-api/

------------------------------------------------------------------------

## 📌 概要

CSV ファイルをアップロードすることで、以下を Web UI
から直接実行できます。

-   統計情報の算出（count / mean / std / min / max）
-   折れ線グラフ（line）
-   棒グラフ（bar）
-   散布図（scatter）

バックエンド・フロントエンド・インフラを一貫して構築しています。

------------------------------------------------------------------------

## 🖼 スクリーンショット

### ポートフォリオトップ

![Portfolio Top](screenshots/portfolio_top.png)

### CSV API 実行画面

![CSV API UI](screenshots/csv_api_ui.png)

### Stats 実行結果（統計テーブル）

![Stats Result](screenshots/stats_result.png)

### Plot 実行結果（グラフ表示）

![Plot Result](screenshots/plot_result.png)

------------------------------------------------------------------------

## 🛠 技術スタック

  レイヤ          技術
  --------------- -------------------------------
  Backend         FastAPI / Python
  Data            pandas / matplotlib
  Frontend        HTML / CSS / JavaScript
  Container       Docker
  Reverse Proxy   nginx
  SSL             Let's Encrypt
  OS              Raspberry Pi OS (linux/arm64)

------------------------------------------------------------------------

## 📂 構成

``` text
csv-api/
├── main.py
├── Dockerfile
├── requirements.txt
├── README.md
└── screenshots/
    ├── portfolio_top.png
    ├── csv_api_ui.png
    ├── stats_result.png
    └── plot_result.png
```

nginx document root:

``` text
/var/www/html/
├── index.html
├── css/style.css
└── csv-api/index.html
```

------------------------------------------------------------------------

## 🔌 提供 API

### GET /health

``` json
{ "status": "ok" }
```

### POST /status

Form Data: - file: CSV ファイル

### POST /plot

Form Data: - file: CSV ファイル - column: カラム名（カンマ区切り） -
type: line / bar / scatter

Response: - PNG 画像

------------------------------------------------------------------------

## 🐳 Docker

### ローカルビルド

``` bash
docker build -t csv-api .
docker run -d --restart unless-stopped -p 127.0.0.1:8000:8000 csv-api
```

### DockerHub から実行

``` bash
docker pull oit2003/csv-api:latest
docker run -d -p 8000:8000 oit2003/csv-api:latest
```

**Supported Platforms** - linux/amd64 - linux/arm64

------------------------------------------------------------------------

## 🚀 Project Status

**v1.0.1 -- Documentation Improved Release**

-   Production environment: Raspberry Pi (linux/arm64)
-   Docker image published on DockerHub
-   Multi-architecture image support:
    -   linux/amd64
    -   linux/arm64
-   Verified environments:
    -   Raspberry Pi OS (linux/arm64)
    -   openSUSE Linux (linux/amd64)

The project is fully reproducible and environment-independent.

The same Docker image runs successfully across different CPU
architectures.

The API is served behind nginx with HTTPS enabled via Let's Encrypt.

------------------------------------------------------------------------

## 🧪 Verified Environments

  Environment       Architecture   Status
  ----------------- -------------- -------------
  Raspberry Pi OS   linux/arm64    ✅ Verified
  openSUSE Linux    linux/amd64    ✅ Verified

------------------------------------------------------------------------

## 🎯 目的

-   FastAPI を用いた実践的 API 設計
-   Docker + nginx + HTTPS による公開運用
-   採用担当者が実際に触れるポートフォリオの提供

------------------------------------------------------------------------

## 👤 Author

Yoshihiro Inamasu\
Python / FastAPI / Docker / Linux
