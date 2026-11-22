#!/usr/bin/env python3
"""Integer checks for the row-reflection formula on 3-by-even-grid perfect-matching complexes.
This self-contained script uses only the Python standard library.
"""
from collections import defaultdict, deque
from functools import lru_cache

def compatible(p, q):
    return (p & q) == 0 and (7 ^ (p | q)) in (0, 3, 6)

# Symbols: no prescribed boundary edges, a top/bottom horizontal pair,
# a middle-row horizontal edge, or all three horizontal edges.
alphabet = ((0, 1), (5, -1), (2, -1), (7, 1))
expected_states = ((0,), (1, 4, 7), (7,), (0, 3, 6), (), (3, 6), (1, 4))
expected_A = (
    (0, 1, -1, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, -1, 0),
    (1, 0, 0, 0, -1, 0, 0),
    (0, 1, -1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, -1, 0, 1),
    (0, 0, 0, 1, 0, -1, 0),
)
expected_b = (0, 1, 1, 0, 0, 0, 1)

def automaton():
    start = frozenset((0,))
    states = [start]
    index = {start: 0}
    todo = deque((start,))
    transitions = []
    while todo:
        S = todo.popleft()
        row = []
        for forced, weight in alphabet:
            T = frozenset(q for p in S for q in range(8)
                          if (q & forced) == forced and compatible(p, q))
            if T not in index:
                index[T] = len(states)
                states.append(T)
                todo.append(T)
            row.append((index[T], weight))
        transitions.append(row)
    a = [[0] * len(states) for _ in states]
    for i, row in enumerate(transitions):
        for j, weight in row:
            a[i][j] += weight
    b = [int(any(compatible(p, 0) for p in S)) for S in states]
    return tuple(tuple(sorted(s)) for s in states), tuple(tuple(r) for r in a), tuple(b)

def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)

def machine_q(n, A, b):
    v = b
    for _ in range(2*n - 1):
        v = mv(A, v)
    return v[0]

def brute_tilings(n):
    L = 2*n
    N = 3*L
    edges = []
    for row in range(3):
        for col in range(L):
            if row < 2: edges.append((row*L+col, (row+1)*L+col))
            if col+1 < L: edges.append((row*L+col, row*L+col+1))
    edge_id = {e:i for i,e in enumerate(edges)}
    adj = [[] for _ in range(N)]
    for i,(u,v) in enumerate(edges):
        adj[u].append((v,i));adj[v].append((u,i))
    @lru_cache(None)
    def rec(used):
        if used==(1<<N)-1:return ((),)
        u=next(i for i in range(N) if not(used>>i&1))
        return tuple((e,)+t for v,e in adj[u] if not(used>>v&1)
                     for t in rec(used|(1<<u)|(1<<v)))
    return rec(0),edges,edge_id

def direct_q(n):
    tilings, edges, edge_id = brute_tilings(n)
    L=2*n
    def flip(v):return (2-v//L)*L + v%L
    pairs=[]; seen=set()
    for i,(u,v) in enumerate(edges):
        if i in seen:continue
        j=edge_id[tuple(sorted((flip(u),flip(v))))]
        seen.update((i,j))
        if i==j or set(edges[i]).isdisjoint(edges[j]):
            pairs.append(frozenset((i,j)))
    faces = {0}
    for t in tilings:
        tt=set(t)
        allowable=[i for i,o in enumerate(pairs) if o<=tt]
        for mask in range(1<<len(allowable)):
            faces.add(sum(1<<i for k,i in enumerate(allowable) if mask>>k&1))
    q=sum(-1 if x.bit_count()%2 else 1 for x in faces)
    return q,len(tilings),len(faces)

def main():
    S,A,b=automaton()
    assert S==expected_states, (S,expected_states)
    assert A==expected_A, (A,expected_A)
    assert b==expected_b, (b,expected_b)
    v=b
    assert [machine_q(n,A,b) for n in (1,2,3)] == [0,-1,1]
    for _ in range(6): v=mv(A,v)
    assert v==b, 'A^6 b != b'
    for n in range(1,101):
        q=machine_q(n,A,b)
        expect=(0 if n%3==1 else -1 if n%3==2 else 1)
        assert q==expect,(n,q,expect)
    data=[]
    for n in range(1,9):
        direct,t,f=direct_q(n)
        assert direct==machine_q(n,A,b),(n,direct,machine_q(n,A,b))
        data.append((n,direct,t,f))
    print('AUTOMATON_SEVEN_STATES_AND_EXACT_A6B_IDENTITY_OK')
    print('DIRECT_DOMINO_TILING_ORBIT_CHECKS_OK')
    for n,q,t,f in data:
        print('n=%d signed_orbit_face_sum=%d perfect_tilings=%d invariant_faces=%d'%(n,q,t,f))
    print('ROW_REFLECTION_CHARACTER_AND_QUOTIENT_RANK_FORMULA_OK')

if __name__=='__main__':main()
