print("  welcome TO CUB Bank  ")
print("  choose your Transaction option  ")
print(" 1.withdraw ")
print(" 2.deposite ")
print(" 3. pin  ")
print(" 4.Check your Balance")
print(" 5. Exit ")
pin=1234
currentbalance=5000
password=int(input("enter the pin:"))

if password==pin:
    a=int(input("Enter your choice of Transaction:"))
    if a==1:
        b=int(input("Enter your withdraw amount:"))
        c=currentbalance-b
        print("current balance is:",c)
    elif a==2:
        d=int(input("Enter the deposite amount:"))
        e=currentbalance+d
        print("current balance is :",e)
    elif a==3:
        print("change your pin ")
        new_pin=int(input("Enter the new pin :"))
        retry_pin=int(input("Enter your pin again:"))
        if new_pin==retry_pin:
             print("Pin sccessfully changed")
        else:
            print("Please enter a same pin")
             
    elif a==4:
        f=currentbalance
        print(" Your Balance is :",f)
    elif a==5:
      
        print(" THANK YOU EXIT ")
    else:
        print(" Please Enter the Transaction between 1 to 5 ")
              

    
          
    
