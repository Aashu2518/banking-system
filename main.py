bal=0

while True:
    print("1.Deposit 2.Withdraw 3.Balance 4.Exit")
    c=input()

    if c=="1":
        bal+=int(input("Amount: "))
    elif c=="2":
        bal-=int(input("Amount: "))
    elif c=="3":
        print("Balance:",bal)
    else:
        break
