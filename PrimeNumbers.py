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



a=input('enter a string :')# palindrome in string
b=a[::-1]
if a==b:
    print(a,'is a palindrome')
else:
    print(a,'is not a palindrome')
    print('a is not equal to b')
if a!=b:
    print(b, 'the reverse of', a)
#output: