"""Exact finite checks for Pell/Pell-Lucas residue fiber-frequency theorem.
Uses complete state periods and direct counting, not probabilistic sampling.
The mathematical proof in RESULT.md establishes all exponents.
"""
from collections import Counter


def predicted_histogram(k):
    if k == 1:
        return {2: 1, 3: 2}
    h = k - 2
    square_count = 1 + sum(3 ** (h - 2*j - 1) for j in range((h + 1)//2))
    out = {2: 3**k - 2*square_count}
    for j in range((h+1)//2):
        out[2 + 6 * 3**j] = 2 * 3**(h - 2*j - 1)
    out[2 + 3**(h//2 + 1)] = 2
    return out


def actual_histogram(k, seed):
    modulus = 3**k
    target = 8 * 3**(k-1)
    a, b = seed
    state0 = seed
    counts = [0] * modulus
    for n in range(target):
        if n > 0 and (a, b) == state0:
            raise AssertionError(f'Unexpected shorter period: k={k}, n={n}')
        counts[a] += 1
        a, b = b, (2*b + a) % modulus
    assert (a, b) == state0, (seed, k, 'state period mismatch')
    assert min(counts) >= 1, (seed, k, 'not residue complete')
    return dict(Counter(counts))


def main():
    total_period_terms = 0
    for k in range(1, 12):
        expected = predicted_histogram(k)
        assert sum(expected.values()) == 3**k
        assert sum(a * b for a, b in expected.items()) == 8 * 3**(k-1)
        actuals = []
        for label, seed in [('Pell', (0, 1)), ('Pell-Lucas', (1, 1))]:
            observed = actual_histogram(k, seed)
            assert observed == expected, (label, k, observed, expected)
            actuals.append(observed)
            total_period_terms += 8 * 3**(k-1)
        assert actuals[0] == actuals[1]
        print(f'k={k}: modulus={3**k}; period={8*3**(k-1)}; distribution={sorted(expected.items())}; OK')
    print(f'PASS: two sequences, 11 exponents, {total_period_terms} complete-period terms')


if __name__ == '__main__':
    main()
