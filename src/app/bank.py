class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []
        pass

    def open_account(self, account):
        account_number = account['number']
        assert not self._account_exists(account), f'Account number {account_number} already taken!'

        self.accounts.append(account)
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        assert amount > 0, 'Amount has to be greater than 0'
        assert self._account_exists(sender), 'Sender has no account yet!'
        assert self._account_exists(recipient), 'Recipient has no account yet!'

        transaction = {
            'sender': sender,
            'recipient': recipient,
            'subject': subject,
            'amount': amount
        }
        self.transactions.append(transaction)
        return transaction

    def _account_exists(self, account_to_search):
        matches = list(filter(
            lambda account: account == account_to_search,
            self.accounts))

        return matches and len(matches) == 1

