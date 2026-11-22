"""Exact-rational checks for binary-persistence tomography of ballistic renewal motion.

Scientific scope: iid positive flight speeds, a fixed flight length L, complete
renewal upon reaching 0. These finite calculations illustrate the exact proof;
they do not certify the theorem for arbitrary probability measures.
"""
from fractions import Fraction as F


def size_biased_from_flight(phi):
    invmean = sum(p/v for v, p in phi.items())
    return {v: p / (v * invmean) for v, p in phi.items()}


def original_from_stationary(psi):
    mean = sum(v*p for v, p in psi.items())
    return {v: v*p/mean for v, p in psi.items()}


def observable(psi, L, a, t):
    return sum(p*max(F(0), L-a-v*t) for v,p in psi.items()) / L


def transform(psi, L, a, z):
    return L*z/(L-a)*observable(psi, L, a, (L-a)/z)


def direct_stoploss(psi,z):
    return sum(p*max(F(0),z-v) for v,p in psi.items())


def piecewise_slope(psi,z):
    # At a non-atom point, the exact derivative of the stop-loss potential.
    assert z not in psi
    return sum(p for v,p in psi.items() if v<z)


def check():
    count=0
    L=F(1)
    for vs,ps in [
       ([F(1),F(2),F(4)],[F(1,4),F(1,2),F(1,4)]),
       ([F(1),F(3,2),F(3),F(4)],[F(1,6),F(1,3),F(1,4),F(1,4)]),
       ([F(1),F(7,4),F(4)],[F(2,7),F(3,7),F(2,7)]),
    ]:
        psi=dict(zip(vs,ps))
        assert sum(ps)==1
        phi=original_from_stationary(psi)
        assert size_biased_from_flight(phi)==psi
        count+=1
        vmax=max(vs)
        vmin=min(vs)
        acrit=L*vmax/(vmin+vmax)
        for a in [acrit,F(9,10),F(19,20)]:
            if a>=L:continue
            assert (L-a)*vmax/a<=vmin
            for z in [F(13,10),F(9,5),F(5,2),F(7,2),F(9,2),F(6)]:
                if z > (L-a)*vmax/a:
                    assert transform(psi,L,a,z)==direct_stoploss(psi,z)
                    count+=1
            for z in [F(6,5),F(8,5),F(5,2),F(7,2)]:
                if z not in psi and z>(L-a)*vmax/a:
                    tiny=F(1,100000)
                    assert (transform(psi,L,a,z+tiny)-transform(psi,L,a,z-tiny))/(2*tiny)==piecewise_slope(psi,z)
                    count+=1
    # Sharp lower-threshold ambiguity; both have exactly support endpoints 1,4.
    psi1={F(1):F(1,10),F(4):F(1,10),F(13,10):F(4,5)}
    psi2={F(1):F(1,10),F(4):F(1,10),F(11,10):F(2,5),F(3,2):F(2,5)}
    assert sum(psi1.values())==sum(psi2.values())==1
    assert sum(v*p for v,p in psi1.items())==sum(v*p for v,p in psi2.items())
    assert original_from_stationary(psi1)!=original_from_stationary(psi2)
    a=F(7,10)
    assert a<F(4,5)
    for i in range(1,200):
        t=a/F(4)*F(i,200)
        assert observable(psi1,L,a,t)==observable(psi2,L,a,t)
        count+=1
    # Critical detector a=4/5 separates those previously indistinguishable laws.
    a=F(4,5)
    assert observable(psi1,L,a,F(3,20))!=observable(psi2,L,a,F(3,20))
    count+=1
    print('PASS',count,'exact-rational checks: stop-loss transform, inverse slopes, sharp ambiguity')

if __name__=='__main__':
    check()
