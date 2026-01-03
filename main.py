from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, File, Form, UploadFile
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
async def plot(file: UploadFile = File(...), column: str = Form(...), type: str = "line"):
    df = pd.read_csv(file.file)

    columns = [c.strip() for c in column.split(",")]

    for c in columns:
        if c not in df.columns:
            return JSONResponse({"error": f"column '{c}' not found"}, status_code=400)

    plt.figure()

    if type == "line":
        for c in columns:
            plt.plot(df[c], label=c)
        plt.legend()
    elif type == "bar":
        df[columns].plot(kind="bar")
        plt.legend()
    elif type == "scatter":
        if len(columns) != 2:
            return JSONResponse(
                {"error": "scatter requires exactly 2 columns"}, status_code=400
            )
        plt.scatter(df[columns[0]], df[columns[1]])
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
    else:
        return JSONResponse(
            {"error": f"Unknown graph type '{type}'. Use line/bar/scatter"},
            status_code=400,
        )

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return StreamingResponse(buf, media_type="image/png")
