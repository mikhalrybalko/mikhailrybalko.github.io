
def my_range(m,n):
    result=[]
    while n > m:
        result.append(m)
        m=m+1
    return result 
print (my_range(100,120))


def my_reverse(l):
    result=[]
    for n in l:
        result = [n] + result
    return result 
print (my_reverse([1,2,3,4,5])) 
