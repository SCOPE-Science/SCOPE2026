"""Exhaustive small-graph and exact-series checks for two- and three-cycle counts."""
from fractions import Fraction
from itertools import product
from math import factorial
checks=0

def h(n,p=1):
    return sum((Fraction(1,j**p) for j in range(1,n+1)), Fraction(0))

def theorem(n):
    a=h(n-1); b=h(n-1,2); c=h(n-1,3); d=h(n-1,4)
    ed=a
    vd=a-b
    et=4*(a-b)
    vt=et+4*sum((h(t-1)/Fraction(t*t) for t in range(2,n)),Fraction(0))-16*(b-2*c+d)
    cov=-4*(b-c)
    return (ed,vd,et,vt,cov)

states=[((),0,0)]
for n in range(2,7):
    newstates=[]
    for old,doubles,tri in states:
        edges=dict(old)
        for u,v in product(range(1,n),repeat=2):
            inc=edges.get((min(u,v),max(u,v)),0) if u!=v else 0
            out=dict(edges)
            for target in (u,v):
                e=(target,n)
                out[e]=out.get(e,0)+1
            newstates.append((tuple(sorted(out.items())),doubles+int(u==v),tri+inc))
    states=newstates
    M=len(states)
    assert M==factorial(n-1)**2
    ED=Fraction(sum(a for _,a,_ in states),M)
    ET=Fraction(sum(b for _,_,b in states),M)
    VD=Fraction(sum(a*a for _,a,_ in states),M)-ED*ED
    VT=Fraction(sum(b*b for _,_,b in states),M)-ET*ET
    CT=Fraction(sum(a*b for _,a,b in states),M)-ED*ET
    got=(ED,VD,ET,VT,CT)
    predicted=theorem(n)
    for x,y in zip(got,predicted):
        assert x==y,(n,got,predicted)
        checks+=1
    print('n',n,'histories',M,'moments',*(str(x) for x in got))

# Sign of the limiting 3-cycle variance correction, using finite rational bounds.
N=100
z2lo=h(N,2)
z4lo=h(N,4)
z3hi=h(N,3)+Fraction(1,2*N*N)
assert 36*z3hi-16*z2lo-16*z4lo < 0
checks+=1
# Exact sign certificate for every n: local increments change sign once.
for t in range(3,32):
    delta=h(t-1)-4*(Fraction(t-1,t)**2)
    assert (delta<0 if t<=21 else delta>0)
    checks+=1
assert h(31)>4
checks+=1
# With the limiting deficit strictly negative, the finite correction is
# negative before and after its single minimum.
# Each finite-n covariance is strictly negative once triangles are possible.
for n in range(4,101):
    assert theorem(n)[4]<0
    checks+=1
print('Rational upper bound on asymptotic variance-minus-mean:',float(36*z3hi-16*z2lo-16*z4lo))
print('PASS',checks,'finite assertions')
