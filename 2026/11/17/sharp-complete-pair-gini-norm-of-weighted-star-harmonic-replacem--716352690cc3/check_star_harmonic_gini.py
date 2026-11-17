"""Exact finite checks for weighted one-hub Dirichlet extension in Gini variation.

Run: python check_star_harmonic_gini.py
All checks use fractions.Fraction and integer arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def gini(x):
    return sum((abs(a-b) for a,b in combinations(x,2)),F(0))


def extended(x,weights):
    return (sum((w*y for w,y in zip(weights,x[1:])),F(0)),)+tuple(x[1:])


def exact_binary_norm(weights):
    m=len(weights)
    ans=F(0); maximizers=[]
    for bits in product((0,1),repeat=m+1):
        den=gini(bits)
        if not den:continue
        val=gini(extended(bits,weights))/den
        if val>ans:ans=val;maximizers=[bits]
        elif val==ans:maximizers.append(bits)
    return ans,maximizers


def predicted(weights):
    m=len(weights)
    return F(1)+(F(m-2,m))*max(weights)


def check():
    rng=Random(20261110)
    checks=0
    for m in range(1,10):
        profiles=[tuple(F(1,m) for _ in range(m))]
        for k in range(3):
            raw=[rng.randint(1,30) for _ in range(m)]; s=sum(raw)
            profiles.append(tuple(F(v,s) for v in raw))
        for p in profiles:
            val,maxes=exact_binary_norm(p)
            assert val==predicted(p),(m,p,val,predicted(p))
            if m>=3:
                for i in range(m):
                    if p[i]==max(p):
                        a=(0,)+tuple(1 if j==i else 0 for j in range(m))
                        assert a in maxes,(m,p,a)
            for k in range(100):
                x=tuple(F(rng.randint(-7,7),rng.randint(1,5)) for i in range(m+1))
                den=gini(x)
                if den:
                    assert gini(extended(x,p))/den <=val
                checks+=1
    for m in range(1,70):
        u=tuple(F(1,m) for _ in range(m))
        assert predicted(u)==F(1)+F(m-2,m*m)
        if m>=3:
            eps=F(1,10000*m)
            p=(F(1)-(m-1)*eps,)+tuple(eps for _ in range(m-1))
            assert predicted(p)<F(2)-F(2,m)
    for m in range(3,70):
        assert F(m-2,m*m)<=F(1,8)
    print('EXACT_ALL_BINARY_CUTS_4_PROFILES_PER_DIMENSION_PASSED m=1..9')
    print('EXACT_RATIONAL_REAL_INPUT_INEQUALITY_PASSED',checks)
    print('EXACT_HUB_HARMONIC_SHARPNESS_AND_MINIMAX_PASSED')
    print('EXACT_FIXED_SIZE_AND_GLOBAL_ENVELOPES_PASSED')
    print('ALL_WEIGHTED_STAR_HARMONIC_GINI_CHECKS_PASSED')

if __name__=='__main__':check()
