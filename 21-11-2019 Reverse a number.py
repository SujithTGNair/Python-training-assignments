n=int(input())
v=""
while n>1:
    if n>10:
        a=n%10
        a=str(a)
        v=v+a
        n=n//10
    else:
        n=str(n)
        v=v+n
        break
print(v)
