"""Exact diagnostic for uniform-vertex Euclidean radial shells of tree zonotopes.

Run with Python 3.9 or later, standard library only: python3 CHECKER.py
No network or numerical dependencies are used. Finite tests are not a proof.
"""
from collections import Counter
from itertools import product
from fractions import Fraction
from math import comb
from heapq import heapify, heappop, heappush


def edges_from_prufer(n, word):
    if n == 2:
        return [(0, 1)]
    degrees = [1] * n
    for v in word:
        degrees[v] += 1
    heap = [v for v in range(n) if degrees[v] == 1]
    heapify(heap)
    edges = []
    for v in word:
        u = heappop(heap)
        edges.append((u, v))
        degrees[u] -= 1
        degrees[v] -= 1
        if degrees[v] == 1:
            heappush(heap, v)
    edges.append((heappop(heap), heappop(heap)))
    return edges


def direct_shells(n, edges, record_joint=False):
    shells = Counter()
    joint = Counter()
    for signs in product((-1, 1), repeat=len(edges)):
        twice = [0] * n
        for (u, v), sign in zip(edges, signs):
            twice[u] += sign
            twice[v] -= sign
        local_squares = tuple(x*x for x in twice)
        shells[sum(local_squares)] += 1
        if record_joint:
            joint[local_squares] += 1
    return shells, joint


def prediction(n, edges):
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    p = Counter({0: 1})
    for d in deg:
        factor = Counter()
        for j in range(d + 1):
            factor[(d - 2*j)**2] += comb(d, j)
        new = Counter()
        for a, ca in p.items():
            for b, cb in factor.items():
                new[a+b] += ca*cb
        p = new
    den = 2**len(edges)
    assert all(count % den == 0 for count in p.values())
    return Counter({q: count//den for q, count in p.items()}), deg


def test_all_labelled_trees():
    trees = 0
    vertex_checks = 0
    for n in range(2, 8):
        for word in product(range(n), repeat=n-2):
            edges = edges_from_prufer(n, word)
            observed, _ = direct_shells(n, edges)
            expected, deg = prediction(n, edges)
            assert observed == expected, (n, word, observed, expected)
            assert sum(observed.values()) == 2**(n-1)
            assert max(observed) == sum(d*d for d in deg)
            assert observed[max(observed)] == 2
            assert min(observed) == sum(d % 2 for d in deg)
            mean = sum(Fraction(q,4)*c for q,c in observed.items()) / 2**(n-1)
            variance = sum((Fraction(q,4)-mean)**2*c for q,c in observed.items()) / 2**(n-1)
            assert mean == Fraction(n-1,2)
            assert variance == sum(comb(d,2) for d in deg)/4
            trees += 1
            vertex_checks += 2**(n-1)
    assert trees == sum(n**(n-2) for n in range(2,8))
    return trees, vertex_checks


def test_independence():
    edges = [(0,1),(1,2),(1,3),(3,4),(4,5),(4,6),(6,7)]
    n=8
    shells, joint = direct_shells(n,edges,record_joint=True)
    predicted, degrees=prediction(n,edges)
    assert shells == predicted
    local_counts=[]
    for d in degrees:
        a=Counter()
        for j in range(d+1):
            a[(d-2*j)**2]+=comb(d,j)
        local_counts.append(a)
    keys=list(product(*(sorted(a) for a in local_counts)))
    for key in keys:
        numerator=1
        for q,c in zip(key,local_counts):
            numerator*=c[q]
        assert numerator % 2**len(edges)==0
        assert joint[key] == numerator // 2**len(edges)
    assert set(joint)==set(keys)
    return len(keys)


def test_nonisomorphic_same_degree():
    # Two distinct six-vertex spiders with arm lengths (3,1,1) and (2,2,1).
    edges1=[(0,1),(1,2),(2,3),(0,4),(0,5)]
    edges2=[(0,1),(1,2),(0,3),(3,4),(0,5)]
    a, _=direct_shells(6,edges1)
    b, _=direct_shells(6,edges2)
    assert a == b
    return a


def main():
    labelled, orientations=test_all_labelled_trees()
    joint_states=test_independence()
    same=test_nonisomorphic_same_degree()
    print(f'TREE_RADIAL_PASS labelled_trees={labelled} orientations={orientations} joint_states={joint_states} six_vertex_shells={dict(sorted(same.items()))}')

if __name__=='__main__':
    main()
