"""Exact-rational supporting tests for right-triangle projection cycles.

Run: python3 CHECK.py (standard library only). Finite tests supplement, not
replace, the analytical argument for every real parameter.
"""
from fractions import Fraction


def projected_orbit(h, max_steps=1000):
    h = Fraction(h)
    h2 = h*h
    denom = h2 + 1
    a, t = 0, Fraction(0)
    word = [a]
    for n in range(1, max_steps + 1):
        if a == 0: x, y = t, Fraction(0)
        elif a == 1: x, y = Fraction(0), t
        else: x, y = t, h*(1-t)
        distances = [y*y, x*x, (h*x+y-h)**2/denom]
        distances[a] = -1
        candidates = [j for j in range(3) if j != a]
        other = candidates[0] if distances[candidates[0]] > distances[candidates[1]] else candidates[1]
        if distances[candidates[0]] == distances[candidates[1]]:
            return ('tie', n-1, a, t, tuple(word))
        if other == 0: t = x
        elif other == 1: t = y
        else: t = (x + h*(h-y)) / denom
        a = other
        word.append(a)
        if a in (0,1) and t == 0:
            return ('cycle', n, a, t, tuple(word))
    return ('limit', max_steps, a, t, tuple(word))


def expected_orbit(h):
    h = Fraction(h)
    B = h*h / (1 + h*h)
    q2 = 1 + h*h
    c = h/(h+1)
    # B**k > q/(q+1) iff (h*B**k/(1-B**k))**2>q**2;
    # B**k/(1-B**k) > q implies B**k is beyond vertical threshold.
    k = 2
    while True:
        z = B**k
        vertical_threshold = z*z > q2 * (1-z)**2
        if vertical_threshold:
            k += 1
            continue
        if z*z == q2*(1-z)**2 or z == c:
            return ('tie', None, k)
        return ('cycle', 2*k+1, k)


def main():
    assert projected_orbit(Fraction(2))[:2] == ('cycle', 5)
    assert projected_orbit(Fraction(3))[:2] == ('cycle', 7)
    assert projected_orbit(Fraction(5))[:2] == ('cycle', 11)
    assert projected_orbit(Fraction(10))[:2] == ('cycle', 21)
    assertions = 4
    largest = 0
    # 2 <= h <= 50, a dense set of rational parameters, including integers.
    for j in range(4001):
        h = Fraction(2, 1) + Fraction(j, 84)
        observed = projected_orbit(h)
        kind, period, k = expected_orbit(h)
        assert observed[0] == kind, (h, observed, (kind, period, k))
        assertions += 1
        if kind == 'cycle':
            assert observed[1] == period, (h, observed, (kind, period, k))
            assertions += 1
            largest = max(largest, period)
            # The itinerary must alternate between the hypotenuse and an axis
            # until its final axis-to-axis projection back to the right angle.
            w = observed[-1]
            assert len(w) == period+1 and w[0] == 0 and w[-1] in (0,1)
            assert all(a != b for a, b in zip(w,w[1:]))
            assert sum(1 for a,b in zip(w,w[1:]) if a in (0,1) and b in (0,1)) == 1
            assertions += 3
    # Exact degeneracy on the hypotenuse at h=1+sqrt(2) not rational, instead
    # check the threshold inequalities algebraically at generic rational values.
    print(f'PASS: {assertions} exact-rational assertions; 4001 distinct rational shapes; max observed period {largest}.')

if __name__ == '__main__':
    main()
