class Customer:
    def __init__(self, name: str, age: int, has_id: bool = None):
        self.name = name
        self.age = age
        self.has_id = has_id
    def info(self):
        return f'Client name:{self.name}, age: {self.age}, ID: {self.has_id}'
