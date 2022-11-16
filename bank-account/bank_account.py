import threading


class BankAccount:
    def __init__(self):
        self.opened = False
        self.balance = 0
        self.closed = True