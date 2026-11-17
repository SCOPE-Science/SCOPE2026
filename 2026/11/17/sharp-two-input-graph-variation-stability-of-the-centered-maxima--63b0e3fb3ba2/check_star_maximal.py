"""Exact rational diagnostics for the two-input star maximal BV estimate.
Only finite corroboration; the universal result is proved analytically.
Run: python check_star_maximal.py
"""
from fractions import Fraction as F
from itertools import product
import random

def maximal_star(a):
    # a[0] is the center, other entries are leaves; input must be nonnegative.
    m = len(a)-1
    overall = sum(a, F(0))/(m+1)
    return [max(a[0],overall)] + [max(a[i],(a[0]+a[i])/2,overall) for i in range(1,m+1)]

def bv(a):
    return sum((abs(t-a[0]) for t in a[1:]),F(0))

def perturb_norm(m):
    return F(1,2) if m==1 else F(2*m,m+1)

def witness(m):
    base=F(3)
    f=[base] + [base+F(m-1,2)]+[base-1]*(m-1)
    g=f[:]
    g[1] += F(1,8) if m>=2 else F(1)
    return f,g

# Independent truth of normalized formula on exact rational examples.
checks=0
for m in range(1,65):
    f,g=witness(m)
    lhs=bv([a-b for a,b in zip(maximal_star(g),maximal_star(f))])
    rhs=bv([a-b for a,b in zip(g,f)])
    assert lhs==rhs*perturb_norm(m),(m,lhs,rhs)
    checks+=1
print('EXACT_SHARP_WITNESSES_PASSED',checks)

# Exhaustive integer grid of small nonnegative signals (not exhaustive real inputs).
checks=0
for m in range(1,7):
    vals=list(product(range(3),repeat=m+1))
    for v in vals:
        a=[F(x) for x in v]
        out=maximal_star(a)
        assert all(z>=0 for z in out)
        # local finite differences in every coordinate; equality ties not required.
        for k in range(m+1):
            b=a[:]
            b[k]+=F(1,5)
            inp=bv([q-p for q,p in zip(b,a)])
            if inp:
                out2=maximal_star(b)
                diff=bv([q-p for q,p in zip(out2,out)])
                assert diff<=perturb_norm(m)*inp,(m,a,k,diff,inp)
                checks+=1
print('EXACT_INTEGER_GRID_SINGLE_COORDINATE_PERTURBATIONS_PASSED',checks)

# Arbitrary paired signals and their nonlinear differences with fixed pseudorandom seed.
rng=random.Random(2047)
checks=0
for m in range(1,25):
    for iteration in range(350):
        a=[F(rng.randrange(0,201),17) for _ in range(m+1)]
        b=[F(rng.randrange(0,201),17) for _ in range(m+1)]
        den=bv([u-v for u,v in zip(a,b)])
        if den==0:continue
        num=bv([u-v for u,v in zip(maximal_star(a),maximal_star(b))])
        assert num<=perturb_norm(m)*den,(m,num,den)
        checks+=1
print('TWO_INPUT_RATIONAL_TOTAL_VARIATION_CHECKS_PASSED',checks)

# Distinct symbolic active-branch Jacobian budgets, evaluated in exact rationals.
checks=0
for m in range(2,24):
    a=F(1,m+1)
    # positive centered mean: s active leaves, rest use global mean.
    for s in range(1,m+1):
        for k_active in (False,True):
            if k_active and s<1:continue
            v=F(1)+(s-2)*a if k_active else s*a
            assert v<=perturb_norm(m)
            checks+=1
    # negative centered mean: u leaves use the global mean, rest choose self/half.
    for u in range(m):
        for kind in ['self','half','global']:
            v={'self':F(1)+u*a,'half':F(1,2)+u*a,'global':u*a}[kind]
            assert v<=perturb_norm(m)
            checks+=1
print('SYMBOLIC_ACTIVE_BRANCH_BUDGETS_PASSED',checks)

# Signed absolute-value maximal operator has no two-input seminorm bound.
# This is an exact boundary test, not part of the positive-cone norm.
checks=0
for m in range(1,33):
    for den in [4,8,16,32,64]:
        eps=F(1,den)
        f=[F(1)]+[F(-1)]*m
        g=[F(2),eps]+[F(0)]*(m-1)
        assert bv([u-v for u,v in zip(g,f)])==eps
        Mf=maximal_star([abs(z) for z in f])
        Mg=maximal_star([abs(z) for z in g])
        actual=bv([u-v for u,v in zip(Mg,Mf)])
        assert actual==m-eps/2,(m,eps,actual)
        checks+=1
print('EXACT_SIGNED_DOMAIN_OBSTRUCTIONS_PASSED',checks)

print('ALL_STAR_MAXIMAL_TWO_INPUT_BV_DIAGNOSTICS_PASSED')
