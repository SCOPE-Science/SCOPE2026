#!/usr/bin/env python3
"""Exact checks for the graph-spread formulas of apex-paths and apex-cycles.
Enumerations are finite corroboration; the accompanying mathematical proof is universal.
"""
from itertools import product
from fractions import Fraction


def score_of(a):
    N = len(a) + 1
    return Fraction(N * sum(v*v for v in a) - sum(a)**2, N*N)


def allowed(a, closed):
    if any(abs(a[i]-a[i+1]) > 1 for i in range(len(a)-1)):
        return False
    return not closed or abs(a[-1]-a[0]) <= 1


def predicted(m, closed):
    z = 2 if closed else 1
    N = m + 1
    q = m-z
    return Fraction(N*q-(q%2), N*N)


def predicted_profiles(m, closed):
    z=2 if closed else 1
    q=m-z
    return sorted((q//2, q-q//2))


def is_expected_maximizer(a, closed):
    m=len(a)
    z=2 if closed else 1
    if a.count(0)!=z: return False
    if sorted((a.count(-1),a.count(1)))!=predicted_profiles(m,closed): return False
    # For z minimal, every + and - block on path/cycle has a zero separating it.
    if closed:
        return sum(a[i]==0 and a[(i+1)%m]==0 for i in range(m))==0
    return a[0]!=0 and a[-1]!=0 and all(a[i]!=0 for i in range(m) if a[i]!=0) # redundant endpoint check

for m in range(3,11):
    for closed in (False,True):
        if closed and m < 4: continue
        vals=[a for a in product((-1,0,1),repeat=m) if allowed(a,closed)]
        top=max(score_of(a) for a in vals)
        sols=[a for a in vals if score_of(a)==top]
        formula=predicted(m,closed)
        assert top==formula, (m,closed,top,formula)
        assert all(is_expected_maximizer(a,closed) for a in sols), (m,closed,sols)
        # Verify every type of asserted maximal profile satisfies constraints and has top variance.
        for a in vals:
            if not is_expected_maximizer(a,closed): continue
            assert score_of(a)==top,(m,closed,a)
        print(('WHEEL' if closed else 'FAN'),m,'spread',top,'maximizers',len(sols))
print('ALL_FINITE_INTEGER_PROFILES_OK')
for m in range(4,200):
    N=m+1
    assert predicted(m,False)-predicted(m,True)==Fraction(N-(-1)**m,N*N)
print('ONE_EDGE_PARITY_GAP_IDENTITIES_OK')
