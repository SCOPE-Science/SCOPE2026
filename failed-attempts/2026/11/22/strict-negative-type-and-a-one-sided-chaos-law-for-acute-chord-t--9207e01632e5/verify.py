#!/usr/bin/env python3
"""Independent arithmetic and numerical consistency checks of stated formulas.
Run with Python 3 standard library; numerical checks do not replace the proof.
"""
import math
import random


def q_of_t(t):
    return math.sqrt((1-t)/2) + 0.5*math.sqrt((1+t)/2) - 0.5


def eig(l):
    return -(2 + (-1)**l)/(8*(l-.5)*(l+.5)*(l+1.5))


def legendre(l,t):
    if l == 0: return 1.
    if l == 1: return t
    a,b=1.,t
    for k in range(2,l+1):
        a,b=b,((2*k-1)*t*b-(k-1)*a)/k
    return b


def midpoint_integral(f,n=40000):
    return sum(f(-1.+(i+.5)*2/n) for i in range(n))/n


def finite_variance(n):
    return math.comb(n,3)/4 + (math.pi-3)/4 * math.comb(n,2) * math.comb(n-2,2)


def hoeffding_variance(n):
    second=(n-2)**2 * math.comb(n,2) * (math.pi-3)/8
    third=math.comb(n,3) * (11-3*math.pi)/8
    return second+third


def sphere_point(rng):
    z=2*rng.random()-1
    a=2*math.pi*rng.random()
    b=math.sqrt(1-z*z)
    return b*math.cos(a),b*math.sin(a),z


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def acute(a,b,c):
    ab=tuple(y-x for x,y in zip(a,b))
    ac=tuple(y-x for x,y in zip(a,c))
    bc=tuple(z-y for y,z in zip(b,c))
    return dot(ab,ac)>0 and dot(ab,bc)<0 and dot(ac,bc)>0


def check():
    # The probability and covariance are integrated independently of the spectral formula.
    assert abs(midpoint_integral(q_of_t)-.5)<1e-7
    assert abs(midpoint_integral(lambda t:q_of_t(t)**2)-(math.pi-1)/8)<1e-7
    for l in range(1,13):
        lam=midpoint_integral(lambda t,ll=l:(q_of_t(t)-.5)*legendre(ll,t))
        assert abs(lam-eig(l))<2e-7,(l,lam,eig(l))
        assert eig(l)<0
    trace=sum((2*l+1)*(-eig(l)) for l in range(1,50001))
    assert abs(trace-.5)<1.1e-5, trace
    hs=sum((2*l+1)*eig(l)**2 for l in range(1,1001))
    assert abs(hs-(math.pi-3)/8)<2e-10,(hs,(math.pi-3)/8)
    for n in [3,4,5,7,20,100]:
        assert abs(finite_variance(n)-hoeffding_variance(n))<1e-8*max(1,finite_variance(n))
    # Uniform-cap area and belt intersection derived in the proof are checked with
    # direct vector tests at three fixed nondegenerate separations.
    rng=random.Random(20261121)
    for theta in [0.4,1.5,2.6]:
        a=(math.cos(theta/2),-math.sin(theta/2),0.)
        b=(math.cos(theta/2),math.sin(theta/2),0.)
        m=60000
        observed=sum(acute(a,b,sphere_point(rng)) for _ in range(m))/m
        expected=q_of_t(math.cos(theta))
        assert abs(observed-expected)<0.008,(theta,observed,expected)
    kappa3=sum((2*l+1)*eig(l)**3 for l in range(1,1000))
    assert kappa3 < -.001
    print('TRACE_MASS',f'{trace:.12f}')
    print('HILBERT_SCHMIDT_MASS',f'{hs:.12f}')
    print('LIMIT_VARIANCE',f'{(math.pi-3)/16:.12f}')
    print('LIMIT_THIRD_CUMULANT',f'{kappa3:.12f}')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':check()
