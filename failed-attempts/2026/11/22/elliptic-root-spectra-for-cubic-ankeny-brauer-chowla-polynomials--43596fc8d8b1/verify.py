"""Exact finite-field verification of an elliptic root-spectrum identity.

Run: python verify.py. Only elementary integer arithmetic is used.
The finite tests support, but do not replace, the general proof.
"""
from collections import Counter


def field(p, e):
    if e == 1:
        q = p
        def add(a, b): return (a + b) % p
        def mul(a, b): return (a * b) % p
        return q, add, mul, 1
    assert e == 2
    d = next(v for v in range(2, p) if pow(v, (p - 1) // 2, p) == p - 1)
    q = p * p
    def add(a, b): return ((a % p + b % p) % p) + p * (((a // p) + (b // p)) % p)
    def mul(a, b):
        a0, a1 = a % p, a // p
        b0, b1 = b % p, b // p
        return ((a0 * b0 + d * a1 * b1) % p) + p * ((a0 * b1 + a1 * b0) % p)
    return q, add, mul, 1


def check(p, e):
    assert p not in (2, 7)
    q, add, mul, one = field(p, e)
    const = lambda a: a % p
    neg = lambda x: add(0, mul(const(-1), x))
    sq = lambda x: mul(x, x)
    cub = lambda x: mul(x, sq(x))
    roots = {sq(y) for y in range(q)}
    # affine points, plus the unique point at infinity
    H = 1
    for X in range(q):
        rhs = add(add(cub(X), mul(const(13), sq(X))), mul(const(128), X))
        H += 1 if rhs == 0 else (2 if rhs in roots else 0)
    z = 0
    dist = {}
    for shift in (-1, 1):
        hist = Counter()
        for u in range(q):
            num_roots = 0
            for x in range(q):
                value = add(mul(mul(x, add(x, const(shift))), add(x, neg(u))), one)
                if value == 0: num_roots += 1
            hist[num_roots] += 1
            assert num_roots <= 3
        dist[shift] = tuple(hist.get(i, 0) for i in range(4))
    for u in range(q):
        t = add(add(sq(u), u), const(-3))
        if add(sq(t), const(-32)) == 0: z += 1
    assert z % 2 == 0
    assert H % 6 == 0
    expected = (H // 3, q + 1 - (H + z) // 2, z, H // 6 - 1 - z // 2)
    assert all(v >= 0 for v in expected), (p,e,expected)
    assert dist[-1] == expected == dist[1], (p,e,H,z,dist,expected)
    return (q,H,z,expected)


def primes(bound):
    return [n for n in range(3,bound+1,2) if all(n % k for k in range(2,int(n**.5)+1))]


def main():
    cases = []
    for p in primes(97):
        if p != 7: cases.append(check(p, 1))
    for p in (3,5,11,13,17): cases.append(check(p, 2))
    print('ELLIPTIC_CUBIC_OK', len(cases), 'finite fields; sizes',
          ','.join(str(t[0]) for t in cases), '; 2 polynomial families')
    for q, H, z, v in cases[:12]: print('q=',q,'Epoints=',H,'multiple=',z,'hist=',v)

if __name__ == '__main__': main()
