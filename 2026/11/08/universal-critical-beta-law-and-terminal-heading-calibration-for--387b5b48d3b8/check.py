"""Standalone deterministic checks of ageing persistent-walk moment recurrences.

All computations use Python's standard library; finite checks supplement the
analytic scaling-limit proof, rather than certifying it.
"""
from fractions import Fraction as F
from math import comb


def evolving_moments(n, c, a, rational=False):
    """Return position moments A[r]=E X^r and B[r]=E X^r V, r<=4."""
    zero, one = (F(0), F(1)) if rational else (0., 1.)
    A = [one, zero, zero, zero, zero]
    B = [zero] * 5
    for k in range(1, n+1):
        p = c/(k+a)
        q = one - 2*p
        aa, bb = [], []
        for r in range(5):
            aa.append(sum(comb(r,j)*(A[r-j] if j % 2 == 0 else q*B[r-j]) for j in range(r+1)))
            bb.append(sum(comb(r,j)*(q*B[r-j] if j % 2 == 0 else A[r-j]) for j in range(r+1)))
        A, B = aa, bb
    return A, B


def exact_joint(n, c, a):
    # Fair initial sign makes the first step exactly symmetric.
    distribution = {(1,1):F(1,2), (-1,-1):F(1,2)}
    for k in range(2,n+1):
        p=c/(k+a)
        nxt={}
        for (x,s), mass in distribution.items():
            for new_s, prob in ((s,1-p),(-s,p)):
                key=(x+new_s,new_s)
                nxt[key]=nxt.get(key,F(0))+mass*prob
        distribution=nxt
    return distribution


def check():
    count=0
    for c,a in ((F(1,2), F(1)),(F(1),F(1)),(F(2),F(2)),(F(5,3),F(2))):
        for n in range(1,19):
            D=exact_joint(n,c,a)
            assert sum(D.values())==1;count+=1
            A,B=evolving_moments(n,c,a,True)
            for r in range(5):
                assert A[r] == sum((x**r)*v for (x,s),v in D.items());count+=1
                assert B[r] == sum((x**r)*s*v for (x,s),v in D.items());count+=1
            edge=F(1)
            for k in range(2,n+1):edge*=1-c/(k+a)
            assert sum(v for (x,s),v in D.items() if abs(x)==n)==edge;count+=1
            assert all(v>=0 for v in D.values());count+=1
    for c,a in ((0.5,1.),(1.,1.),(2.,2.),(5./3.,2.)):
        n=10000
        A,B=evolving_moments(n,c,a)
        v2=A[2]/n**2;v4=A[4]/n**4
        target2=1/(2*c+1)
        target4=3/((2*c+1)*(2*c+3))
        assert abs(v2-target2) < 0.002;count+=1
        assert abs(v4-target4) < 0.002;count+=1
        assert abs(B[1]/n - target2) < 0.002;count+=1
        binder=1-v4/(3*v2*v2)
        assert abs(binder - 2/(2*c+3)) < 0.007;count+=1
    return count

if __name__=='__main__':
    print(f'PASS: {check()} deterministic assertions')
