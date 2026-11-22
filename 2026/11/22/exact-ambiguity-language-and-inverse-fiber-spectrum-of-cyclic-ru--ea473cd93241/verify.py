#!/usr/bin/env python3
"""Independent finite checks for cyclic three-neighbor XOR on 11-free sources.

This is a finite checker, not a replacement for the all-length proof.
No external packages are needed.
"""
from collections import Counter, defaultdict


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def allowed(x, n):
    return all(not ((x >> i) & 1 and (x >> ((i + 1) % n)) & 1)
               for i in range(n))


def forward(x, n):
    y = 0
    for i in range(n):
        v = ((x >> ((i - 1) % n)) ^ (x >> i) ^
             (x >> ((i + 1) % n))) & 1
        y |= v << i
    return y


def ambiguous_type(y, n):
    if n % 3:
        return 0
    m = n // 3
    matches = []
    for r in range(3):
        if all((y >> i) & 1 for i in range(n) if i % 3 != r) and \
             (sum((y >> (r + 3*j)) & 1 for j in range(m)) & 1) == (m & 1):
            matches.append(r)
    if not matches:
        return 0
    assert (len(matches) == 3) == (y == (1 << n) - 1)
    return 3 if len(matches) == 3 else 2


def decode(y, n):
    ans = []
    for a in (0, 1):
        for b in (0, 1):
            x = [a, b]
            for i in range(1, n-1):
                x.append(((y >> i) & 1) ^ x[i-1] ^ x[i])
            mask = sum(z << j for j,z in enumerate(x))
            if allowed(mask, n) and forward(mask, n) == y:
                ans.append(mask)
    return sorted(ans)


def counts_expected(n):
    if n % 3:
        return {1: lucas(n)}
    m = n // 3
    return {1: lucas(n)-3*(1 << m)+3,
            2: 3*((1 << (m-1))-1),
            3: 1}


def verify():
    for n in range(3,19):
        outputs = defaultdict(list)
        for x in range(1 << n):
            if allowed(x,n):
                outputs[forward(x,n)].append(x)
        got = Counter(map(len, outputs.values()))
        expected = {j:c for j,c in counts_expected(n).items() if c}
        assert got == expected, (n,got,expected)
        assert sum(len(v) for v in outputs.values()) == lucas(n)
        for y, xs in outputs.items():
            condition = ambiguous_type(y,n)
            assert len(xs) == (condition or 1), (n,y,xs,condition)
            if n <= 11:
                assert decode(y,n) == sorted(xs), (n,y,xs)
        if n <= 11:
            for y in range(1 << n):
                assert decode(y,n) == sorted(outputs.get(y,[])), (n,y)
        print('PASS n=%d; admissible=%d; image=%d; fibers=%s' %
              (n, lucas(n), len(outputs), dict(sorted(got.items()))))
    for n in range(3,301):
        sizes = counts_expected(n)
        assert all(v >= 0 for v in sizes.values())
        assert sum(j*v for j,v in sizes.items()) == lucas(n)
        predicted = lucas(n) if n%3 else lucas(n)-3*(1 << (n//3-1))+1
        assert sum(sizes.values()) == predicted
    print('PASS exact cardinality identities n=3..300')


if __name__ == '__main__':
    verify()
