#!/usr/bin/env python3
"""Exact integer tests for the Dyck up-step parity and Walsh congruence theorem.

Run: python verify_dyck_fourier.py
No external packages are required. All frequencies are exhaustively tested only
for the explicitly stated small semilengths; the all-length proof is algebraic.
"""
from math import comb


def bit_sum(z):
    return z.bit_count()


def predicted_parity(n):
    q = n + 1
    out = [0] * (2 * n)
    if bit_sum(q) == 1:
        for i in range(n):
            out[i] = 1
    elif bit_sum(q) == 2:
        b = (q & -q).bit_length() - 1
        a = (q ^ (1 << b)).bit_length() - 1
        for i in range((1 << (b + 1)) - 1, (1 << (a + 1)) - 1):
            out[i] = 1
    return out


def marginals_dp(n):
    # Counts of paths with an up-step at every separately selected position.
    out = []
    for selected in range(2 * n):
        layer = {0: 1}
        for pos in range(2 * n):
            nxt = {}
            for h, amount in layer.items():
                if h + 1 <= 2 * n - pos - 1:  # enough steps remain to return
                    nxt[h + 1] = nxt.get(h + 1, 0) + amount
                if h > 0 and pos != selected:
                    nxt[h - 1] = nxt.get(h - 1, 0) + amount
            layer = nxt
        out.append(layer.get(0, 0))
    return out


def enumerate_dyck(n):
    paths = []
    def rec(pos, height, ups, mask):
        if pos == 2 * n:
            if height == 0:
                paths.append(mask)
            return
        if ups < n:
            rec(pos + 1, height + 1, ups + 1, mask | (1 << pos))
        if height > 0:
            rec(pos + 1, height - 1, ups, mask)
    rec(0, 0, 0, 0)
    return paths


def fwht(values):
    length = len(values)
    step = 1
    while step < length:
        for start in range(0, length, 2 * step):
            for k in range(step):
                a = values[start + k]
                b = values[start + k + step]
                values[start + k] = a + b
                values[start + k + step] = a - b
        step *= 2


def check_small_spectrum(n):
    path_masks = enumerate_dyck(n)
    total = comb(2 * n, n) // (n + 1)
    assert len(path_masks) == total
    counts = [sum(bool(mask & (1 << i)) for mask in path_masks)
              for i in range(2 * n)]
    assert [v & 1 for v in counts] == predicted_parity(n)
    direct = [0] * (1 << (2 * n))
    for mask in path_masks:
        direct[mask] = 1
    fwht(direct)
    interval = [i for i, value in enumerate(predicted_parity(n)) if value]
    for b, w in enumerate(direct):
        # Independently computed from the one-step marginal formula.
        congruence = (total - 2 * sum((b >> i) & 1 for i in interval)) % 4
        assert w % 4 == congruence, (n, b, w, congruence)
        if bit_sum(n + 1) == 1:
            assert w % 2 == 1
        elif bit_sum(n + 1) >= 3:
            assert w % 4 == 0
    return len(direct)


def main():
    # Exact dynamic programming is separate from the first-return generating
    # function proof; this checks every coordinate through semilength 100.
    for n in range(1, 101):
        actual = marginals_dp(n)
        assert [v & 1 for v in actual] == predicted_parity(n), n
    checked = sum(check_small_spectrum(n) for n in range(1, 11))
    for n in (6, 10, 12, 13, 14, 22, 30):
        total = comb(2 * n, n) // (n + 1)
        s = bit_sum(n + 1)
        assert ((total & -total).bit_length() - 1) == s - 1
        assert (all(c % 2 == 0 for c in marginals_dp(n))) == (s >= 3)
    print('DYCK_POSITION_PARITY_AND_MOD4_PASS', 'all_positions_n_le_100',
          'exhaustive_fourier_coefficients', checked)


if __name__ == '__main__':
    main()
