#!/usr/bin/env python3
"""Independent finite diagnostics for distinct images of a generalized word stack map.

Run: python3 verify_tortoise_entropy.py
This is a finite test, not a proof of the all-length entropy theorem.
"""
from functools import lru_cache
from itertools import product

@lru_cache(maxsize=None)
def tortoise_recursive(w):
    if not w:
        return ''
    maximum = max(w)
    pieces = w.split(maximum)
    images = [tortoise_recursive(piece) for piece in pieces]
    return ''.join(images[:2]) + maximum + ''.join(x + maximum for x in images[2:])


def tortoise_stack(w):
    # Equality causes a pop before pushing the next input letter.
    stack, result = [], []
    for x in w:
        while stack and x >= stack[-1]:
            result.append(stack.pop())
        stack.append(x)
    result.extend(reversed(stack))
    return ''.join(result)

@lru_cache(maxsize=None)
def compositions(total, parts):
    if parts == 1:
        return ((total,),)
    return tuple((j,) + tail for j in range(total + 1)
                 for tail in compositions(total - j, parts - 1))

@lru_cache(maxsize=None)
def grammar_words(q, length):
    if q == 1:
        return frozenset(('0' * length,))
    smaller = [grammar_words(q - 1, j) for j in range(length + 1)]
    out = set(smaller[length])
    maximum = str(q - 1)
    for copies in range(1, length + 1):
        for sizes in compositions(length - copies, copies + 1):
            for sections in product(*(smaller[j] for j in sizes)):
                out.add(''.join(sections[:2]) + maximum
                        + ''.join(section + maximum for section in sections[2:]))
    return frozenset(out)


def A2(z):
    return 1.0 / (1.0 - z) + z / (1.0 - 2.0 * z)


def A3(z):
    return A2(z) + z / ((1.0 - 2.0 * z) * (1.0 - z * A2(z)))


def root(f, left, right):
    for _ in range(100):
        m = (left + right) / 2
        if m * f(m) >= 1:
            right = m
        else:
            left = m
    return (left + right) / 2


def polyadd(a, b):
    return [((a[i] if i < len(a) else 0) +
             (b[i] if i < len(b) else 0)) for i in range(max(len(a), len(b)))]


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    return out


def exact_polynomial_check():
    # A_2 = N2 / D2, A_3 = N3 / (D2 * P3).
    d2, n2 = [1, -3, 2], [1, -1, -1]
    p3 = polyadd(d2, polymul([0, -1], n2))
    assert p3 == [1, -4, 3, 1]
    n3 = polyadd(polymul(n2, p3), polymul([0, 1, -1], d2))
    assert n3 == [1, -4, 2, 7, -6, -1]
    p4 = polyadd(polymul(d2, p3), polymul([0, -1], n3))
    assert p4 == [1, -8, 21, -18, -4, 8, 1]


def main():
    exact_polynomial_check()
    enumerated = 0
    expected3 = (1, 3, 6, 14, 35, 91, 242, 653, 1780, 4888)
    for q, maxn in ((2, 9), (3, 9), (4, 7)):
        counts = [1]
        for n in range(1, maxn + 1):
            outputs = set()
            for letters in product('0123'[:q], repeat=n):
                w = ''.join(letters)
                recursive = tortoise_recursive(w)
                stack = tortoise_stack(w)
                assert recursive == stack, (q, n, w, recursive, stack)
                outputs.add(stack)
                enumerated += 1
            predicted = grammar_words(q, n)
            assert outputs == predicted, (q, n, len(outputs), len(predicted))
            if q == 2:
                assert len(outputs) == (2 ** (n - 1) + 1)
            if q == 3:
                assert len(outputs) == expected3[n]
            if q >= 3 and n >= 4:
                forbidden = ''.join(map(str, (q - 1, q - 2, q - 3, q - 1)))
                assert not any(forbidden in w for w in outputs)
            counts.append(len(outputs))
        print(f'q={q}, lengths=0..{maxn}, distinct image counts={counts}')
    r3 = root(A2, .30, .40)
    r4 = root(A3, .25, .30)
    L3, L4 = 1 / r3, 1 / r4
    assert abs(L3 - 2.801937735804838) < 1e-10
    assert abs(L4 - 3.5503790656826695) < 1e-10
    poly4 = lambda z: z**6 + 8*z**5 - 4*z**4 - 18*z**3 + 21*z**2 - 8*z + 1
    assert abs(poly4(r4)) < 1e-12
    assert 2 < L3 < 3 and L3 < L4 < 4
    print(f'lambda_3={L3:.13f}, lambda_4={L4:.13f}, polynomial residual={abs(poly4(r4)):.2g}')
    print('PASS: exact polynomial identities for the ternary series and quaternary sextic')
    print(f'PASS: {enumerated} input words; independent stack/recursion; full grammar comparisons')

if __name__ == '__main__':
    main()
