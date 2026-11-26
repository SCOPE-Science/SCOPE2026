#!/usr/bin/env python3
"""Independent checks for sparse substring-composition reconstruction.
Run: python3 verify_sparse.py
No third-party dependencies.
"""
from itertools import combinations, product
from collections import defaultdict


def geom(k):
    assert k >= 0
    return [1] * (k + 1)


def product_poly(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x * y
    return r


def add_shift(out, p, shift):
    for i, x in enumerate(p):
        out[i + shift] += x


def gap_word(g):
    return ''.join(('0' * t + '1') for t in g[:-1]) + '0' * g[-1]


def layers_direct(word, layers):
    n = len(word)
    r = {k: [0] * (n + 1) for k in layers}
    for i in range(n):
        k = 0
        for j in range(i, n):
            k += word[j] == '1'
            if k in r:
                r[k][j - i + 1] += 1
    return r


def layers_formula(a, b, c, d):
    n = a + b + c + d + 3
    s2 = [0] * (n + 1)
    s3 = [0] * (n + 1)
    add_shift(s2, product_poly(geom(a), geom(c)), b + 2)
    add_shift(s2, product_poly(geom(b), geom(d)), c + 2)
    add_shift(s3, product_poly(geom(a), geom(d)), b + c + 3)
    return (s2, s3)


def order(poly):
    return next(i for i, c in enumerate(poly) if c)


def decode_3(s2, s3):
    # Recover two unordered pairs, then retain exactly the compatible orientations.
    idx3 = order(s3)
    b_plus_c = idx3 - 3
    q = s3[idx3:]
    while q[-1] == 0:
        q.pop()
    a_plus_d = len(q) - 1
    outer_min = max(q) - 1
    outer = (outer_min, a_plus_d - outer_min)
    inner_min = order(s2) - 2
    inner = (inner_min, b_plus_c - inner_min)
    assert min(outer) >= 0 and min(inner) >= 0
    answers = set()
    for a, d in (outer, outer[::-1]):
        for b, c in (inner, inner[::-1]):
            if layers_formula(a, b, c, d) == (s2, s3):
                answers.add(gap_word((a, b, c, d)))
    return answers


def full_profile(word):
    return tuple((k, tuple(v)) for k, v in layers_direct(word, range(len(word) + 1)).items())


def main():
    formulas = 0
    for a,b,c,d in product(range(8), repeat=4):
        w = gap_word((a,b,c,d))
        s2,s3 = layers_formula(a,b,c,d)
        v = layers_direct(w, (2,3))
        assert s2 == v[2] and s3 == v[3]
        assert decode_3(s2[:],s3[:]) == {w,w[::-1]}
        formulas += 1
    checked = 0
    for n in range(3,22):
        signatures = defaultdict(set)
        for ps in combinations(range(n), 3):
            w = ''.join('1' if i in ps else '0' for i in range(n))
            v = layers_direct(w, (2,3))
            key = (tuple(v[2]),tuple(v[3]))
            signatures[key].add(w)
            assert decode_3(v[2],v[3]) == {w,w[::-1]}
            checked += 1
        for words in signatures.values():
            assert len(words) <= 2
            u = next(iter(words))
            assert words == {u,u[::-1]}
    # The highest layer alone is insufficient, even with length and weight known.
    u, v = '11001', '10101'
    assert u != v and u != v[::-1]
    assert layers_direct(u,(3,))[3] == layers_direct(v,(3,))[3]
    # The complete spectrum does fail at the next weight (classical length-eight pair).
    u, v = '01001101', '01101001'
    assert u.count('1') == v.count('1') == 4 and u != v and u != v[::-1]
    assert full_profile(u) == full_profile(v)
    print(f'VERIFY_OK gap_tuples={formulas} weight3_words={checked} top_layer_counterexample=1 weight4_full_collision=1')

if __name__ == '__main__':
    main()
