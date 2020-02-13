#Given the three integers,print the  smallest one.
a=int(input('Enter a first no.:'))
b=int(input("Enter a second number:"))
c=int(input('enter a third number:'))
if a<b and a<c:
    print('a is the smallest no')
elif b<a and b<c:
    print('b is the smallest no')
else:
    print('c is the smallest no')