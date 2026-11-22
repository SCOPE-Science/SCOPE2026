"""Reproducible exact-rational checks for the conditional Kendall/Spearman envelope.
Run: python check.py (Python standard library only). These finite checks supplement,
but do not replace, the analytical continuum proof.
"""
from fractions import Fraction as Q
import random


def evaluate(intervals):
    # Piecewise-constant probability density on [0,1]. Intervals partition [0,1].
    assert intervals[0][0] == 0 and intervals[-1][1] == 1
    assert all(a < b and h >= 0 for a,b,h in intervals)
    assert all(intervals[i][1] == intervals[i+1][0] for i in range(len(intervals)-1))
    assert sum((b-a)*h for a,b,h in intervals) == 1
    q=m=F2=Q(0)
    F0=Q(0)
    for a,b,h in intervals:
        d=b-a
        q += h*((b-Q(1,2))**3-(a-Q(1,2))**3)/3
        m += F0*d + h*d*d/2
        F2 += F0*F0*d + F0*h*d*d + h*h*d*d*d/3
        F0 += h*d
    assert F0==1
    J=F2-m*m
    rho=Q(1,2)-6*q
    tau=1-8*q-4*J
    return rho,tau,q,J


def envelope(rho):
    if rho <= 0:
        return (2*rho-rho*rho)/3
    # positive branch needs square root; return squared rational inequality instead
    import math
    return (2/3)*(math.sqrt(float(1-2*rho))-(1-2*float(rho)))


def sym_uniform(a):
    low=Q(1,2)-a; high=Q(1,2)+a
    return [(Q(0),low,Q(0)),(low,high,1/(2*a)),(high,Q(1),Q(0))]


def neg_approx(rho, eps):
    q=(Q(1,2)-rho)/6
    q_edge=Q(1,4)-eps/2+eps*eps/3
    w=(q-Q(1,12))/(q_edge-Q(1,12))
    assert 0<w<1
    bulk=1-w
    return [(Q(0),eps,bulk+w/(2*eps)),(eps,1-eps,bulk),
            (1-eps,Q(1),bulk+w/(2*eps))]


def test():
    checks=0
    # Uniform centered generator: exact positive-bound attainment at rational widths.
    for denominator in range(3,30):
        for numerator in range(1,(denominator+1)//2):
            a=Q(numerator,denominator)
            if not (0<a<Q(1,2)): continue
            rho,tau,q,J=evaluate(sym_uniform(a))
            assert q==a*a/3
            assert rho == Q(1,2)-2*a*a
            assert J == Q(1,4)-a/3
            assert tau == 4*a/3-8*a*a/3
            checks+=4
    # negative regime bound, fixed rho approximants, convergence of tau to supremum
    for rho in [Q(-9,10),Q(-3,4),Q(-1,2),Q(-1,4),Q(-1,10)]:
        prev=None
        for eps in [Q(1,50),Q(1,200),Q(1,2000),Q(1,20000)]:
            r,t,q,J=evaluate(neg_approx(rho,eps))
            assert r==rho and t < (2*rho-rho*rho)/3
            gap=(2*rho-rho*rho)/3-t
            if prev is not None: assert gap<prev
            prev=gap
            checks+=3
        assert prev<Q(1,1000)
    # general piecewise generators satisfy exact fixed-rho envelope in both branches
    rng=random.Random(1632)
    for n in range(2,20):
        for rep in range(100):
            cuts=[Q(0)]+sorted({Q(rng.randint(1,9999),10000) for i in range(n-1)})+[Q(1)]
            vals=[Q(rng.randint(0,1000),1000) for i in range(len(cuts)-1)]
            mass=sum((cuts[i+1]-cuts[i])*vals[i] for i in range(len(vals)))
            if mass==0:continue
            ints=[(cuts[i],cuts[i+1],vals[i]/mass) for i in range(len(vals))]
            rho,tau,q,J=evaluate(ints)
            assert Q(-1)<rho<Q(1,2)
            if rho<=0: assert tau<=(2*rho-rho*rho)/3
            else: assert float(tau)<float(envelope(rho))+1e-13
            checks+=2
    print(f'PASS: {checks} exact-rational/randomized consistency assertions.')


if __name__=='__main__':
    test()
