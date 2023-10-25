import unittest
from unittest.mock import Mock, patch
from datetime import date
from ..services import crud
import sys

class TestFetchTransactions(unittest.TestCase):

    @patch('plaid_fastapi_gptdata.services.crud.get_transactions')
    @patch('plaid_fastapi_gptdata.config.plaid.get_plaid_client')
    def test_fetch_transactions(self, mock_get_plaid_client, mock_get_transactions):
        mock_get_plaid_client.return_value = Mock()
        mock_get_transactions.return_value = [
            {
                "amount": 100,
                "iso_currency_code": "USD",
                "unofficial_currency_code": None,
                "category": ["Food and Drink", "Restaurants"],
                "date": str(date.today()),
            },
        ]
        
        output = crud.get_transactions(mock_get_plaid_client.return_value, 'test-access-token', date.today(), date.today())

        print(f'Mock response: {mock_get_transactions.return_value}')  
        print(f'Function output: {output}')  

        mock_get_transactions.assert_called_once_with(mock_get_plaid_client.return_value, 'test-access-token', date.today(), date.today())
        self.assertEqual(output, mock_get_transactions.return_value)
            
if __name__ == '__main__':
    unittest.main()
   