"""Independent exhaustive graph and output-collision checks.

Run: python check_graph.py
No third-party modules required.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd


def duplicate(word, i, k):
    return word[:i+k] + word[i:i+k] + word[i+k:]


def components(n, k, ell):
    adjacency = [set() for _ in range(n)]
    for h in (k, ell):
        for i in range(n-h):
            adjacency[i].add(i+h)
            adjacency[i+h].add(i)
    seen = set()
    cs = []
    for start in range(n):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        vertices = []
        while stack:
            v = stack.pop()
            vertices.append(v)
            for w in adjacency[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        edge_count = sum(len(adjacency[v]) for v in vertices)//2
        cs.append((len(vertices), edge_count))
    return cs


def check_graphs():
    checks = 0
    for k in range(1, 6):
        for ell in range(k+1, 9):
            g = gcd(k, ell)
            for n in range(ell, k+ell+1):
                c = max(0, n-k-ell+g)
                comps = components(n, k, ell)
                assert sum(edges - vertices + 1 for vertices, edges in comps) == c
                assert sum(edges == vertices for vertices, edges in comps) == c
                assert all(edges in (vertices-1, vertices) for vertices, edges in comps)
                checks += 1
    print('GRAPH_CYCLE_VERIFY_OK', checks)


def check_collisions():
    checks = 0
    for q in (2, 3):
        for n in range(2, 8):
            if q**n > 2500:
                continue
            for k in range(1, n):
                for word in product(range(q), repeat=n):
                    outputs = [duplicate(word, i, k) for i in range(n-k+1)]
                    for i in range(n-k+1):
                        for j in range(i+1, n-k+1):
                            assert (outputs[i] == outputs[j]) == all(
                                word[t] == word[t+k] for t in range(i, j))
                    assert len(set(outputs)) == n-k+1-sum(
                        word[i] == word[i+k] for i in range(n-k))
                    checks += 1
    print('COLLISION_VERIFY_OK', checks)


def check_dependence():
    cases = [(2, 1, 2, 5), (2, 2, 3, 7), (3, 1, 2, 5),
             (3, 2, 3, 6), (2, 2, 4, 8), (2, 3, 4, 9)]
    for q, k, ell, n in cases:
        a, b = k//gcd(k, ell), ell//gcd(k, ell)
        total = 0
        for word in product(range(q), repeat=n):
            y = sum(word[i] == word[i+k] for i in range(n-k))
            z = sum(word[i] == word[i+ell] for i in range(n-ell))
            total += comb(y, b)*comb(z, a)
        observed = Fraction(total, q**n)
        independent = Fraction(comb(n-k, b)*comb(n-ell, a), q**(a+b))
        assert observed > independent, (q, k, ell, n, observed, independent)
    print('DEPENDENCE_VERIFY_OK', len(cases))


if __name__ == '__main__':
    check_graphs()
    check_collisions()
    check_dependence()
