n=int(input())
o=str(n)
p=len(o)
q=[]
for i in range(0,p):
    a=o[i]
    a=int(a)
    b=a**p
    q.append(b)
c=sum(q)
if c==n:
    print("This is a armstrong number")
else:
    print("This is not a armstrong number")

    
