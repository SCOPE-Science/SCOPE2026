"""Finite diagnostics for the small-regularity-endpoint RPS theorem.
Not a substitute for the proof of the arbitrary-sample-size asymptotic.
Uses only Python 3 and SymPy (SymPy needed for exact determinants).
"""
from math import comb, log, sqrt, pi, gamma, isclose
from random import Random
from sympy import Matrix, eye, ones, Rational, binomial, simplify


def rps(spacings):
    a=list(spacings); r=0.
    while len(a)>1:
        r-=sum(log(x) for x in a)
        b=[a[i]+a[i+1] for i in range(len(a)-1)]
        t=sum(b); a=[x/t for x in b]
    return r


def smooth_RPS(spacings):
    m=len(spacings); r=0.
    for k in range(m-1):
        j=m-k
        b=[sum(comb(k,h)*spacings[i+h] for h in range(k+1)) for i in range(j)]
        t=sum(b)
        r-=sum(log(x/t) for x in b)
    return r


def q_matrix(m):
    h=Matrix.zeros(m,m)
    for k in range(m-1):
        j=m-k
        b=Matrix(j,m,lambda i,l:binomial(k,l-i) if 0<=l-i<=k else 0)
        p=eye(j)-ones(j,j)/j
        h+=Rational(m*m,4**k)*b.T*p*b
    a=Matrix(m,m-1,lambda i,l: 1 if i==l else (-1 if i==m-1 else 0))
    return a.T*h*a

rng=Random(20261118)
checks=0
for m in range(2,11):
    q=q_matrix(m)
    assert all(q[:i,:i].det()>0 for i in range(1,m))
    checks+=m-1
    rmin=sum(j*log(j) for j in range(2,m+1))
    assert isclose(rps([1/m]*m),rmin,rel_tol=1e-12)
    checks+=1
    for _ in range(20):
        v=[rng.random()+0.01 for _ in range(m)]
        s=[x/sum(v) for x in v]
        assert isclose(rps(s),smooth_RPS(s),rel_tol=2e-13)
        assert rps(s)>rmin-1e-12
        checks+=2
    # Compare the exact quadratic form with true RPS for small deviations.
    for scale in [1e-4,3e-5,1e-5]:
        v=[rng.uniform(-1,1) for _ in range(m-1)]
        v.append(-sum(v))
        s=[1/m+scale*x for x in v]
        quadratic=0.5*float((Matrix(v[:-1]).T*q*Matrix(v[:-1]))[0])*scale**2
        remainder=rps(s)-rmin
        assert abs(remainder-quadratic)<(10*m**5*scale**3 + 4e-11), (m,quadratic,remainder)
        checks+=1
    # The recursion makes the regularity-tail coefficient strictly smaller
    # than that of the Moran statistic for m >= 3.
    moran_det=m**(2*(m-1)+1)
    assert q.det()==moran_det if m==2 else q.det()>moran_det
    checks+=1
assert q_matrix(2).det()==8
assert q_matrix(3).det()==Rational(1215,4)
assert isclose(8*pi/sqrt(1215),0.7210273201730866,rel_tol=1e-13)
checks+=3
print('PASS',checks,'finite checks; exact Hessian determinants m=2..10; m=3 constant 8*pi/sqrt(1215)')
for m in range(2,6):
    q=q_matrix(m)
    d=m-1
    volume=pi**(d/2)/gamma(d/2+1)
    coefficient=__import__('math').factorial(d)*volume*2**(d/2)/sqrt(float(q.det()))
    print('m=',m,'det=',q.det(),'C=',format(coefficient,'.12g'))
