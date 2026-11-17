#!/usr/bin/env python3
"""Exact finite checks for the clique-complex homotopy theorem for Latin squares.
This checks face classification, intercalate-free facets, Euler characteristic,
and ordinary mod-2 boundary ranks for explicit small Latin squares. The
all-order homotopy equivalence is proved separately in RESULT.md.
Python standard library only.
"""
from itertools import combinations
from collections import Counter
from math import comb


def latin_check(M):
    n = len(M)
    assert all(len(row) == n and set(row) == set(range(n)) for row in M)
    assert all({M[r][c] for r in range(n)} == set(range(n)) for c in range(n))
    return n


def is_edge(a, b, M):
    (r, c), (s, d) = a, b
    return a != b and (r == s or c == d or M[r][c] == M[s][d])


def maximal_cliques(vertices, adjacency):
    out = []
    def bron(R, P, X):
        if not P and not X:
            out.append(tuple(sorted(R)))
            return
        pivot = max(P | X, key=lambda v: len(P & adjacency[v])) if P or X else None
        for v in sorted(P - (adjacency[pivot] if pivot is not None else set())):
            bron(R | {v}, P & adjacency[v], X & adjacency[v])
            P.remove(v)
            X.add(v)
    bron(set(), set(vertices), set())
    return sorted(set(out))


def mod2rank(rows):
    pivots = {}
    for x in rows:
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                pivots[p] = x
                break
            x ^= pivots[p]
    return len(pivots)


def analyze(M, label):
    n = latin_check(M)
    vs = [(r, c) for r in range(n) for c in range(n)]
    ix = {v:i for i,v in enumerate(vs)}
    adj = [set() for _ in vs]
    for i,j in combinations(range(n*n),2):
        if is_edge(vs[i], vs[j], M):
            adj[i].add(j)
            adj[j].add(i)
    mc = maximal_cliques(range(n*n), adj)
    lines = set()
    for r in range(n): lines.add(tuple(sorted(ix[(r,c)] for c in range(n))))
    for c in range(n): lines.add(tuple(sorted(ix[(r,c)] for r in range(n))))
    for s in range(n): lines.add(tuple(sorted(ix[(r,c)] for r in range(n) for c in range(n) if M[r][c] == s)))
    # Every non-collinear 3-clique is a rainbow triangle.
    rainbow = set()
    for r in range(n):
        for c in range(n):
            for s in range(n):
                if M[r][c] == s: continue
                c2 = next(d for d in range(n) if M[r][d] == s)
                r2 = next(t for t in range(n) if M[t][c] == s)
                rainbow.add(tuple(sorted([ix[(r,c)], ix[(r,c2)], ix[(r2,c)]])))
    assert len(rainbow) == n*n*(n-1)
    intercalates = set()
    for r,t in combinations(range(n),2):
        for c,d in combinations(range(n),2):
            if M[r][c] == M[t][d] and M[r][d] == M[t][c]:
                intercalates.add(tuple(sorted(ix[v] for v in [(r,c),(r,d),(t,c),(t,d)])))
    # For n>=3, all maximal cliques are lines or intercalates or
    # rainbow triangles not contained in an intercalate.
    facets = lines | intercalates | {tri for tri in rainbow if not any(set(tri) <= set(tet) for tet in intercalates)}
    if n >= 3: assert set(mc) == facets, (label, len(set(mc)^facets))
    # Each rainbow triangle belongs to at most one intercalate 3-face.
    usage = Counter(t for tet in intercalates for t in combinations(tet,3))
    assert all(t in rainbow and usage[t] == 1 for t in usage)
    assert len(usage) == 4*len(intercalates)
    allfaces = {(): True}
    for facet in mc:
        for k in range(1,len(facet)+1):
            for f in combinations(facet,k): allfaces[f] = True
    maxk = max(map(len, allfaces))
    levels = [[t for t in allfaces if len(t)==k] for k in range(maxk+1)]
    fvec = tuple(len(levels[k]) for k in range(1,maxk+1))
    assert fvec[0] == n*n
    assert fvec[1] == 3*n*comb(n,2)
    assert fvec[2] == 3*n*comb(n,3) + n*n*(n-1)
    if maxk >= 4: assert fvec[3] == 3*n*comb(n,4) + len(intercalates)
    chi = sum((-1)**(k-1)*len(levels[k]) for k in range(1,maxk+1))
    target = 1+(n-1)**3-len(intercalates)
    assert chi == target
    # Boundary over F_2 for degrees 1.. max dimension. Rows are
    # represented as bits; rank is exactly computed by XOR elimination.
    ranks = [0]*(maxk+1)
    for k in range(1,maxk):
        lower = {f:i for i,f in enumerate(levels[k])}
        cols = []
        for face in levels[k+1]:
            x = 0
            for i in range(k+1): x ^= 1 << lower[face[:i]+face[i+1:]]
            cols.append(x)
        ranks[k] = mod2rank(cols)
    betti = [len(levels[k+1])-ranks[k]-ranks[k+1] for k in range(maxk)]
    assert betti[0] == 1 and betti[1] == 0
    assert betti[2] == target-1
    assert not any(betti[3:])
    return label,n,len(intercalates),len(mc),fvec,chi,tuple(betti)


def main():
    squares = [
        ('Z2', [[(r+c)%2 for c in range(2)] for r in range(2)]),
        ('Z3', [[(r+c)%3 for c in range(3)] for r in range(3)]),
        ('Z4', [[(r+c)%4 for c in range(4)] for r in range(4)]),
        ('V4', [[r^c for c in range(4)] for r in range(4)]),
        ('Z5', [[(r+c)%5 for c in range(5)] for r in range(5)]),
        ('nongroup_5', [
            [0,1,2,3,4],
            [1,0,3,4,2],
            [2,3,4,0,1],
            [3,4,1,2,0],
            [4,2,0,1,3],
        ]),
        ('Z6', [[(r+c)%6 for c in range(6)] for r in range(6)]),
    ]
    for label,M in squares:
        name,n,I,mx,f,chi,b=analyze(M,label)
        print(f'{name}: n={n}, intercalates={I}, maximal={mx}, f_vector={f}, chi={chi}, betti_mod2={b}')
    print('VERIFY_OK_LATIN_HOMOTOPY_FINITE_CHECKS')

if __name__ == '__main__':main()
