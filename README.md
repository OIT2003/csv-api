# CSV Statistics & Visualization API

FastAPI + pandas + matplotlib を使った  
**CSVをアップロードして統計情報やグラフ画像を返すAPI**です。

Pythonによるデータ処理・API設計・可視化の実装例として作成しました。

---

## Features

- CSVファイルをアップロード
- 数値カラムの統計情報をJSONで取得
- 指定カラムのグラフ画像を生成
- グラフタイプ選択(ine / bar / scatter)
- 複数カラム対応(例： `price / sales`)
- Swagger UI で操作可能

---

## Demo

![Swagger UI](images/swagger-ui.png)

---

## Tech Stack

- Python 3.11
- FastAPI
- pandas
- matplotlib
- uvicorn
- Docker

---

## Setup

```bash
git clone https://github.com/oit2003/csv-api.git
cd csv-api
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pandas matplotlib python-multipart
```

起動：

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Docker

Python環境を用意せずにDockerだけで起動できます。

### Build

```bash
docker build -t csv-api
```

### Run

```bash
docker run -p 8000:8000 csv-api
```

ブラウザで開く：

```
http://localhost:8000/docs
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
