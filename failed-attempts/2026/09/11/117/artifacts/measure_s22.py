"""TARGET measurement: S22 near the diagonal lambda0=lambda1.

S22(t,h) = sum over ordered triples (a,m,b), a!=m, b!=m, of
chain_term(a,m,b,2,2,lam)/8, with lam = (t+h, t-h, 3, 7, 11).

chain_term is the calibrated assembly from derive_s22.py (validated by
n1=2875 at three weight sets and N2=4876875/8 at three weight sets, i.e.
equivalent to n2=609250 via Aspinwall-Morrison).

Laurent analysis: substitute h->0 symbolically per term; each term is
c_{-k}(t)/h^k + ... with k<=2 (d=2 doubles the (li-lj) factors).
Cancel symbolically: S22 = P(h)/Q(h) over QQ(t)[h]; read pole order and residue.
Fractions in t are handled by evaluating at several integer t values and
interpolating (residue must be t-independent per the claim; pole order likewise).
"""
import itertools
from fractions import Fraction as Q
import sys
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-998/output/artifacts")
from derive_s22 import chain_term

SPEC = (Q(3), Q(7), Q(11))

def S22_at(t, h):
    lam = (t + h, t - h) + SPEC
    tot = Q(0)
    for a, m, b in itertools.product(range(5), repeat=3):
        if a == m or b == m:
            continue
        tot += chain_term(a, m, b, 2, 2, lam)
    return tot / 8  # ordered weight 1/(2*d1*d2) = 1/8

def laurent_at_t(t, npts=7):
    """Fit S22(t,h) = sum_{k} c_k h^k for h in small offsets; exact over QQ.
    Use values at h = 1/L for large L to solve for coefficients c_{-2..3}."""
    hs = [Q(1, L) for L in range(50, 50 + npts)]
    ys = [S22_at(Q(t), h) for h in hs]
    # Solve Vandermonde for exponents -2..npts-3
    import copy
    exps = list(range(-2, npts - 2))
    n = len(exps)
    # Gaussian elimination over Fractions
    M = [[hs[j] ** e for e in exps] + [ys[j]] for j in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pivv = M[col][col]
        M[col] = [x / pivv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [rv - f * cv for rv, cv in zip(M[r], M[col])]
    return dict(zip(exps, [M[i][n] for i in range(n)]))

if __name__ == "__main__":
    print("S22 term count:", sum(1 for a in range(5) for m in range(5) for b in range(5) if a != m and b != m))
    for t in (0, 1, 5, 17, 100):
        c = laurent_at_t(t)
        print(f"t={t}: " + " ".join(f"h^{e}:{c[e]}" for e in sorted(c)))
    print("target residue: -125/96 =", Q(-125, 96))
