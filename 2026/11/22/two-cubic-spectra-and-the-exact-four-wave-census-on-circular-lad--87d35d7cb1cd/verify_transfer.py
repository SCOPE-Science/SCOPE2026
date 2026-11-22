#!/usr/bin/env python3
"""Exact finite transfer certificate for four-phase excitation on C_n square K_2.
Requires Python 3, networkx and sympy. All arithmetic is exact.
"""
import networkx as nx
import sympy as sp
from itertools import product

Q = 4
R = list(product(range(Q), repeat=2))
def good(a,b,c):
    return all((b[1-t] == (b[t]+1)%4 or
                a[t] == (b[t]+1)%4 or
                c[t] == (b[t]+1)%4) for t in (0,1))
G=nx.DiGraph()
G.add_nodes_from((a,b) for a in R for b in R)
for a in R:
    for b in R:
        for c in R:
            if good(a,b,c):G.add_edge((a,b),(b,c))
C=set()
shapes=[]
for group in nx.strongly_connected_components(G):
    u=next(iter(group))
    if len(group)>1 or G.has_edge(u,u):
        C.update(group)
        shapes.append((len(group),G.subgraph(group).number_of_edges()))
assert sorted(shapes)==sorted([(4,4)]*4+[(144,496)]),shapes
assert len(C)==160

def rot(r,g):return ((r[0]+g)%4,(r[1]+g)%4)
def shift(s,g):return (rot(s[0],g),rot(s[1],g))
def normal(s):return shift(s,-s[0][0])
V=sorted({normal(s) for s in C})
assert len(V)==40
I={v:i for i,v in enumerate(V)}
mult=[[[0]*4 for _ in V] for _ in V]
for v in V:
    for w in G.successors(v):
        if w in C:
            mult[I[v]][I[normal(w)]][w[0][0]]+=1

t=sp.Symbol('t')
expected={
0:t**29*(t-1)**6*(t+1)**2*(t**3-4*t**2-t-4),
2:t**29*(t-1)**2*(t+1)**6*(t**3+4*t**2+7*t-4),
1:t**28*(t**2+1)**4*(t**2-t+2)*(t**2+t+2),
3:t**28*(t**2+1)**4*(t**2-t+2)*(t**2+t+2)
}
for k in range(4):
    M=sp.Matrix(40,40,lambda i,j:sum(mult[i][j][g]*sp.I**(k*g) for g in range(4)))
    poly=M.charpoly(t).as_expr()
    assert sp.expand(poly-expected[k])==0, (k,sp.factor(poly))
print('All four 40-by-40 twisted characteristic-polynomial identities: PASS')

A=[3,4,18];B=[3,-4,2];S=[2,1]
for n in range(2,31):
    S.append(S[-1]-2*S[-2])
    A.append(4*A[-1]+A[-2]+4*A[-3])
    B.append(-4*B[-1]-7*B[-2]+4*B[-3])
def formula(n):
    return A[n]+B[n]+8*(1+(-1)**n)+16*((1,0,-1,0)[n%4])+2*(1+(-1)**n)*S[n]
# Direct transfer trace on full 256-node graph (all cyclic closed walks are included).
nodes=sorted(G.nodes()); pos={v:i for i,v in enumerate(nodes)}
outs=[[pos[w] for w in G.successors(v)] for v in nodes]
for n in range(3,13):
    trace=0
    for x in range(256):
        row={x:1}
        for _ in range(n):
            new={}
            for u,m in row.items():
                for v in outs[u]:new[v]=new.get(v,0)+m
            row=new
        trace+=row.get(x,0)
    assert trace == formula(n), (n,trace,formula(n))
    assert trace%4==0
    print(f'n={n} periodic_four_states={trace} temporal_orbits={trace//4}')
print('Unrestricted n follows from the exact finite twisted characteristic polynomials.')
