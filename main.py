from balance import bal , show_bal , statements , stat
from deposit import add
from withdraw import withdraw_money
def library():
    while True:
        print("\n1. To Display Balance")
        print("2. To Deposit Money")
        print("3. To Withdraw Money")
        print("4. To Check Statements")
        print("5. To exit the system")
        choice = int(input("Select your choice "))
        
        if choice==1:   show_bal()
        elif choice==2: add()
        elif choice==3: withdraw_money()
        elif choice==4: stat()
        elif choice==5: 
            print("Thank you for working with us")
            break
        else:
            print("Wrong option selected")
            
library()