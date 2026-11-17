"""Exact finite certificate for the Euclidean width theorem on complete split graph associahedra.

No third-party dependencies. Execute with Python 3: python verify.py
"""
from itertools import combinations


def tube_crossings(c, m, a, b):
    """Closed-form count of connected non-singleton sets crossing the partition."""
    B = (2 ** c - 1) * 2 ** m
    return B - (2 ** a - 1) * 2 ** b - (2 ** (c-a) - 1) * 2 ** (m-b)


def reference_width_squared_data(c, m):
    """Return (numerator, denominator) of width squared divided by n."""
    n = c + m
    B = (2 ** c - 1) * 2 ** m
    if n <= 14:
        return (B // 2) ** 2, n - 1
    h = n // 2
    q = m // 2
    central = B - 2 ** h - 2 ** (n-h) + 2 ** q + 2 ** (m-q)
    return central ** 2, h * (n-h)


def is_expected_contact(c, m, a, b):
    n = c + m
    k = a + b
    if n <= 14:
        return (a == 0 and b == 1) or (a == c and b == m-1)
    h = n // 2
    return k in (h, n-h) and b in (m // 2, (m + 1) // 2)


def finite_certificate():
    profiles = 0
    cuts = 0
    ties = 0
    for n in range(4, 64):
        for c in range(2, n-1):
            m = n-c
            base_num, base_den = reference_width_squared_data(c, m)
            found = False
            for a in range(c+1):
                for b in range(m+1):
                    k = a+b
                    if k in (0, n):
                        continue
                    crossing = tube_crossings(c, m, a, b)
                    diff = crossing * crossing * base_den - base_num * k * (n-k)
                    assert diff >= 0, (n, c, m, a, b, 'under candidate')
                    is_tie = (diff == 0)
                    assert is_tie == is_expected_contact(c, m, a, b), (n,c,m,a,b,'tie mismatch')
                    if is_tie:
                        ties += 1
                        found = True
                    cuts += 1
            assert found
            profiles += 1
    return profiles, cuts, ties


def direct_tube_check():
    """Independent subset-based check of the graph-tube counting identity."""
    tests = 0
    for n in range(4, 10):
        for c in range(2, n-1):
            m = n-c
            connected = []
            for mask in range(1, 1 << n):
                clique_hit = bool(mask & ((1 << c)-1))
                single_leaf = not clique_hit and mask.bit_count()==1
                if clique_hit or single_leaf:
                    connected.append(mask)
            for a in range(c+1):
                for b in range(m+1):
                    k=a+b
                    if k in (0,n): continue
                    A=sum(1 << j for j in range(a)) + sum(1 << (c+j) for j in range(b))
                    direct=sum(bool(t&A) and bool(t&(((1<<n)-1)^A)) for t in connected)
                    assert direct==tube_crossings(c,m,a,b), (n,c,m,a,b,direct)
                    tests+=1
    return tests


if __name__ == '__main__':
    p, c, t = finite_certificate()
    d = direct_tube_check()
    print(f'SPLIT_GRAPH_WIDTH_PASS profiles={p} exact_cuts={c} min_cuts={t} direct_tube_tests={d} threshold_n=15')
