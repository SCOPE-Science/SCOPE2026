#!/usr/bin/env python3
"""Exact length-independent transfer determinant for the Rule 73 period-three space-time occupation statistic."""
import sympy as S
import networkx as nx
u,z=S.symbols('u z'); T=3; N=1<<T; rule=73
G=nx.DiGraph()
for a in range(N):
 for b in range(N):
  for c in range(N):
   if all(((rule>>(4*((a>>t)&1)+2*((b>>t)&1)+((c>>t)&1)))&1)==((b>>((t+1)%3))&1) for t in range(T)):
    G.add_edge(a*N+b,b*N+c)
C=[c for c in nx.strongly_connected_components(G) if len(c)>1 or any(G.has_edge(a,a) for a in c)]
V=sorted(set().union(*C));assert len(V)==19 and G.subgraph(V).number_of_edges()==32
pos={v:i for i,v in enumerate(V)}
M=S.zeros(19)
for a,b in G.subgraph(V).edges: M[pos[a],pos[b]]=u**((a%N).bit_count())
P=S.factor((S.eye(19)-z*M).det(method='domain-ge'))
Q=(1+u**5*z**4+u**6*z**5)**2*(1-u**6*z**3-u**6*z**4-2*u**5*z**4-2*u**6*z**5-u**11*z**7+(2*u**11-u**12)*z**8+2*u**12*z**9)
assert S.expand(P-Q)==0
# fixed orbits, tripled histories, are a subshift with 4 pair vertices
M1=S.zeros(4)
for a in range(2):
 for b in range(2):
  for c in range(2):
   aa=7*a;bb=7*b;cc=7*c
   if all(((rule>>(4*a+2*b+c))&1)==b for _ in range(1)):
    M1[2*a+b,2*b+c]=u**(3*b)
Q1=S.factor((S.eye(4)-z*M1).det())
assert S.expand(Q1-(1-u**6*z**3-u**6*z**4))==0
print('cyclic_vertices',len(V),'edges',G.subgraph(V).number_of_edges())
print('weighted_zeta_determinant',P)
print('fixed_zeta_determinant',Q1)
print('symbolic_factorization_verified',True)
