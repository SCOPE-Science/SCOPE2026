"""Exact verification of skew-symmetric Littlewood demerit-factor moments.

Stdlib only. Exhaustively enumerates the full skew-symmetric subspace
(2^m sequences, m=(n+1)/2) for odd n=3..21, using exact integer
autocorrelations and Fraction arithmetic. Checks:
  (1) C_k == 0 identically for all odd k;
  (2) E[C_k^2] == 2(n-k)-1 for all even k;
  (3) mean energy == (m-1)(2m-3), mean demerit == (m-1)(2m-3)/n^2;
  (4) strict bias M_skew - M_unrest == -2(m-1)/n^2 < 0 (m>1);
  (5) prints exact variance table Var(E), Var(D).
"""
from fractions import Fraction
from itertools import product


def skew_seqs(m):
    n = 2 * m - 1
    c = m - 1
    for bits in product((1, -1), repeat=m):
        s = [0] * n
        for i in range(m):
            s[i] = bits[i]
        for t in range(1, m):
            s[c + t] = ((-1) ** t) * bits[c - t]
        yield s


def autocorrs(s):
    n = len(s)
    return [sum(s[j] * s[j + k] for j in range(n - k)) for k in range(1, n)]


def main():
    var_table = {}
    for m in range(2, 12):
        n = 2 * m - 1
        cnt = 1 << m
        sum_E = 0
        sum_E2 = 0
        # per-k sums of C_k^2
        ksum = {k: 0 for k in range(1, n)}
        odd_nonzero = 0
        for s in skew_seqs(m):
            ck = autocorrs(s)
            for idx, k in enumerate(range(1, n)):
                ksum[k] += ck[idx] * ck[idx]
                if k % 2 == 1 and ck[idx] != 0:
                    odd_nonzero += 1
            e = sum(v * v for v in ck)
            sum_E += e
            sum_E2 += e * e
        assert odd_nonzero == 0, (m, odd_nonzero)
        for k in range(1, n):
            ek = Fraction(ksum[k], cnt)
            if k % 2 == 1:
                assert ek == 0, (m, k, ek)
            else:
                assert ek == 2 * (n - k) - 1, (m, k, ek)
        meanE = Fraction(sum_E, cnt)
        assert meanE == (m - 1) * (2 * m - 3), (m, meanE)
        varE = Fraction(sum_E2, cnt) - meanE * meanE
        meanD = Fraction(meanE, n * n)
        varD = Fraction(varE, n ** 4)
        mun = Fraction(n - 1, 2 * n)
        assert meanD - mun == Fraction(-2 * (m - 1), n * n), (m, meanD)
        assert meanD < mun
        var_table[n] = (meanE, varE, meanD, varD)
        print(f"n={n} m={m}: meanE={meanE} VarE={varE} "
              f"meanD={meanD} VarD={varD} gap={meanD - mun}")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
