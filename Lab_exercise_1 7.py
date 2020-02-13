"""You live 4 miles from university .The bus drives at 25mph but spends 2min at each of the 10stops on the
 way.How long will the bus journey take ?Alternatively ,you could run to university.You jog the first mile at 7mph; then runthe nexttwo at 15 mph; before jogging the last at 7moh again.
Willthis be quicker or slower than bus?"""
a=4
t1=(a//0.41)+20
print("The time taken by bus to reach the journeyis:",t1)

t2=a//0.47
print("The time taken by boy to reach the journey is:",t2)

if t1<t2:
    print("  bus is  quicker than boy:")
else:
    print("Boy is quicker than bus:")