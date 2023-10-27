from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_signup_user_bad_pass():
    response = client.post("/signup",json={
        "email": "user@returngis.net",
        "password": "pass"
    })
    print(response)
    assert response.status_code == 400