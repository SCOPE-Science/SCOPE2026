from fractions import Fraction as F
# exact orbit ledger already in e1.py; extend + height check
def theta(p):
    x,y=p
    return (F(1,1)/(x*y), x/(F(1,1)+x*y))
p=(F(1),F(1))
pts=[]
for i in range(16):
    pts.append(p)
    p=theta(p)
for i,q in enumerate(pts):
    print(i, q[0], q[1], len(str(q[0])), len(str(q[1])))
print("distinct:", len(set(pts)))
# check positivity: all coords >0
print("all positive:", all(a>0 and b>0 for a,b in pts))
