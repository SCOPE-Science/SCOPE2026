"""Checks for a lattice walk with a partially reactive trap and Poisson resetting.
Only independent algebraic and finite-parameter checks; no numerical test proves the universal theorem.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def model(m,k,q):
    r=(1-q)**2/q
    delta=(1-q*q)/q
    f=k*q**m/(k+delta)
    return (1/f-1)/r

def closed(m,k,q):
    a=1+q+k*sum((q**j for j in range(1,m+1)),F(0))
    return a/(k*q**m*(1-q))

def p_poly(m,k,q):
    p0=-m+2*q+m*q*q
    p1=-(m-1)*q+2*sum((q**j for j in range(2,m+1)),F(0))+q**(m+1)
    return p0+k*p1

def derivative_exact(m,k,q):
    a=1+q+k*sum((q**j for j in range(1,m+1)),F(0))
    ap=1+k*sum((j*q**(j-1) for j in range(1,m+1)),F(0))
    return (q*(1-q)*ap-(m-(m+1)*q)*a)/(k*q**(m+1)*(1-q)**2)

def bisect(m,k):
    l=0.; u=1.
    for j in range(90):
        t=(l+u)/2
        if p_poly(m,k,t)<0:l=t
        else:u=t
    return (l+u)/2

checks=0
for m in range(1,17):
    for k in [F(1,10),F(1,2),F(1),F(2),F(5),F(29,7)]:
        for q in [F(1,9),F(1,3),F(2,5),F(3,4),F(8,9)]:
            assert closed(m,k,q)==model(m,k,q)
            checks+=1
            h=F(1,1_000_000)
            # algebraically independent derivative by quotient rules
            a=1+q+k*sum((q**j for j in range(1,m+1)),F(0))
            d=q**m*(1-q)
            ap=1+k*sum((j*q**(j-1) for j in range(1,m+1)),F(0))
            dp=q**(m-1)*(m-(m+1)*q)
            exact=(ap*d-a*dp)/(k*d*d)
            assert exact==derivative_exact(m,k,q)
            assert exact==p_poly(m,k,q)/(k*q**(m+1)*(1-q)**2)
            checks+=2

for m in range(1,13):
    last=1.0
    for k in [0.001,0.01,0.1,0.3,1,2,5,10,100,10000]:
        q=bisect(m,k)
        assert q<last
        last=q
        assert abs(p_poly(m,k,q))<max(1,m*k)*1e-10
        h=min(1e-5,q/100,(1-q)/100)
        assert closed(m,k,q-h)>closed(m,k,q)*(1-1e-10)
        assert closed(m,k,q+h)>closed(m,k,q)*(1-1e-10)
        checks+=4
    q0=(sqrt(1+m*m)-1)/m
    assert last<q0
    if m==1:
        for k in [0.01,.1,1,5,100,1e5]:
            s=sqrt(k+2)
            q=1/(1+s)
            r=s*s/(1+s)
            assert isclose(q,bisect(m,k),rel_tol=1e-12)
            assert isclose(closed(1,k,q),(1+s)**2/k,rel_tol=1e-12)
            assert isclose(r,(1-q)**2/q,rel_tol=1e-12)
            checks+=3
    else:
        # Perfect absorber stationary polynomial has a unique root in (0,1).
        l=0.0; u=1.0
        for _ in range(80):
            q=(l+u)/2
            v=-(m-1)+2*sum(q**j for j in range(1,m))+q**m
            if v<0:l=q
            else:u=q
        qinf=(l+u)/2
        assert qinf<last<q0
        checks+=1
print('PASS',checks,'exact/numerical assertions')
