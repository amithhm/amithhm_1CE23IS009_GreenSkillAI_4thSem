'''Find Prime numbers from 0 to 50.
Segrgate those into odd and even'''
def is_eoro(num):
    if num%2==0:
        return True
    else:
        return False
def is_prime(num):
    k=0
    if num<=1:
        return False
    else:
        for i in range(2,((num**0.5)+1)):
            if num%i==0:
                k=1
                break
        if k==0:
            return True
        else:
            return False
even=[]
odd=[]    
for num in range(51):
    if is_prime(num):
        if is_eoro(num):
            even.append(num)
        else:
            odd.append(num)
print("\nThe EVEN Prime numbers are:\n",even,"\n")
print("\nThe ODD Prime numbers are:\n",odd,"\n")