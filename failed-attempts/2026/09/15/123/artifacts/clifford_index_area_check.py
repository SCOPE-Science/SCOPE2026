"""Bounded recovery test: verify Clifford index = n+3 and area table.
Jacobi operator J = Delta + (|A|^2 + n) = Delta + 2n on Clifford minimal
hypersurface S^k(r1) x S^{n-k}(r2), r1=sqrt(k/n), r2=sqrt((n-k)/n).
Index = #{Laplacian eigenvalues < 2n, with multiplicity}.
"""
import math
from math import comb


def sphere_area(m, r):
    return (r ** m) * 2 * (math.pi ** ((m + 1) / 2)) / math.gamma((m + 1) / 2)


def mult_sphere(m, j):
    if j == 0:
        return 1
    if m == 1:
        return 2
    if j == 1:
        return m + 1
    return comb(m + j, j) - comb(m + j - 2, j - 2)


def eig_sphere(m, r2, j):
    if m == 1:
        return j * j / r2
    return j * (j + m - 1) / r2


def index_clifford(n, k, jmax=8):
    r1sq = k / n
    r2sq = (n - k) / n
    idx = 0
    terms = []
    for j1 in range(jmax + 1):
        for j2 in range(jmax + 1):
            s = eig_sphere(k, r1sq, j1) + eig_sphere(n - k, r2sq, j2)
            if s < 2 * n - 1e-9:
                m = mult_sphere(k, j1) * mult_sphere(n - k, j2)
                idx += m
                terms.append(((j1, j2), round(s, 3), m))
    return idx, terms


print("== Area table: equator vs Clifford ==")
for n in [3, 4, 5, 6]:
    eq = sphere_area(n, 1.0)
    print(f"n={n} equator area={eq:.6f}")
    for k in range(1, n):
        r1 = math.sqrt(k / n)
        r2 = math.sqrt((n - k) / n)
        a = sphere_area(k, r1) * sphere_area(n - k, r2)
        print(f"  k={k} Clifford area={a:.6f} ratio={a / eq:.4f}")

print()
print("== Index check: count Laplacian eigenvalues < 2n ==")
ok = True
for n in [3, 4, 5, 6]:
    for k in range(1, n):
        idx, terms = index_clifford(n, k)
        status = "OK" if idx == n + 3 else "FAIL"
        if idx != n + 3:
            ok = False
        print(f"n={n} k={k} index={idx} expected={n + 3} [{status}] terms={terms}")
print()
print("ALL CLIFFORD INDEX CHECKS PASS" if ok else "MISMATCH FOUND")
