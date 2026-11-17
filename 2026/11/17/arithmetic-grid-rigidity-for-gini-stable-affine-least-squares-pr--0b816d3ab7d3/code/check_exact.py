"""Exact-rational diagnostics for Gini stability of affine least-squares fitting.

Run with: python code/check_exact.py
Uses only Python's standard library. Exact finite tests corroborate the proof
but do not replace its all-dimensional coarea and differentiability arguments.
"""
from fractions import Fraction as Q
from itertools import product, combinations


def gini(v):
    return sum(abs(v[j] - v[i]) for i in range(len(v)) for j in range(i + 1, len(v)))


def proj(t, y):
    n = len(t)
    mean_t = sum(t) / n
    mean_y = sum(y) / n
    centered = [v - mean_t for v in t]
    s = sum(v * v for v in centered)
    b = sum(ci * yi for ci, yi in zip(centered, y)) / s
    return [mean_y + b * ci for ci in centered]


def exact_norm(t):
    n = len(t)
    assert n >= 2 and all(t[i] < t[i + 1] for i in range(n - 1))
    c = [v - sum(t) / n for v in t]
    B = gini(t)
    S = sum(x * x for x in c)
    mks = [sum(c[n - k:]) / (k * (n - k)) for k in range(1, n)]
    return B / S * max(mks), mks


def cut_norm(t):
    n = len(t)
    best = Q(0)
    witness = None
    for k in range(1, n):
        for S in combinations(range(n), k):
            x = [Q(int(i in S)) for i in range(n)]
            ratio = gini(proj(t, x)) / gini(x)
            if ratio > best:
                best = ratio
                witness = S
    return best, witness


def derivative_data(h):
    n = len(h)
    r = [Q(2 * i + 1 - n, 2) for i in range(n)]
    mean = sum(h) / n
    d = [sum(h[n - k:]) / (k * (n - k)) - mean / (n - k) for k in range(1, n)]
    w = [k * (n - k) for k in range(1, n)]
    avg = sum(wk * dk for wk, dk in zip(w, d)) / sum(w)
    assert avg == sum(ri * hi for ri, hi in zip(r, h)) / sum(w)
    return Q(2) * (max(d) - avg), Q(2) * (avg - min(d)), d


def main():
    cases = 0
    cuts = 0
    arbitrary = 0
    derivatives = 0
    irregular = 0
    for n in range(2, 9):
        grids = [list(map(Q, range(n))),
                 [Q(i*i + i + 1) for i in range(n)],
                 [Q(3*i + (i % 2)) for i in range(n)],
                 [Q(i*i + 5*i + 2) for i in range(n)]]
        for t in grids:
            assert all(t[i] < t[i + 1] for i in range(n-1))
            nrm, mks = exact_norm(t)
            direct, witness = cut_norm(t)
            assert nrm == direct, (n, t, nrm, direct)
            cuts += 2**n-2
            if n >= 3:
                is_equal = len(set(t[i+1]-t[i] for i in range(n-1))) == 1
                assert (nrm == 1) == is_equal
                if not is_equal:
                    assert nrm > 1
                    irregular += 1
            else:
                assert nrm == 1
            for v in product((-1, 0, 1), repeat=n):
                y = [Q(a) for a in v]
                if gini(y):
                    assert gini(proj(t, y)) <= nrm * gini(y)
                    arbitrary += 1
            cases += 1
        for variant in range(4):
            h = [Q((i*i + 3*variant*i + (i+variant)%3) % 13-6) for i in range(n)]
            dplus, dminus, d = derivative_data(h)
            assert dplus >= 0 and dminus >= 0
            r = [Q(2*i+1-n, 2) for i in range(n)]
            b0 = sum(range(1,n))  # overwritten below
            b0 = gini(r)
            s0 = sum(x*x for x in r)
            assert b0 == 2*s0
            bb = sum(Q(2*i+1-n)*h[i] for i in range(n))
            sh = sum(h)/n
            sb = 2*sum(r[i]*(h[i]-sh) for i in range(n))
            deriv_ratio = (bb*s0-b0*sb)/(s0*s0)
            assert deriv_ratio/Q(2)+Q(2)*max(d) == dplus
            assert deriv_ratio/Q(2)+Q(2)*min(d) == -dminus
            derivatives += 1
    assert exact_norm(list(map(Q, [0,1,2,9])))[0] == Q(28,25)
    print('EXACT_ALL_BINARY_CUT_OPERATOR_NORMS_PASSED',cuts)
    print('EXACT_RATIONAL_TWO_INPUT_BOUNDS_PASSED',arbitrary)
    print('EXACT_UNIFORM_RIGIDITY_AND_IRREGULAR_AMPLIFICATION_PASSED',cases,irregular)
    print('EXACT_TWO_SIDED_PERTURBATION_DERIVATIVES_PASSED',derivatives)
    print('EXPLICIT_FOUR_SAMPLE_28_OVER_25_WITNESS_PASSED')
    print('ALL_AFFINE_GINI_DESIGN_CHECKS_PASSED')


if __name__ == '__main__':
    main()
