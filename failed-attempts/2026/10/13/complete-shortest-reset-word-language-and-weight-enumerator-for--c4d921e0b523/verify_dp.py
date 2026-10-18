"""Exact subset-image counting and position-containment checks for Wielandt DFAs."""
from collections import defaultdict
from math import comb


def transitions(n):
    a = tuple(i + 1 if i < n - 1 else 1 for i in range(n))
    b = tuple(i + 1 if i < n - 1 else 0 for i in range(n))
    return a, b


def image(mask, tr):
    out = 0
    for i, q in enumerate(tr):
        if mask & (1 << i):
            out |= 1 << q
    return out


def test(n):
    a, b = transitions(n)
    L = n * n - 3 * n + 3
    fixed_a = {j * (n - 1) for j in range(n - 1)}
    fixed_b = {1 + j * n for j in range(max(n - 2, 0))}
    assert len(fixed_a | fixed_b) == len(fixed_a) + len(fixed_b)
    assert max(fixed_a) < L
    if fixed_b:
        assert max(fixed_b) < L

    all_state_mask = (1 << n) - 1
    permitted = {0, 1} if n > 2 else {0}
    for t in range(L):
        if t == 0:
            before = all_state_mask
        else:
            j, r = divmod(t - 1, n - 1)
            before = sum(1 << (v % n) for v in range(r + 1, r + n - j))
        if t + 1 == L:
            after = 1 << 1
        else:
            j, r = divmod(t, n - 1)
            after = sum(1 << (v % n) for v in range(r + 1, r + n - j))
        for letter, tr in ((1, a), (0, b)):
            if t in fixed_a and letter != 1:
                continue
            if t in fixed_b and letter != 0:
                continue
            assert image(before, tr) & ~after == 0, (n, t, letter)

    if n <= 12:
        table = [tuple(image(mask, tr) for mask in range(1 << n))
                 for tr in (a, b)]
        counts = {(all_state_mask, 0): 1}
        previous = 0
        for depth in range(1, L + 1):
            new = defaultdict(int)
            for (mask, k), value in counts.items():
                new[(table[0][mask], k + 1)] += value
                new[(table[1][mask], k)] += value
            counts = new
            if depth == L - 1:
                previous = sum(value for (mask, _), value in counts.items()
                               if mask.bit_count() == 1)
        assert previous == 0 if L > 1 else True
        observed = defaultdict(int)
        for (mask, k), value in counts.items():
            if mask.bit_count() == 1:
                observed[k] += value
        q = (n - 2) * (n - 3)
        expected = {n - 1 + k: comb(q, k) for k in range(q + 1)}
        assert dict(observed) == expected, (n, dict(observed), expected)
        print(f"n={n}: L={L}, shortest={sum(observed.values())}, weights={len(observed)} OK")


for n in range(2, 41):
    test(n)
print('VERIFY_OK: subset dynamic program, weight enumerator, and interval inclusions')
