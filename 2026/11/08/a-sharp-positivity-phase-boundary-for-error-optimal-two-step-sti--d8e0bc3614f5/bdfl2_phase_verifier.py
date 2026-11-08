"""Standalone reproducibility checks for the positivity frontier of optimal two-step stiff LMMs.
No external dependencies are used; exact rational identities and high-precision recurrences are checked.
"""
from fractions import Fraction as F


def coeff(k,r):
    d=3+2*k-k*k
    return (4*(1-k*k-k*r)/(d+2*r), ((1+k)*(3*k-1)-2*k*k*r)/(d+2*r))

def frontier(k):
    return (1+k)/(2*(1-k)) if k<=F(1,2) else (1-k*k)/k

def at(k,r,n):
    a,b=coeff(k,r)
    x,y=F(1),F(1)/(1+r)
    for _ in range(n): x,y=y,a*y+b*x
    return x

N=0
for k in [F(i,20) for i in range(20)]:
    edge=frontier(k)
    for r in [F(0),edge/4,edge/2,edge*F(99,100),edge]:
        x,y=F(1),F(1)/(1+r)
        a,b=coeff(k,r)
        for t in range(75):
            assert x>=0,(k,r,t,x)
            x,y=y,a*y+b*x
            N+=1

for k in [F(0),F(1,10),F(1,4),F(2,5),F(1,2),F(3,5),F(3,4),F(9,10)]:
    edge=frontier(k)
    for r in [edge*F(6,5),edge*F(3,2),edge*F(2),edge*F(5),edge*F(10)]:
        a,b=coeff(k,r)
        x,y=F(1),F(1)/(1+r)
        negative=False
        for t in range(1000):
            if x<0:
                negative=True
                break
            x,y=y,a*y+b*x
            N+=1
        assert negative,(k,r)

# Separate exact characteristic and starter-algebra certificates.
for k in [F(i,25) for i in range(25)]:
    for r in [F(j,10) for j in range(1,51)]:
        a,b=coeff(k,r)
        d=3+2*k-k*k
        delta=a*a+4*b
        assert delta*(d+2*r)**2 == 4*(1+k)**3*(1+k-2*(1-k)*r)
        z=1/(1+r)
        assert (z*z-a*z-b)*(1+r)**2*(d+2*r) == r*r*(2*k*k*r+(1+k)**2)
        assert (z-a/2)*(1+r)*(d+2*r) == 2*k*k*r+k*k+2*k*r*r+2*k*r+2*k+1
        N+=3

assert frontier(F(0))==F(1,2)
assert frontier(F(1,2))==F(3,2)
assert at(F(1,2),F(3,2),0)==1
assert at(F(1,2),F(3,2),1)==F(2,5)
assert at(F(1,2),F(3,2),2)==0
assert at(F(1,2),F(3,2),100)==0
print('PASS',N,'rational checks; boundary k=1/2,r=3/2 gives exact termination from n=2')
