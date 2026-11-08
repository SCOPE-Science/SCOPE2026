"""Finite rational-pattern calibration and layered-permutation encoding checks.
Run using Python 3.10+; no third-party packages.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def perm_from_gaps(w):
    blocks = []
    run = 1
    for bit in w:
        if bit == 1:
            blocks.append(run)
            run = 1
        else:
            run += 1
    blocks.append(run)
    permutation = []
    lo = 1
    for length in blocks:
        permutation.extend(range(lo + length - 1, lo - 1, -1))
        lo += length
    return tuple(permutation)


def gaps_from_perm(a):
    return tuple(int(a[i] < a[i + 1]) for i in range(len(a) - 1))


def first_eligible_word(w, p, q):
    k = max(1, (q - 1).bit_length())
    L = k + 2
    marker = (0,) * L + (1,)
    for i in range(len(w) - (L + 1 + k) + 1):
        if w[i:i + L + 1] == marker:
            value = 0
            for b in w[i + L + 1:i + L + 1 + k]:
                value = 2 * value + b
            if value < q:
                return value < p
    return False


def finite_prob_dp(n, p, q):
    """Exact probability over n independent fair bits, via finite automaton."""
    k = max(1, (q - 1).bit_length())
    L = k + 2
    marker = (0,) * L + (1,)
    m = len(marker)
    # state = (longest suffix matching a proper prefix, bits-to-read, value)
    weights = {(0, 0, 0): 1}
    accepted = 0
    for _ in range(n):
        next_weights = defaultdict(int)
        accepted *= 2
        for (pref, left, val), weight in weights.items():
            for b in (0, 1):
                # Prefix state must be maintained even while reading a sample.
                v = marker[:pref] + (b,)
                end = v[-m:] == marker
                pref_new = max((t for t in range(m) if v[-t:] == marker[:t]), default=0)
                # Empty suffix is always the empty prefix.
                if left:
                    value_new = 2 * val + b
                    if left == 1:
                        if value_new < q:
                            if value_new < p:
                                accepted += weight
                        else:
                            next_weights[(pref_new, 0, 0)] += weight
                    else:
                        next_weights[(pref_new, left - 1, value_new)] += weight
                    assert not end, 'Two sampled markers should not overlap.'
                elif end:
                    next_weights[(pref_new, k, 0)] += weight
                else:
                    next_weights[(pref_new, 0, 0)] += weight
        weights = next_weights
    return Fraction(accepted, 2 ** n)


def tests():
    for n in range(1, 10):
        seen = set()
        for bits in product((0, 1), repeat=n - 1):
            perm = perm_from_gaps(bits)
            assert gaps_from_perm(perm) == bits
            assert perm not in seen
            seen.add(perm)
        assert len(seen) == 2 ** (n - 1)
    for p, q in ((1, 3), (2, 5), (3, 7)):
        for n in range(1, 16):
            exact_brute = sum(first_eligible_word(w, p, q) for w in product((0, 1), repeat=n))
            assert Fraction(exact_brute, 2 ** n) == finite_prob_dp(n, p, q)
        for n in (32, 64, 128, 192):
            win = finite_prob_dp(n, p, q)
            eligible = finite_prob_dp(n, q, q)
            assert q * win == p * eligible
        print(f'ratio_{p}_{q}_n192={float(finite_prob_dp(192,p,q)):.8f}')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    tests()
