"""Finite independent checks for an avalanche-complex arithmetic theorem.

Requires Python 3 standard library. Run: python3 verify.py
"""
from collections import defaultdict
from math import gcd, lcm


def simulate(a, b):
    n = a + b
    cfg = [1] * n
    cfg[0] = 0
    cfg[a] = 0
    starting = tuple(cfg)
    fired = []
    while True:
        mask = sum((1 << i) for i, c in enumerate(cfg) if c >= 1)
        fired.append(mask)
        next_cfg = cfg.copy()
        for offset, length in ((0, a), (a, b)):
            for i in range(length):
                at = offset + i
                if mask & (1 << at):
                    next_cfg[at] -= 1
                    next_cfg[offset + (i + 1) % length] += 1
        cfg = next_cfg
        if tuple(cfg) == starting:
            break
        assert len(fired) <= a * b + 1, (a, b)
    assert len(fired) == lcm(a, b), (a, b, len(fired))
    assert len(set(fired)) == lcm(a, b)
    expected = set()
    d = gcd(a, b)
    for x in range(a):
        for y in range(b):
            if x % d == y % d:
                expected.add(((1 << n) - 1) ^ (1 << x) ^ (1 << (a + y)))
    assert set(fired) == expected, (a, b)
    return fired


def mod2_ranks_and_betti(a, b, generators):
    faces = {0}
    for face in generators:
        s = face
        while True:
            faces.add(s)
            if s == 0:
                break
            s = (s - 1) & face
    layers = defaultdict(list)
    for f in faces:
        layers[f.bit_count() - 1].append(f)
    ranks = {}
    for k in sorted(layers):
        if k < 1:
            continue
        pivot = {}
        ids = {f: i for i, f in enumerate(layers[k - 1])}
        for f in layers[k]:
            c = 0
            t = f
            while t:
                low = t & -t
                c ^= 1 << ids[f ^ low]
                t ^= low
            while c:
                hi = c.bit_length() - 1
                if hi in pivot:
                    c ^= pivot[hi]
                else:
                    pivot[hi] = c
                    break
        ranks[k] = len(pivot)
    betti = {}
    for k, faces_k in layers.items():
        if k < 0:
            continue
        r_current = 1 if k == 0 and faces_k else ranks.get(k, 0)
        r_next = ranks.get(k + 1, 0)
        beta = len(faces_k) - r_current - r_next
        assert beta >= 0, (a, b, k, beta)
        if beta:
            betti[k] = beta
    assert betti == {a + b - gcd(a, b) - 2: 1}, (a, b, betti)
    return len(faces), betti


def main():
    cases = 0
    tested_chains = 0
    max_faces = 0
    # Includes coprime, equal, proper-divisor, and nontrivial-gcd examples.
    for a in range(3, 9):
        for b in range(3, 9):
            generators = simulate(a, b)
            cases += 1
            if a + b <= 12:
                count, betti = mod2_ranks_and_betti(a, b, generators)
                tested_chains += 1
                max_faces = max(max_faces, count)
                print('HOMOLOGY', a, b, 'gcd', gcd(a, b), 'faces', count, 'betti', betti)
    assert cases == 36
    assert tested_chains > 10
    print('CHECKED_SIMULATIONS', cases)
    print('CHECKED_COMPLETE_GF2_CHAINS', tested_chains)
    print('MAXIMUM_ENUMERATED_FACES', max_faces)
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
