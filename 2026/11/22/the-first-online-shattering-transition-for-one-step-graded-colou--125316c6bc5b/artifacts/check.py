#!/usr/bin/env python3
"""Finite checks for one-step coloured-star counting classifiers.

This program verifies finite instances and explicit full online mistake trees.
The all-parameter arguments are given separately in RESULT.md.
"""
from functools import lru_cache
from itertools import combinations, product


def profiles(q, d):
    return [v for v in product(range(d + 1), repeat=q) if sum(v) <= d]


def eval_h(h, v):
    if h == "TOP":
        return 1
    if h == "BOTTOM":
        return 0
    subset, threshold = h
    return int(sum(v[i] for i in range(len(v)) if subset >> i & 1) >= threshold)


def hypotheses(q, d):
    return ["TOP", "BOTTOM"] + [
        (subset, t) for subset in range(1, 1 << q) for t in range(1, d + 1)
    ]


def online_dim(q, d):
    xs = profiles(q, d)
    hyps = hypotheses(q, d)
    n = len(hyps)
    query = list(set(sum((1 << i) for i, h in enumerate(hyps) if eval_h(h, v)) for v in xs))

    @lru_cache(None)
    def dim(active):
        best = 0
        for pos in query:
            a, b = active & pos, active & ~pos
            if not a or not b or min(a.bit_count(), b.bit_count()) <= best:
                continue
            best = max(best, 1 + min(dim(a), dim(b)))
        return best

    return dim((1 << n) - 1), dim.cache_info().currsize


def vc_dim(q, d):
    xs = profiles(q, d)
    hs = hypotheses(q, d)
    functions = [tuple(eval_h(h, v) for v in xs) for h in hs]
    best = 0
    for k in range(1, q + 2):
        found = False
        for chosen in combinations(range(len(xs)), k):
            traces = {tuple(f[j] for j in chosen) for f in functions}
            if len(traces) == (1 << k):
                found = True
                break
        if not found:
            break
        best = k
    return best


def witness(q):
    # Each of 2^(q+1) label paths has a distinct explicit classifier.
    root = (0,) * (q - 1) + (2,)
    second_plus = (0,) * (q - 1) + (1,)
    second_minus = (0,) * (q - 1) + (3,)
    for branch0, branch1 in product((0, 1), repeat=2):
        for bits in product((0, 1), repeat=q - 1):
            subset = sum(bits[i] << i for i in range(q - 1))
            if branch0 and branch1:
                hypothesis = (subset | (1 << (q - 1)), 1)
                second = second_plus
                queries = [tuple(int(i == j) for i in range(q)) for j in range(q - 1)]
            elif branch0 and not branch1:
                hypothesis = (subset | (1 << (q - 1)), 2)
                second = second_plus
                queries = [tuple(int(i == j or i == q - 1) for i in range(q)) for j in range(q - 1)]
            elif not branch0 and branch1:
                hypothesis = (subset | (1 << (q - 1)), 3)
                second = second_minus
                queries = [tuple((1 if i == j else 2 if i == q - 1 else 0) for i in range(q)) for j in range(q - 1)]
            else:
                hypothesis = (subset, 1) if subset else "BOTTOM"
                second = second_minus
                queries = [tuple(int(i == j) for i in range(q)) for j in range(q - 1)]
            assert eval_h(hypothesis, root) == branch0
            assert eval_h(hypothesis, second) == branch1
            assert all(eval_h(hypothesis, x) == b for x, b in zip(queries, bits))
            assert sum(root) <= 3 and sum(second) <= 3
            assert all(sum(x) <= 3 for x in queries)
    return 1 << (q + 1)


def main():
    for q in (2, 3, 4):
        for d in (1, 2, 3):
            h = hypotheses(q, d)
            assert len(h) == d * ((1 << q) - 1) + 2
            assert len({tuple(eval_h(g, v) for v in profiles(q, d)) for g in h}) == len(h)
            got, states = online_dim(q, d)
            expect = q + int(d == 3)
            assert got == expect, (q, d, got, expect)
            print('Ldim', 'colors', q, 'degree', d, 'hypotheses', len(h), 'value', got, 'states', states)
    for q in (2, 3):
        for d in (1, 2, 3):
            v = vc_dim(q, d)
            assert v == q
            print('VC', 'colors', q, 'degree', d, 'value', v)
    for q in range(2, 10):
        n = witness(q)
        print('explicit full tree', 'colors', q, 'leaves', n, 'OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
