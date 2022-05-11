for x in range(1,1001):
    s = ""
    if x%3 == 0 and x%5 == 0:
        s = "Fizzbuzz"
    elif x % 3 == 0:
        s = "Fizz"
    elif x % 5 == 0:
        s = "Buzz"
    elif s == "":
        s = x
    print (s)