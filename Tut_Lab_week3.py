balance = 1000.0
while True:
    print('''\nATM Menu:)
                1. Check Balance
                2. Deposit Money
                3. Withdraw Money
                  4. Exit''')

    choice = int(input("Enter your choice (1-4): "))

    if choice==1:
        print(balance)
    elif choice==2:
        balance=int(input())+balance
    elif choice==3:
        balance=balance-int(input())