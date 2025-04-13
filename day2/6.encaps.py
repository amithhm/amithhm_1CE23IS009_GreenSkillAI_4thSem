class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def balance(self):
        print(f"Rs.{self.__balance}/-")
b=Bank(52000)
b.balance()
        