#is_prime functuion to determine a prime number - true or false 
def is_prime(n):
    for l in range(2,n):
        if n%l==0:
            return False
    return True 
print(is_prime(1))
print(is_prime(20))


def primes_below(n):
    a=  []
    for l in range(1,n):
        if is_prime(l):
            a.append(l)
    return(a)   
print(primes_below(100))


def palindrome_primes():
    a=  []
    for l in range(10000,100000):
        if is_prime(l):
            if str(l) == str(l)[::-1]:
                a.append(l)
    return(a)
print(palindrome_primes())
