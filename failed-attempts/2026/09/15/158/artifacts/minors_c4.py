"""Compute (n-1)-minors of sparse generic symmetric matrix for n=4, G=C4, and factor generators."""
import sympy as sp

# C4: vertices 1-2-3-4-1. Diagonal vars a,b,c,d; edges 12,23,34,14: p,q,r,s; zeros x13=x24=0.
a, b, c, d, p, q, r, s = sp.symbols('a b c d p q r s')
M = sp.Matrix([
    [a, p, 0, s],
    [p, b, q, 0],
    [0, q, c, r],
    [s, 0, r, d],
])

minors = {}
# (removed placeholder)

from itertools import combinations
rows4 = list(range(4))
gens = {}
for di in range(4):
    for dj in range(4):
        rr = [x for x in rows4 if x != di]
        cc = [x for x in rows4 if x != dj]
        sub = M.extract(rr, cc)
        det = sp.expand(sub.det())
        gens[(di, dj)] = det

seen = set()
for k, v in gens.items():
    print(f"M_{k} =", v)
print()
print("=== factorizations (distinct up to sign) ===")
uniq = []
for k, v in gens.items():
    done = False
    for (k2, w) in uniq:
        if sp.simplify(v - w) == 0 or sp.simplify(v + w) == 0:
            print(f"M_{k} == +/- M_{k2}")
            done = True
            break
    if not done:
        uniq.append((k, v))
for k, v in uniq:
    print(f"M_{k} = {v}")
    print(f"   factor: {sp.factor(v)}")
