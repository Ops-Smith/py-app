from app import app # This imports the Flask App

def test_home():
    # Use Flask's test client
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome David!. You've successfully rebuilt the Flask App" in response.data
def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
