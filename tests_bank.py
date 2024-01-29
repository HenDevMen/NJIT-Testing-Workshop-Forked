from virtualBankLimited import BankAccount
from Exceptions import InternalDepositException, WithdrawlException, BalanceRetrievealException
import pytest
import coverage

# Runs before every test, creating a BankAccount object with the username 'name' and balance 100.
@pytest.fixture(autouse=True)
def bank_account():
        return BankAccount(username= 'name', balance=100)

def test_view_balance_success(bank_account):
        assert bank_account.view_balance() == 100

def test_deposit_success(bank_account):
        bank = BankAccount(username= 'name', balance=100)
        assert bank_account.deposit(100) == 200.0

def test_withdraw_success(bank_account):
        bank = BankAccount(username= 'name', balance=100)
        assert bank_account.withdraw(50) == 50.0

def test_deposit_throws(bank_account):
        bank = BankAccount(username= 'name', balance=100)
        with pytest.raises(InternalDepositException):
                bank_account.deposit(-30)
