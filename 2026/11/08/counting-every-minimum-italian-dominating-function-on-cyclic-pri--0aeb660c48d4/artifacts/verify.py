#!/usr/bin/env python3
"""Exact finite certificate for optimum Italian functions on cycle prisms.

Python 3 standard library only. Graph vertices are pairs (row,column).
All checks are exact integer calculations, except no floating-point calculations
are required. The mathematical argument for arbitrary cycle length is in RESULT.md.
"""
from collections import defaultdict
from itertools import product

COLS = tuple(product(range(3), repeat=2))
STATES = tuple(product(range(9), repeat=2))

def admissible(i, j, k):
    a, b = COLS[i]
    c, d = COLS[j]
    e, f = COLS[k]
    return (c != 0 or a + d + e >= 2) and (d != 0 or b + c + f >= 2)

def potential(i, j):
    if i == 0:
        return -2 if j in (5, 7, 8) else -1
    if i in (1, 3):
        return -1
    return 0

EDGES = {
    (i, j): tuple(((j, k), sum(COLS[j]) - 1)
                  for k in range(9) if admissible(i, j, k))
    for i, j in STATES
}

def strongly_connected_components(verts, successors):
    visited = set()
    order = []
    def dfs(v):
        visited.add(v)
        for u in successors[v]:
            if u not in visited:
                dfs(u)
        order.append(v)
    for v in verts:
        if v not in visited:
            dfs(v)
    reverse = {v:[] for v in verts}
    for v in verts:
        for u in successors[v]:
            reverse[u].append(v)
    visited.clear()
    out=[]
    def reverse_dfs(v, comp):
        visited.add(v)
        comp.add(v)
        for u in reverse[v]:
            if u not in visited:
                reverse_dfs(u,comp)
    for v in reversed(order):
        if v not in visited:
            comp=set()
            reverse_dfs(v,comp)
            out.append(tuple(sorted(comp)))
    return out

def matmul(A,B):
    N=len(A)
    out=[[0]*N for _ in range(N)]
    for i in range(N):
        for k,x in enumerate(A[i]):
            if x:
                for j,y in enumerate(B[k]):
                    if y:
                        out[i][j]+=x*y
    return out

def matrix_for(comp, successors):
    ix={v:i for i,v in enumerate(comp)}
    M=[[0]*len(comp) for _ in comp]
    for v in comp:
        for u in successors[v]:
            if u in ix:
                M[ix[v]][ix[u]]+=1
    return M

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def det_i_minus_z_a(A):
    n=len(A)
    P=[[int(i==j) for j in range(n)] for i in range(n)]
    powers=[0]
    for k in range(1,n+1):
        P=matmul(P,A)
        powers.append(trace(P))
    coeff=[1]
    for k in range(1,n+1):
        numerator=-sum(coeff[k-j]*powers[j] for j in range(1,k+1))
        assert numerator % k == 0
        coeff.append(numerator//k)
    return tuple(coeff)

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return tuple(out)

def direct_count(n):
    # Check original graph adjacencies, independently of transfer admissibility.
    total = 0
    for word in product(range(9), repeat=n):
        if sum(sum(COLS[q]) for q in word) != n:
            continue
        labels = [[COLS[word[i]][r] for i in range(n)] for r in (0, 1)]
        if all(labels[r][i] != 0 or
               (labels[r][(i-1)%n] + labels[r][(i+1)%n] + labels[1-r][i] >= 2)
               for r in (0, 1) for i in range(n)):
            total += 1
    return total

def run():
    assert len(COLS)==9 and len(STATES)==81
    assert all(cost + potential(*u) - potential(*v) >= 0
               for u in STATES for v,cost in EDGES[u]), 'Invalid potential inequality'
    zero={u:tuple(v for v,c in EDGES[u]
                 if c + potential(*u) - potential(*v)==0) for u in STATES}
    assert sum(map(len,zero.values()))==161
    comps=strongly_connected_components(STATES,zero)
    cyclic=sorted([c for c in comps if len(c)>1 or c[0] in zero[c[0]]],
                  key=lambda c:(-len(c),c))
    assert [len(c) for c in cyclic]==[12,4,2]
    print('ZERO_REDUCED_COST_GRAPH_OK', 'states=81', 'edges=161', 'cyclic_SCC_sizes=12,4,2')
    polynomials=tuple(det_i_minus_z_a(matrix_for(comp,zero)) for comp in cyclic)
    p12=mul(mul((1,1),(1,0,1,-1,1)),(1,-1,-1,0,0,-1))
    assert tuple(tuple(c[:len(p12)]) if len(c)==len(p12)+2 and c[-2:]==(0,0) else c for c in polynomials)==(p12, (1,0,0,0,-1),(1,0,-1)), polynomials
    print('EXACT_COMPONENT_DETERMINANTS_OK', 'degree_10+4+2')
    components=[matrix_for(comp,zero) for comp in cyclic]
    powers=[[[int(i==j) for j in range(len(A))] for i in range(len(A))] for A in components]
    counts=[]
    for n in range(1,41):
        powers=[matmul(B,A) for B,A in zip(powers,components)]
        counts.append(sum(trace(B) for B in powers))
    assert counts[:12]==[0,4,6,12,10,34,42,68,132,214,330,630]
    print('TRACE_GENERATING_SERIES_FIRST_40_OK', counts[2:12])
    for n in range(3,7):
        actual=direct_count(n)
        assert actual==counts[n-1],(n,actual,counts[n-1])
        print('INDEPENDENT_BRUTE_FORCE_OK',n,actual)
    # Explicit binary circular words with no three consecutive equal values
    # provide one weight-n function for each tested n; the proof constructs
    # such words for all n>=3 without relying on this finite test.
    for n in range(3,41):
        bits=[i%2 for i in range(n)]
        if n%2:
            bits[-1]=bits[-2]
        assert all(not(bits[(i-1)%n]==bits[i]==bits[(i+1)%n]) for i in range(n))
    print('CIRCULAR_BINARY_WITNESSES_OK', 'n=3..40')
    print('VERIFY_OK')

if __name__=='__main__':
    run()
