from hashlib import sha256
import json

Class block:
    def __init__(self, index, transactions, timestamp):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp

