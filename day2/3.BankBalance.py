c_balance=1000
def credit(c_balance,credits):
    c_balance=c_balance+credits
    print(f"Rs.{credits} is credited to your A/c and bal:{c_balance}")

def debit(c_balance,debits):
    c_balance-=debits
    print(f"Rs.{debits} is debitted from your A/c and bal:{c_balance}")

credit(c_balance,100)
debit(c_balance,200)