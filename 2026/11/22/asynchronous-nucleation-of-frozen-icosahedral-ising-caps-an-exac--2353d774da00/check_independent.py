"""Independent finite-state verification with a separately sourced graph and iterative energy-order recursion.
Requires NetworkX; no data files.
"""
from collections import Counter
from fractions import Fraction
from math import comb
import networkx as nx
H=nx.icosahedral_graph()
assert len(H)==12 and H.number_of_edges()==30 and set(dict(H.degree()).values())=={5}
vertices=sorted(H.nodes())
neighbors={v:tuple(H.neighbors(v)) for v in vertices}
CAP=set(frozenset((v,*neighbors[v])) for v in vertices)
assert len(CAP)==12

# Represent a spin state as an immutable set of positive vertices, rather than bit masks.
states=[frozenset(v for v in vertices if (mask>>v)&1) for mask in range(4096)]
cut=lambda S:sum((u in S)!=(v in S) for u,v in H.edges())
def choices(S):
    return [v for v in vertices if sum((w in S)!=(v in S) for w in neighbors[v])>=3]

# Build an actual dynamic-programming solution in strictly increasing energy order.
probs={}; terminals=[]
for S in sorted(states,key=cut):
    moves=choices(S)
    if not moves:
        terminals.append(S)
        probs[S]=Fraction(int(S in CAP),1)
    else:
        next_states=[(S-{v}) if v in S else (S|{v}) for v in moves]
        assert all(cut(T)<cut(S) for T in next_states)
        probs[S]=sum((probs[T] for T in next_states),Fraction(0))/len(moves)
assert len(terminals)==14 and set(terminals)==CAP|{frozenset(),frozenset(vertices)}
c=[sum((probs[S] for S in states if len(S)==k),Fraction(0)) for k in range(13)]
expected=[Fraction(0)]*13
for d,n in ((3,170100000),(4,1651550400),(5,739236313)):
    for j in range(d+1):
        expected[d+j]+=Fraction(n*(-1)**j*comb(d,j),85050000)
actual=[Fraction(0)]*13
for k,a in enumerate(c):
    for j in range(13-k):
        actual[k+j]+=a*(-1)**j*comb(12-k,j)
assert actual==expected
assert sum(probs.values(),Fraction(0))/4096==Fraction(10067037913,87091200000)
assert Counter(probs[S] for S in states if len(S)==3)=={Fraction(0):160,Fraction(1,30):60}
print('PASS second checker: independent graph, 4096 energy-ordered states, all exact coefficients')
print('coefficients by positive-spin count:',[str(v) for v in c])
