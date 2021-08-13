class Atm(object):
        def __init__(self,atmcardnumber,pinumber):
                self.atmcardnumber = atmcardnumber
                self.pinumber = pinumber

        def CashWithdrawl(self):
                print("You have withdrawn 2000")
        def BalanceEnquiry(self):
                print("ou have balance 8000")

account = Atm("1234","9876")
print(account.atmcardnumber)
print(account.pinumber)

