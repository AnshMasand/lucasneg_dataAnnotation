import sys
from fastapi.testclient import TestClient
from fastapi import APIRouter, Request
from datetime import date, timedelta
from freezegun import freeze_time 
router = APIRouter()

@freeze_time("2022-02-01")  
def test_get_savings_rate():
    client = TestClient(router) 
    year = 2022
    month = 1
    access_token = "fake_access_token"
    income = 3000.00

    response = client.get(
        f"/plaid/savings_rate/{year}/{month}", 
        params={"access_token": access_token, "income": income}
    )
    if response.status_code == 200 and response.json() is not None:
        return True
    else:
        return False

test_passed = test_get_savings_rate()

if test_passed:
    sys.exit(0)
else:
    sys.exit(1)

