from module import *
from classes import Customer
import isBob
import isAdult
def enter_club(customer) -> None:
    name = customer.name
    age = customer.age
    has_id = customer.has_id
    if isBob.is_Bob(name) == False:
        isAdult.is_Adult(age,has_id)

client1 = Customer('Bob',29,True)
client2 = Customer('James', 29,True)
client3 = Customer('Sandra',29)
client4 = Customer('Mario',20,True)

def main() -> None:
    greet()
    print('We have new clients:\n')
    print(client1.info())
    print(client2.info())
    print(client3.info())
    print(client4.info())

if __name__ == "__main__":
    main()
    print('\n')
    enter_club(client1)
    enter_club(client2)
    enter_club(client3)
    enter_club(client4)
    

    
