"""Independent exact checks for the complete-bipartite mixed-action equilibrium count.

Run with Python 3.9 or later. Standard library only.
"""
from fractions import Fraction
from itertools import product
from math import comb


def central(t):
    return comb(t, t // 2) if t % 2 == 0 else 0


def claimed_count(a, b, ca, cb):
    da, db = 2 * ca - a, 2 * cb - b
    qa, qb = central(a), central(b)
    return (qa * qb + 2 * (da * db > 0)
            + (2 ** a - qa) * (db == 0)
            + (2 ** b - qb) * (da == 0))


def payoffs(a, b, ca, cb, actions, vertex):
    n = a + b
    is_coordinator = (vertex < ca) if vertex < a else (a <= vertex < a + cb)
    neighborhood = range(a, n) if vertex < a else range(0, a)
    outcomes = []
    for own_action in (0, 1):
        # Twice the original r=1/2 payoff, an equivalent normalization.
        agreements = sum(own_action == actions[j] for j in neighborhood)
        outcomes.append(agreements if is_coordinator else -agreements)
    return outcomes


def is_equilibrium(a, b, ca, cb, actions):
    for i in range(a + b):
        payoff = payoffs(a, b, ca, cb, actions, i)
        if payoff[actions[i]] < max(payoff):
            return False
    return True


def brute_count(a, b, ca, cb):
    return sum(is_equilibrium(a, b, ca, cb, x)
               for x in product((0, 1), repeat=a + b))


def exact_role_probability(a, b):
    total_assignments = 2 ** (a + b)
    successful = 0
    for ca in range(a + 1):
        for cb in range(b + 1):
            if claimed_count(a, b, ca, cb) > 0:
                successful += comb(a, ca) * comb(b, cb)
    return Fraction(successful, total_assignments)


def predicted_probability(a, b):
    if not a % 2 and not b % 2:
        return Fraction(1)
    if a % 2 and b % 2:
        return Fraction(1, 2)
    even = a if a % 2 == 0 else b
    return Fraction(1, 2) + Fraction(central(even), 2 ** (even + 1))


def main():
    cases = profiles = extremaal = probability_cases = 0
    for a in range(1, 6):
        for b in range(1, 6):
            values = []
            for ca in range(a + 1):
                for cb in range(b + 1):
                    actual = brute_count(a, b, ca, cb)
                    prediction = claimed_count(a, b, ca, cb)
                    assert actual == prediction, (a, b, ca, cb, actual, prediction)
                    cases += 1
                    profiles += 2 ** (a + b)
                    values.append(actual)
            expected_min = central(a) * central(b) if a % 2 == 0 and b % 2 == 0 else 0
            assert min(values) == expected_min
            if a % 2 == 0 and b % 2 == 0:
                expected_max = central(a) * central(b) + 2 ** a - central(a) + 2 ** b - central(b)
                assert max(values) == expected_max
            extremaal += 1
            assert exact_role_probability(a, b) == predicted_probability(a, b)
            probability_cases += 1
    print(f"PASS: {cases} exact role-composition enumerations")
    print(f"PASS: {profiles} independently evaluated binary action profiles")
    print(f"PASS: {extremaal} all-role existence/minimum and even-even maximum checks")
    print(f"PASS: {probability_cases} exact independent-role probability checks")
    print("Finite checks corroborate but do not establish the all-order theorem.")


if __name__ == "__main__":
    main()
