import balance 
def add():
    amt=int(input("Enter amount to deposit"))
    balance.bal+=amt
    print("Updated Balance:",balance.bal)
    balance.statements.append(f"{amt} deposited to the account")