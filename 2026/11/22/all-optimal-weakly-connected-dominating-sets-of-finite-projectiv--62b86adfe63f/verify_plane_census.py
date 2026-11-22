#!/usr/bin/env python3
"""Independent exhaustive weak-connection test for PG(2,2) and PG(2,3).
Standard-library Python; run: python3 verify_plane_census.py
"""
from itertools import combinations
from collections import Counter


def projective_vectors(q):
    result = set()
    for x in range(q):
        for y in range(q):
            for z in range(q):
                a = (x, y, z)
                if a == (0, 0, 0):
                    continue
                leading = next(t for t in a if t != 0)
                # Here q is prime (2 or 3): modular inverse exists.
                inv = pow(leading, -1, q)
                result.add(tuple((t * inv) % q for t in a))
    return sorted(result)


def graph(q):
    vectors = projective_vectors(q)
    n = q*q+q+1
    assert len(vectors) == n
    adj = [0]*(2*n)
    for i, x in enumerate(vectors):
        for j, y in enumerate(vectors):
            if sum(a*b for a,b in zip(x,y)) % q == 0:
                adj[i] |= 1 << (n+j)
                adj[n+j] |= 1 << i
    assert all(x.bit_count() == q+1 for x in adj)
    return adj


def connected_weak_stars(adj, selected):
    size = len(adj)
    if selected == 0:
        return False
    full = (1<<size)-1
    reached = selected & -selected
    queue = [reached.bit_length()-1]
    while queue:
        v=queue.pop()
        neighbors=adj[v] if selected & (1<<v) else adj[v] & selected
        rest = neighbors & ~reached
        while rest:
            low = rest & -rest
            rest ^= low
            reached |= low
            queue.append(low.bit_length()-1)
    return reached == full


def classify(adj, selected, n):
    p = (selected & ((1<<n)-1)).bit_count()
    e = sum((adj[i]&selected).bit_count() for i in range(n) if selected & (1<<i))
    return p, 2*n - p - (2*n - selected.bit_count()), e


def expected_candidates(adj, q):
    n=q*q+q+1
    cand=set()
    for center in range(n):
        pencil=[j for j in range(n) if adj[center] & (1<<(n+j))]
        assert len(pencil)==q+1
        for omitted in pencil:
            chosen=[j for j in pencil if j!=omitted]
            lines = sum(1<<(n+j) for j in chosen)
            union=0
            for j in chosen:
                union |= adj[n+j]
            uncovered = ((1<<n)-1) & ~union
            assert uncovered.bit_count()==q
            for extra in range(n):
                if union & (1<<extra):
                    cand.add(lines|uncovered|(1<<extra))
    # Dualize points and lines, preserving the incidence representation.
    both=set(cand)
    for s in list(cand):
        both.add(((s&((1<<n)-1))<<n) | (s>>n))
    return both


def report(q):
    adj=graph(q)
    n=q*q+q+1
    target=2*q+1
    theory=expected_candidates(adj,q)
    brute=set()
    by_type=Counter()
    for picks in combinations(range(2*n),target):
        s=sum(1<<v for v in picks)
        if connected_weak_stars(adj,s):
            brute.add(s)
            p,b,e=classify(adj,s,n)
            by_type[(p,b,e)]+=1
    assert brute == theory, (len(brute),len(theory),len(brute^theory))
    assert len(brute)==2*n*(q+1)*(q*q+1)
    assert all(connected_weak_stars(adj,s) for s in theory)
    if q==2:
        assert by_type=={(3,2,1):84,(2,3,1):84,(3,2,2):21,(2,3,2):21}
        # Full lower-cardinality search for the smaller incidence graph.
        assert all(not connected_weak_stars(adj,sum(1<<i for i in C))
                   for k in range(target) for C in combinations(range(2*n),k))
    elif q==3:
        assert by_type=={(4,3,1):468,(3,4,1):468,(4,3,3):52,(3,4,3):52}
        # Degree-count bound proves impossibility below target for all q.
    print(f"q={q} points={n} minimum_size={target} minimum_sets={len(brute)} types={sorted(by_type.items())} OK")

if __name__=='__main__':
    report(2)
    report(3)
