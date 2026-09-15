"""Jacobian / dimension check for C4 n=4 case at random rank-2 points."""
import sympy as sp
import random

a, b, c, d, p, q, r, s = sp.symbols('a b c d p q r s')
M = sp.Matrix([
    [a, p, 0, s],
    [p, b, q, 0],
    [0, q, c, r],
    [s, 0, r, d],
])
from itertools import combinations
rows4 = list(range(4))
gens = []
keys = []
for di in range(4):
    for dj in range(di, 4):
        rr = [x for x in rows4 if x != di]
        cc = [x for x in rows4 if x != dj]
        sub = M.extract(rr, cc)
        det = sp.expand(sub.det())
        gens.append(det)
        keys.append((di, dj))
print(f"num gens (upper triangle incl diag): {len(gens)}")
vars8 = [a, b, c, d, p, q, r, s]
J = sp.Matrix([[sp.diff(g, v) for v in vars8] for g in gens])

random.seed(0)
for trial in range(5):
    u = [random.randint(-3, 3) for _ in range(4)]
    v = [random.randint(-3, 3) for _ in range(4)]
    # M entries
    pt = {
        a: u[0]*u[0]+v[0]*v[0], b: u[1]*u[1]+v[1]*v[1],
        c: u[2]*u[2]+v[2]*v[2], d: u[3]*u[3]+v[3]*v[3],
        p: u[0]*u[1]+v[0]*v[1], q: u[1]*u[2]+v[1]*v[2],
        r: u[2]*u[3]+v[2]*v[3], s: u[0]*u[3]+v[0]*v[3],
    }
    # check sparsity constraints automatically satisfied? need u1u3+v1v3=0? NO - random point won't satisfy!
    print(f"trial {trial}: u={u} v={v}")
    print("   sparsity check f13=", u[0]*u[2]+v[0]*v[2], " f24=", u[1]*u[3]+v[1]*v[3])
