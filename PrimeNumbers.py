#is_prime functuion to determine a prime number - true or false 
def is_prime(n):
    for l in range(2,n):
        if n%l==0:
            return False
    return True 
print(is_prime(1))
print(is_prime(20))