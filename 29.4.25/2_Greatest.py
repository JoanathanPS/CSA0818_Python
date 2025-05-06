a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
c=float(input("Enter a number:"))


if(a<b):
    if(b<c):
        print("The greatest is",c)
    else:
        print("The greatest is",b)
else:
    if (a<c):
        print("The greatesr is",c)
    else:
        print("The greates is",b)
