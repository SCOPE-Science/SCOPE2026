"""Reproducibility checks for a quantitative hexagonal rigidity theorem.

Run: python checker.py. The proof is analytic; finite tests are consistency checks.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
import random

def bounds(delta):
    assert F(0) <= delta <= F(1,100)
    u=4*delta/(F(9,2)+delta)
    eps=(1+F(2,3)*delta)*(1+u/F(2))-1
    eta=2*u+eps
    h=2*(eta+eps)
    assert u<=delta
    assert eps<=F(6,5)*delta
    assert h<=9*delta
    assert (1+F(6,5)*delta)/(1-9*delta)<=1+12*delta

def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def norm(z, rows): return max(abs(a*z[0]+b*z[1]) for a,b in rows)

def vertices(rows):
    constraints=rows+ [(-a,-b) for a,b in rows]
    out=set()
    for i,(a,b) in enumerate(constraints):
        for c,d in constraints[i+1:]:
            det=a*d-b*c
            if det==0: continue
            x,y=(d-b)/det,(a-c)/det
            if all(s*x+t*y<=1 for s,t in constraints): out.add((x,y))
    return out

def case(rows):
    v=((F(1),F(1,2)),(F(-1,2),F(1,2)),(F(-1,2),F(-1)))
    vn=[norm(z,rows) for z in v]
    t=max(norm((v[i][0]-v[j][0],v[i][1]-v[j][1]),rows)/vn[k]
          for i,j,k in [(0,1,2),(1,2,0),(2,0,1)])
    assert t >= F(3,2)
    delta=t-F(3,2)
    if delta>F(1,100): return False
    c=sum(vn)/3
    q1=((v[0][0]-v[1][0])/(F(3,2)*c), (v[0][1]-v[1][1])/(F(3,2)*c))
    q2=((v[1][0]-v[2][0])/(F(3,2)*c), (v[1][1]-v[2][1])/(F(3,2)*c))
    # Given z=x*q1+y*q2, its canonical hexagonal gauge is max(|x|,|y|,|x-y|).
    det=cross(q1,q2)
    def N_H(z):
        x=cross(z,q2)/det
        y=cross(q1,z)/det
        return max(abs(x),abs(y),abs(x-y))
    assert all(norm(z,rows)<=1+F(6,5)*delta for z in (q1,q2,(q1[0]+q2[0],q1[1]+q2[1])))
    outer=1/(1-9*delta)
    assert all(N_H(z)<=outer for z in vertices(rows))
    return True

for i in range(101): bounds(F(i,10000))
base=[(F(1),F(0)),(F(0),F(1)),(F(1),F(-1))]
assert case(base)
rng=random.Random(20261114)
checked=1
for j in range(500):
    rows=[]
    for a,b in base:
        scale=F(rng.randrange(997,1004),1000)
        rows.append((a*scale,b*scale))
    # Optional weak extra support inequalities, potentially cutting corners.
    for k in range(2):
        x=F(rng.randrange(-100,101),100)
        y=F(rng.randrange(-100,101),100)
        rows.append((x/F(2),y/F(2)))
    checked+=int(case(rows))
assert checked>=100
print('PASS: 101 exact rational coefficient checks and',checked,'polygon cases')
