print("wellcome to the Republic of Turkey Ziraat Bank ")
print(" what is the action you want to do ? ")
seçenekler="""
1-deposit
2-witdraw money
3-balance viewing
4-send money
5-exit
"""
balance=10000
while True:
    choice=( input ("enter choice  1/2/3/4/5 :"))

    if choice =="5":
        print("Exiting Transactions are being recorded")
        print("Have a nice day...")
        break
    else:    
        amount=float(input("enter the amount of money :"))

    if choice == "1":
        print( "yeni balance :", balance + amount)
        balance += amount
    elif choice == "2":
        if balance<amount:
            print("insufficient balance: ",balance)
        else:    
            print("new balance :",balance - amount) 
        balance -= amount 
    elif choice =="3":
        print ("balance :",balance)
    elif choice =="4":
        if balance<amount:
            print("insufficient balance ,  balance : ",balance)
        else:    
            print ("available balance :",balance - amount) 
            balance -= amount 
            

           
    
        
