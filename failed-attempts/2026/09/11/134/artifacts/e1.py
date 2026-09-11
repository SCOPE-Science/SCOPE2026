from fractions import Fraction as F
def theta(p):
    x,y=p
    return (F(1,1)/(x*y), x/(1+x*y))
p=(F(1),F(1))
seen=[]
for i in range(12):
    seen.append(p)
    p=theta(p)
    print(i, p[0], p[1])
print("distinct:", len(set(seen)))
