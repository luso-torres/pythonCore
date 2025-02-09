import time

def connect() -> None:
    print('Connecting to internet...')
    time.sleep(1)
    print('You are connected!')

def greet() -> None:
    print('Hello')

def bye() -> None:
    print('Bye')

class Customer:
    def __init__(self, name, age, has_id = None):
        self.name = name
        self.age = age
        self.has_id = has_id
    def info(self):
        return f'Client name:{self.name}, age: {self.age}, ID: {self.has_id}'

if __name__ == '__main__':
    connect()