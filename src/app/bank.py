class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []
        pass

    def open_account(self, account):
        self.accounts.append(account)
        return account

    def add_transaction(self, sender, recipient, subject, amount):
        assert amount > 0, 'Amount has to be greater than 0'
        transaction = {
            'sender':sender,
            'recipient': recipient,
            'subject':subject,
            'amount':amount
        }
        self.transactions.append(transaction)
        return transaction


