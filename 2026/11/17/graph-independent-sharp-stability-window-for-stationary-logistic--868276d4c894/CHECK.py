"""Standalone exact algebra and finite graph cross-checks for a coupled logistic map.
Run: python CHECK.py . The mathematical proof is in RESULT.md.
"""
import math
import sympy as s
import networkx as nx
import numpy as np
D=s.symbols('D')
S=1+1/(4*(4*D-1))
h2=s.factor(S*(s.Rational(3,2)-S))
Q=s.factor(16*((1-S)**2-h2))
t=s.factor(8*(1-2*D)*(1-S))
d1=s.factor(Q*(1-4*D))
assert s.factor(Q+8*(16*D**2-9*D+1)/(4*D-1)**2)==0
assert s.factor(1+t+d1-(128*D**2-64*D+5)/(4*D-1))==0
assert s.factor(1-t+d1-(8*D-3)*(16*D-3)/(4*D-1))==0
assert s.factor(1-d1+(128*D**2-76*D+9)/(4*D-1))==0
lower=(4+math.sqrt(6))/16
upper=(19+math.sqrt(73))/64
assert .4<lower<.41<.42<upper<.4375
cases=0
for n,G in [('path7',nx.path_graph(7)),('star5',nx.star_graph(5)),('cycle10',nx.cycle_graph(10)),('complete43',nx.complete_bipartite_graph(4,3))]:
    A=nx.to_numpy_array(G,nodelist=list(G.nodes()))
    P=A/A.sum(axis=1)[:,None]
    partition=nx.bipartite.color(G)
    for coupling in [.39,.41,.42,.44]:
        sum_uv=1+1/(4*(4*coupling-1))
        gap=math.sqrt(sum_uv*(1.5-sum_uv))
        X=np.array([(sum_uv+gap)/2 if partition[v]==0 else (sum_uv-gap)/2 for v in G.nodes()])
        M=(1-2*coupling)*np.eye(len(X))+2*coupling*P
        F=lambda y:4*y*(1-y)
        assert max(abs(M@F(X)-X))<1e-12
        J=M@np.diag(4*(1-2*X))
        rho=max(abs(np.linalg.eigvals(J)))
        assert (rho<1)==(lower<coupling<upper)
        cases+=1
print(f'BIPARTITE_LOGISTIC_EXACT_OK algebra=4 graph_cases={cases}')
