a=[1,2,3,4,5,6,7,8]
b=sum(a)
c=len(a)
print(b)
print(c)
print (b/c)
a.sort()
print(a)
print(a)
if (c%2)!=0:
    d=int(c/2)
    print(d)
    print (a[d])
else:
    d=int(c/2-1)
    print(d)
    print(a[d])
print (max(a))
print (min(a))

if (max(a))==(min(a)):
             print("both number are same")
else:
    print("both number are different")
