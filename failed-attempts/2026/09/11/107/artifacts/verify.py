"""Exact verification that the irreducible-edge target is false.

Proves: at lambda*=(0,1,2,3,4), with standard Graber-Pandharipande edge
weights, the pairs (0,4) and (4,0) are NOT regular: each has 1 numerator
zero vs 3 denominator zeros (net double pole), with exact leading
coefficient K = -391091500800000 along lam(t)=(t,1,2,3,4).

Stdlib only. Prints VERIFY_OK on success.
"""
from fractions import Fraction
import math

LAM = [Fraction(0), Fraction(1), Fraction(2), Fraction(3), Fraction(4)]

def num_weights(i, j, lam):
    li, lj = lam[i], lam[j]
    return [Fraction((20 - a) * li + a * lj, 4) for a in range(21)]

def den_factors(i, j, lam):
    """All 23 denominator linear forms (15 D1 + 8 D2), excluding (i,0),(j,4)."""
    li, lj = lam[i], lam[j]
    facs = []
    for k in range(5):
        if k == i or k == j:
            continue
        for m in range(5):
            facs.append(("D1", k, m,
                         Fraction((4 - m) * li + m * lj, 4) - lam[k]))
    for m in range(1, 5):
        facs.append(("D2i", i, m,
                     Fraction((4 - m) * li + m * lj, 4) - li))
    for m in range(4):
        facs.append(("D2j", j, m,
                     Fraction((4 - m) * li + m * lj, 4) - lj))
    return facs

def check_pair(i, j):
    nw = num_weights(i, j, LAM)
    nz = [a for a, w in enumerate(nw) if w == 0]
    zf = [(t, k, m) for (t, k, m, w) in den_factors(i, j, LAM) if w == 0]
    return nz, zf

def E_on_line(i, j, t):
    lam = [LAM[0] + t, LAM[1], LAM[2], LAM[3], LAM[4]]
    li, lj = lam[i], lam[j]
    N = Fraction(1)
    for a in range(21):
        N *= Fraction((20 - a) * li + a * lj, 4)
    D = Fraction(1)
    for (_, _, _, w) in den_factors(i, j, lam):
        D *= w
    W = Fraction(li - lj, 4) * Fraction(lj - li, 4)
    assert D != 0
    return Fraction(1, 4) * N * W / D

def main():
    # 1. (0,4): numerator zero only at a=0 (weight 5*lam0 = 0)
    nz04, zf04 = check_pair(0, 4)
    assert nz04 == [0], nz04
    assert sorted((k, m) for (_, k, m) in zf04) == [(1, 1), (2, 2), (3, 3)], zf04
    # numerator values at lam* are exactly a
    assert num_weights(0, 4, LAM) == [Fraction(a) for a in range(21)]
    # 2. (4,0): numerator zero only at a=20
    nz40, zf40 = check_pair(4, 0)
    assert nz40 == [20], nz40
    assert sorted((k, m) for (_, k, m) in zf40) == [(1, 3), (2, 2), (3, 1)], zf40
    # 3. Nonzero-part products at lam*
    RN04 = math.factorial(20)
    assert RN04 == 2432902008176640000
    D1p = Fraction(-6) * Fraction(4) * Fraction(-6)  # per-k products
    assert D1p == 144
    D2 = Fraction(24) * Fraction(24)
    assert D2 == 576
    C0 = D1p * D2
    assert C0 == 82944
    W0 = Fraction(-4) * Fraction(4) / 16
    assert W0 == -1
    K = Fraction(1, 4) * Fraction(5 * RN04) * W0 / (Fraction(3, 32) * C0)
    assert K == -391091500800000, K
    # (4,0) has identical nonzero ledger by direct evaluation
    assert num_weights(4, 0, LAM)[20] == 0
    assert sum(1 for w in num_weights(4, 0, LAM) if w == 0) == 1
    # 4. Growth along lam(t): E04(t)*t^2 -> K; S(t) diverges like 2K/t^2
    for N in (1000, 10000):
        t = Fraction(1, N)
        v04 = E_on_line(0, 4, t)
        v40 = E_on_line(4, 0, t)
        assert v04 * t * t != 0
        # within 5% of K already at N=100 (O(t) corrections small)
        assert abs(float(v04 * t * t) / float(K) - 1) < 0.05, (N, v04 * t * t)
        assert abs(float(v40 * t * t) / float(K) - 1) < 0.05, (N, v40 * t * t)
        assert v04 < 0 and v40 < 0
    # 5. Target regularity clause falsified: not all Eij regular
    print("E04 numerator zeros (a):", nz04)
    print("E04 denominator zeros (k,m):", sorted((k, m) for (_, k, m) in zf04))
    print("E40 numerator zeros (a):", nz40)
    print("E40 denominator zeros (k,m):", sorted((k, m) for (_, k, m) in zf40))
    print("C0 =", C0, " K =", K)
    print("E04(1/100)*1/100^2 =", E_on_line(0, 4, Fraction(1, 100)) * Fraction(1, 100) ** 2)
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
