"""Exact finite checks for the joint prime-power binomial-column theorem."""
from collections import Counter
from math import comb


def harmonic(p):
    hs = [0]
    for j in range(1, p):
        hs.append((hs[-1] + pow(j, -1, p)) % p)
    return hs


def predicted(p, a, u, v):
    hs = harmonic(p)
    z = Counter(hs)
    u0, u1 = u % p, u // p
    v0 = v % p
    if u0 == 0:
        return p ** a if u1 == v0 else 0
    return p ** (a - 1) * z[((u1-v0) * pow(u0,-1,p)) % p]


def verify(p, a):
    h = p ** a
    period = p ** (a+3)
    mod = p*p
    hist = Counter()
    aa = bb = 0
    for n in range(period):
        if n >= h:
            aa = comb(n, h) % mod
        if n >= p*h:
            bb = comb(n, p*h) % mod
        hist[(aa,bb)] += 1
        x, r = divmod(n, h)
        j = r // (h // p)
        predicted_a = (x * (1+p*harmonic(p)[j])) % mod
        assert aa == predicted_a, (p, a, n, aa, predicted_a)
        y, s = divmod(n, p*h)
        q = s // h
        predicted_b = (y * (1+p*harmonic(p)[q])) % mod
        assert bb == predicted_b, (p, a, n, bb, predicted_b)
    for u in range(mod):
        for v in range(mod):
            assert hist[(u,v)] == predicted(p,a,u,v), (p,a,u,v,hist[(u,v)],predicted(p,a,u,v))
    assert sum(hist.values()) == period
    assert all(sum(hist[(u,v)] for v in range(mod)) == period//mod for u in range(mod))
    assert all(sum(hist[(u,v)] for u in range(mod)) == period//mod for v in range(mod))
    hs = harmonic(p)
    print(f'p={p}, a={a}, N={period}, image={len(hist)}/{mod*mod}, harmonic={hs}, multiplicities={sorted(set(hist.values()))}')


if __name__ == '__main__':
    for prime, exponent in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2),(7,1),(11,1)]:
        verify(prime, exponent)
    print('ALL EXACT CHECKS PASSED')
