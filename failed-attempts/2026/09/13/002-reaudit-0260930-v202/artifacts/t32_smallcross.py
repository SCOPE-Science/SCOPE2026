"""T32 (final, bounded): cross-check the ten smaller r=2 factors F(mu,k) by the
character-free matrix pipeline: F_disconn(mu,k;2) = |Ck| (M^2)[mu,k]/9!.
Assert equality with MN character values from T29."""
import sys
sys.path.insert(0, "output/artifacts")
from fractions import Fraction
from math import factorial
from collections import Counter
from t11_gjv import build_M
from char_sum import hurwitz_double
types, M = build_M()
idx = {t: i for i, t in enumerate(types)}
def csize(ct):
    c = Counter(ct); z = 1
    for ln, m in c.items(): z *= (ln**m)*factorial(m)
    return factorial(9)//z
n = len(types)
M2 = [[sum(M[i][k]*M[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
A=(6,2,1); B=(3,3,3)
K = [(9,),(4,4,1),(4,3,2),(5,3,1),(5,2,2)]
ok = True
for k in K:
    for mu in (A, B):
        hMN, nMN = hurwitz_double(tuple(mu), tuple(k), 2, 9)
        nMat = M2[idx[tuple(sorted(mu, reverse=True))]][idx[k]]*csize(k)
        hMat = Fraction(nMat, factorial(9))
        flag = "OK" if (hMN == hMat and nMN == nMat) else "MISMATCH"
        if hMN != hMat or nMN != nMat: ok = False
        print(flag, mu, k, "MN H =", hMN, "N =", nMN, "| matrix H =", hMat, "N =", nMat)
print("ALL TEN CROSS-CHECKED" if ok else "FAILURES")
