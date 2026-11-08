"""Exact cyclic prime-power Gabor ambiguity/rank tests.

Run: python checker.py
Standard-library arithmetic, optionally NumPy for one independent Gram test.
"""
from collections import Counter
from math import gcd, pi
from cmath import exp
from random import Random


def layer_predicate(g, p, k, a, j):
    n=p**k
    m=p**j
    h=[g[x]*g[(x-a)%n] for x in range(n)]
    H=[sum(h[x] for x in range(r,n,m)) for r in range(m)]
    block=m//p
    return any(len({H[r+t*block] for t in range(p)})>1 for r in range(block))


def predicted_zero(g,p,k,a,b):
    n=p**k
    if b==0:
        return not any(g[x]*g[(x-a)%n] for x in range(n))
    j=k
    while b%p==0:
        b//=p
        j-=1
    return not layer_predicate(g,p,k,a,j)


def predicted_rank(g,p,k):
    n=p**k
    return sum(not predicted_zero(g,p,k,a,b) for a in range(n) for b in range(n))


def direct_complex_ambiguity(g,a,b):
    n=len(g)
    return sum(g[x]*g[(x-a)%n]*exp(2j*pi*(b*x%n)/n) for x in range(n))


def check_small_cases():
    rng=Random(74629)
    for p,k,trials in [(2,2,5),(2,3,5),(3,2,10),(3,3,5),(5,2,7),(7,2,3)]:
        n=p**k
        for rep in range(trials):
            g=[rng.randrange(0,5) for _ in range(n)]
            if not any(g):g[0]=1
            for a in range(n):
                for b in range(n):
                    z=predicted_zero(g,p,k,a,b)
                    val=direct_complex_ambiguity(g,a,b)
                    if z:
                        assert abs(val)<1e-8*max(1,sum(u*u for u in g)), (p,k,rep,a,b,val)
                    else:
                        assert abs(val)>1e-6, (p,k,rep,a,b,val)
    print('EXACT_LAYER_VS_NUMERIC_FOURIER_PASS')


def check_cross():
    for p in [3,5,7,11]:
        n=p*p
        S=set(range(p))|{p*j for j in range(p)}
        assert len(S)==2*p-1
        assert {(x-y)%n for x in S for y in S}==set(range(n))
        flat=[int(x in S) for x in range(n)]
        counts=Counter(sum(not predicted_zero(flat,p,2,a,b) for b in range(n)) for a in range(n))
        assert counts == Counter({n:n-p-1,p:p-1,n-p+1:2}), (p,counts)
        assert predicted_rank(flat,p,2)==n*n-(p-1)*(p*p-p+2)
        taper=[(2**x if x in S else 0) for x in range(n)]
        assert predicted_rank(taper,p,2)==n*n
        if p<=5:
            for a in range(n):
                for b in range(n):
                    if a in (1,p,p+1,p*p-1) or b in (0,1,p):
                        assert abs(direct_complex_ambiguity(taper,a,b))>1e-5
    print('CROSS_RANK_AND_TAPER_PASS')


def check_gram():
    try: import numpy as np
    except ImportError:
        print('NUMPY_NOT_PRESENT_GRAM_CHECK_SKIPPED');return
    n=9;p=3
    S=set(range(p))|{p*j for j in range(p)}
    g=np.array([int(x in S) for x in range(n)],dtype=float)
    ws=[]
    for a in range(n):
        for b in range(n):
            w=np.array([g[(x-a)%n]*np.exp(2j*np.pi*b*x/n) for x in range(n)])
            ws.append(np.outer(w,w.conj()).reshape(-1))
    W=np.array(ws).T
    s=np.linalg.svd(W,compute_uv=False)
    count=int(np.count_nonzero(s>1e-7))
    assert count==predicted_rank(list(map(int,g)),p,2)==65, (count,s)
    print('FULL_GRAM_81_PROJECTORS_PASS')

if __name__=='__main__':
    check_small_cases()
    check_cross()
    check_gram()
    print('PRIME_POWER_CYCLOTOMIC_GABOR_CHECKS_PASS')
