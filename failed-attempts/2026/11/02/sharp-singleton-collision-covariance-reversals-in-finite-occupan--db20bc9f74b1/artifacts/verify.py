"""Independent exact checks for singleton/collision covariance."""
from fractions import Fraction as F
from itertools import product
from math import comb

checks=0

def assert_equal(x,y):
    global checks
    assert x==y,(x,y)
    checks+=1

def direct(p,n):
    E_s=E_q=E_sq=F(0)
    m=len(p)
    for xs in product(range(m),repeat=n):
        w=F(1)
        for j in xs:w*=p[j]
        c=[xs.count(j) for j in range(m)]
        S=sum(v==1 for v in c)
        Q=sum(comb(v,2) for v in c)
        E_s+=w*S;E_q+=w*Q;E_sq+=w*S*Q
    return E_sq-E_s*E_q

def formula(p,n):
    s2=sum(t*t for t in p)
    if n==2:return -2*s2*(1-s2)
    return comb(n,2)*sum(t*(1-t)**(n-3)*((n-2)*(s2-t*t)-n*s2*(1-t)**2) for t in p)

def uniform(m,n):
    if n==2:
        return -2*F(1,m)*(1-F(1,m))
    return F(comb(n,2)*(m-1)*(n-2*m),m**3)*F(m-1,m)**(n-3)

def binary(p,n):
    q=1-p
    if n==2:return -2*(p*p+q*q)*(1-p*p-q*q)
    return n*(n-1)*(p*q**(n-1)+q*p**(n-1))*(n*p*q-1)

profiles=[[F(1,m)]*m for m in range(2,6)]
profiles += [[F(1,2),F(1,3),F(1,6)], [F(2,3),F(1,6),F(1,6)], [F(4,5),F(1,20),F(1,20),F(1,20),F(1,20)], [F(1,8),F(2,8),F(5,8)]]
for p in profiles:
    for n in range(2,7):
        if len(p)**n<=16000:assert_equal(direct(p,n),formula(p,n))
for m in range(2,18):
    for n in range(2,35):
        p=[F(1,m)]*m
        x=formula(p,n)
        assert_equal(x,uniform(m,n))
        assert_equal((x>0)-(x<0), (-1 if n<2*m else (0 if n==2*m else 1)))
for k in range(1,20):
    p=F(k,20);q=1-p
    for n in range(2,35):
        x=formula([p,q],n)
        assert_equal(x,binary(p,n))
        if n>=3:assert_equal((x>0)-(x<0), (n*p*q>1)-(n*p*q<1))

assert_equal(formula([F(1,2),F(1,2)],5),F(5,16))
assert_equal(formula([F(1,2),F(1,2)],4),F(0))
assert formula([F(1,10),F(9,10)],5)<0
checks+=1
print('CHECKS_PASS',checks)
