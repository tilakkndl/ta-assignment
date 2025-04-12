def reversal(str):
    return str[::-1]

def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        factorial(num-1)


def prime_checking(num):
    if num==0 or num==1 or num==2:
        return False
    is_prime=True
    for x in range(2,num):
        if num%x==0:
            is_prime=False
            return is_prime
    
    return is_prime