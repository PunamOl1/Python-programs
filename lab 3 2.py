x= int (input())
def fizz_fuzz(x):
 if(x%3==0) and (x%5==0):
     print ( " fizzfuzz")
 elif(x%3==0):
     print("fizz")
 elif(x%5==0):
     print(" fuzz")
 else:
     print(x)
fizz_fuzz(x)