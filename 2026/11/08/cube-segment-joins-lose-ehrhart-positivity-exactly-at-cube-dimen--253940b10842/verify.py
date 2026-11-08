"""Exact arithmetic checks for cube--segment join Ehrhart coefficients.

The analytic proof is in RESULT.md; this independent arithmetic checker
confirms the coefficient formulas and the first sharp cutoff.
"""
from fractions import Fraction
from math import comb, factorial


def bernoulli(upto):
    b = [Fraction(1)]
    for n in range(1, upto + 1):
        b.append(-sum(Fraction(comb(n + 1, j)) * b[j]
                      for j in range(n)) / Fraction(n + 1))
    return b


def ehrhart_coefficients(d):
    # L_d(t) = sum_{j=0}^t (t-j+1)(j+1)^d at integer arguments.
    vals = [sum((t - j + 1) * (j + 1) ** d
                for j in range(t + 1)) for t in range(d + 3)]
    diffs = [vals]
    while len(diffs[-1]) > 1:
        a = diffs[-1]
        diffs.append([a[j + 1] - a[j] for j in range(len(a) - 1)])
    res = [Fraction(0) for _ in range(d + 3)]
    falling = [1]
    for k in range(d + 3):
        scale = Fraction(diffs[k][0], factorial(k))
        for j, a in enumerate(falling):
            res[j] += scale * a
        # multiply by (t - k)
        new = [0] * (len(falling) + 1)
        for j, a in enumerate(falling):
            new[j] -= k * a
            new[j + 1] += a
        falling = new
    return res


def main():
    b = bernoulli(36)
    assert b[1] == Fraction(-1, 2)
    assert b[16] == Fraction(-3617, 510)
    assert b[18] == Fraction(43867, 798)
    checks = 0
    for d in range(1, 33):
        c = ehrhart_coefficients(d)
        assert c[0] == 1
        assert c[-1] == Fraction(1, (d + 1) * (d + 2))
        assert c[-2] == Fraction(2, d + 1)
        if d >= 2:
            assert c[d] == Fraction(23, 12)
            assert c[1] == d + 2 * b[d] - b[d + 1]
        else:
            assert c[1] == Fraction(11, 6)
        checks += 4
        for k in range(2, d):
            r = d + 2 - k
            pref = Fraction(comb(d + 1, k - 1) * (r - 1),
                            k * (d + 1))
            if r % 2 == 0:
                predicted = pref * (r - b[r])
            else:
                predicted = pref * (r + Fraction(2 * r, r - 1) * b[r - 1])
            assert c[k] == predicted, (d, k, c[k], predicted)
            checks += 1
        if d <= 16:
            assert all(z > 0 for z in c)
        elif d == 17:
            assert c[1] == Fraction(-30301, 798)
            assert all(c[k] > 0 for k in range(2, d + 3))
        else:
            r = max(x for x in range(18, d + 1) if x % 4 == 2)
            k = d + 2 - r
            assert 2 <= k <= d - 1 and c[k] < 0
        checks += 1
        # Explicit polynomial recount at all d+3 interpolation nodes.
        for t in range(d + 3):
            expected = sum((t - j + 1) * (j + 1) ** d
                           for j in range(t + 1))
            assert sum(c[j] * (t ** j) for j in range(len(c))) == expected
            checks += 1
    print(f"EXACT_CHECKS_OK={checks}")
    print("CRITICAL_COEFFICIENT_d17_t1=-30301/798")
    print("EHRHART_POSITIVE_d1_TO_d16=YES")
    print("NEGATIVE_WITNESSES_d17_TO_d32=YES")


if __name__ == "__main__":
    main()
