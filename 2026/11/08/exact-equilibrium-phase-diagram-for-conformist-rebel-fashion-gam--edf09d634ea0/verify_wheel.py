"""Direct exact enumeration for pure equilibria of binary wheel fashion games.

No external packages. The analytic proof is separate: this program verifies finite
instances only, and does not infer the all-size theorem from enumeration.
"""
from math import comb
from fractions import Fraction


def perrin(m):
    p = [3, 0, 2]
    for k in range(3, m + 1):
        p.append(p[k - 2] + p[k - 3])
    return p


def compositions23(m):
    c = [0] * (m + 1)
    c[0] = 1
    for k in range(1, m + 1):
        c[k] = (c[k - 2] if k >= 2 else 0) + (c[k - 3] if k >= 3 else 0)
    return c


def is_nash(n, hub, rim, hub_conformist, defect):
    # A rim player has precisely three neighbors, so its best reply is strict.
    for i in range(n):
        ones = hub + rim[(i - 1) % n] + rim[(i + 1) % n]
        is_conformist = defect and i == 0
        if is_conformist:
            if rim[i] != int(ones >= 2):
                return False, False
        else:
            if rim[i] != int(ones <= 1):
                return False, False
    same = sum(v == hub for v in rim)
    if hub_conformist:
        good = 2 * same >= n
        strict = 2 * same > n
    else:
        good = 2 * same <= n
        strict = 2 * same < n
    return good, good and strict


def test():
    p = perrin(15)
    c = compositions23(15)
    checks = 0
    profiles = 0
    for n in range(3, 16):
        # Direct count of maximal independent sets of a cycle.
        rooted = sum(Fraction(n, z) * comb(z, n - 2 * z)
                     for z in range((n + 2) // 3, n // 2 + 1))
        assert rooted.denominator == 1 and rooted.numerator == p[n], (n, rooted, p[n])
        for defect in (False, True):
            for hub_conformist in (False, True):
                expected = ((4 if n % 2 == 0 else 0) if hub_conformist else 2 * p[n]) if not defect else (0 if hub_conformist else 2 * (c[n - 4] if n >= 4 else 0))
                expected_strict = (0 if hub_conformist else
                                   (2 * p[n] - (4 if n % 2 == 0 else 0)) if not defect else
                                   2 * (c[n - 4] if n >= 4 else 0))
                count = strict_count = 0
                for raw in range(1 << (n + 1)):
                    hub = raw & 1
                    rim = tuple((raw >> (i + 1)) & 1 for i in range(n))
                    ok, strict = is_nash(n, hub, rim, hub_conformist, defect)
                    count += ok
                    strict_count += strict
                    profiles += 1
                assert (count, strict_count) == (expected, expected_strict), (n, defect, hub_conformist, count, strict_count, expected, expected_strict)
                checks += 1
    print(f"CHECK_OK: {checks} exact wheel/type cases; {profiles} complete action profiles;")
    print("Perrin MIS identity checked for n=3..15; both total and strict equilibrium counts confirmed.")


if __name__ == "__main__":
    test()
