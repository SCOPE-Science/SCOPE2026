"""Reproducibility checks for finite circular-arc vacancy statistics.

Only exact finite calculations and numerical root checks; the analytical
proof of global root uniqueness and asymptotics is in RESULT.md.
"""
from fractions import Fraction
from math import comb, exp


def continuous_cov(n, a):
    assert n >= 2 and Fraction(0) < a < Fraction(1)
    t = 1 - a
    u = max(Fraction(0), 1 - 2*a)
    return t**n + (n - 1)*u**n - n*t**(2*n - 1)


def discrete_exact_cov(n, length, arc):
    """Exact covariance for uniformly chosen positive integer cyclic gaps.

    Gaps are uniform positive compositions of `length` into n parts;
    K counts gaps > arc, and U is total excess divided by length.
    This finite lattice model independently approximates the continuous
    Dirichlet spacing law as length grows.
    """
    assert n >= 2 and 0 < arc < length
    dp = {0: (1, 0, 0, 0)}
    for pos in range(n):
        new = {}
        remaining = n - pos - 1
        for used, (count, sum_k, sum_u, sum_ku) in dp.items():
            for gap in range(1, length - used - remaining + 1):
                k = int(gap > arc)
                u = max(gap - arc, 0)
                rec = new.get(used + gap, (0, 0, 0, 0))
                new[used + gap] = (
                    rec[0] + count,
                    rec[1] + sum_k + count*k,
                    rec[2] + sum_u + count*u,
                    rec[3] + sum_ku + u*sum_k + k*sum_u + count*k*u,
                )
        dp = new
    count, sum_k, sum_u, sum_ku = dp[length]
    assert count == comb(length - 1, n - 1)
    return Fraction(sum_ku*count - sum_k*sum_u, count*count*length)


def zero_bisect(n):
    lo = 1e-7
    hi = .99
    for _ in range(75):
        mid = (lo+hi)/2
        val = float(continuous_cov(n, mid))
        if val > 0: hi = mid
        else: lo = mid
    return (lo+hi)/2


def main():
    print('Exact rational sign tests (n, initial negative, terminal positive):')
    for n in range(2, 21):
        f_low = continuous_cov(n, Fraction(1, 10*n))
        f_high = continuous_cov(n, Fraction(3, 4))
        assert f_low < 0 and f_high > 0
        print(n, f_low < 0, f_high > 0)
    print('Independent lattice-composition comparison:')
    for n, L, b in [(3, 80, 16), (3, 160, 32), (4, 80, 16), (4, 160, 32),
                    (4, 80, 40), (4, 160, 80), (5, 80, 16), (5, 160, 32)]:
        d = discrete_exact_cov(n, L, b)
        c = continuous_cov(n, Fraction(b, L))
        print(f'n={n}, L={L}, a={b}/{L}, discrete={float(d):.9g}, continuous={float(c):.9g}, error={float(d-c):.9g}')
    c_star = 1.793282132900598
    print('Thresholds and two-term scaling:')
    for n in (2,3,4,5,10,25,50,100):
        a = zero_bisect(n)
        approx = c_star/n + (c_star/2 - c_star*c_star)/(n*n)
        print(f'n={n}, threshold={a:.12g}, n*threshold={n*a:.12g}, two-term={approx:.12g}')
        assert abs(continuous_cov(n, a)) < 1e-9
    assert continuous_cov(2, Fraction(1,2)) == 0
    print('All verification checks passed.')

if __name__ == '__main__':
    main()
