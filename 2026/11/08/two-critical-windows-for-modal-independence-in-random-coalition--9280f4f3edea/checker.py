"""Finite verification of two-agent, two-outcome coalition independence.

Run: python checker.py
Each matrix entry is 0 (unavailable), 1 (outcome u), or 2 (outcome v).
The proof of asymptotic limits is analytical and is not delegated to this file.
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import comb

SETS = (frozenset(), frozenset((1,)), frozenset((2,)), frozenset((1, 2)))


def can_enforce(mat, m, coalition, goal):
    if coalition == 0:
        values = [x for x in mat if x]
        return bool(values) and all(x in goal for x in values)
    if coalition == 1:
        return any(
            any(mat[m*i+j] for j in range(m))
            and all(mat[m*i+j] in goal for j in range(m) if mat[m*i+j])
            for i in range(m)
        )
    if coalition == 2:
        return any(
            any(mat[m*i+j] for i in range(m))
            and all(mat[m*i+j] in goal for i in range(m) if mat[m*i+j])
            for j in range(m)
        )
    if coalition == 3:
        return any(x in goal for x in mat if x)
    raise ValueError(coalition)


def modal_ia_direct(mat, m):
    # Every disjoint pair of coalitions for the two-agent language.
    for a, b in ((0, 0), (0, 1), (1, 0), (0, 2), (2, 0),
                 (0, 3), (3, 0), (1, 2), (2, 1)):
        for x, y in product(SETS, repeat=2):
            if (can_enforce(mat, m, a, x) and can_enforce(mat, m, b, y)
                    and not can_enforce(mat, m, a | b, x & y)):
                return False
    return True


def pure(mat, m, outcome, rows):
    for i in range(m):
        entries = ([mat[m*i+j] for j in range(m)] if rows else
                   [mat[m*j+i] for j in range(m)])
        if outcome in entries and all(x in (0, outcome) for x in entries):
            return True
    return False


def modal_ia_profile(mat, m):
    ru, rv = pure(mat, m, 1, True), pure(mat, m, 2, True)
    cu, cv = pure(mat, m, 1, False), pure(mat, m, 2, False)
    return not ((ru and cv) or (rv and cu))


def action_ia(mat, m):
    occupied_rows = [i for i in range(m)
                     if any(mat[m*i+j] for j in range(m))]
    occupied_cols = [j for j in range(m)
                     if any(mat[m*i+j] for i in range(m))]
    return all(mat[m*i+j] for i in occupied_rows for j in occupied_cols)


def action_probability_formula(m, p):
    z = (1-p)**(m*m)
    for r in range(1, m+1):
        for s in range(1, m+1):
            z += comb(m, r)*comb(m, s)*p**(r*s)*(1-p)**(m*m-r*s)
    return z


def check():
    expected = {1: (3, 3), 2: (61, 41), 3: (11115, 1179)}
    for m in (1, 2, 3):
        totals = Counter()
        exact_action_probability = Fraction(0)
        p = Fraction(2, 5)
        for mat in product((0, 1, 2), repeat=m*m):
            direct = modal_ia_direct(mat, m)
            profile = modal_ia_profile(mat, m)
            structural = action_ia(mat, m)
            assert direct == profile, ('characterization', m, mat)
            assert not structural or direct, ('structural=>modal', m, mat)
            totals[(direct, structural)] += 1
            if structural:
                k = sum(bool(x) for x in mat)
                exact_action_probability += (p/2)**k*(1-p)**(m*m-k)
        assert sum(totals.values()) == 3**(m*m)
        assert (sum(v for (a, b), v in totals.items() if a),
                sum(v for (a, b), v in totals.items() if b)) == expected[m]
        assert exact_action_probability == action_probability_formula(m, p)
        print(f'm={m}: tested={3**(m*m)}, modal_valid={expected[m][0]}, '
              f'action_independent={expected[m][1]}')
    print('COALITION_IA_FINITE_CHECKS_OK')


if __name__ == '__main__':
    check()
