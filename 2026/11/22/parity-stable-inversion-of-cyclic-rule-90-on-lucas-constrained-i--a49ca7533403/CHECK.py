"""Independent finite tests for Rule 90 with cyclic no-adjacent-one inputs.

Run using Python 3 standard library: python3 CHECK.py.
"""
from collections import Counter


def next_state(x, n):
    mask = (1 << n) - 1
    left = ((x << 1) & mask) | (x >> (n - 1))
    right = (x >> 1) | ((x & 1) << (n - 1))
    return left ^ right


def alternate_update(bits):
    n = len(bits)
    return tuple(bits[(i - 1) % n] ^ bits[(i + 1) % n] for i in range(n))


def allowed(x, n):
    return all(not ((x >> i) & 1 and (x >> ((i + 1) % n)) & 1)
               for i in range(n))


def lucas(n):
    a, b = 2, 1
    if n == 0:
        return a
    for _ in range(n-1):
        a, b = b, a + b
    return b


def measured(n, t):
    inputs = [x for x in range(1 << n) if allowed(x, n)]
    fiber = Counter()
    for x in inputs:
        cur = x
        for _ in range(t):
            cur = next_state(cur, n)
        fiber[cur] += 1
    return len(inputs), Counter(fiber.values()), len(fiber)


def expected(n):
    L = lucas(n)
    if n & 1:
        return L, Counter({1:L}), L
    m = n // 2
    distinct1 = L - (1 << (m+1)) + 1
    distinct2 = (1 << m) - 2
    assert distinct1 >= 0 and distinct2 >= 0
    return L, Counter({k:v for k,v in [(1,distinct1),(2,distinct2),(3,1)] if v}), L - (1 << m)


def run():
    tested = 0
    for n in range(2, 17):
        mask = (1 << n) - 1
        for x in range(1 << n):
            y = next_state(x, n)
            bits = tuple((x >> i) & 1 for i in range(n))
            other = sum(bit << i for i, bit in enumerate(alternate_update(bits)))
            assert y == other
        exp = expected(n)
        assert measured(n,1) == exp, (n, measured(n,1), exp)
        tested += 1
        if n % 4:
            for t in (2,3,5):
                assert measured(n,t) == exp, (n,t)
                tested += 1
        else:
            assert measured(n,2)[-1] < exp[-1]
            signal = sum(1 << i for i in range(0,n,4))
            assert allowed(signal,n)
            assert next_state(signal,n) != 0
            assert next_state(next_state(signal,n),n) == 0
            tested += 1
    print('VERIFY_OK n=2..16 all states, 15 one-step cases, 33 further-time cases, independent update evaluator')

if __name__=='__main__':
    run()
