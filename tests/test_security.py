from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

user2_id = str(uuid.uuid4())

##############################################
############ Security unit tests #############
##############################################

# Security Acceptance Criteria: https://github.com/OWASP/user-security-stories/blob/master/security-acceptance-criteria.md 
# User Security Stories: https://github.com/OWASP/user-security-stories/blob/master/user-security-stories.md

## As a Software company Customer, I want the application to validate input to be correct and fit for the intended purpose.

def test_create_user_with_invalid_email():
    sample_payload = {
        "id": user2_id,
        "first_name": "PLACEHOLDER",
        "last_name": "PLACEHOLDER",        
        "email": "PLACEHOLDER",
        "username": "PLACEHOLDER",
        "password": "PLACEHOLDER",
        "address": "PLACEHOLDER",
        "activated": False,
        "createdAt": "2023-03-17T00:04:32",
    }
    response = client.post("/api/users/", json=sample_payload)
    assert response.status_code == 422

def test_create_user_with_admin_as_username():
    sample_payload = {
        "id": user2_id,
        "first_name": "PLACEHOLDER",
        "last_name": "PLACEHOLDER",        
        "email": "placeholder@returngis.net",
        "username": "admin",
        "password": "PLACEHOLDER",
        "address": "PLACEHOLDER",
        "activated": False,
        "createdAt": "2023-03-17T00:04:32",
    }
    response = client.post("/api/users/", json=sample_payload)
    assert response.status_code == 422

def test_create_user_with_user_as_username():
    sample_payload = {
        "id": user2_id,
        "first_name": "PLACEHOLDER",
        "last_name": "PLACEHOLDER",        
        "email": "placeholder@returngis.net",
        "username": "user",
        "password": "PLACEHOLDER",
        "address": "PLACEHOLDER",
        "activated": False,
        "createdAt": "2023-03-17T00:04:32",
    }
    response = client.post("/api/users/", json=sample_payload)
    assert response.status_code == 422