import sys
from fastapi.testclient import TestClient
from fastapi import APIRouter, Request
from freezegun import freeze_time
router = APIRouter()

@freeze_time("2022-02-01")  
def test_get_monthly_cash_flow():
    client = TestClient(router) 
    year = 2022
    month = 2
    access_token = "fake_access_token"

    response = client.get(
        f"/plaid/cash_flow/{year}/{month}", 
        params={"access_token": access_token}
    )
    if response.status_code == 200 and response.json() is not None:
        assert 'cash_flow' in response.json()
        assert 'period' in response.json()
        return True
    else:
        return False

test_passed = test_get_monthly_cash_flow()

if test_passed:
    sys.exit(0)
else:
    sys.exit(1)