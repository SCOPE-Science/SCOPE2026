"""Exact rational checks for a two-level E-optimal coordinate sampling formula.

Run: python artifacts/verify_friendship_sampling.py
No third-party packages are required. This tests finite cases; the theorem is symbolic.
"""
from fractions import Fraction as Q


def design(m, s, t):
    q = 2 * m
    c = 1 + s
    r = q * t * t
    assert m >= 2 and 0 < s < 1 and t > 0 and r < c
    boundary = (t + r) / (2 + t)
    if s <= boundary:
        den = c + q + 2 * q * t
        x = (c + q * t) / den
        y = (1 + t) / den
        rate = (c - r) / den
        phase = "radial"
    else:
        den = 2 * s * (1 - s) + q * (2 * s - r)
        x = 2 * s * (1 - s) / den
        y = (2 * s - r) / den
        rate = (1 - s) * y
        phase = "pair"
    return x, y, rate, phase


def radial_ge(x, y, threshold, c, r):
    """Exact criterion: the least radial eigenvalue is >= threshold."""
    if x < threshold or c * y < threshold:
        return False
    return (x - threshold) * (c * y - threshold) >= r * x * y


def radial_gt(x, y, threshold, c, r):
    return x > threshold and c * y > threshold and (x - threshold) * (c * y - threshold) > r * x * y


def matrix(m, s, t):
    q = 2 * m
    n = q + 1
    C = [[Q(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(1, n):
        C[0][i] = C[i][0] = t
    for i in range(m):
        a, b = 2 * i + 1, 2 * i + 2
        C[a][b] = C[b][a] = s
    return C


def energy(C, v):
    return sum(v[i] * C[i][j] * v[j] for i in range(len(v)) for j in range(len(v)))


def matvec(C, v):
    return [sum(C[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]


def verify():
    designs = 0
    radial_certificates = 0
    grid_bounds = 0
    energy_identities = 0
    phase_counts = {"radial": 0, "pair": 0}
    for m in range(2, 8):
        q = 2 * m
        for s in [Q(1, 20), Q(1, 10), Q(1, 5), Q(2, 5), Q(3, 5), Q(4, 5), Q(9, 10)]:
            for t in [Q(1, 40), Q(1, 20), Q(1, 10), Q(3, 20), Q(1, 5), Q(1, 4), Q(3, 10), Q(1, 3), Q(2, 5)]:
                c, r = 1 + s, q * t * t
                if r >= c:
                    continue
                x, y, rate, phase = design(m, s, t)
                assert x > 0 and y > 0 and x + q * y == 1
                assert radial_ge(x, y, rate, c, r)
                assert (1 - s) * y >= rate
                assert (x - rate) * (c * y - rate) == r * x * y
                if phase == "pair":
                    assert (1 - s) * y == rate
                    assert s > (t + r) / (2 + t)
                else:
                    assert s <= (t + r) / (2 + t)
                designs += 1
                radial_certificates += 1
                phase_counts[phase] += 1
                # No class-symmetric rational grid design can exceed the claimed rate.
                for k in range(101):
                    trial_x = Q(k, 100)
                    trial_y = (1 - trial_x) / q
                    assert (1 - s) * trial_y <= rate or not radial_gt(trial_x, trial_y, rate, c, r), (m,s,t,k,x,y,rate,trial_x,trial_y,phase)
                    grid_bounds += 1
                if m <= 4 and designs % 4 == 0:
                    C = matrix(m, s, t)
                    p = [x] + [y] * q
                    v = [Q((3 * i + 2) % 11 - 5, 7) for i in range(q + 1)]
                    grad = matvec(C, v)
                    expected = energy(C, v) - sum(p[i] * grad[i] ** 2 for i in range(q + 1))
                    actual = Q(0)
                    for i in range(q + 1):
                        updated = v.copy()
                        updated[i] -= grad[i]
                        actual += p[i] * energy(C, updated)
                    assert expected == actual
                    energy_identities += 1
    assert phase_counts["radial"] > 0 and phase_counts["pair"] > 0
    # Exact special point, where the pairwise mode limits the optimum.
    x, y, rate, phase = design(2, Q(1, 2), Q(1, 5))
    assert (x, y, rate, phase) == (Q(25, 193), Q(42, 193), Q(21, 193), "pair")
    # Both closed-form branches coincide exactly at a rational transition point.
    m, q, t, s = 2, 4, Q(1, 5), Q(9, 55)
    r = q * t * t
    assert s == (t + r) / (2 + t)
    x, y, rate, phase = design(m, s, t)
    den_pair = 2 * s * (1 - s) + q * (2 * s - r)
    assert phase == "radial"
    assert x == 2 * s * (1 - s) / den_pair
    assert y == (2 * s - r) / den_pair
    assert rate == (1 - s) * (2 * s - r) / den_pair
    print('PASS exact rational analytical checks')
    print('admissible parameter designs:', designs)
    print('radial/pair phases:', phase_counts['radial'], '/', phase_counts['pair'])
    print('exact active-eigenvalue certificates:', radial_certificates)
    print('symmetric rational-grid upper bounds:', grid_bounds)
    print('exact expected-energy identities:', energy_identities)
    print('witness m=2,s=1/2,t=1/5: hub=25/193, leaf=42/193, rate=21/193')
    print('scope: finite tests support; do not replace the general proof')


if __name__ == '__main__':
    verify()
