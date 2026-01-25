from fastapi.testclient import TestClient
from main import app
import io

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_status():
    csv_content = "price,sales\n100,10\n200,20\n"
    file = {"file": ("test.csv", io.BytesIO(csv_content.encode()), "text/csv")}

    response = client.post("/status", files=file)

    assert response.status_code == 200
    assert "summary" in response.json()
