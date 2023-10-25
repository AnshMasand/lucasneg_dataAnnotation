import sys
from fastapi.testclient import TestClient
from fastapi import APIRouter, Request
from datetime import date, timedelta
from freezegun import freeze_time 
router = APIRouter()

def main():
    client = TestClient(router) 

    @freeze_time("2022-02-01")  
    def test_get_debt_to_income():
        access_token = "fake_access_token"
        monthly_income = 5000.00 # change this to any valid value

        response = client.get(
            "/plaid/debt_to_income", 
            params={"access_token": access_token, "monthly_income": monthly_income}
        )
        if response.status_code == 200 and response.json() is not None:
            return True
        else:
            return False

    test_passed = test_get_debt_to_income()

    if test_passed:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()