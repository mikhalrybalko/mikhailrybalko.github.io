
def my_range(m,n):
    result=[]
    while n > m:
        result.append(m)
        m=m+1
    return result 
print (my_range(100,120))