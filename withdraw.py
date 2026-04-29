import balance
def withdraw_money():
    money=int(input("Enter amount to withdraw"))
    if money==0:
        print("Enter Valid Amount")
    elif money<=balance.bal:
        balance.bal-=money
        print("Withdraw Successfull \nRemaining Balance is",balance.bal)
        balance.statements.append(f"{money} withdrew from the amount")
    
    else:
        print("Insuffcient balance")    