#!/usr/bin/env python3
"""Reproduce small Catalan/connected-type counts and a component-swap witness.
The asymptotic limit is proved in the accompanying manuscript, not by these checks.
"""
from itertools import permutations
from math import comb, ceil, log


def intervals(n):
    return [(i, i+d) for d in range(n) for i in range(n-d)]


def ideals(n):
    arr=intervals(n); index={x:j for j,x in enumerate(arr)}
    pred={index[(i,j)]: (index[(i+1,j)], index[(i,j-1)]) for i,j in arr if i<j}
    def rec(pos, chosen):
        if pos==len(arr):
            yield frozenset(arr[i] for i in chosen)
        else:
            yield from rec(pos+1, chosen)
            if pos not in pred or all(p in chosen for p in pred[pos]):
                yield from rec(pos+1, chosen | {pos})
    yield from rec(0, set())


def connected(fullbottom_ideal, n):
    adj={i: set() for i in range(n)}
    for i,j in fullbottom_ideal:
        if i!=j: adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen: seen.add(j); stack.append(j)
    return len(seen)==n


def canonical_edges(st, n):
    edges=frozenset((i,j) for i,j in st if i!=j)
    reps=[]
    for p in permutations(range(n)):
        code=0
        bit=1
        for i in range(n):
            for j in range(i+1,n):
                if tuple(sorted((p[i],p[j]))) in edges: code|=bit
                bit <<=1
        reps.append(code)
    return min(reps)


def c(m):
    cat=comb(2*m-2,m-1)//m
    return (cat+comb(m-1,(m-1)//2))//2

for n in range(1,7):
    configurations=list(ideals(n))
    assert len(configurations)==comb(2*n+2,n+1)//(n+2), (n,len(configurations))
    connected_types={canonical_edges(s,n) for s in configurations if all((i,i) in s for i in range(n)) and connected(s,n)}
    assert len(connected_types)==c(n),(n,len(connected_types),c(n))
    print(f'CATALAN_AND_CONNECTED_TYPES n={n} states={len(configurations)} types={len(connected_types)} PASS')

# Each component consists of consecutive vertices 0..2 (or 3..5).
def block(edges,start):
    return {(start+i,start+i) for i in range(3)} | {(start+i,start+j) for i,j in edges}
P3={(0,1),(1,2)}; K3={(0,1),(1,2),(0,2)}
A=block(P3,0)|block(K3,3)
B=block(K3,0)|block(P3,3)
assert A!=B
assert A in set(ideals(6)) and B in set(ideals(6))
assert canonical_edges(A,6)==canonical_edges(B,6)
print('DISTINCT_EQUIVALENT_P3_K3_BLOCK_ORDERS PASS')

# Demonstrate the choice m=ceil(log_4 n+4log_4(log n)) and number of available types.
for n in [10**5,10**6,10**8,10**12,10**18]:
    m=ceil(log(n,4)+4*log(log(n),4))
    r=n//m
    assert c(m)>=r,(n,m,c(m),r)
    print(f'COMPONENT_SUPPLY n={n} m={m} r={r} c_m={c(m)} PASS')
print('VERIFY_OK')
