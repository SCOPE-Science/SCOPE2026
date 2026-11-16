"""Exact hyperoctahedral/conjugation orbit verification for 4-cube optimal phases.
Inputs are checker-generated normalized lists: one 16-digit exponent word per line.
"""
from itertools import permutations
from pathlib import Path

def normalized_orbit(a, q):
    orbit = set()
    for pi in permutations(range(4)):
        permuted = [sum(((x >> j) & 1) << pi[j] for j in range(4)) for x in range(16)]
        for mask in range(16):
            b = [a[permuted[x] ^ mask] for x in range(16)]
            c = b[0]
            slopes = [(b[1 << j] - c) % q for j in range(4)]
            for sgn in (1, -1):
                orbit.add(tuple((sgn * (b[x] - c - sum(slopes[j] * ((x >> j) & 1) for j in range(4)))) % q for x in range(16)))
    return orbit

def check(q, filename):
    path = Path(filename)
    words = [line.strip() for line in path.read_text().splitlines() if len(line.strip()) == 16]
    S = {tuple(map(int,w)) for w in words}
    assert len(S) == len(words)
    assert all(max(a) < q and all(a[x]==0 for x in (0,1,2,4,8)) for a in S)
    remaining = set(S)
    sizes = []
    reps = []
    while remaining:
        a = min(remaining)
        orbit = normalized_orbit(a,q)
        assert orbit <= S, 'Optimizer set must be invariant under cube symmetries'
        reps.append(''.join(map(str,a)))
        sizes.append(len(orbit))
        remaining -= orbit
    assert sorted(sizes) == ([48,192] if q==3 else [12,12])
    assert len(S) == (240 if q==3 else 24)
    print(f'ORBIT_CHECK_PASS q={q} sizes={sizes} representatives={reps}')

if __name__ == '__main__':
    import sys
    if len(sys.argv)!=3: raise SystemExit('Usage: python orbit_checker.py q optimizer_list.txt')
    check(int(sys.argv[1]),sys.argv[2])
