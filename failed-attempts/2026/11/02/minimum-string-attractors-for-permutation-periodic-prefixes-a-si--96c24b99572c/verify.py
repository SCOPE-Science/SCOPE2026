#!/usr/bin/env python3
"""Independent finite check of the periodic-permutation-prefix attractor theorem.
No nonstandard dependencies. Run with: python verify.py
"""
from itertools import product


def word(q, m, r):
    return tuple(range(q)) * m + tuple(range(r))


def brute_attractor(w, chosen):
    # Compare literal substring values: no appeal to the periodicity proof.
    n = len(w)
    hit = {}
    selected = set(chosen)
    for i in range(n):
        for j in range(i + 1, n + 1):
            u = w[i:j]
            if u not in hit:
                hit[u] = False
            if not hit[u] and any(i <= p < j for p in selected):
                hit[u] = True
    return all(hit.values())


def predicted_bad(q, m, r, chosen):
    if m == 1 or r == q - 1:
        return False
    return (
        chosen[r] == r
        and chosen[q - 1] == m * q - 1
        and all(chosen[j] in (j, m * q + j) for j in range(r))
    )


def expected_good(q, m, r):
    total = (m + 1) ** r * m ** (q - r)
    return total if m == 1 or r == q - 1 else total - 2**r * m ** (q - r - 2)


def main():
    cases = profiles = candidates = bad = 0
    # Independent enumeration of every minimum-size candidate in this range.
    for q in range(2, 7):
        mmax = 5 if q <= 5 else 3
        for m in range(1, mmax + 1):
            for r in range(q):
                w = word(q, m, r)
                opts = [tuple(i for i, x in enumerate(w) if x == a)
                        for a in range(q)]
                successes = misses = 0
                for chosen in product(*opts):
                    actual = brute_attractor(w, chosen)
                    prediction = not predicted_bad(q, m, r, chosen)
                    assert actual == prediction, (q, m, r, chosen, actual)
                    successes += actual
                    misses += (not actual)
                    candidates += 1
                assert successes == expected_good(q, m, r), (q, m, r, successes)
                if m >= 2 and r <= q - 2:
                    # The unique purported obstruction word is literally unhit
                    # by every structurally exceptional selection.
                    u = (q - 1,) + tuple(range(r + 1))
                    starts = [i for i in range(len(w) - len(u) + 1)
                              if w[i:i + len(u)] == u]
                    assert starts == [(t + 1) * q - 1 for t in range(m - 1)]
                bad += misses
                cases += 1
                profiles += successes
    print('VERIFY_OK parameter_cases=%d candidate_sets=%d valid_sets=%d invalid_sets=%d '
          'alphabet_sizes=2..6 complete_factors=True' %
          (cases, candidates, profiles, bad))


if __name__ == '__main__':
    main()
