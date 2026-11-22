#!/usr/bin/env python3
"""Finite checks for size spectra of tree representatives of modal types.

No numerical experiment in this file substitutes for the all-depth proofs.
"""
from collections import Counter
from functools import lru_cache
from math import erf, sqrt


def canonical_types(q, h):
    """Unique minimal unordered, q-coloured rooted trees of height <= h."""
    layer = tuple((color, ()) for color in range(q))
    for _ in range(h):
        result = []
        for bits in range(1 << len(layer)):
            children = tuple(layer[i] for i in range(len(layer)) if (bits >> i) & 1)
            for color in range(q):
                result.append((color, children))
        layer = tuple(result)
    return layer


def order(tree):
    return 1 + sum(order(child) for child in tree[1])


def sig(tree, h):
    color, children = tree
    if h == 0:
        return color, ()
    return color, frozenset(sig(t, h - 1) for t in children)


def bisim(t, u, h):
    """Direct depth-h back/forth game; intentionally no canonical signatures."""
    if t[0] != u[0]:
        return False
    if h == 0:
        return True
    a, b = t[1], u[1]
    return all(any(bisim(x, y, h-1) for y in b) for x in a) and all(
        any(bisim(x, y, h-1) for x in a) for y in b
    )


def poly_histogram(q, h):
    """Iterated weighted subset formula without listing full next-layer types."""
    hist = Counter({1: q})
    for _ in range(h):
        coefficients = [1]
        for weight, multiplicity in sorted(hist.items()):
            for _ in range(multiplicity):
                coeff2 = coefficients + [0]*weight
                for i, value in enumerate(coefficients):
                    coeff2[i + weight] += value
                coefficients = coeff2
        hist = Counter({i + 1: q*v for i, v in enumerate(coefficients) if v})
    return hist


def all_unordered_colored_trees(q, max_n):
    """Independent enumeration by vertex count rather than modal signatures."""
    by_size = [[] for _ in range(max_n + 1)]
    for n in range(1, max_n + 1):
        shapes = [(s, order(s)) for j in range(1, n) for s in by_size[j]]
        shapes.sort(key=lambda t: (t[1], repr(t[0])))

        @lru_cache(None)
        def forest(remaining, lower):
            if remaining == 0:
                return ((),)
            ans = []
            for i in range(lower, len(shapes)):
                sh, weight = shapes[i]
                if weight > remaining:
                    break
                ans.extend(((sh,) + rest for rest in forest(remaining-weight, i)))
            return tuple(ans)
        for children in forest(n-1, 0):
            for color in range(q):
                by_size[n].append((color, children))
    return by_size


def independent_small_models():
    for q, h in ((1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)):
        max_n = 6
        all_by_size = all_unordered_colored_trees(q, max_n)
        minima = {}
        for n in range(1, max_n + 1):
            for tree in all_by_size[n]:
                key = sig(tree, h)
                minima[key] = min(minima.get(key, n), n)
        computed = Counter(minima.values())
        predicted = poly_histogram(q, h)
        assert {n: v for n, v in predicted.items() if n <= max_n} == dict(computed), (q, h, computed, predicted)
        # Verify genuinely different bisimulation implementation for small models.
        examples = [t for n in range(1, min(4, max_n)+1) for t in all_by_size[n]]
        for a in examples:
            for b in examples:
                assert (sig(a, h) == sig(b, h)) == bisim(a, b, h)
        print('small-model',q,h,'checked',sum(map(len,all_by_size)),'types_to_size_6',sum(computed.values()))


def recursive_moments(q, h):
    hist = poly_histogram(q, h)
    N = sum(hist.values())
    mean = sum(weight*count for weight, count in hist.items())/N
    variance = sum((weight-mean)**2*count for weight, count in hist.items())/N
    assert N == q * (2 ** (sum(poly_histogram(q,h-1).values()))) if h else N == q
    return hist, N, mean, variance


def normal_bound():
    for q,h in ((1,2),(1,3),(1,4),(2,2),(2,3)):
        hist,N,mean,var=recursive_moments(q,h)
        predecessor = poly_histogram(q,h-1)
        n=sum(predecessor.values())
        W=sum(s*k for s,k in predecessor.items())
        S2=sum(s*s*k for s,k in predecessor.items())
        S3=sum(s*s*s*k for s,k in predecessor.items())
        assert 1 + W/2 == mean
        assert S2/4 == var
        bound = 0.56 * S3/(S2**1.5)
        assert bound <= 1.12/sqrt(n) + 1e-12
        M=1+W
        assert abs(mean-(M+1)/2)<1e-9
        assert set(hist) == set(range(1, M+1))
        assert hist[1] == hist[M] == q
        assert all(hist[k] == hist[M+1-k] for k in range(1,M+1))
        assert 2*var == sum((s*s*k) for s,k in predecessor.items())/2
        print('normal-bound',q,h,'types',N,'max_order',M,'mean',mean,'sd',sqrt(var),
              'BE_actual_bound',round(bound,6),'BE_uniform_bound',round(1.12/sqrt(n),6))
        # Direct finite-h cdf comparison to the normal is far from a proof of the CLT.
        cum=0
        D=0
        for weight in sorted(hist):
            y=(weight-mean)/sqrt(var)
            lower=(1+erf(y/sqrt(2)))/2
            D=max(D,abs(cum/N-lower))
            cum+=hist[weight]
            D=max(D,abs(cum/N-lower))
        assert D <= bound + 1e-12


if __name__=='__main__':
    independent_small_models()
    normal_bound()
    print('VERIFY_OK')
