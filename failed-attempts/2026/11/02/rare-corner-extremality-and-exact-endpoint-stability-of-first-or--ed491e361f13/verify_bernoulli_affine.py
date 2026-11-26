#!/usr/bin/env python3
"""Finite exact checks for weighted-product first-order ANOVA projections."""
from fractions import Fraction as F
from itertools import product
from math import comb, exp, factorial, pi, sqrt


def probability(y, p):
    a=F(1)
    for yi,pi in zip(y,p):
        a*=pi if yi else 1-pi
    return a


def kernel(x,y,p):
    return F(1)+sum((xi-pi)*(yi-pi)/(pi*(1-pi)) for xi,yi,pi in zip(x,y,p))


def exact_rare(p):
    r=[min(pi,1-pi) for pi in p]
    v=F(0)
    for y in product((0,1),repeat=len(p)):
        v+=probability(y,r)*abs(sum((F(yi)/ri for yi,ri in zip(y,r)),F(0))-(len(p)-1))
    return v


def brute_rows(p):
    points=list(product((0,1),repeat=len(p)))
    weights=[probability(y,p) for y in points]
    rows=[]
    for x in points:
        entries=[kernel(x,y,p) for y in points]
        rows.append(sum((w*abs(k) for w,k in zip(weights,entries)),F(0)))
        assert sum((w*k for w,k in zip(weights,entries)),F(0))==1
    return max(rows),rows


def homogeneous_formula(n,r):
    return sum((F(comb(n,j))*r**j*(1-r)**(n-j)*abs(F(j)/r-(n-1))
               for j in range(n+1)),F(0))


def central_formula(n):
    m=n//2
    return F((2*m+1)*comb(2*m,m),4**m)

count=0
params=[F(1,7),F(1,4),F(2,5),F(1,2),F(3,5),F(5,6)]
for n in range(1,6):
    from itertools import islice
    for idx,values in enumerate(product(params,repeat=n)):
        if n>=3 and idx % max(1,(len(params)**n)//(75 if n==3 else 35)) != 0:
            continue
        b,rows=brute_rows(values)
        a=exact_rare(values)
        assert b==a,(values,b,a)
        count+=len(rows)*2**n
for n in range(1,19):
    assert homogeneous_formula(n,F(1,2))==central_formula(n)
    for r in [F(1,7),F(1,4),F(2,5)]:
        assert F(1)<=homogeneous_formula(n,r)<=2*n-1
    count+=4

for n in range(2,6):
    for r in [F(1,10),F(1,4),F(2,5)]:
        for i in range(n):
            p=[r]*n
            larger=p[:]
            larger[i]=F(1,2)
            assert exact_rare(larger)<=exact_rare(p)
            count+=1

for n in range(2,5):
    p=[F(1,3)+F(i,30) for i in range(n)]
    pts=list(product((0,1),repeat=n))
    # Independent projection formula using conditional means, checked on point masses.
    for y in pts:
        for x in pts:
            got=probability(y,p)*kernel(x,y,p)
            expected=probability(y,p)*(1-n)
            for i in range(n):
                if x[i]==y[i]:
                    expected+=probability(y,p)/(p[i] if y[i] else 1-p[i])
            assert got==expected,(n,x,y,got,expected)
            count+=1

# Independent direct row and sign witness at an unsymmetric weight profile.
p=[F(1,5),F(3,7),F(4,5),F(1,3)]
r=[min(pi,1-pi) for pi in p]
xstar=tuple(1 if pi<=F(1,2) else 0 for pi in p)
pts=list(product((0,1),repeat=len(p)))
sgn={y:(1 if kernel(xstar,y,p)>=0 else -1) for y in pts}
attained=sum((probability(y,p)*kernel(xstar,y,p)*sgn[y] for y in pts),F(0))
assert attained==exact_rare(p)
# Worst positive-input undershoot is half of the excess projection norm.
f={y:(1 if kernel(xstar,y,p)<0 else 0) for y in pts}
negative_projection=sum((probability(y,p)*kernel(xstar,y,p)*f[y] for y in pts),F(0))
assert negative_projection==-(exact_rare(p)-1)/2
count+=2

# Limit profiles (diagnostic, not a substitute for the asymptotic proof).
for lam in [F(1,2),F(1),F(3,2),F(2),F(11,4)]:
    n=500
    r=lam/n
    value=float(homogeneous_formula(n,r))/n
    k=(lam.numerator+lam.denominator-1)//lam.denominator-1
    target=2*exp(-float(lam))*float(lam)**k/factorial(k)
    assert abs(value-target)<.014,(lam,value,target)
    count+=1
print('PASS checks=',count, 'random asymmetric sharp norm=',attained,
      'positive undershoot=',negative_projection)
