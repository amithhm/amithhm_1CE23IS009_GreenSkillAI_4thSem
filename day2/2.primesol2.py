def is_prime(n):
    k=0
    if n<=1:
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
even=[]
odd=[]
mo3=[]
range_upto=int(input("\nEnter 0 to n to find prime numbers:\n"))
for i in range(range_upto):
    if is_prime(i):
        if i%2==0:
            even.append(i)
        else:
            if i%3==0:
                mo3.append(i)
            odd.append(i)
print(f"even primes: {even}")
print(f"odd primes: {odd}")
print(f"multiple of 3 in primes: {mo3}\n")
