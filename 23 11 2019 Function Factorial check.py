def factorial(a):
    a=int(a+1)
    b=int(1)
    for i in range(1,a):
        i=int(i)
        b=b*i
    return b
print(factorial(5))
