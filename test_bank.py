from virtualBankLimited import BankAccount
from Exceptions import InternalDepositException, WithdrawalException, BalanceRetrievalException
import pytest

def test_view_balance_success():
    bank_account = BankAccount(username='name', balance=100)
    actual_balance = bank_account.view_balance()
    assert actual_balance == 100

def test_view_balance_unsuccessful():
    bank_account = BankAccount(username='name', balance=-100)
    with pytest.raises(BalanceRetrievalException):
        bank_account.view_balance()

def test_deposit_function():
    bank_account = BankAccount(username='name', balance=100)

    bank_account.deposit(10)

    assert bank_account.view_balance() == 110

def test_withdraw_function_successful():
    bank_account = BankAccount(username='name', balance=100)

    bank_account.withdraw(75)

    assert bank_account.view_balance() == 25

def test_withdraw_function_overdraft():
    bank_account = BankAccount(username='name', balance=100)

    bank_account.withdraw(150)

    assert bank_account.view_balance() == WithdrawalException

def test_withdraw_function_unsuccessful():

    bank_account = BankAccount(username='name', balance=100)

    bank_account.withdraw(-50)

    assert bank_account.view_balance() == WithdrawalException
