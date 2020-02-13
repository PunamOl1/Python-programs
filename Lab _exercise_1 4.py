#Given the integer N- the no. of minutes that is passed since mid night-how many hours (0-23) and minutes (0-59)are dispalyed on the 24hour digital clock
s=int(input("enter a time in minute:"))
t=s//60
u=s%60
print ("the no. of time in hour after midnight:",t)

print ("The no.of minute:",u)
