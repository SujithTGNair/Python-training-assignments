list1=[10,11,13,-11,-3,4]
oddlist=[]
evenlist=[]
for i in list1:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print(oddlist)
print(evenlist)
