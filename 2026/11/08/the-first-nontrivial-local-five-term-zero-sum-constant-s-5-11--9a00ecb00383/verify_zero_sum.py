#!/usr/bin/env python3
"""Exact finite certificate for the five-term local zero-sum constant modulo 25."""
from itertools import combinations

P = 5


def compositions(total):
    for a in range(total + 1):
        for b in range(total - a + 1):
            for c in range(total - a - b + 1):
                yield (a, b, c, total - a - b - c)


def rank_test(counts):
    residues = tuple(r for r, count in enumerate(counts, 1) for _ in range(count))
    size = len(residues)
    basis = {}
    equations_seen = 0
    for selected in combinations(range(size), P):
        s = sum(residues[i] for i in selected)
        if s % P:
            continue
        equations_seen += 1
        equation = [0] * (size + 1)
        for i in selected:
            equation[i] = 1
        equation[-1] = (-s // P) % P
        while True:
            col = next((j for j in range(size) if equation[j] != 0), None)
            if col is None:
                if equation[-1]:
                    return False, len(basis), equations_seen
                break
            if col not in basis:
                factor = pow(equation[col], -1, P)
                basis[col] = [(factor * t) % P for t in equation]
                break
            factor = equation[col]
            equation = [(u - factor * v) % P
                        for u, v in zip(equation, basis[col])]
    return True, len(basis), equations_seen


def main():
    bad_ten = {}
    for c in compositions(10):
        solvable, rank, _ = rank_test(c)
        if solvable:
            bad_ten[c] = rank
    expected = {
        (0, 0, 5, 5): 2, (0, 5, 0, 5): 2, (0, 5, 5, 0): 2,
        (5, 0, 0, 5): 2, (5, 0, 5, 0): 2, (5, 5, 0, 0): 2,
        (0, 4, 2, 4): 8, (2, 0, 4, 4): 8,
        (4, 2, 4, 0): 8, (4, 4, 0, 2): 8,
        (1, 4, 4, 1): 8, (4, 1, 1, 4): 8,
    }
    assert bad_ten == expected, ('profile classification mismatch', bad_ten)
    print('TEN_PROFILES_EXHAUSTED 286 SOLVABLE 12 RANK2 6 RANK8 6')
    print('TEN_PROFILES', sorted(bad_ten))

    admissible_deletion_profiles = []
    direct_consistent = []
    processed = 0
    for c in compositions(11):
        if all(tuple(c[j] - (j == i) for j in range(4)) in bad_ten
               for i in range(4) if c[i]):
            admissible_deletion_profiles.append(c)
        consistent, _, eqs = rank_test(c)
        processed += eqs
        if consistent:
            direct_consistent.append(c)
    assert not admissible_deletion_profiles
    assert not direct_consistent
    print('ELEVEN_PROFILES_EXHAUSTED 364 DIRECT_CONSISTENT 0 DELETION_CONSISTENT 0')
    print('DIRECT_GAUSS_EQUATIONS_PROCESSED', processed)

    example = [1] * 4 + [21] + [2] * 4 + [17]
    assert len(example) == 10 and all(x % 5 for x in example)
    zero_mod_five = [sum(example[i] for i in selected)
                     for selected in combinations(range(10), 5)
                     if sum(example[i] for i in selected) % 5 == 0]
    assert zero_mod_five and set(x % 25 for x in zero_mod_five) == {0}
    assert len(zero_mod_five) == 2
    print('TEN_TERM_SHARPNESS_OK 2_ONLY_ZERO_MOD_25_FIVE_SUMS')
    print('VERIFY_OK exact_exhaustion=True independent_audit=False')


if __name__ == '__main__':
    main()
