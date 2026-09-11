"""S4-census lemma for fallback: only cube and cross-polytope among 4D Hanner
polytopes are S4-permutation-invariant. Certifies explicit distinguishing points
for each mixed Hanner type P (point in P whose coordinate-transposition image
lies outside P). All checks are exact rational arithmetic (stdlib only)."""
from fractions import Fraction as Q

def in_P1(p):
    # P1 = B_inf^1 x B_1^3: |t|<=1 and ||w||_1<=1, split (x1 | x2,x3,x4)
    t, w = abs(p[0]), [abs(p[1]), abs(p[2]), abs(p[3])]
    return t <= 1 and sum(w) <= 1

def in_P1star(p):
    # P1* = {(t,w): |t| + ||w||_inf <= 1}
    return abs(p[0]) + max(abs(p[1]), abs(p[2]), abs(p[3])) <= 1

def in_P2(p):
    # P2 = B_inf^2 x B_1^2: max(|x1|,|x2|)<=1, |x3|+|x4|<=1
    return max(abs(p[0]), abs(p[1])) <= 1 and abs(p[2]) + abs(p[3]) <= 1

def in_P2star(p):
    # P2* = {(u,v): ||u||_1 + ||v||_inf <= 1}
    return abs(p[0]) + abs(p[1]) + max(abs(p[2]), abs(p[3])) <= 1

def swap(p, i, j):
    q = list(p); q[i], q[j] = q[j], q[i]; return tuple(q)

def check():
    cases = [
        ("P1 (1+3 inf-sum)", in_P1, (Q(1), Q(1,2), Q(1,2), Q(0)), (0, 1)),
        ("P1* (1+3 1-sum)", in_P1star, (Q(0), Q(0), Q(1), Q(1)), (0, 2)),
        ("P2 (2+2 inf-prod)", in_P2, (Q(1), Q(1), Q(1,2), Q(1,2)), (1, 2)),
        ("P2* (2+2 1-sum)", in_P2star, (Q(0), Q(0), Q(1), Q(1)), (0, 2)),
    ]
    for name, mem, a, (i, j) in cases:
        b = swap(a, i, j)
        assert mem(a), f"{name}: witness not in P"
        assert not mem(b), f"{name}: swapped witness still in P"
        print(f"{name}: a={[float(x) for x in a]} in P; swap({i},{j}) outside P. OK")
    # Cube and cross-polytope are S4-invariant by definition (max|x|, sum|x| symmetric).
    print("Cube B_inf^4 and cross-polytope B_1^4 are S4-invariant: by symmetric norms.")
    print("CENSUS_OK: exactly 2 of 6 Hanner types in R^4 are S4-invariant (up to the standard census).")
check()
