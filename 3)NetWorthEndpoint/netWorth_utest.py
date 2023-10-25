import sys
from fastapi.testclient import TestClient
from fastapi import APIRouter, Request
from datetime import date, timedelta
from freezegun import freeze_time 
router = APIRouter()


@freeze_time("2022-02-01")  
def test_get_net_worth():
    client = TestClient(router) 
    access_token = "fake_access_token"
    
    response = client.get(
        "/plaid/net_worth", 
        params={"access_token": access_token}
    )
    
    if response.status_code == 200 and 'net_worth' in response.json():
        return True
    else:
        return False

test_passed = test_get_net_worth()

if test_passed:
    sys.exit(0)
else:
    sys.exit(1)