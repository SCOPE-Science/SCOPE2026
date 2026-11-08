#!/usr/bin/env python3
"""Exact reproducibility checks for stationary states of the three-color cyclic automaton.

Requirements: Python 3.10+ and SymPy (tested with SymPy 1.13+).
Run: python verify_strip.py
No external data files or network access.
"""
from collections import deque
from itertools import product
from math import factorial
import sympy as sp

X = sp.Symbol('X')
P_COEFF = [1,-18,121,-528,2397,-9207,21654,-54108,232146,-476280,-302535,1574640,1686177,728271,-39149487,77944680,-36137988,-25509168,19131876]
Q_COEFF = [1,3,13,-132,-717,-4320,-7695,-1134,134946,454653,898128,-164025,-3726648,-11081529,-11868849,-13463172,11691702,12754584,19131876]
P=sp.Poly.from_list(P_COEFF,gens=X)
Q=sp.Poly.from_list(Q_COEFF,gens=X)
assert P.degree()==Q.degree()==18

# Column count types, not ordered columns: ten compositions of three.
C=list(t for t in product(range(4),repeat=3) if sum(t)==3)
assert len(C)==10
W=[factorial(3)//(factorial(t[0])*factorial(t[1])*factorial(t[2])) for t in C]
assert sum(W)==27
nodes=list(product(range(10),repeat=2))
ix={v:k for k,v in enumerate(nodes)}
edges=[]
B=sp.zeros(100)
for a,b in nodes:
    for c in range(10):
        # A site of middle-column color i sees all three sites of
        # each adjacent column, plus the other two middle sites.
        if all(C[a][(i+1)%3]+C[b][(i+1)%3]+C[c][(i+1)%3]<=3
               for i in range(3) if C[b][i]):
            u=ix[(a,b)];v=ix[(b,c)]
            edges.append((u,v,W[c]))
            B[u,v]=W[c]
assert len(edges)==496

# Strongly connected components, with separate in/out reachability.
g=[[] for _ in nodes];rg=[[] for _ in nodes]
for u,v,_ in edges:
    g[u].append(v);rg[v].append(u)
def visit(s,graph,allowed):
    stack=[s];seen={s}
    while stack:
        for v in graph[stack.pop()]:
            if v in allowed and v not in seen:
                seen.add(v);stack.append(v)
    return seen
unseen=set(range(100));scc=[]
while unseen:
    u=next(iter(unseen));f=visit(u,g,unseen);b=visit(u,rg,unseen)
    # This intersection need not be complete SCC if a component is only
    # partially found by a naive intersection; it is complete here via
    # mutual reachability of the seed and every member.
    comp=f & b
    scc.append(comp)
    unseen-=comp
recurrent=[c for c in scc if len(c)>1 or any(u in g[u] for u in c)]
assert sorted([len(c) for c in recurrent])==[1,72]
main=next(c for c in recurrent if len(c)==72)
other=next(c for c in recurrent if len(c)==1)
assert all(u in visit(min(main),g,main) for u in main)
assert all(u in visit(min(main),rg,main) for u in main)
assert any(u in g[u] for u in main)  # a positive loop forces period one
assert B[next(iter(other)),next(iter(other))]==6

# All-100-state characteristic polynomial. Exactly reproduce the
# 18+18+18 spectral decomposition and the 45 zero eigenvalues.
expected=(sp.Poly(X**45*(X-6),X)*P*(Q**2))
actual=B.charpoly(X).as_poly(X)
assert actual==expected

# Spatial fixed-point counts as closed-walk weights.
expected_counts={3:2070,4:9636,5:67263,6:548688,7:4246827,8:35421972,
                 9:292865328,10:2430735969}
for n in range(1,11):
    # All diagonal entries of B**n by sparse path recursion.
    total=0
    for start in range(100):
        row={start:1}
        for _ in range(n):
            nxt={}
            for u,v,w in edges:
                if u in row:
                    nxt[v]=nxt.get(v,0)+row[u]*w
            row=nxt
        total+=row.get(start,0)
    if n in expected_counts:assert total==expected_counts[n],(n,total)

# Direct, independent, ordered-color enumeration for genuine Moore tori.
for n,expected_n in ((3,2070),(4,9636)):
    num=0
    for flat in product(range(3),repeat=3*n):
        fixed=True
        for i in range(3):
            if not fixed:break
            for j in range(n):
                c=flat[i*n+j]
                predator=(c+1)%3
                count=sum(flat[((i+di)%3)*n+(j+dj)%n]==predator
                          for di in (-1,0,1) for dj in (-1,0,1)
                          if di or dj)
                if count>=4:
                    fixed=False;break
        num+=fixed
    assert num==expected_n,(n,num)

# Sturm/root sign checks of the largest Perron root enclosure.
lo=sp.Rational(86245,10000);hi=sp.Rational(86246,10000)
assert P.eval(lo)<0<P.eval(hi)
assert P.count_roots(8,sp.oo)==1
assert P.count_roots(lo,hi)==1
print('VERIFY_OK compositions=10 weighted_edges=496 recurrent_scc=72+1')
print('VERIFY_OK charpoly=X^45*(X-6)*P18*Q18^2')
print('VERIFY_OK ring_F3=2070 ring_F4=9636 n_to_10_counts=verified')
print('VERIFY_OK Perron_root_interval=(8.6245,8.6246)')
