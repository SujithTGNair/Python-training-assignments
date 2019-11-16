a=str(input())
b=a.casefold()
c=reversed(b)
print(b)
print(c)
if tuple(b)==tuple(c):
    print("The input text is palindrome")
else:
    print("the input text is not palindrome")
