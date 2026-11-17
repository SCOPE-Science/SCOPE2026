#!/usr/bin/env python3
"""Exact spatial transfer and Perron certificate for three-step Wireworld returns."""
import json
import networkx as nx
import sympy as sp
from pathlib import Path

B=25

def unpack(i):
    return divmod(i,5)

def is_head(symbol,t):
    return symbol>=2 and symbol-2==t

def admissible(a,b,c):
    L,M,R=unpack(a),unpack(b),unpack(c)
    for row in range(2):
        state=M[row]
        for t in range(3):
            # Eight Moore incidences: each diagonal in the opposite row
            # is counted twice on the two-row periodic quotient.
            heads=(int(is_head(L[row],t))+int(is_head(R[row],t))+
                   2*int(is_head(L[1-row],t))+2*int(is_head(R[1-row],t))+
                   2*int(is_head(M[1-row],t)))
            if state==1 and heads in (1,2):
                return False
            if state>=2 and t==(state-2+2)%3 and heads not in (1,2):
                return False
    return True

edges=[]
for a in range(B):
    for b in range(B):
        for c in range(B):
            if admissible(a,b,c):
                edges.append((a*B+b,b*B+c))
G=nx.DiGraph()
G.add_nodes_from(range(B*B))
G.add_edges_from(edges)
comps=[part for part in nx.strongly_connected_components(G)
       if len(part)>1 or G.has_edge(next(iter(part)),next(iter(part)))]
assert len(comps)==1
nodes=sorted(comps[0]); assert len(nodes)==283
lookup={v:i for i,v in enumerate(nodes)}
E=[(lookup[u],lookup[v]) for u,v in edges if u in lookup and v in lookup]
assert len(edges)==4090 and len(E)==1816
A=sp.zeros(len(nodes))
for u,v in E:
    A[u,v]+=1
x=sp.symbols('x')
p8=x**8-x**6+3*x**4-3*x**2+3
q8=x**8+2*x**6+3*x**4+6*x**2+3
r10=x**10+2*x**9+5*x**8+12*x**7+29*x**6-8*x**5-41*x**4+122*x**3+153*x**2-30*x-36
s11=x**11-8*x**10+18*x**9-62*x**8+47*x**7+116*x**6+126*x**5+280*x**4-77*x**3-648*x**2+12*x+144
expected=x**228*p8**2*q8*r10**2*s11
assert A.charpoly(x).as_expr().expand()==sp.expand(expected)

cert=json.loads((Path(__file__).parent/'spectral_certificate.json').read_text())
assert cert['scc_nodes']==nodes
w=cert['integer_vector'];assert len(w)==283 and min(w)>0
U=[0]*len(nodes)
for u,v in E:
    U[u]+=w[v]
assert all(644175*w[i] < 100000*U[i] < 644176*w[i] for i in range(len(nodes)))

def power_sum(poly,N):
    cs=[int(i) for i in sp.Poly(poly,x).all_coeffs()]
    d=len(cs)-1; a=[d]
    for n in range(1,N+1):
        kmax=min(n-1,d)
        t=sum(cs[k]*a[n-k] for k in range(1,kmax+1))
        if n<=d: t+=n*cs[n]
        a.append(-t)
    return a

N=12
ps=[power_sum(p,N) for p in (p8,q8,r10,s11)]
print('columns=25 pair_states=625 legal_edges=4090 cyclic_states=283 cyclic_edges=1816')
print('charpoly=x^228*(p8)^2*q8*(r10)^2*s11 [exact identity]')
print('Perron bounds: 6.44175 < lambda < 6.44176')
for n in range(3,N+1):
    F3=2*ps[0][n]+ps[1][n]+2*ps[2][n]+ps[3][n]
    fixed=4**n
    assert (F3-fixed)%3==0 and F3>=fixed
    print(f'n={n} fixed={fixed} third_return={F3} primitive_three_orbits={(F3-fixed)//3}')
