import uuid
import time

class Transaction:
    def __init__(self, *, sender, recipient, subject, amount, category):
        assert type(sender) == int, 'Sender needs to be an integer'
        assert type(recipient) == int, 'Recipient needs to be an integer'
        assert type(amount) == float, 'Amount needs to be a float'
        assert amount > 0, 'Amount needs to be greater than 0'

        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.amount = amount
        self.category = category
        self.id = uuid.uuid4()
        self.timestamp = time.time()
        self.time = time.strftime("%Y-%m-%d %H:%M:%S")

    def info(self):
        return f'Transaction-ID: {self.id}. Timestamp: {self.timestamp}. Time: {self.time}. From {self.sender} to {self.recipient}: {self.subject} (category: {self.category}) - {self.amount} €'
