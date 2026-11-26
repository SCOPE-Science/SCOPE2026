"""Exact independent checks for root branching and depth in uniform plane trees.
Run with Python 3.10+; standard library only. Finite checks do not prove the theorem.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def shapes(n):
    if n == 1:
        return ((),)
    out = []
    def compositions(total, parts):
        if parts == 0:
            if total == 0:
                yield ()
            return
        if parts == 1:
            if total >= 1:
                yield (total,)
            return
        for j in range(1, total - parts + 2):
            for tail in compositions(total - j, parts - 1):
                yield (j,) + tail
    for k in range(1, n):
        for sizes in compositions(n-1, k):
            out.extend(product(*(shapes(a) for a in sizes)))
    return tuple(out)

@lru_cache(None)
def stats(tree):
    if not tree: return (1,0)
    children=[stats(t) for t in tree]
    return (1+sum(x for x,y in children), sum(x+y for x,y in children))

def closed(n):
    assert n >= 2
    b=comb(2*n,n)
    a=Fraction((2*n-1)*4**n,4*b)
    mean_d=Fraction(3*(n-1),n+1)
    mean_p=a-Fraction(n,2)
    mean_dp=3*a-Fraction(7*n-4,2)
    covariance=Fraction(6*a-2*n*n-3*n+2,n+1)
    return mean_d,mean_p,mean_dp,covariance

def main():
    checks=0
    for n in range(2,10):
        trees=shapes(n)
        assert len(trees)==comb(2*n-2,n-1)//n
        data=[]
        for t in trees:
            sz, dep=stats(t)
            assert sz==n
            data.append((len(t),dep))
        denom=len(data)
        md=Fraction(sum(x for x,y in data),denom)
        mp=Fraction(sum(y for x,y in data),denom)
        mdp=Fraction(sum(x*y for x,y in data),denom)
        cov=mdp-md*mp
        assert (md,mp,mdp,cov)==closed(n)
        checks+=5
    for n in range(2,1201):
        md,mp,mdp,cov=closed(n)
        assert cov == mdp-md*mp
        assert cov == 0 if n == 2 else cov < 0
        checks += 2
    for n in range(3,701):
        # Inductive algebraic comparison for the sign of the covariance.
        r=Fraction(4**n,comb(2*n,n))
        t=Fraction(2*(2*n*n+3*n-2),3*(2*n-1))
        assert r<t
        ratio_r=Fraction(2*(n+1),2*n+1)
        tn=Fraction(2*(2*(n+1)**2+3*(n+1)-2),3*(2*(n+1)-1))
        assert tn/t-ratio_r == Fraction(n-1,(n+2)*(2*n+1))
        checks += 2
    for n in (5000,15000,50000):
        cov=closed(n)[3]
        assert abs(float(cov)/n+2) < 0.1
        checks+=1
    print(f'PASS: {checks} independent exact finite checks; all 2 <= n <= 9 plane trees exhaustively enumerated.')
if __name__=='__main__': main()
