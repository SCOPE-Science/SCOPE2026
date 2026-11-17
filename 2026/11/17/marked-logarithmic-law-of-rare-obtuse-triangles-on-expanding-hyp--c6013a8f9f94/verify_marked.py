"""Standalone standard-library checks of hyperbolic-circle rare-obtuseness marks.
Run: python verify_marked.py
Numerical tests corroborate, but do not replace, the analytic proof.
"""
import math
import random

PI=math.pi
rng=random.Random(12112026)

def J(q):
    ell=math.log(1/q)
    return sum(q**(2*k+1)*(ell/(2*k+1)+1/(2*k+1)**2)
               for k in range(1000))

def is_obtuse(a,b,c,q):
    return ((c>PI and math.tan(a/2)*math.tan(b/2)<q)
        or (a>PI and math.tan(b/2)*math.tan(c/2)<q)
        or (b>PI and math.tan(a/2)*math.tan(c/2)<q))

for R in (1.5,3.5):
    q=1/math.cosh(R)**2
    exact=6*J(q)/PI**2
    n=160000
    count=0
    for _ in range(n):
        r=[rng.expovariate(1) for i in range(3)]
        a,b,c=[2*PI*t/sum(r) for t in r]
        count+=is_obtuse(a,b,c,q)
    empirical=count/n
    se=math.sqrt(exact*(1-exact)/n)
    assert abs(empirical-exact)<6*se+0.002, (R,empirical,exact)
    print('radius',R,'empirical',round(empirical,6),'exact',round(exact,6))

# Independent numerical verification of the transformed-density normalization.
for q in (0.001,0.00001):
    ell=math.log(1/q)
    total=0.0
    nu=1600;nv=80;low=-3;high=4
    for i in range(nu):
        u=low+(i+0.5)*(high-low)/nu
        one=1+q**(2*u)
        for j in range(nv):
            w=(j+0.5)/nv
            total+=1/(one*(1+w*w*q**(2*(1-u))))
    total*=(high-low)/(nu*nv)
    assert abs(total-J(q)/(q*ell))<0.001, (q,total,J(q)/(q*ell))

# Test geodesic-scale formulas at fixed interior logarithmic marks.
for q in (1e-12,1e-25,1e-40):
    R=math.acosh(q**(-0.5))
    for u in (0.18,0.32,0.68,0.82):
        x=q**u;y=q**(1-u)*0.37
        a=2*math.asinh(math.sinh(R)*x/math.hypot(1,x))
        b=2*math.asinh(math.sinh(R)*y/math.hypot(1,y))
        assert abs(a/(2*R)-max(1-2*u,0))<0.13
        assert abs(b/(2*R)-max(2*u-1,0))<0.13
print('MARKED_HYPERBOLIC_CHECKS_OK')
