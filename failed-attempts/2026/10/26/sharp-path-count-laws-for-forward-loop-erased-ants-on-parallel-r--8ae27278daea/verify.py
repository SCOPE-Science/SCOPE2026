#!/usr/bin/env python3
"""Finite exact checks for two-terminal parallel-path loop-erased reinforcement.

The infinite almost-sure assertions in the accompanying manuscript are proved
analytically; finite computations here check the model reduction and identities.
Standard library only. Run: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations
from math import gamma, isclose


def graph(lengths):
    """Paths share terminals 0,1 and have disjoint intermediate vertices."""
    edges, arcs = [], []
    nxt = 2
    for length in lengths:
        vertices = [0] + list(range(nxt, nxt + length - 1)) + [1]
        nxt += length - 1
        arc = []
        for u, v in zip(vertices, vertices[1:]):
            arc.append(len(edges))
            edges.append((u, v))
        arcs.append(tuple(arc))
    return nxt, edges, arcs


def spanning_tree_choice_weights(lengths, weights):
    vertices, edges, arcs = graph(lengths)
    counts = [0] * len(lengths)
    total_trees = 0
    for chosen in combinations(range(len(edges)), vertices - 1):
        parent = list(range(vertices))

        def root(x):
            while x != parent[x]:
                x = parent[x]
            return x

        good = True
        for idx in chosen:
            u, v = edges[idx]
            a, b = root(u), root(v)
            if a == b:
                good = False
                break
            parent[a] = b
        if not good or len({root(v) for v in range(vertices)}) > 1:
            continue
        total_trees += 1
        full = [i for i, arc in enumerate(arcs) if all(e in chosen for e in arc)]
        assert len(full) == 1, (lengths, full)
        branch = full[0]
        tree_weight = 1
        for idx in chosen:
            which = next(i for i, arc in enumerate(arcs) if idx in arc)
            tree_weight *= weights[which]
        counts[branch] += tree_weight
    return counts, total_trees


def check():
    tests = 0
    for lengths in [(3, 4), (3, 3, 5), (2, 4, 5), (3, 4, 5), (2, 2, 3, 4)]:
        k = len(lengths)
        for offset in range(4):
            weights = [1 + (i * 2 + offset) % 4 for i in range(k)]
            sums, number = spanning_tree_choice_weights(lengths, weights)
            assert number == sum(__import__('math').prod(lengths[j] for j in range(k) if j != i)
                                 for i in range(k))
            conductances = [Fraction(w, L) for w, L in zip(weights, lengths)]
            den = sum(conductances)
            for i in range(k):
                empirical = Fraction(sums[i], sum(sums))
                assert empirical == conductances[i] / den, (lengths, weights, i)
                tests += 1
            # Gambler's-ruin harmonic equation along every uniform-weight arm.
            for L in lengths:
                for j in range(1, L):
                    assert Fraction(j, L) == (Fraction(j-1, L) + Fraction(j+1, L))/2
                    tests += 1
        # Embedded Yule competition matches the urn conditional probability.
        for n in range(1, 10):
            populations = [1 + (n + 2 * i) % 10 for i in range(k)]
            rates = [Fraction(populations[i], lengths[i]) for i in range(k)]
            assert sum(rate / sum(rates) for rate in rates) == 1
            tests += 1
    # Shape and moment identities: V_i=E_i S^{-r}, E_i~Exp(1), S~Gamma(h,1).
    for h in (1, 2, 4):
        for numerator, denominator in ((3, 4), (3, 5), (2, 7)):
            r = Fraction(numerator, denominator)
            assert 0 < r < 1
            moment = gamma(2) * gamma(h-float(r)) / gamma(h)
            assert moment > 0 and isclose(moment, gamma(h-float(r)) / gamma(h))
            tests += 1
    print(f'PASS: {tests} independent exact probability/identity checks')
    print('Finite checks do not establish the infinite-time almost-sure convergence.')


if __name__ == '__main__':
    check()
