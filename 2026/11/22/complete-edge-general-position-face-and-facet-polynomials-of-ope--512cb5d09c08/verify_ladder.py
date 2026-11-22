#!/usr/bin/env python3
"""Independent shortest-path and enumerator checks for two-rail ladders."""
from collections import Counter, deque
from itertools import combinations
from math import comb


def edges(n):
    # edge IDs: upper horizontal 0..n-2, lower horizontal n-1..2n-3, rungs 2n-2..3n-3
    return ([(i, i + 1) for i in range(n - 1)]
            + [(n + i, n + i + 1) for i in range(n - 1)]
            + [(i, n + i) for i in range(n)])


def path_triples(n):
    E = edges(n)
    adj = [[] for _ in range(2 * n)]
    for i, (u, v) in enumerate(E):
        adj[u].append((v, i))
        adj[v].append((u, i))
    triples = set()
    for source in range(2 * n):
        distance = [None] * (2 * n)
        distance[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, _ in adj[u]:
                if distance[v] is None:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        def search(u, path):
            for v, edge_id in adj[u]:
                if distance[v] == distance[u] + 1:
                    next_path = (*path, edge_id)
                    for triple in combinations(next_path, 3):
                        triples.add(sum(1 << k for k in triple))
                    search(v, next_path)
        search(source, ())
    return triples


def table_triples(n):
    m = n - 1
    triples = set()
    def add(*ids):
        triples.add(sum(1 << t for t in ids))
    # Three horizontal edges on one rail.
    for offset in (0, m):
        for a, b, c in combinations(range(m), 3):
            add(offset + a, offset + b, offset + c)
    # Two horizontal edges on one rail, one on the opposite rail or one rung.
    for offset, other in ((0, m), (m, 0)):
        for a, c in combinations(range(m), 2):
            for b in range(m):
                if b < a or b > c:
                    add(offset + a, offset + c, other + b)
            for r in range(n):
                if not (a + 1 <= r <= c):
                    add(offset + a, offset + c, 2*m + r)
    # One horizontal on each rail, plus one rung.
    for a in range(m):
        for b in range(m):
            for r in range(min(a,b)+1, max(a,b)+1):
                add(a, m+b, 2*m+r)
    return triples


def from_polynomial(n):
    m = n - 1
    # Compute coefficient arrays by integer arithmetic only.
    face = Counter()
    for k in range(n+1):
        face[k] += comb(n,k)
        face[k+1] += 2*m*comb(n,k)
        face[k+2] += m*comb(n,k)
    for exponent in range(1,n):
        for k in range(exponent+1):
            face[k+2] += 2*(n-2)*comb(exponent,k)
    face[3] += m*(m-1)*(n+3)//3
    face[4] += comb(m,2)
    facet = Counter({n+2:m})
    for k in range(3,n+2):
        facet[k] += 2*(n-2)
    if m >= 3:
        facet[3] += 2*comb(m,3)
    if m >= 2:
        facet[4] += comb(m,2)
    return (+face if hasattr(face, '__pos__') else face),facet


def structural_counts(n):
    m = n-1
    horizontal = [()] + [(i,) for i in range(m)] + list(combinations(range(m),2))
    def allowable(A,B):
        if len(A)==2 and any(b<A[0] or b>A[1] for b in B):return None
        if len(B)==2 and any(a<B[0] or a>B[1] for a in A):return None
        R=set(range(n))
        if len(A)==2:R.intersection_update(range(A[0]+1,A[1]+1))
        if len(B)==2:R.intersection_update(range(B[0]+1,B[1]+1))
        for a in A:
            for b in B:
                R.difference_update(range(min(a,b)+1,max(a,b)+1))
        return R
    face=Counter()
    facet=Counter()
    for A in horizontal:
        for B in horizontal:
            R=allowable(A,B)
            if R is None:continue
            for k in range(len(R)+1):
                face[len(A)+len(B)+k] += comb(len(R),k)
            maximal=True
            for row in (0,1):
                for h in range(m):
                    H=A if row==0 else B
                    if h in H or len(H)==2:continue
                    AA=tuple(sorted((*A,h))) if row==0 else A
                    BB=tuple(sorted((*B,h))) if row==1 else B
                    newer=allowable(AA,BB)
                    if newer is not None and R.issubset(newer):
                        maximal=False
            if maximal:
                facet[len(A)+len(B)+len(R)]+=1
    return face,facet


def exhaustive_counts(n, triples):
    edge_count=3*n-2
    forbidden=list(triples)
    admissible=bytearray(1<<edge_count)
    face=Counter()
    for mask in range(len(admissible)):
        yes=all((mask&t)!=t for t in forbidden)
        if yes:
            admissible[mask]=1
            face[mask.bit_count()] += 1
    facet=Counter()
    for mask,good in enumerate(admissible):
        if good and all(not admissible[mask|(1<<i)] for i in range(edge_count) if not mask>>i&1):
            facet[mask.bit_count()]+=1
    return face,facet


def tidy(x):return {k:v for k,v in x.items() if v}

def run():
    for n in range(2,8):
        t1=path_triples(n)
        t2=table_triples(n)
        assert t1==t2, ('geodesic-table',n,t1^t2)
        expected=from_polynomial(n)
        structural=structural_counts(n)
        brute=exhaustive_counts(n,t1)
        assert (tidy(expected[0]),tidy(expected[1])) == (tidy(structural[0]),tidy(structural[1]))
        assert (tidy(expected[0]),tidy(expected[1])) == (tidy(brute[0]),tidy(brute[1]))
        print('n=',n,'triples=',len(t1),'faces=',sum(brute[0].values()),'facets=',sum(brute[1].values()),'maximum=',max(brute[0]),'max_count=',brute[0][max(brute[0])])
    for n in range(8,41):
        assert all(tidy(a)==tidy(b) for a,b in zip(structural_counts(n),from_polynomial(n))),n
    print('VERIFY_OK')

if __name__=='__main__':run()
