"""Hunt for points of V(I3) NOT in rank<=2 locus (extra component witnesses).
Rank<=2 locus: all 4x4 minors (just det) vanish AND all 3-minors vanish. V(I3) requires only 3-minors.
So extra component points: 3-minors all vanish but det(X) != 0!

Search: solve 10 cubics with det != 0. Use random linear slicing + nsolve over RR/CC.
Set up: pick random integer linear equations to cut down, use sympy nsolve from many starts.
"""
import sympy as sp
import random

a, b, c, d, p, q, r, s = sp.symbols('a b c d p q r s')
M = sp.Matrix([
    [a, p, 0, s],
    [p, b, q, 0],
    [0, q, c, r],
    [s, 0, r, d],
])
rows4 = list(range(4))
gens = []
for di in range(4):
    for dj in range(di, 4):
        rr = [x for x in rows4 if x != di]
        cc = [x for x in rows4 if x != dj]
        gens.append(sp.expand(M.extract(rr, cc).det()))
detX = sp.expand(M.det())
print("det =", detX)
print("det factored:", sp.factor(detX))

# Try to find V point with det != 0 via nsolve: fix 5 vars randomly, solve 3 eqns? overdetermined (10 eq in 3 unknowns).
# Better: penalty/optimization approach: minimize sum of squares of gens over random starts, check det.
import random
random.seed(7)
f = sp.lambdify((a,b,c,d,p,q,r,s), [g for g in gens] + [detX], 'math')
import math

def residuals(pt):
    vals = f(*pt)
    return vals

# use simple coordinate descent / random hill climbing from many starts
best = None
for trial in range(20000):
    pt = [random.uniform(-2,2) for _ in range(8)]
    # local polish: a few random steps
    cur = sum(v*v for v in f(*pt)[:10])
    step = 0.2
    for it in range(60):
        improved = False
        for k in range(8):
            for sgn in (1,-1):
                q2 = list(pt); q2[k] += sgn*step
                c2 = sum(v*v for v in f(*q2)[:10])
                if c2 < cur:
                    cur = c2; pt = q2; improved = True
        step *= 0.97
        if cur < 1e-14:
            break
    detv = f(*pt)[10]
    if cur < 1e-10 and abs(detv) > 1e-6:
        print("CANDIDATE extra-component point:", pt, "resid", cur, "det", detv)
        break
    if best is None or cur < best[0]:
        best = (cur, pt, detv)
else:
    print("no det!=0 point found; best:", best)
