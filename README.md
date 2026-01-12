# CSV Statistics & Visualization API

FastAPI + pandas + matplotlib を使った  
**CSVをアップロードして統計情報やグラフ画像を返すAPI**です。

Pythonによるデータ処理・API設計・可視化の実装例として作成しました。

---

## Features

- CSVファイルをアップロード
- 数値カラムの統計情報をJSONで取得
- 指定カラムのグラフ画像を生成
- グラフタイプ選択（line / bar / scatter）
- 複数カラム対応（例: `price,sales`）
- Swagger UI で操作可能
- Docker 対応
- HTTPS 公開対応（nginx + Let's Encrypt）
- DockerHub 公開済み

---

## Demo

### Local / Docker (Swagger UI)

![Swagger UI](images/swagger-ui.png)

### Docker (Public Access)

![Docker Swagger UI](images/docker-swagger-ui.png)

---

## Public Access

This API is publicly available at:

- https://oit2003.com/docs

---

## DockerHub

Pull and run:

```bash
docker pull oit2003/csv-api
docker run -p 8000:8000 oit2003/csv-api
```

---

## Tech Stack

- Python 3.11
- FastAPI
- pandas
- matplotlib
- uvicorn
- Docker
- nginx
- Let's Encrypt

---

## Setup (Local)

```bash
git clone https://github.com/oit2003/csv-api.git
cd csv-api
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pandas matplotlib python-multipart
```

Run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Docker (Local Build)

```bash
docker build -t csv-api .
docker run -p 8000:8000 csv-api
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{ "status": "ok" }
```

---

### Get Statistics from CSV

```
POST /stats
```

**Parameters**

- file: CSV file

---

### Generate Plot Image

```
POST /plot
```

**Parameters**

- file: CSV file
- column: column name  
  - single: `price`
  - multiple: `price,sales`
- type: line | bar | scatter (optional, default=line)

---

## Sample CSV

```csv
price,sales
100,10
200,20
300,40
450,80
500,120
```

---

## Author

Yoshihiro Inamasu  
Python / Linux / API Development
