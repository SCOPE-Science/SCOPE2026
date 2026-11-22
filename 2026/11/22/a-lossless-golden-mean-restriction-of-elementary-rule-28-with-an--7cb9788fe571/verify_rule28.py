#!/usr/bin/env python3
"""Exhaustive finite-ring verification of a restricted Rule-28 image theorem."""

def bits(word, n):
    return [(word >> i) & 1 for i in range(n)]


def hard_core(x, n):
    return all(not ((x >> i) & 1 and (x >> ((i + 1) % n)) & 1)
               for i in range(n))


def image_allowed(y, n):
    a = bits(y, n)
    return all(not (a[i] and a[(i + 1) % n] and a[(i + 2) % n])
               and (a[i] or not a[(i + 1) % n] or a[(i + 2) % n]
                    or a[(i + 3) % n])
               for i in range(n))


def rule28(x, n):
    a = bits(x, n)
    ans = 0
    for i in range(n):
        code = 4*a[(i-1) % n] + 2*a[i] + a[(i+1) % n]
        ans |= ((28 >> code) & 1) << i
    return ans


def decode(y, n):
    a = bits(y, n)
    return sum((a[i] & (1-a[(i-1) % n])) << i for i in range(n))


def lucas(n):
    if n == 0:
        return 2
    p, q = 2, 1
    for _ in range(2, n+1):
        p, q = q, p+q
    return q


def check_local_implication():
    # A five-bit local witness for the inverse test, centered at index 2.
    from itertools import product
    for t in product((0,1), repeat=5):
        if any(t[i:i+3] == (1,1,1) for i in range(3)):
            continue
        if any(t[i:i+4] == (0,1,0,0) for i in range(2)):
            continue
        x = [int(t[i] == 1 and t[i-1] == 0) for i in range(1,5)]
        # x at sites 1,2,3 suffices to evaluate y at site 2.
        neighborhood = (x[0], x[1], x[2])
        z = (28 >> (4*neighborhood[0] + 2*neighborhood[1] + neighborhood[2])) & 1
        assert z == t[2], (t,z)


def check():
    for n in range(1, 16):
        xs = [x for x in range(1 << n) if hard_core(x, n)]
        actual = [rule28(x, n) for x in xs]
        targets = {y for y in range(1 << n) if image_allowed(y, n)}
        assert len(xs) == lucas(n), (n,'source-count',len(xs))
        assert len(actual) == len(set(actual)), (n,'collision')
        assert set(actual) == targets, (n,'image',set(actual)^targets)
        for x,y in zip(xs,actual):
            assert decode(y, n) == x, (n,'left-inverse',x,y)
        for y in targets:
            assert hard_core(decode(y,n), n)
            assert rule28(decode(y,n),n)==y
    check_local_implication()
    print('VERIFY_OK restricted Rule 28: lengths 1..15, both directions, Lucas counts')


if __name__ == '__main__':
    check()
