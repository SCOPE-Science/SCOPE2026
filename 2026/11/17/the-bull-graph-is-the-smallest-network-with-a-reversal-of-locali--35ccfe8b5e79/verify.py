#!/usr/bin/env python3
"""Exact spectral-moment identity checks for minimal localized consensus reversal.

Each claimed exponential formula is certified by characteristic roots and the
first m moments, with m distinct eigenvalues (an invertible Vandermonde system).
Requires SymPy, NetworkX, and mpmath. The time-global sign argument is in RESULT.md.
"""
import itertools
import networkx as nx
import sympy as sp
import mpmath as mp
R=sp.Rational

def Lmatrix(G):
    L=sp.zeros(len(G))
    for u,v in G.edges():
        L[u,u]+=1; L[v,v]+=1; L[u,v]-=1; L[v,u]-=1
    return L

def spectral_moment_check(L,v,w,terms):
    vals=list(L.eigenvals())
    assert all(lam in vals for lam in terms)
    powers=sp.eye(L.rows)
    for k in range(len(vals)):
        measured=powers[v,v]-powers[w,w]
        predicted=sum(c*lam**k for lam,c in terms.items())
        assert sp.simplify(predicted-measured)==0, (k,measured,predicted)
        powers=powers*L

def label(G):
    n=len(G);d=sorted(dict(G.degree()).values())
    return {(3,(1,1,2)):'P3',(4,(1,1,1,3)):'star',
            (4,(1,1,2,2)):'P4',(4,(1,2,2,3)):'paw',
            (4,(2,2,3,3)):'diamond'}.get((n,tuple(d)))

root2=sp.sqrt(2)
checks={
 ('P3',1,2):{sp.Integer(1):R(1,2),sp.Integer(3):-R(1,2)},
 ('star',1,3):{sp.Integer(1):R(2,3),sp.Integer(4):-R(2,3)},
 ('P4',1,2):{2-root2:root2/4,2+root2:-root2/4},
 ('paw',1,2):{sp.Integer(1):R(1,2),sp.Integer(3):-R(1,2)},
 ('paw',1,3):{sp.Integer(1):R(2,3),sp.Integer(4):-R(2,3)},
 ('paw',2,3):{sp.Integer(1):R(1,6),sp.Integer(3):R(1,2),sp.Integer(4):-R(2,3)},
 ('diamond',2,3):{sp.Integer(2):R(1,2),sp.Integer(4):-R(1,2)}
}
graphs=[G for G in nx.graph_atlas_g() if 1<=len(G)<=4 and nx.is_connected(G)]
assert len(graphs)==10
seen=set(); equal_checked=0
for G in graphs:
    d=dict(G.degree());L=Lmatrix(G)
    for v,w in itertools.combinations(G.nodes(),2):
        if d[v]==d[w]:
            spectral_moment_check(L,v,w,{})
            equal_checked+=1
    for lo,hi in itertools.combinations(sorted(set(d.values())),2):
        key=(label(G),lo,hi)
        assert key in checks,key
        v=next(v for v in G if d[v]==lo)
        w=next(w for w in G if d[w]==hi)
        spectral_moment_check(L,v,w,checks[key]);seen.add(key)
assert seen==set(checks)

G=nx.Graph();G.add_nodes_from(range(5));G.add_edges_from([(0,1),(1,2),(2,0),(0,3),(2,4)])
L=Lmatrix(G)
s13=sp.sqrt(13);s5=sp.sqrt(5)
a=(5-s13)/2;b=(5-s5)/2;c=(5+s5)/2;d=(5+s13)/2
A=(13-3*s13)/52;B=(5+s5)/20;C=(5-s5)/20;D=(13+3*s13)/52
bull={a:A,b:-B,c:-C,d:D}
spectral_moment_check(L,0,1,bull)
assert all(sp.N(t)>0 for t in [A,B,C,D])
assert sp.simplify(sum(bull.values()))==0
assert sp.simplify(sum(-lam*val for lam,val in bull.items()))==-1

mp.mp.dps=55
F=lambda s: (mp.mpf(13)-3*mp.sqrt(13))/52*mp.exp(-(5-mp.sqrt(13))*s/2) - (5+mp.sqrt(5))/20*mp.exp(-(5-mp.sqrt(5))*s/2) - (5-mp.sqrt(5))/20*mp.exp(-(5+mp.sqrt(5))*s/2) + (13+3*mp.sqrt(13))/52*mp.exp(-(5+mp.sqrt(13))*s/2)
s=mp.findroot(F,(mp.mpf('3.0'),mp.mpf('3.4')))
assert mp.mpf('3.14')<s<mp.mpf('3.15')
assert F(s/2)<0 and F(2*s)>0
print('VERIFY_OK connected_graph_types=10 distinct_degree_formulas=7 equal_degree_pairs='+str(equal_checked)+' exact_bull_modes=5')
print('HEAT_TIME_ROOT',mp.nstr(s,40))
print('CONSENSUS_TIME_ROOT',mp.nstr(s/2,40))
print('NOTE spectral-moment identities exact; all-time uniqueness proof is analytical')
