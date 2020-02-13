"""n students take k apples and distributts them among each other evenly.The reaming (the undivisible)part remains inthe basket.How many apples will each single students get?How many apples will remain
in the basket ?The programmmer reads thenumber N and k.it should print the two answer of the abive questions above."""
d=int (input ("enter no of students:"))
p=int(input ("enter a no. apple:"))
s=p//d
n=p%d
print ("the no.of apples received by individual students:",s)
print("The no. of reamining apples in the basket:",n)