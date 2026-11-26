"""Finite sanity checks for the two equal-norm rank-one Schatten quotient.
Uses only the Python standard library; all general claims require their analytic proof.
"""
import math
import random


def logcosh(x):
    x = abs(x)
    return x + math.log1p(math.exp(-2*x)) - math.log(2)


def h(p, z):
    k = p / (2 - p)
    return math.exp((0.5 * p * logcosh(z) + (1-0.5*p)*logcosh(k*z) - logcosh(p*z))/p)


def equation(p,z):
    k = p/(2-p)
    return math.tanh(z)+math.tanh(k*z)-2*math.tanh(p*z)


def critical(p):
    # Positive sign near zero and negative after the unique crossing.
    lo, hi = 1e-7, 1.0
    while equation(p,hi) > 0 and hi < 100:
        hi *= 2
    assert equation(p,lo)>0 and equation(p,hi)<0
    for _ in range(110):
        mid=(lo+hi)/2
        if equation(p,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def finite_ratio(p,c,d,theta=0):
    # Traces and determinant are exactly the rank-two Gram data.
    rr=p/2
    tr=2+2*c*d*math.cos(theta)
    det=(1-c*c)*(1-d*d)
    disc=math.sqrt(max(0.0,tr*tr-4*det))
    la=max(0.,(tr+disc)/2)
    lb=max(0.,(tr-disc)/2)
    return ((la**rr+lb**rr)/((1+c)**p+(1-c)**p))**(1/p)


def main():
    random.seed(1019)
    checks=0
    for p in (1.1, 1.2, 1.5, 1.8, 1.95):
        z=critical(p)
        k=p/(2-p)
        c,d=math.tanh(z),math.tanh(k*z)
        best=h(p,z)
        assert abs(finite_ratio(p,c,d)-best)<2e-11
        for _ in range(1200):
            c0=random.random()
            d0=random.random()
            phase=2*math.pi*random.random()
            assert finite_ratio(p,c0,d0,phase)<best+2e-11
            checks+=1
        print(f'p={p}: z={z:.12f}, c={c:.12f}, d={d:.12f}, K={best:.12f}')
    x0lo,x0hi=1.,2.
    for _ in range(100):
        mid=(x0lo+x0hi)/2
        if mid*math.tanh(mid)<1:x0lo=mid
        else:x0hi=mid
    z0=(x0lo+x0hi)/2
    coef=(z0*z0-1)/2
    for e in (0.02,0.005,0.001):
        value=(h(1+e,critical(1+e))-1)/e**2
        assert abs(value-coef)<0.02
        checks+=1
    expected=math.sqrt((1+math.sqrt(2))/2)
    assert abs(h(1.9999,critical(1.9999))-expected)<0.001
    print(f'endpoint trace-class coefficient={coef:.12f}; Hilbert endpoint={expected:.12f}; {checks+1} tests passed')

if __name__=='__main__':
    main()
