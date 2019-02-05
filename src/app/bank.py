class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        assert account not in self.accounts, 'Account number 1 already taken!'
        self.accounts.append(account)
        return account

    def add_transaction(self, sender, recipient, subject, amount):
        _transaction = {
            'sender':sender,
            'recipient': recipient,
            'subject': subject,
            'amount': amount
        }
        assert amount > 0, 'Amount has to be greater than 0'
        self.transactions.append(_transaction)
        return _transaction








