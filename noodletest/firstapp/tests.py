from django.test import TestCase
from . import views
import requests

# Create your tests here.

def register_user_without_vals():
    url = "http://127.0.0.1:8000/firstapp/register-user/"
    data = { "name": "John Doe", "email": "john.doe@wonderfulemail.com" }
    headers = "Content-Type: application/json"
    res = requests.POST(url, data, headers=headers)
    assert res["user_id"] == True

