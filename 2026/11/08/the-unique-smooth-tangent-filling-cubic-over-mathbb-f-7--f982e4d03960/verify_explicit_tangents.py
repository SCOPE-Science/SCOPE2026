#!/usr/bin/env python3
"""Independent tangent-line and coverage certificate for one explicit cubic.

The polynomial and its derivatives are hard-coded independently of the
complete linear-series census; no numerical data or functions are imported.
"""
from collections import Counter
q=7
points = [(a,b,1) for a in range(q) for b in range(q)]
points += [(1,b,0) for b in range(q)] + [(0,1,0)]
assert len(points)==57

def normal(v):
    v = [a%q for a in v]
    i=next(i for i,a in enumerate(v) if a)
    t=pow(v[i],-1,q)
    return tuple((t*a)%q for a in v)

def F(a,b,c):
    return (a*b*b-a*a*c-2*b*c*c)%q

def grad(a,b,c):
    return (b*b-2*a*c,2*a*b-2*c*c,-a*a-4*b*c)

curve=[p for p in points if F(*p)==0]
assert len(curve)==12
assert all(any(w%q for w in grad(*p)) for p in curve)
lines={normal(grad(*pt)) for pt in curve}
expected = {(0,0,1),(1,0,0),(0,1,0)}
expected |= {(0,1,t) for t in (3,5,6)}
expected |= {(1,0,t) for t in (1,2,4)}
expected |= {(1,t,0) for t in (1,2,4)}
assert lines == expected, (lines,expected)
counts = Counter(sum(sum(a*b for a,b in zip(L,point))%q==0 for L in lines)
                 for point in points)
assert counts==Counter({1:36,2:9,3:9,5:3}), counts
assert all(r>0 for r in counts)
# All nonzero finite-field squares and nonsquares are the two cosets below.
squares={x*x%q for x in range(1,q)}
nonsquares=set(range(1,q))-squares
assert squares == {1,2,4} and nonsquares == {3,5,6}
# Independent explicit irreducibility criterion: F is smooth over Fbar_7
# is proved in RESULT.md from its three derivative equations.
print('EXPLICIT_CUBIC_RATIONAL_POINTS',len(curve))
print('EXPLICIT_TANGENT_LINES',sorted(lines))
print('INCIDENCE_SPECTRUM',sorted(counts.items()))
print('F7_EXPLICIT_CUBIC_TANGENT_FILLING_PASS')
