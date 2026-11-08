"""Independent occupancy-class enumeration for synchronous majority on balanced complete multipartite graphs.

Run: python verify_balanced_multipartite_counts.py
Only the Python standard library is needed.
"""
from itertools import product
from math import comb


def closed_form(r, n):
    assert r >= 4 and n >= 1
    mid = comb(n, n // 2) if n % 2 == 0 else 0
    fixed = 2 + (mid ** r if n % 2 == 0 else 0)
    period_two = (comb(r, r // 2) if r % 2 == 0
                  else r * comb(r - 1, (r - 1) // 2) * (2 ** n - 2))
    if n % 2 == 0:
        for t in range(2, r - 1, 2):
            period_two += comb(r, t) * comb(t, t // 2) * mid ** (r - t)
    return fixed, period_two


def occupancy_census(r, n):
    """Enumerate all part occupancy profiles, weighted by labelled assignments."""
    threshold_twice = (r - 1) * n

    def step(occupancies):
        total = sum(occupancies)
        out = []
        for count in occupancies:
            count_twice = 2 * (total - count)
            out.append(n if count_twice > threshold_twice else
                       0 if count_twice < threshold_twice else count)
        return tuple(out)

    fixed = two = 0
    for profile in product(range(n + 1), repeat=r):
        first = step(profile)
        labelled_weight = 1
        for count in profile:
            labelled_weight *= comb(n, count)
        if first == profile:
            fixed += labelled_weight
        elif step(first) == profile:
            two += labelled_weight
    return fixed, two


def main():
    checks = 0
    for r in range(4, 9):
        for n in range(1, 5):
            if (n + 1) ** r > 300000:
                continue
            counted = occupancy_census(r, n)
            expected = closed_form(r, n)
            assert counted == expected, (r, n, counted, expected)
            checks += 1
            print(f'r={r}, n={n}: fixed={counted[0]}, primitive_two={counted[1]}')
    print(f'PASS: {checks} exhaustive occupancy-profile parameter cases')


if __name__ == '__main__':
    main()
