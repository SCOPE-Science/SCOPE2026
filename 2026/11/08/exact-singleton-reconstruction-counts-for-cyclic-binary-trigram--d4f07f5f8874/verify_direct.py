"""Direct reconstruction-profile census for binary cyclic words.

Run: python3 verify_direct.py
The cyclic triple at index i uses positions i, i+1, i+2 modulo n,
including lengths n=1 and n=2. No theorem-specific run assumptions.
"""
from collections import defaultdict

EXPECTED = [2,3,4,6,8,12,16,19,22,24,28,29,34,34,38,41,44,44]

def canonical_rotation(w):
    return min(w[i:] + w[:i] for i in range(len(w)))

def profile(w):
    n = len(w)
    p = [0] * 8
    for i in range(n):
        j = (w[i] << 2) | (w[(i+1)%n] << 1) | w[(i+2)%n]
        p[j] += 1
    return tuple(p)

def count_singleton_profiles(n):
    fibers = defaultdict(set)
    for x in range(1 << n):
        w = tuple((x >> i) & 1 for i in range(n))
        fibers[profile(w)].add(canonical_rotation(w))
    return sum(len(classes) == 1 for classes in fibers.values())

if __name__ == '__main__':
    for n in range(1, 19):
        observed = count_singleton_profiles(n)
        assert observed == EXPECTED[n-1], (n, observed, EXPECTED[n-1])
        print(n, observed)
    print('DIRECT_OK')
