#!/usr/bin/env python3
"""Check the six-leaf quartet interpolation certificate by edge insertion.

Uses only the Python standard library. Run from this directory:
    python3 verify_insertions.py
"""
from itertools import combinations
from hashlib import sha256
from json import load
from pathlib import Path

P = 1000003


def trees():
    current = [frozenset({(0, 100), (1, 100), (2, 100)})]
    for leaf in (3, 4, 5):
        next_level = []
        for edges in current:
            for u, v in sorted(edges):
                t = 100 + leaf
                replacement = {tuple(sorted((u, t))), tuple(sorted((v, t))), (leaf, t)}
                next_level.append(frozenset((edges - {(u, v)}) | replacement))
        current = next_level
    return current


def get_path(edges, a, b):
    adjacency = {}
    for x, y in edges:
        adjacency.setdefault(x, []).append(y)
        adjacency.setdefault(y, []).append(x)
    stack = [(a, [a])]
    while stack:
        x, path = stack.pop()
        if x == b:
            return set(path)
        stack.extend((y, path + [y]) for y in adjacency[x] if y not in path)
    raise AssertionError("Disconnected tree")


def signature(edges):
    out = []
    for a, b, c, d in combinations(range(6), 4):
        for u, v, w, z in ((a, b, c, d), (a, c, b, d), (a, d, b, c)):
            out.append(int(get_path(edges, u, v).isdisjoint(get_path(edges, w, z))))
    assert len(out) == 45
    assert all(sum(out[j:j + 3]) == 1 for j in range(0, 45, 3))
    return tuple(out)


def get_internal_splits(edges):
    splits = []
    for u, v in edges:
        if u < 100 or v < 100:
            continue
        adjacency = {}
        for a, b in edges - {(u, v)}:
            adjacency.setdefault(a, []).append(b)
            adjacency.setdefault(b, []).append(a)
        region = {u}
        frontier = [u]
        while frontier:
            a = frontier.pop()
            for b in adjacency.get(a, []):
                if b not in region:
                    region.add(b)
                    frontier.append(b)
        L = tuple(sorted(region.intersection(range(6))))
        R = tuple(sorted(set(range(6)) - set(L)))
        if (len(L), L) > (len(R), R):
            L, R = R, L
        splits.append(''.join(map(str, L)) + '|' + ''.join(map(str, R)))
    return sorted(splits)


def entry(sig, row, columns):
    x = 1
    for j in columns:
        x *= sig[row][j]
    return x


def modular_determinant(M, prime=P):
    A = [list(map(lambda x: x % prime, row)) for row in M]
    n = len(A)
    assert all(len(row) == n for row in A)
    determinant = 1
    for j in range(n):
        pivot = next((k for k in range(j, n) if A[k][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            determinant = -determinant
        d = A[j][j]
        determinant = determinant * d % prime
        inv = pow(d, prime - 2, prime)
        for k in range(j + 1, n):
            if A[k][j]:
                z = A[k][j] * inv % prime
                for m in range(j + 1, n):
                    A[k][m] = (A[k][m] - z * A[j][m]) % prime
                A[k][j] = 0
    return determinant % prime


def main():
    certificate = load(open(Path(__file__).with_name('CERTIFICATE.json'), encoding='utf-8'))
    assert certificate['prime'] == P and certificate['n_trees'] == 105
    t = trees()
    lookup = {signature(E): E for E in t}
    sig = sorted(lookup)
    assert len(t) == len(lookup) == 105
    assert sha256(bytes(x for s in sig for x in s)).hexdigest() == certificate['signature_sha256']
    witness31 = certificate['rank_one']
    D31 = modular_determinant([[entry(sig, r, col) for col in witness31['columns']]
                               for r in witness31['rows']])
    assert D31 == witness31['minor_determinant_mod_prime'] == 243
    assert len(witness31['rows']) == len(witness31['columns']) == 31
    # Exactly one resolution of each four-leaf subset is displayed.
    # Thus the 46 constant/singleton columns have 15 independent
    # disjoint-support relations, and their rank is at most 31.
    D105 = modular_determinant([[entry(sig, r, col) for col in certificate['rank_two']['columns']]
                                for r in range(105)])
    assert D105 == certificate['rank_two']['full_determinant_mod_prime'] == 582830
    assert len(certificate['rank_two']['columns']) == 105
    for col in certificate['rank_two']['columns']:
        assert 0 <= len(col) <= 2 and all(0 <= i < 45 for i in col)
    w = certificate['mixture_witness']
    a, b = w['pair_one']
    c, d = w['pair_two']
    assert len({a, b, c, d}) == 4
    assert all(sig[a][j] + sig[b][j] == sig[c][j] + sig[d][j] for j in range(45))
    for k in (a, b, c, d):
        assert get_internal_splits(lookup[sig[k]]) == w['split_systems'][str(k)]
    i, j = w['separating_joint_event']['quartets']
    observed = [sig[a][i] * sig[a][j] + sig[b][i] * sig[b][j],
                sig[c][i] * sig[c][j] + sig[d][i] * sig[d][j]]
    assert observed == w['separating_joint_event']['pair_counts'] == [1, 0]
    print('PASS: 105 distinct trees; degree-one rank 31; degree-two rank 105.')
    print('PASS: modular determinants', D31, D105, 'and explicit mixture separation.')


if __name__ == '__main__':
    main()
