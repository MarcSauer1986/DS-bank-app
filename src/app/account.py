class Account:
    def __init__(self, *, firstname, lastname, number, balance=0.0):
        assert type(number) == int, 'Number needs to be an integer'
        assert type(balance) == float, 'Balance needs to be a float'

        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance

    def info(self):
        return f'Number {self.number}: {self.firstname} {self.lastname} - {self.balance} €'

    def has_funds_for(self, amount_to_compare):
        return amount_to_compare <= self.balance

    def add_to_balance(self, add_money):
        assert add_money > 0, 'Amount needs to be greater than 0'
        self.balance = self.balance + add_money

    def subtract_from_balance(self, subtract_money):
        assert subtract_money < self.balance, 'Account has not enough funds'
        self.balance = self.balance - subtract_money
