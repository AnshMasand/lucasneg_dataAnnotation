import sys
from fastapi.testclient import TestClient
from fastapi import APIRouter, Request
router = APIRouter()

def main():
    client = TestClient(router) 

    def test_get_accounts_balances():
        access_token = "fake_access_token"
        
        response = client.get(
            "/plaid/accounts_balances", 
            params={"access_token": access_token}
        )
        if response.status_code == 200 and response.json() is not None:
            return True
        else:
            return False

    test_passed = test_get_accounts_balances()

    if test_passed:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()