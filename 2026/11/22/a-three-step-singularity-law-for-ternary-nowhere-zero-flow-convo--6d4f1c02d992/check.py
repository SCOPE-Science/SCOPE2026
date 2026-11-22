"""Independent integer character enumeration for ternary nowhere-zero dipole flows.

Run with python3 check.py; all work uses the Python standard library.
"""
from itertools import product
from math import factorial


def expected_multiplier(counts, n):
    return ((-1) ** n) * sum((-2) ** t for t in counts) // 3


def expected_nullity(n):
    if n % 3 != 1:
        return 0
    m = (n - 1) // 3
    return 3 * factorial(n) // (factorial(m) ** 2 * factorial(m + 1))


def flow_count(n):
    return (2**n + 2 * (-1)**n) // 3


def check(n):
    flows = [x for x in product((1, 2), repeat=n) if sum(x) % 3 == 0]
    assert len(flows) == flow_count(n), (n, len(flows))
    zeros = 0
    checks = 0
    for xi in product(range(3), repeat=n):
        phases = [0, 0, 0]
        for x in flows:
            phases[sum(a * b for a, b in zip(x, xi)) % 3] += 1
        assert phases[1] == phases[2], (n, xi, phases)
        empirical = phases[0] - phases[1]
        counts = tuple(xi.count(j) for j in range(3))
        predicted = expected_multiplier(counts, n)
        assert empirical == predicted, (n, xi, empirical, predicted)
        if predicted == 0:
            zeros += 1
            assert sorted(counts) == [(n-1)//3, (n-1)//3, (n-1)//3+1]
        checks += 1
    assert zeros == expected_nullity(n), (n, zeros, expected_nullity(n))
    return len(flows), zeros, checks


def main():
    total = 0
    for n in range(2, 10):
        flow, nullity, checked = check(n)
        total += checked
        print('n=%d flows=%d nullity=%d rank=%d frequencies=%d' % (
            n, flow, nullity, 3**n-nullity, checked))
    print('VERIFY_OK direct_character_frequencies=%d lengths=2..9' % total)


if __name__ == '__main__':
    main()
