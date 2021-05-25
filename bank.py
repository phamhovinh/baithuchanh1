class bank:
    account_type="savings"
    location="guntur"
    def__init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.account_type=bank.account_type
        self.location=bank.location

    def_repr_(self):
        print("wellcome to the SBI ATM machine")
        print("-------------------------------")
        account_pin=int(input('please enter your pin number"))
        if (account_pin==123):
                              account(self)
        else:
            print("pin incorrect.please try again")
            error(self)
            return ' '.join([self.name,self.account_number])
    def error(self):
        account_pin=int(input("please enter your pin number"))
        if(account_pin==123):
            account(self)
        else:
            print("pin incorrect. please try again")
            errol(self)
    def account(self):
        print("your card number is:XXXX XXXX XXXX 1337")
        print("would you like to desposit/withdraw/check balance?")
        print("""
1) balance
2) withdraw
3) deposit
4) quit
""")
        option=int(input("please enter your choice:")
        if(option==1):
                   balance(self)
        elif(option==2):
            withdraw(self)
        elif(option==3):
            deposit(self)
        elif(option==4):
            exit()
    def balance(self):
        print("balance:"self.balance)
        account(self)
    def withdraw(self):
        w=int(input("please enter desired amount:"))
        if(self.balance>0 and self.balance>=w):
            self.balance=self.balance-w
            print("your transaction is successfull")
            print("your balance:",self.balance)
            print("")
        else:
            print("your transaction is cancelled due to ")
            print("amount is not sufficient in your account")
        account(self)
        def exit():
            print("exit")
        t1=bank('mahesh,1453210145,5000)
        print(t1)
