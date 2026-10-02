"""Corroborating computation for the TARGET impossibility proof (sympy + stdlib).

Theorem under test: for an apolar AG algebra A=R/Ann(F), socle d, char not dividing
d!, any linear form L with F(point)!=0 gives a Jordan block of size d+1 for xL,
via L^d o F = d! * F(point). Hence general-L Jordan type always has longest part
d+1 = 7 for d=6, contradicting the target's 'longest part <= 6'.
"""
from sympy import Matrix
import math, itertools

NV = 4
DEG = 6

def mons(nv, d):
    out = []
    def rec(i, rem, cur):
        if i == nv - 1:
            out.append(tuple(cur + [rem])); return
        for e in range(rem + 1):
            rec(i + 1, rem - e, cur + [e])
    rec(0, d, [])
    return out

def apply_r(F, r):
    """Partial^r applied to F (dict exp->coeff)."""
    out = {}
    for e, c in F.items():
        if all(e[i] >= r[i] for i in range(NV)):
            f = 1
            for i in range(NV):
                f *= math.factorial(e[i]) // math.factorial(e[i] - r[i])
            ne = tuple(e[i] - r[i] for i in range(NV))
            out[ne] = out.get(ne, 0) + c * f
    return out

def eval_F(F, a):
    return sum(c * math.prod(ai ** ei for ai, ei in zip(a, e)) for e, c in F.items())

def Lpower_circ_F(F, a, d=6):
    """Compute L^d o F with L = sum a_i x_i, by expanding L^d. Result: scalar."""
    total = 0
    for r in mons(NV, d):
        mf = math.factorial(d)
        for i in range(NV):
            mf //= math.factorial(r[i])
        coeff = mf * math.prod(ai ** ei for ai, ei in zip(a, r))
        total += coeff * apply_r(F, r).get((0, 0, 0, 0), 0)
    return total

# ---- 1. conjugate partition of H=(1,4,6,8,6,4,1)
H = [1, 4, 6, 8, 6, 4, 1]
lam = sorted(H, reverse=True)
conj = []
j = 1
while True:
    c = sum(1 for x in lam if x >= j)
    if c == 0:
        break
    conj.append(c); j += 1
print("H =", H, "sum =", sum(H))
print("sorted =", lam)
print("conjugate =", tuple(conj), "sum =", sum(conj))
assert tuple(conj) == (7, 5, 5, 5, 3, 3, 1, 1), "conjugate mismatch"
assert sum(H) == 30

# ---- 2. identity L^6 o F = 720 F(a), on two test sextics
E = lambda *e: tuple(e)
F_fermat = {E(6,0,0,0): 1, E(0,6,0,0): 1, E(0,0,6,0): 1, E(0,0,0,6): 1}
F_peraz = {E(1,0,5,0): 1, E(0,1,0,5): 1, E(0,0,6,0): 2, E(0,0,0,6): 3, E(0,0,3,3): 1}
a0 = [1, 1, 1, 1]
for name, F in [("fermat", F_fermat), ("perazzo-like", F_peraz)]:
    lhs = Lpower_circ_F(F, a0)
    rhs = math.factorial(6) * eval_F(F, a0)
    print(f"{name}: L0^6 o F = {lhs}, 720*F(1,1,1,1) = {rhs}, equal = {lhs == rhs}, "
          f"F(a0) = {eval_F(F, a0)} != 0 -> [L0^6] != 0 in A6 -> Jordan block of size 7")
    assert lhs == rhs and rhs != 0

# ---- 3. Fermat HF via catalecticant ranks (exact), confirming AG setup h6=1
def cat(F, r):
    Rm = mons(NV, r); Sm = mons(NV, DEG - r)
    Sidx = {e: i for i, e in enumerate(Sm)}
    M = [[0] * len(Rm) for _ in range(len(Sm))]
    for j, e in enumerate(Rm):
        for ne, c in apply_r(F, e).items():
            M[Sidx[ne]][j] = c
    return Matrix(M)

h = [cat(F_fermat, i).rank() for i in range(7)]
print("Fermat HF =", h)
assert h[0] == 1 and h[6] == 1 and h == h[::-1]

print("VERIFY_OK: conjugate=(7,5,5,5,3,3,1,1); L^6-identity holds; "
      "general L carries a Jordan 7-block; target 'longest part <= 6' unsatisfiable.")
