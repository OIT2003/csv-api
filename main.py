from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/status")
async def stats(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    summary = df.describe().to_dict()

    return JSONResponse({"summary": summary})


@app.post("/plot")
async def plot(file: UploadFile = File(...), column: str = None, type: str = "line"):
    df = pd.read_csv(file.file)

    if column not in df.columns:
        return JSONResponse({"error": f"column '{column}' not found"}, status_code=400)

    plt.figure()

    if type == "line":
        df[column].plot()
    elif type == "bar":
        df[column].plot(kind="bar")
    elif type == "scatter":
        plt.scatter(range(len(df[column])), df[column])
    else:
        return JSONResponse(
            {"error": f"Unknown graph type '{type}'. Use line/bar/scatter"},
            status_code=400,
        )

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return StreamingResponse(buf, media_type="image/png")
