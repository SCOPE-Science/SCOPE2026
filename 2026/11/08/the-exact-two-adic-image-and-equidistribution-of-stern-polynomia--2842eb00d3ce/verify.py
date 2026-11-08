#!/usr/bin/env python3
"""Independent finite checks of the Stern-polynomial value image at t=-2.

Every test is finite and is not used as a replacement for the proof.
"""
from collections import Counter


def left(v, modulus):
    a, b = v
    return (-2 * a % modulus, (a + b) % modulus)


def right(v, modulus):
    a, b = v
    return ((a + b) % modulus, -2 * b % modulus)


def image(k):
    mod = 1 << k
    seen = {(0, 1)}
    new = set(seen)
    while new:
        nxt = {left(x, mod) for x in new} | {right(x, mod) for x in new}
        new = nxt - seen
        seen.update(new)
    return seen


def check():
    total_states = 0
    total_indices = 0
    for k in range(1, 9):
        mod = 1 << k
        sub = 1 << min(3, k)
        admissible = {(a, b) for a in range(mod) for b in range(mod)
                      if (b - 5 * a - 1) % sub == 0}
        found = image(k)
        assert found == admissible, (k, 'image')
        assert len(found) == 1 << (2 * k - min(k, 3)), (k, 'cardinality')
        incoming = Counter()
        for state in found:
            incoming[left(state, mod)] += 1
            incoming[right(state, mod)] += 1
        assert all(incoming[v] == 2 for v in found), (k, 'predecessors')
        for a, b in found:
            assert (b - 5 * a - 1) % sub == 0
        total_states += len(found)
        # direct Stern recurrence from scratch for each residue modulus
        entries = [0, 1]
        for n in range(2, (1 << 15) + 1):
            if n & 1:
                entries.append((entries[n // 2] + entries[n // 2 + 1]) % mod)
            else:
                entries.append((-2 * entries[n // 2]) % mod)
        for n in range(1 << 15):
            assert (entries[n], entries[n+1]) in found, (k, n)
        total_indices += 1 << 15

    for k in range(1, 10):
        mod = 1 << k
        f0 = lambda x: (-2*x*pow(1+16*x,-1,mod)) % mod
        f1 = lambda x: ((1+6*x)*pow(-7-40*x,-1,mod)) % mod
        x0 = {f0(x) for x in range(mod)}
        x1 = {f1(x) for x in range(mod)}
        assert x0 == set(range(0, mod, 2)), ('projective even', k)
        assert x1 == set(range(1, mod, 2)), ('projective odd', k)
        for y in range(mod):
            if y % 2 == 0:
                x = (-(y//2) * pow(1+8*y,-1,mod)) % mod
                assert f0(x) == y
            else:
                numerator = -(1+7*y)//2
                x = numerator * pow(3+20*y,-1,mod) % mod
                assert f1(x) == y
    for k in range(3, 13):
        mod = 1 << k
        lam = (-5 * pow(3,-1,mod)) % mod
        observed = set()
        v = 1
        for _ in range(1 << (k - 3)):
            observed.add(v)
            v = v * lam % mod
        assert len(observed) == 1 << (k-3)
        assert v == 1
        assert observed == {x for x in range(mod) if x % 8 == 1}
    # Binary-chain statistics and convergence from the initial state
    for k in range(1, 6):
        mod = 1 << k
        ct = Counter({(0, 1): 1})
        for _ in range(45):
            nxt = Counter()
            for v, num in ct.items():
                nxt[left(v, mod)] += num
                nxt[right(v, mod)] += num
            ct = nxt
        target = (1 << 45) / len(image(k))
        relative_error = max(abs(n-target)/target for n in ct.values())
        assert relative_error < 0.01, ('dyadic limit', k, relative_error)
    print('VERIFY_OK modular_images=1..8 state_census=%d predecessor_degrees=PASS direct_stern_indices=%d projective_images=1..9 unit_generators=3..12 dyadic_mixing=PASS' % (total_states, total_indices))


if __name__ == '__main__':
    check()
