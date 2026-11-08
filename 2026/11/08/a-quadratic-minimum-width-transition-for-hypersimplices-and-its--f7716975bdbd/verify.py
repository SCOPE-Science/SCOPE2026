"""Finite reproducibility checks for the exact hypersimplex minimum-width theorem.

This code does not certify infinitely many dimensions; see the analytic proof.
"""
from fractions import Fraction
from itertools import product, combinations
from math import comb


def hwidth_sq(u, k, weights=None):
    """Unnormalised squared width / squared Euclidean normal length.

    u stores y_i=s_i v_i. weights store s_i^{-2}.
    """
    n=len(u)
    k=min(k,n-k)
    if weights is None: weights=(1,)*n
    w=[Fraction(a) for a in weights]
    mean=sum(wi*Fraction(ui) for ui,wi in zip(u,w))/sum(w)
    u=[Fraction(a)-mean for a in u]
    den=sum(wi*ui*ui for ui,wi in zip(u,w))
    if not den: return None
    vals=sorted(u,reverse=True)
    width=sum(vals[:k])-sum(vals[-k:])
    return width*width/den


def exact_step_min_sq(n, k, weights=None):
    """Exact proposed minimum, with all optimal subset sizes/indices."""
    k=min(k,n-k)
    if weights is None: weights=(1,)*n
    ws=tuple(map(Fraction,weights))
    total=sum(ws)
    best=None; ss=[]
    for j in range(1,n):
        d=min(j,n-j,k)
        for S in combinations(range(n),j):
            A=sum(ws[i] for i in S)
            B=total-A
            val=Fraction(d*d)*total/(A*B)
            if best is None or val<best:
                best=val; ss=[S]
            elif val==best: ss.append(S)
    return best,ss

checks=0
for n in range(2,8):
    for k in range(1,n):
        b,ss=exact_step_min_sq(n,k)
        closed=min(Fraction(n,n-1), Fraction(k*k*n,(n//2)*(n-n//2)) if k <= n//2 else Fraction((n-k)**2*n,(n//2)*(n-n//2)))
        assert b==closed,(n,k,b,closed)
        # Exhaustive small grid; strictness for non-step minimizers checked via equality.
        for u in product((-2,-1,0,1,2),repeat=n):
            val=hwidth_sq(u,k)
            if val is None: continue
            assert val>=b, (n,k,u,val,b)
            if val==b:
                # A centered 2-level direction has only two distinct coordinates.
                assert len(set(u))==2, (n,k,u,val)
            checks+=1
for weights in [(1,2,3),(1,2,5,8),(1,3,5,7,11),(1,2,3,5,8,13)]:
    n=len(weights)
    for k in range(1,n):
        b,ss=exact_step_min_sq(n,k,weights)
        for u in product((-1,0,1),repeat=n):
            val=hwidth_sq(u,k,weights)
            if val is not None:
                assert val>=b, (n,k,weights,u,val,b)
                checks+=1
# Explicit equality at rank 2, n=15 and rank 3, n=35.
for k in [1,2,3,4,5]:
    n=4*k*k-1
    assert Fraction(n,n-1)==Fraction(k*k*n,(n//2)*(n-n//2))
    assert n>=2*k
    checks+=1
print('HYPERSIMPLEX_WIDTH_CHECKS_PASSED', 'grid_profiles=', checks,
      'weighted_profiles=',4, 'phase_boundaries=',5)
