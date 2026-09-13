# Exact integer check: degree-1 Markov type I data (Vianna Prop 4.8 / §4).
# No floating point; all asserts exact.
from math import isqrt

print("=== Prop 4.8 constraint: n1+n2+n3+d = 12, d=1 => sum 11 ===")
cands = []
for n1 in range(1, 12):
    for n2 in range(1, 12):
        for n3 in range(1, 12):
            if n1 + n2 + n3 != 11:
                continue
            prod = 1 * n1 * n2 * n3
            r = isqrt(prod)
            if r * r != prod:
                continue
            ok = True
            for ni, nj, nk in ((n1, n2, n3), (n2, n3, n1), (n3, n1, n2)):
                if (1 * ni * nj) % nk != 0:
                    ok = False
            if ok:
                cands.append((n1, n2, n3, r))
print("admissible (n1,n2,n3,S):", cands)
assert (2, 3, 6, 6) in cands and (1, 5, 5, 5) in cands

print()
print("=== Min Markov triple (p,q,r)=(3,2,1) for (n1,n2,n3)=(2,3,6), d=1 ===")
n1, n2, n3, S = 2, 3, 6, 6
p, q, r = 3, 2, 1
lhs = n1*p*p + n2*q*q + n3*r*r
rhs = S*p*q*r
print("lhs =", lhs, "rhs =", rhs)
assert lhs == rhs == 36
print("OK: 2*9+3*4+6*1 = 36 = 6*3*2*1.")

print()
print("=== Newton-hull edge lengths (Thm 5.1: n1*p, n2*q, n3*r) ===")
L = (n1*p, n2*q, n3*r)
print("edge lengths:", L)
assert L == (6, 6, 6)
A, B, C = L
assert A + B > C and B + C > A and C + A > B
print("OK: genuine triangle (6,6,6).")

print()
print("=== Contrast: (1,5,5) small solutions are hull-degenerate ===")
def small_sols(n1, n2, n3, S, lim=12):
    out = []
    for pp in range(1, lim+1):
        for qq in range(1, lim+1):
            for rr in range(1, lim+1):
                if n1*pp*pp + n2*qq*qq + n3*rr*rr == S*pp*qq*rr:
                    out.append((pp, qq, rr))
    return out
deg = True
for (pp, qq, rr) in small_sols(1, 5, 5, 5):
    A, B, C = 1*pp, 5*qq, 5*rr
    if A + B > C and B + C > A and C + A > B:
        deg = False
        print("nondegenerate found:", (pp, qq, rr))
        break
print("all (1,5,5) solutions with p,q,r<=12 degenerate:", deg)
assert deg
print("OK: degree-1 triangular diagram must use the (2,3,6) family; pinned node type ((2,3),(3,2),(6,1)).")
