#!/usr/bin/env python3
"""Independent finite tests for a theorem on Thue-Morse prefix fair length.
Only finite testing; the proof of the all-prefix theorem is in RESULT.md.
"""

def thue_morse(n):
    return [(i.bit_count() & 1) for i in range(n)]


def fair_direct(w):
    # Direct ordered-pair comparison, independent of the cumulative recurrence.
    zero_one = sum(w[i] == 0 and w[j] == 1
                   for i in range(len(w)) for j in range(i + 1, len(w)))
    one_zero = sum(w[i] == 1 and w[j] == 0
                   for i in range(len(w)) for j in range(i + 1, len(w)))
    return zero_one == one_zero


def min_fair_factorization_all_prefixes(w):
    n = len(w)
    # An independent dynamic program on every contiguous suffix.
    dp = [n + 1] * (n + 1)
    dp[0] = 0
    for i in range(n):
        zero = one = zero_one = 0
        for j in range(i, n):
            if w[j] == 0:
                zero += 1
            else:
                zero_one += zero
                one += 1
            if 2 * zero_one == zero * one:
                dp[j+1] = min(dp[j+1], dp[i] + 1)
    return dp


def predicted(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    k, r = divmod(n, 4)
    if r == 0:
        return 1
    if r == 1:
        return 2
    if r == 2:
        return 3
    return 2 if (k.bit_count() & 1) == 0 else 3


def run():
    n = 2048
    word = thue_morse(n)
    dp = min_fair_factorization_all_prefixes(word)
    for j in range(n + 1):
        assert dp[j] == predicted(j), (j, dp[j], predicted(j))
    # A second genuinely direct fairness computation checks the recurrence,
    # rather than silently assuming it in both independent tests.
    for start in range(48):
        for end in range(start+1, min(start+32, 96)+1):
            fragment = word[start:end]
            zeros = ones = z_o = 0
            for bit in fragment:
                if bit == 0:
                    zeros += 1
                else:
                    z_o += zeros
                    ones += 1
            assert (2*z_o == zeros*ones) == fair_direct(fragment)
    # Check exact imbalance and ordered-pair difference at all prefixes.
    z = o = ab = 0
    for j, bit in enumerate(word, 1):
        if bit == 0:
            z += 1
        else:
            ab += z
            o += 1
        diff = 2*ab-z*o
        k, r = divmod(j, 4)
        if r == 0:
            expected = 0
        elif r == 1:
            expected = -2*k*(1 if (k.bit_count() & 1) == 0 else -1)
        elif r == 2:
            expected = 1 if (k.bit_count() & 1) == 0 else -1
        else:
            expected = 2*(k+1)*(1 if (k.bit_count() & 1) == 0 else -1)
        assert diff == expected, (j,diff,expected)
    print('TM_FAIR_PREFIX_VERIFY_OK', n, 'independent_dynamic_program', 'pair_count_crosscheck')


if __name__ == '__main__':
    run()
