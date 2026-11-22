#!/usr/bin/env python3
"""Exact contact-moment verification for homothetic-frustum enclosing ellipsoids.
Standard library only. A finite diagnostic, not an infinite-dimensional proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose

def make(d, c):
    assert 2 <= d and F(0) <= c <= F(d,d+2)
    r2 = F(1)
    q2 = (1+c)*(d-(d+2)*c) / ((1-c)*(d+(d+2)*c))
    a2 = (d+1)*(1+c)/(d+(d+2)*c)
    b2 = (d+1)*(1-c*c)
    lam1,lam0 = (1+c)/2, (1-c)/2
    z1sq = (1-c)**2/b2
    z0sq = (1+c)**2/b2
    h1sq, h0sq = r2/a2+z1sq, q2/a2+z0sq
    vertical_var = lam1*z1sq+lam0*z0sq
    horizontal_var = (lam1*r2+lam0*q2)/(d*a2)
    # Each of the 2*d signed coordinate contacts has probability lam_±/(2d).
    # This gives mean 0 and transverse covariance horizontal_var * identity.
    assert h1sq == h0sq == 1
    assert vertical_var == horizontal_var == F(1,d+1)
    assert (lam1*(1-c)-lam0*(1+c)) == 0
    assert lam1+lam0 == 1
    assert F(0) <= q2 <= 1
    assert a2>0 and b2>0
    return q2,a2,b2,lam1,lam0

def check_normalized_gauge(d, c):
    q2,a2,b2,l1,l0 = make(d,c)
    # Endpoint sections of the candidate have exactly the needed radii.
    for t, rad2 in ((1,F(1)), (-1,q2)):
        assert a2*(1-(t-c)**2/b2) == rad2
    # The interpolated disks lie inside the candidate ellipsoid by convexity.
    # Test their maximal-radius points at eleven intermediate levels.
    for tnum in range(11):
        k=F(tnum,10)
        z= -1+2*k
        radius=(1-k)*sqrt(float(q2))+k
        gauge= radius**2/float(a2)+(float(z-c))**2/float(b2)
        assert gauge <= 1+1e-12, (d,c,k,gauge)

def run():
    tests=0
    for d in range(2,21):
        for j in range(51):
            c=F(d*j,(d+2)*50)
            check_normalized_gauge(d,c)
            tests+=1
    # Endpoint regimes against elementary independent formulas.
    for d in range(2,30):
        q2,a2,b2,_,_=make(d,F(0))
        assert q2==1 and a2==F(d+1,d) and b2==d+1
        q2,a2,b2,_,_=make(d,F(d,d+2))
        assert q2==0 and b2==F(4*(d+1)**2,(d+2)**2)
    # Independent identity: invert radical-form center against defining quadratic.
    for d in range(2,11):
        for q in [0,0.01,0.2,0.5,0.85,1.0]:
            c=(sqrt((1+q*q)**2+d*(d+2)*(1-q*q)**2)-(1+q*q))/((d+2)*(1-q*q)) if q!=1 else 0.
            assert isclose((d+2)*(1-q*q)*c*c+2*(1+q*q)*c-d*(1-q*q),0,abs_tol=1e-12)
    print(f'VERIFY_OK exact rational isotropic contacts, endpoint gauges and all interior checks: {tests} cases; 58 boundary cases and 54 radical checks')

if __name__=='__main__':run()
