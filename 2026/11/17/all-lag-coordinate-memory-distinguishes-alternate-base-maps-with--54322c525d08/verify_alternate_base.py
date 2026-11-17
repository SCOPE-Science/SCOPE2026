"""Exact rational checks of covariance formulas for periodically alternating beta maps.
Only Python standard library. Run: python verify_alternate_base.py
"""
from fractions import Fraction as F


def sawtooth(beta):
    # Piecewise affine representation of x -> fractional_part(beta*x), 0<=x<1.
    a = beta.numerator // beta.denominator
    cuts = [F(0)] + [F(j, 1) / beta for j in range(1, a+1)] + [F(1)]
    return [(cuts[j], cuts[j+1], beta, -F(j)) for j in range(a+1)]


def nested(beta, Q):
    # x -> fractional_part(beta*fractional_part(Q*x)); Q positive integer.
    basic = sawtooth(beta)
    out=[]
    for j in range(Q):
        for lo,hi,slope,intercept in basic:
            out.append(((j+lo)/Q,(j+hi)/Q,Q*slope,intercept-slope*j))
    return out


def integ(one, two):
    # Integrate the product of two piecewise affine functions over [0,1].
    i=j=0
    z=F(0)
    while i<len(one) and j<len(two):
        x0,x1,a,b=one[i]
        y0,y1,c,d=two[j]
        lo=max(x0,y0);hi=min(x1,y1)
        if lo<hi:
            z += a*c*(hi**3-lo**3)/3 + (a*d+b*c)*(hi**2-lo**2)/2 + b*d*(hi-lo)
        if x1 <= y1:i+=1
        if y1 <= x1:j+=1
    return z


def mean(f):
    return integ(f, [(F(0),F(1),F(0),F(1))])


def cov(f,g):
    return integ(f,g)-mean(f)*mean(g)


def check(p,q,k):
    assert p>q>=2 and __import__('math').gcd(p,q)==1
    beta=F(p,q); n=k*q;N=k*p
    a=p//q;r=beta-a
    mu=(a+r*r)/(2*beta)
    A=(a*(1-3*r+3*r*r)+r**3)/(12*beta**2)
    delta=r*(1-r)/(4*beta)
    U=[(F(0),F(1),F(1),F(0))]
    f=sawtooth(beta)
    assert mean(f)==mu
    assert cov(U,f)==A
    checks=2
    for t in range(1,3):
        Q=N**t
        direct=delta**2+(cov(U,sawtooth(F(Q,1)))+cov(f,nested(beta,Q)))/2
        predicted=delta**2+(F(1,24)+beta*A/2)/Q
        assert direct==predicted,(p,q,k,t,'even',direct,predicted)
        checks+=1
    for t in range(0,2):
        Q=N**t
        direct=-delta**2+(cov(U,nested(beta,Q))+cov(f,sawtooth(F(N*Q,1))))/2
        predicted=-delta**2+(A/2+beta/F(24*N))/Q
        assert direct==predicted,(p,q,k,t,'odd',direct,predicted)
        checks+=1
    assert (F(1,24)+beta*A/2)>0
    return checks

if __name__=='__main__':
    tests=[(3,2,1),(3,2,2),(4,3,1),(4,3,2),(5,2,1),(5,3,1),(7,3,1),(7,4,1),(8,5,1),(9,4,1)]
    counts=0
    for p,q,k in tests:
        counts+=check(p,q,k)
    print('VERIFY_OK rational_base_cases=%d exact_affine_integral_checks=%d lags=1..4 stationary_component_means=verified'%(len(tests),counts))
