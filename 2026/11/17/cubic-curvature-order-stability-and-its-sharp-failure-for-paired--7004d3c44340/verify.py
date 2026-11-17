"""Independent finite tests of the paired-arc stability identities.

Analytical validity for arbitrary profiles is established in the accompanying proof;
this script checks formulas and representative feasible examples only.
"""
import math


def params(m):
    a = math.asin(2 * math.sin(m) - 1 / math.sin(m))
    assert 0 < a < m
    return a


def layer(m, delta):
    a = params(m)
    assert 0 < delta < min(m - a, a / 2)
    eta = a - math.asin(2 * math.sin(a) - math.sin(a + delta))
    assert 0 < eta < a
    # The two intervals on each side are arranged with opposite sign.
    q_one = (eta + delta - 2 * math.sin(eta) - 2 * math.sin(delta)
             + math.sin(eta + delta)) / 4
    deficit = delta - math.sin(delta) - 2 * q_one
    distance = eta + delta
    return eta, deficit, distance


def verify():
    m = math.asin(math.sqrt((1 + math.sqrt(17)) / 8))
    a = params(m)
    checked = 0
    for j in range(100):
        mm = math.pi / 4 + (math.pi / 2 - math.pi / 4) * (j + .5) / 100
        aa = params(mm)
        for k in range(10):
            delta = min(mm - aa, aa / 2) * (.01 + .95 * (k + 1) / 11)
            eta, gap, dist = layer(mm, delta)
            # Exact moment preservation, one half-line (even reflection handles other).
            assert abs(math.sin(aa) - math.sin(aa - eta) -
                       (math.sin(aa + delta) - math.sin(aa))) < 2e-14
            assert gap >= dist ** 3 / (12 * math.pi ** 2) - 2e-14
            assert gap > 0
            checked += 3
    ratios = []
    for k in range(5, 14):
        delta = 2 ** (-k)
        eta, gap, dist = layer(m, delta)
        ratios.append(gap / dist ** 3)
    assert abs(ratios[-2] - 1 / 16) < 0.00008, ratios[-2]
    assert 1/16 < ratios[0] < .067
    print('VERIFY_OK', checked, 'finite equalities and inequalities')
    print('m=', repr(m), 'a=', repr(a))
    print('cubic_ratio_start_end=', repr(ratios[0]), repr(ratios[-2]))
    print('claimed_asymptotic_ratio=', repr(1/16))


if __name__ == '__main__':
    verify()
