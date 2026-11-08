#!/usr/bin/env python3
"""Exact checks for the three-agent confidence exit-time theorem.

Only arithmetic/model reproducibility; the mathematical proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import product


def direct_exit_word(bits, m):
    """Return first exit index among a supplied fair-mark prefix, or None."""
    x = Fraction(1, 2)
    threshold = Fraction(1, 2 ** m)
    for k, b in enumerate(bits, start=1):
        x = (x + b) / 2
        if not (threshold < x < 1 - threshold):
            return k
    return None


def run_length_exact_mean(m):
    """Exact finite run-length state recurrence, independent of word-coding proof."""
    # Before m-1 draws the process cannot exit. Every draw extends or
    # resets the equal-symbol run. The final stage has an early absorbing
    # boundary; thereafter the standard m-run hitting clock applies.
    states = {0: Fraction(1)}
    hit = Fraction(0)
    for k in range(1, m):
        nxt = {}
        for r, p in states.items():
            if r == 0:
                possibilities = ((1, p),)
            else:
                possibilities = ((r + 1, p / 2), (1, p / 2))
            for rnew, q in possibilities:
                if k == m - 1 and rnew == m - 1:
                    hit += k * q
                else:
                    nxt[rnew] = nxt.get(rnew, Fraction(0)) + q
        states = nxt
    # A regular m-run, started with current run length r>=1, requires
    # 2**m-2**r additional draws in expectation (one-step recurrence).
    for r, p in states.items():
        hit += p * (m - 1 + (2 ** m - 2 ** r))
    return hit


def exhaustive_early_pattern(m):
    """Verify the exact prefix exit rule for all 2**m possible words."""
    for bits in product((0, 1), repeat=m):
        first = direct_exit_word(bits, m)
        early = all(b == bits[0] for b in bits[:m - 1])
        latest = all(b == bits[0] for b in bits)
        assert (first == m - 1) == early, (m, bits, first)
        if not early:
            assert (first == m) == all(b == bits[-1] for b in bits), (m, bits, first)


def main():
    for m in range(2, 21):
        got = run_length_exact_mean(m)
        want = 2 ** m - 3
        assert got == want, (m, got, want)
    for m in range(2, 9):
        exhaustive_early_pattern(m)
    # Strict equality rejection at the first possible exit.
    assert direct_exit_word([0, 0], 3) == 2
    assert direct_exit_word([1, 1], 3) == 2
    assert direct_exit_word([0], 2) == 1
    assert direct_exit_word([1], 2) == 1
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
