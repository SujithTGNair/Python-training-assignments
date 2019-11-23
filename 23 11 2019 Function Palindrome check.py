def checkpalindrome(x):
    x=str()
    y=x.casefold()
    z=reversed(y)
    if list(y)==list(z):
        a="This is a palindrome string"
    else:
        a="This is not a palindrome string"
    return a
print(checkpalindrome("malayalam"))
