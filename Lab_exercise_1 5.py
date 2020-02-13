# A school decided to replace the desks in three classrooms.Each desk sit two students.Given the number of students in eachclass,print the smallest possible number of desks that can be purchased.
a=int(input("Enter a number of students in class first class:"))
b=int(input("Enter a no if students in class second:"))
c=int(input("Enter a no of students in class third "))
d=a//2
e=b//2
f=c//2
r=d+e+f
print("The total no. of desk to be purchased:",r)