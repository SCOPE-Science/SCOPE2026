"""Independent finite-state and numerical tests for a resetting Zeno clock.
Python 3 standard library only. Finite tests do not certify the infinite theorem.
"""
from fractions import Fraction
from math import exp, gamma, log, isclose


def exact_depth(K, c=Fraction(2, 5), r=Fraction(1, 2), beta=2):
    # Absorb at depth K, with successful escape represented by zero extra time.
    a, b = Fraction(0), Fraction(0)
    for k in reversed(range(K)):
        p = c / (k + 1) ** beta
        a = r ** k + (1 - p) * a
        b = p + (1 - p) * b
    assert b != 1
    return a / (1 - b)


def independent_depth(K, c=Fraction(2, 5), r=Fraction(1, 2), beta=2):
    surv = Fraction(1)
    duration = Fraction(0)
    for k in range(K):
        duration += r ** k * surv
        surv *= 1 - c / (k + 1) ** beta
    return duration / surv


def zeta_em(s):
    assert s > 1
    n = 2048
    v = sum(k ** (-s) for k in range(1, n))
    v += n ** (1 - s) / (s - 1) + 0.5 * n ** (-s)
    v += s * n ** (-s - 1) / 12
    v -= s * (s + 1) * (s + 2) * n ** (-s - 3) / 720
    return v


def expected_clock(beta, c=0.4, r=0.55):
    # q = exp(-sum_{m>=1} c^m zeta(m*beta)/m)
    logq = -sum(c ** j * zeta_em(j * beta) / j for j in range(1, 120))
    surviv = 1.0
    duration = 1.0
    for k in range(1, 150):
        surviv *= 1 - c / k ** beta
        duration += r ** k * surviv
    return duration * exp(-logq)


def main():
    n = 0
    for K in range(1, 27):
        for b in (2, 3):
            for c in (Fraction(1, 3), Fraction(2, 5)):
                for r in (Fraction(1, 2), Fraction(2, 3)):
                    assert exact_depth(K, c, r, b) == independent_depth(K, c, r, b)
                    n += 1
    # critical beta=1 has s_k=(1-c)_k/k!, check the binomial generating series.
    c, r = 0.4, 0.55
    sk = 1.0
    m = 1.0
    for k in range(1, 180):
        sk *= 1 - c / k
        m += r ** k * sk
    crit = (1-r) ** (c-1)
    assert isclose(m, crit, rel_tol=2e-14)
    limit_amplitude = gamma(1-c) * crit
    ratios = []
    for beta in (1.3, 1.15, 1.08, 1.04, 1.02):
        mean = expected_clock(beta, c, r)
        ratio = mean / (limit_amplitude * exp(c / (beta-1)))
        ratios.append(ratio)
        assert 0.99 < ratio < 1.01, (beta, ratio)
    assert abs(ratios[-1] - 1) < abs(ratios[0] - 1)
    print('PASS', n, 'exact rational depth comparisons; critical generating identity')
    print('Near-critical amplitude ratios:', [round(x, 9) for x in ratios])
    print('Limit amplitude:', round(limit_amplitude, 12))
    print('Scope: finite tests and numerical asymptotic checks; infinite assertions proved analytically.')


if __name__ == '__main__':
    main()
