#!/usr/bin/env python3
"""Exact period-three transfer certificate for Brian's Brain on three-row tori.
Run: python verify_transfer.py (requires SymPy 1.10+; standard Python otherwise).
Perron bounds use integer arithmetic and the adjacent perron_vector.txt file.
"""
import sys
from pathlib import Path
from collections import Counter
import sympy as sp

# A four-symbol local history: 0,1,2 mean rotating temporal states;
# 3 means always quiescent. Each width-three vertical column has 4^3 symbols.
col = [[(s >> (2*r)) & 3 for r in range(3)] for s in range(64)]
excited = [[sum(1 << r for r, a in enumerate(col[s]) if a != 3 and
                (a+t) % 3 == 1) for t in range(3)] for s in range(64)]

def triple_ok(left, centre, right):
    for t in range(3):
        L, M, R = excited[left][t], excited[centre][t], excited[right][t]
        outside = L.bit_count() + R.bit_count()
        for r, c in enumerate(col[centre]):
            if c == 3 or (c+t) % 3 == 0:
                neighbours = outside + M.bit_count() - ((M >> r) & 1)
                if (neighbours == 2) != (c != 3):
                    return False
    return True

N = 4096
edges = [[] for _ in range(N)]
reverse = [[] for _ in range(N)]
for a in range(64):
    for b in range(64):
        v = 64*a+b
        for c in range(64):
            if triple_ok(a,b,c):
                w = 64*b+c
                edges[v].append(w)
                reverse[w].append(v)
edge_count = sum(map(len, edges))
active_nodes = sum(bool(edges[i] or reverse[i]) for i in range(N))
assert edge_count == 12286 and active_nodes == 2125, (edge_count, active_nodes)

sys.setrecursionlimit(100000)
visited = [False] * N
order = []
def visit(v):
    visited[v] = True
    for w in edges[v]:
        if not visited[w]: visit(w)
    order.append(v)
for v in range(N):
    if not visited[v]: visit(v)

visited = [False]*N
components = []
def reverse_visit(v, part):
    visited[v] = True
    part.append(v)
    for w in reverse[v]:
        if not visited[w]:reverse_visit(w, part)
for v in reversed(order):
    if not visited[v]:
        part = []
        reverse_visit(v, part)
        if len(part)>1 or v in edges[v]: components.append(part)
assert len(components)==1, [(len(p),p[:5]) for p in components]
nodes = sorted(components[0]); size = len(nodes)
index = {v:i for i,v in enumerate(nodes)}
A = [[] for _ in nodes]
for node in nodes:
    A[index[node]] = [index[w] for w in edges[node] if w in index]
internal_edges = sum(map(len,A))
assert (size,internal_edges)==(184,559), (size,internal_edges)

x=sp.Symbol('x')
Q=x**8+18*x**5+9*x**4+81*x**2+81*x+81
R=(x**12-x**11-36*x**9-18*x**8+18*x**7+324*x**6+1053*x**5+
   405*x**4-81*x**3-11664*x**2-11664*x-2916)
M=sp.MutableSparseMatrix(size,size,{(i,j):1 for i,row in enumerate(A) for j in row})
calculated=M.charpoly(x).as_expr()
assert sp.Poly(calculated-x**156*Q**2*R,x).is_zero

# Count spatially labelled closed walks directly rather than using the charpoly.
traces = [0]*13
for seed in range(size):
    layer = {seed:1}
    for n in range(1,13):
        nxt = {}
        for v,z in layer.items():
            for w in A[v]: nxt[w] = nxt.get(w,0)+z
        layer=nxt
        traces[n]+=layer.get(seed,0)
assert traces[1:13]==[1,1,1,145,181,3133,5356,7417,40420,153451,320266,1322353]

# A fully integer-valued Collatz--Wielandt certificate, in sorted SCC order.
vec=[int(t) for t in (Path(__file__).parent/'perron_vector.txt').read_text().split()]
assert len(vec)==size and min(vec)>0
low_num,high_num=326505918,326505920 # 3.26505918 and 3.26505920 * 10^8
for i,row in enumerate(A):
    lhs=sum(vec[j] for j in row)*100000000
    assert low_num*vec[i]<lhs<high_num*vec[i], (i,lhs,vec[i])
# SCC is irreducible and contains a loop, hence the Perron eigenvalue is simple
# and strictly dominates the other eigenvalues in modulus.
assert any(i in A[i] for i in range(size))
print('TOTAL_STATE_PAIRS=4096 GRAPH_EDGES=12286 ACTIVE_VERTICES=2125')
print('CYCLIC_SCC_VERTICES=184 EDGES=559')
print('CHARPOLY=x^156 Q(x)^2 R(x) [Q degree 8; R degree 12]')
print('PERRON_RHO_BOUNDS=3.26505918<rho<3.26505920')
for n in range(3,13):
    print(f'n={n} fixed_F3={traces[n]} primitive3_orbits={(traces[n]-1)//3}')
print('ALL_CHECKS_PASS')
