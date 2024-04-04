from Exceptions import BalanceRetrievalException, InternalDepositException, WithdrawalException


class BankAccount:
    """
    A class used to represent a bank account
    ...

    Attributes
    ----------
    username : str
        the username of the current person banking
    balance : float
        the amount of money in the bank

    Methods
    -------
    transactionOption()
        Asks for input on what the user wants to do,
        based on the option it runs the expected function.
        If anything other than exit, function loops.
    leave()
        Prints thank you and exits the transaction_options loop.
    viewBalance()
        Returns the amount stored in the bank account
    deposit()
        Add funds to your bank account
    withdraw()
        Remove funds from your bank account
    """

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def transaction_options(self):
        print('\n[1] View Balance')
        print('[2] Deposit')
        print('[3] Withdraw')
        print('[4] Exit')
        try:
            select = int(input('Select an option: '))
        except ValueError:
            print('invalid input')
            return
        if select == 1:
            try:
                bal = BankAccount.view_balance(self)
                print('\nCurrent Balance: $' + str(bal))
            except BalanceRetrievalException:
                print("Error getting balance")
        elif select == 2:
            try:
                amount = float(input('Enter the deposit amount: '))
                BankAccount.deposit(self, amount)
                print('\nDeposit successful!')
            except InternalDepositException:
                print("Deposit error")
        elif select == 3:
            try:
                amount = float(input('Enter the withdrawal amount: '))
                BankAccount.withdraw(self, amount)
                print('\nWithdrawal successful!')
            except WithdrawalException:
                print('Withdraw error')
        elif select == 4:
            BankAccount.leave(self)
            return

    def leave(self):
        """
        print thank you and then leave the transaction loop (call quit())
        """
        print('\nThank You')
        quit()


    def view_balance(self):
        """
        return the bank account's current balance without doing any transaction

        Returns
        -------
        your account balance
        """
        try:
            if self.balance < 0:
                raise BalanceRetrievalException
            return self.balance
        except:
            raise BalanceRetrievalException

    def deposit(self, amount):
        # TODO implement function

        self.balance = self.balance + amount
        """
        This function should handle adding money to the bank.
        It takes an amount (should be int or float) and will add that to the existing account balance.
        If there is an error raise an InternalDepositException
        Parameters
        ----------
        amount: float
            Dollar amount depositing

        Returns
        -------
        The bank account's total balance after deposit

        Raises
        ------
        InternalDepositException
            when amount is negative or NaN
        """
        pass

    def withdraw(self, amount):
        # TODO implement function
        
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
        else:
            raise WithdrawalException

        """
        This function handles taking money out of the bank.
        It takes a numeric amount, and will remove that from the existing account balance if it is less than the balance.
        If there is an error raise a WithdrawalException

        Parameters
        ----------
        amount: float
            Dollar amount withdrawing

        Returns
        -------
        The bank account's total balance after withdraw

        Raises
        ------
        WithdrawalException
            When amount is negative, NaN or > the account balance
        """
        pass


if __name__ == '__main__':
    bank_account = BankAccount(username='name', balance=100)
    while True:
        bank_account.transaction_options()
