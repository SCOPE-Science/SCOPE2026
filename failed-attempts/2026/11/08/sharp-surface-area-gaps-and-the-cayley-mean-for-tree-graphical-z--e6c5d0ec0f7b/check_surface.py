"""Finite consistency checks for tree graphical-zonotope surface areas.

Usage: python check_surface.py
The asymptotic check is diagnostic, not an infinite proof.
"""
import itertools
import math
import numpy as np
import networkx as nx
from scipy.special import gammaln, logsumexp


def splits(tree):
    n = len(tree)
    out=[]
    for u,v in list(tree.edges()):
        tree.remove_edge(u,v)
        k=len(nx.node_connected_component(tree,u))
        tree.add_edge(u,v)
        out.append(min(k,n-k))
    return sorted(out)


def surface_from_splits(tree):
    n=len(tree)
    return 2*sum(math.sqrt(k*(n-k)) for k in splits(tree))


def facet_area_direct(tree):
    n=len(tree)
    ee=list(tree.edges())
    B=np.zeros((n,n-1))
    for j,(u,v) in enumerate(ee):
        B[u,j]=1
        B[v,j]=-1
    gram=B.T@B
    assert abs(np.linalg.det(gram)-n) < 0.00001
    out=0.
    for j in range(n-1):
        Q=np.delete(B,j,axis=1)
        out += 2*math.sqrt(max(0.,float(np.linalg.det(Q.T@Q))))
    return out


def path_top(n):
    return 2*sum(math.sqrt(j*(n-j)) for j in range(1,n))


def star_bottom(n):
    return 2*(n-1)*math.sqrt(n-1)


def gap(n):
    return 2*(math.sqrt(2*(n-2))-math.sqrt(n-1))


def expected_formula(n):
    k=np.arange(1,n,dtype=float)
    a=(gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)
       +(k-1)*np.log(k)+(n-k-1)*np.log(n-k)
       -(n-2)*np.log(n)+.5*np.log(k*(n-k)))
    return float(np.exp(logsumexp(a)))


# Verify each facet as a Gram volume and inspect all tree shapes up to 11 vertices.
for n in range(5,12):
    vals=[]
    for T in nx.nonisomorphic_trees(n):
        a=surface_from_splits(T)
        if n<=9:
            b=facet_area_direct(T)
            assert abs(a-b)<2e-7,(n,a,b)
        vals.append((a,T.copy()))
    vals.sort(key=lambda z:z[0])
    assert abs(vals[0][0]-star_bottom(n))<1e-6
    assert abs(vals[-1][0]-path_top(n))<1e-6
    assert sum(abs(v-star_bottom(n)-gap(n))<1e-6 for v,_ in vals)==1
    assert sum(abs(v-path_top(n)+gap(n))<1e-6 for v,_ in vals)==1
    assert vals[1][0]>vals[0][0]+1e-7 and vals[-2][0]<vals[-1][0]-1e-7
    assert sorted(dict(vals[1][1].degree()).values())==[1]*(n-2)+[2,n-2]
    assert sorted(dict(vals[-2][1].degree()).values())==[1]*3+[2]*(n-4)+[3]

# Separately enumerate labeled trees using Prufer sequences for n<=6.
for n in range(2,7):
    acc=0.
    count=0
    for code in itertools.product(range(n),repeat=n-2):
        T=nx.from_prufer_sequence(list(code))
        acc+=surface_from_splits(T)
        count+=1
    assert count==n**(n-2)
    assert abs(acc/count-expected_formula(n))<1e-7

# Large-n finite numerical consistency with proved sharp leading constant.
for n in [500,1000,5000,20000]:
    ratio=expected_formula(n)/(n**1.5*math.log(n))
    assert 0.79<ratio<0.86,(n,ratio)

print('TREE_ZONOTOPE_SURFACE_EXTREMAL_CAYLEY_CHECKS_PASSED')
