"""Deterministic numerical tests for stationary opposite-tail counts of a Brownian gas.
Requires Python 3, scipy, and numpy. Run: python check.py
These checks support but do not replace the asymptotic proofs in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.special import erfc, kv

PI = math.pi

def q(b, t):
    return 0.5 * erfc(b/(2.0*math.sqrt(t))) if t > 0 else 0.0

def J_age(b):
    return quad(lambda t: math.exp(-t) * q(b,t)**2,0,math.inf,epsabs=1.e-12,epsrel=1.e-12,limit=300)[0]

def J_radial(b):
    return quad(lambda theta:(b/math.sin(theta))*kv(1,b/math.sin(theta)),0,PI/4,
                epsabs=1.e-12,epsrel=1.e-12,limit=300)[0]/PI

def F_pair(b):
    return J_radial(b)

def ncrit(b):
    p=math.exp(-b)/2
    j=F_pair(b)
    return j/(j-p*p)

def covariance(n,b):
    p=math.exp(-b)/2
    j=F_pair(b)
    return n*((n-1)*j-n*p*p)

def check():
    checks=0
    for b in (0.01,0.1,0.2,0.5,1.,2.,3.,5.,10.):
        j=J_age(b);jr=J_radial(b)
        assert abs(j-jr) < 2.e-11,(b,j,jr)
        assert j > (math.exp(-b)/2)**2,(b,j)
        checks+=2
    for b,nlo,nhi in ((0.5,9,10),(1.,3,4),(2.,1,2),(3.,1,2)):
        assert covariance(nlo,b)<0,(b,nlo)
        assert covariance(nhi,b)>0,(b,nhi)
        checks+=2
    for b in (1e-4, 3e-4,1e-3):
        n=ncrit(b)
        lead=PI/(2*b*b*math.log(1/b))
        assert 1. < n/lead < 1.35,(b,n,lead)
        checks+=1
    for b in (10.,15.,20.):
        j=F_pair(b)
        asym=(2**(-0.75)/math.sqrt(PI)) * b**(-0.5)*math.exp(-math.sqrt(2)*b)
        assert abs(j/asym-1) < 0.14,(b,j/asym)
        checks+=1
    for b in (10.,15.,20.):
        dev=ncrit(b)-1
        asym=(2**0.75*math.sqrt(PI)/4) * math.sqrt(b)*math.exp(-(2-math.sqrt(2))*b)
        assert abs(dev/asym-1)<0.2,(b,dev/asym)
        checks+=1
    for n in (1000, 10000, 100000):
        for c, expected_sign in ((1.0, -1), (5.0, 1)):
            b = math.sqrt(c/(n*math.log(n)))
            assert covariance(n,b)*expected_sign > 0,(n,c,covariance(n,b))
            checks+=1
    assert covariance(1,0.5)<0
    checks+=1
    print('PASSED',checks,'deterministic checks')
    for b in (0.5,1.,2.):
        print('b=',b,'J=',format(F_pair(b),'.12g'),'Ncrit=',format(ncrit(b),'.12g'))
if __name__ == '__main__': check()
