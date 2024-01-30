from virtualBankLimited import BankAccount
from Exceptions import InternalDepositException, WithdrawalException, BalanceRetrievalException
import pytest

def test_view_balance_success():
    bank_account = BankAccount(username='name', balance=100)
    actual_balance = bank_account.view_balance()
    assert actual_balance == 100

