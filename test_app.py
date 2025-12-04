from app import app # This imports the Flask App

def test_home():
    # Use Flask's test client
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    
    # Decode bytes to string for comparison
    response_text = response.data.decode('utf-8')
    assert "🚀 Welcome to Our CI/CD Pipeline! Application successfully deployed through Development → Staging → Production" in response_text

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200