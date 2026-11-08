"""Exact tests for maximal independent sets in two-token biclique graphs.

Only the Python standard library is needed. All graph adjacencies are built
from the token-move definition, not from the proof's normal form.
"""
from collections import Counter
from itertools import combinations
from math import comb


def graph(m, n):
    pairs = list(combinations(range(m + n), 2))
    edges = {p: set() for p in pairs}
    for a, b in combinations(pairs, 2):
        d = set(a) ^ set(b)
        if len(d) == 2:
            x, y = d
            if (x < m) != (y < m):
                edges[a].add(b)
                edges[b].add(a)
    return pairs, edges


def direct_maximal_independent_sets(m, n):
    vertices, edges = graph(m, n)
    # Bron-Kerbosch for maximal cliques of the graph complement.
    # This generator contains no structural assumptions about the host.
    all_v = set(vertices)
    nonedges = {v: (all_v - {v}) - edges[v] for v in vertices}
    out = set()

    def bk(r, p, x):
        if not p and not x:
            out.add(frozenset(r))
            return
        pool = p | x
        pivot = max(pool, key=lambda v: len(p & nonedges[v])) if pool else None
        for v in tuple(p - (nonedges[pivot] if pivot is not None else set())):
            bk(r | {v}, p & nonedges[v], x & nonedges[v])
            p.remove(v)
            x.add(v)

    bk(set(), set(vertices), set())
    return out


def structural_sets(m, n):
    vertices, _ = graph(m, n)
    all_u = frozenset((i, j) for i, j in vertices
                      if (i < m) == (j < m))
    result = {all_u}
    for r in range(1, m + 1):
        if m-r == 1:
            continue
        for s in range(1, n + 1):
            if n-s == 1:
                continue
            for row_zero in combinations(range(m), r):
                row_zero = set(row_zero)
                row_used = set(range(m)) - row_zero
                for col_zero in combinations(range(m, m+n), s):
                    col_zero = set(col_zero)
                    col_used = set(range(m,m+n)) - col_zero
                    chosen = frozenset((i, j) for i, j in vertices if
                        (i in row_used and j in row_used) or
                        (i in col_used and j in col_used) or
                        (i in row_zero and j in col_zero))
                    if chosen in result:
                        raise AssertionError('non-unique encoding')
                    result.add(chosen)
    return result


def polynomial(m, n):
    counts = Counter({comb(m,2) + comb(n,2): 1})
    for r in range(1,m+1):
        if m-r==1:continue
        for s in range(1,n+1):
            if n-s==1:continue
            size = comb(m-r,2)+comb(n-s,2)+r*s
            counts[size] += comb(m,r)*comb(n,s)
    return +counts


def verify():
    # Independent graph-definition enumeration, not a tautological
    # check of the formula, on the complete rectangle 2..5.
    for m in range(2, 6):
        for n in range(2, 6):
            direct = direct_maximal_independent_sets(m, n)
            structural = structural_sets(m, n)
            if direct != structural:
                raise AssertionError(('MIS mismatch',m,n,len(direct),len(structural)))
            coeff = Counter(map(len, direct))
            if coeff != polynomial(m,n):
                raise AssertionError(('coefficient mismatch',m,n,coeff,polynomial(m,n)))
            print('DIRECT_MAXIMAL_INDEPENDENT_OK',m,n,len(direct))
    # Additional larger parameters, with an independent set/dominating check
    # for every structural candidate, and an exact coefficient/count check.
    for m in range(2, 8):
        for n in range(2, 8):
            pairs, edges = graph(m,n)
            sets=structural_sets(m,n)
            for S in sets:
                if any(edges[x] & S for x in S):
                    raise AssertionError(('not independent',m,n))
                if any((y not in S and not (edges[y] & S)) for y in pairs):
                    raise AssertionError(('not dominating',m,n))
            if Counter(map(len,sets)) != polynomial(m,n):
                raise AssertionError(('formula',m,n))
            expected=1+(2**m-m-1)*(2**n-n-1)
            if len(sets)!=expected:
                raise AssertionError(('total',m,n,len(sets),expected))
    for m in range(2, 8):
        for n in range(m, 10):
            coeff=polynomial(m,n)
            predicted = 2 if (m,n)==(2,2) else (2*n-3 if m==2 else comb(m,2)+n-m)
            if min(coeff)!=predicted:
                raise AssertionError(('independent domination minimum',m,n))
            if (m,n)==(2,2): count=1
            elif m==2: count=comb(n,2)+(comb(n,3) if n>=4 else 0)
            elif n>m: count=m*comb(n,2)
            else:
                count=m*comb(m,2)+sum(comb(m,r)*(comb(m,r)+comb(m,r+1)) for r in range(2,m-1))
            if coeff[predicted]!=count:
                raise AssertionError(('minimum counts',m,n,coeff[predicted],count))
    print('FORMULA_AND_DOMINATION_OK m,n=2..7')
    print('INDEPENDENT_DOMINATION_AND_MINIMUM_COUNTS_OK 2<=m<=7, m<=n<10')
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
