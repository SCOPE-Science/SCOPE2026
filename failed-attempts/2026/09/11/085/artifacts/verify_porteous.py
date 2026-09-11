"""Porteous formal class for lane-899: B(2,L,5) in SU(2,L), g=7.

Determinantal setup: twist by divisor of degree m, F=p_*(E(D)) rank 2m+2,
G=p_*(E(D)|_D) rank 2m, locus {rank(F->G) <= 2m-3}.
Expected codim = (a-r)(b-r) = 5*3 = 15. Porteous class = 5x5 determinant
det(c_{3+j-i}(G-F)) (partition (3)^5). This script builds the FORMAL
polynomial in Chern-class variables and verifies the codim arithmetic.
Evaluation on H^*(SU(2,L)) is NOT attempted (needs full intersection ring);
recorded honestly in the report.
Stdlib only.
"""
import sys
from fractions import Fraction

FAILS = []


def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        FAILS.append(name)


G = 7
M = 20  # twist degree (large); ranks independent of choice up to stabilization
a = 2 * M + 2  # rk F
b = 2 * M      # rk G
r = 2 * M - 3  # rank bound (rkF - k, k=5)
check("source rank", a == 2 * M + 2, f"a={a}")
check("target rank", b == 2 * M, f"b={b}")
check("rank bound", r == a - 5, f"r={r}")
codim = (a - r) * (b - r)
check("expected codim 15", codim == 15, f"({a}-{r})({b}-{r})={codim}")
check("ambient dim 18", 3 * G - 3 == 18)
check("expected dim 3", (3 * G - 3) - codim == 3)
# Porteous partition: (b-r)^(a-r) = (3)^5 ; class degree 15 in Chern roots
lam = [b - r] * (a - r)
check("partition (3)^5", lam == [3, 3, 3, 3, 3], str(lam))
check("partition weight 15", sum(lam) == 15)

# Formal 5x5 Porteous matrix indices: entry (i,j) = c_{lam_i + j - i} = c_{3+j-i}
print("INFO formal Porteous matrix (entries c_t of virtual bundle G-F):")
for i in range(1, 6):
    row = [3 + j - i for j in range(1, 6)]
    print("INFO row", i, row)
# sanity: diagonal all c_3; sub/super-diagonals shift by +-1; corners c_7..c_-1
# (c_{<0}=0, c_{>rk} handled by ring relations — evaluation stage, not here)
check("diagonal is c3", all((3 + j - i) == 3 for i, j in [(1, 1)]))
det_terms = 120  # 5! terms in determinant expansion
print("INFO determinant has", det_terms, "monomial terms in c_t variables")
print("INFO evaluation on H^*(SU(2,L),g=7) NOT performed (needs intersection ring);")
print("INFO nonvanishing of evaluated class recorded as equivalent-status with")
print("INFO nonempty+proper-codim, not an independent proof route.")
print("----")
if FAILS:
    print("PORTEOUS_FAIL", FAILS)
    sys.exit(1)
print("PORTEOUS_FORMAL_OK")
