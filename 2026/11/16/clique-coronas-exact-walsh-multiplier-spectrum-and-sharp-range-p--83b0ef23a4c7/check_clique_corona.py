"""Exact finite checks for clique-corona independent-set Walsh spectra.

No external packages are needed.  Execute: python check_clique_corona.py
"""
from fractions import Fraction
from math import comb


def fwht(a):
    a = list(a)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return a


def graph(h, b):
    n = h * (b + 1)
    adj = [0] * n
    for i in range(h):
        for j in range(i):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
        for t in range(b):
            v = h + i * b + t
            adj[i] |= 1 << v
            adj[v] |= 1 << i
    return adj


def independent_indicator(adj):
    n = len(adj)
    good = bytearray(1 << n)
    good[0] = 1
    for s in range(1, 1 << n):
        kbit = s & -s
        i = kbit.bit_length() - 1
        good[s] = good[s ^ kbit] and not (adj[i] & (s ^ kbit))
    return good


def predicted_spectrum(h, b):
    q = 1 << b
    ans = {}
    def bump(v, k):
        ans[v] = ans.get(v, 0) + k
    bump(0, (1 << h) * (q**h - 1 - h * (q - 1)))
    bump(q ** (h - 1), (1 << (h-1)) * h * (q - 1))
    bump(-(q ** (h - 1)), (1 << (h-1)) * h * (q - 1))
    for j in range(h + 1):
        bump(q ** (h - 1) * (q + h - 2 * j), comb(h, j))
    return {v: c for v, c in ans.items() if c}


def krawtchouk(h, j, t):
    return sum((-1) ** a * comb(t, a) * comb(h-t, j-a)
               for a in range(max(0, j-(h-t)), min(j, t) + 1))


def predicted_projection_norm(h, b):
    q = 1 << b
    if (h % 2) or q > h:
        return Fraction(sum(comb(h,z)*(q-1)**(h-z)*abs(q*z+1-h) for z in range(h+1)), q**h)
    j = (h+q) // 2
    removed = Fraction(comb(h, j), 1 << h)
    at_center_zero = sum(comb(h, z) * (q-1)**(h-z) * abs(Fraction(q*z+1-h)-removed)
                         for z in range(h+1)) / q**h
    at_center_nonzero = sum(comb(h,t)*abs(krawtchouk(h,j,t)) for t in range(1,h+1))
    at_center_nonzero = Fraction(at_center_nonzero, 1<<h)
    return at_center_zero + at_center_nonzero


def test(h, b):
    adj = graph(h, b)
    assert len(adj) <= 16
    W = fwht(independent_indicator(adj))
    from collections import Counter
    got = dict(Counter(W))
    pred = predicted_spectrum(h, b)
    assert got == pred, (h, b, got, pred)
    q = 1 << b
    nonzero = [abs(z) for z in W if z]
    assert min(nonzero) == q**(h-1)
    want_rank = (1<<h)*(1+h*(q-1))
    if h%2==0 and q <= h:
        want_rank -= comb(h, (h+q)//2)
    assert len(nonzero) == want_rank
    support = [int(w != 0) for w in W]
    kernel_numer = fwht(support)
    exact_norm = Fraction(sum(abs(x) for x in kernel_numer), 1<<len(adj))
    expected_norm = predicted_projection_norm(h,b)
    assert exact_norm == expected_norm, (h,b,exact_norm,expected_norm)
    print('PASS h={} b={} vertices={} rank={} min={} projection_norm={}'.format(
        h,b,len(adj),want_rank,min(nonzero),exact_norm))


if __name__ == '__main__':
    tests = [(2,1),(2,2),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(5,1),(5,2),(6,1),(7,1)]
    for h,b in tests:
        test(h,b)
    print('CLIQUE_CORONA_EXACT_PASS {} complete transforms'.format(len(tests)))
