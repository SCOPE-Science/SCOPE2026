"""Exact mathematical checks for the positive-island theorem.

Run: python3 check.py
Requires only the Python standard library.
"""
from math import comb
from fractions import Fraction
from itertools import product


def C(n,k):
    if n < 0 or k < 0 or k > n:
        return 0
    return comb(n,k)


def marg(m,N,a):
    return Fraction(C(N-a+m-2,m-2),C(N+m-1,m-1))


def joint(m,N,a,b):
    return Fraction(C(N-a-b+m-3,m-3),C(N+m-1,m-1))


def cov(m,N,a,b):
    assert a!=b
    pa,pb=marg(m,N,a),marg(m,N,b)
    return m*(m-1)*joint(m,N,a,b)-m*m*pa*pb


def q(m,a,L):
    return Fraction(C(L-a+m-3,m-3),C(L+m-2,m-2))


def compositions(m,N):
    if m==1:
        yield (N,)
    else:
        for v in range(N+1):
            for tail in compositions(m-1,N-v):
                yield (v,)+tail


def run():
    tests=0
    # Every legal pair is classified by the conditional occupancy probability.
    for m in range(3,12):
        for N in range(0,32):
            for a in range(N+1):
                p=marg(m,N,a)
                plus=[]
                for b in range(N+1):
                    if b==a:
                        continue
                    v=cov(m,N,a,b)
                    threshold=q(m,a,N-b)-Fraction(m,m-1)*p
                    assert (v>0)-(v<0)==(threshold>0)-(threshold<0)
                    tests+=1
                # Include the distinguished diagonal in the *formal*
                # conditional test to check the integer interval property.
                full=[b for b in range(N+1) if q(m,a,N-b)>Fraction(m,m-1)*p]
                assert not full or full==list(range(min(full),max(full)+1))
                tests+=1
    # Rational exact independent full state-space enumeration.
    for m,N in [(3,4),(3,7),(4,7),(4,12),(5,6),(5,8),(6,6)]:
        all_states=list(compositions(m,N))
        den=len(all_states)
        assert den==C(N+m-1,m-1)
        for a in range(N+1):
            xa=[s.count(a) for s in all_states]
            for b in range(N+1):
                if a==b:
                    continue
                xb=[s.count(b) for s in all_states]
                emp=Fraction(sum(x*y for x,y in zip(xa,xb)),den)-Fraction(sum(xa)*sum(xb),den**2)
                assert emp==cov(m,N,a,b),(m,N,a,b,emp,cov(m,N,a,b))
                tests+=1
    assert cov(4,12,2,7)==Fraction(-48,29575)
    assert cov(4,12,2,8)==Fraction(108,41405)
    assert cov(4,12,2,9)==Fraction(72,41405)
    assert cov(4,12,2,10)==Fraction(-876,207025)
    for m in range(3,12):
        for N in range(1,50):
            for b in range(1,N+1):
                # Vacancy covariance sign derived by algebra: m*b>2*N+m-2.
                assert (cov(m,N,0,b)>0)==(m*b>2*N+m-2)
                tests+=1
    print('PASS:',tests,'exact identity/sign/interval/enumeration assertions')
    print('Example: m=4,N=12,a=2, b=7..10:')
    print([str(cov(4,12,2,b)) for b in range(7,11)])

if __name__=='__main__': run()
