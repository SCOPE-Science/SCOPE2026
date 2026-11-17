"""Reproduce exact fractional-matching Euclidean vertex projections and optional numeric checks."""
from fractions import Fraction as F
from itertools import combinations
import math
import numpy as np
from scipy.optimize import minimize
import networkx as nx


def cycles(G):
    """Canonical simple odd cycles of an undirected simple graph."""
    out = set()
    for start in sorted(G):
        def rec(path):
            a = path[-1]
            for b in G[a]:
                if b == start and len(path) >= 3 and len(path)%2:
                    edges=tuple(sorted(tuple(sorted((u,v))) for u,v in zip(path,path[1:]+[start])))
                    out.add(edges)
                elif b>start and b not in path:
                    rec(path+[b])
        rec([start])
    return sorted(out, key=lambda c:(len(c),c))


def disjoint_packs(Cs):
    out=[]
    def rec(i, covered, selected):
        if i == len(Cs):
            out.append(tuple(selected));return
        rec(i+1,covered,selected)
        c=Cs[i]; v=set(u for e in c for u in e)
        if covered.isdisjoint(v):rec(i+1,covered|v,selected+[c])
    rec(0,set(),[])
    return out


def matchings(G,free):
    edges=[e for e in G.edges if set(e)<=set(free)]
    o=[]
    def rec(i, used, arr):
        if i==len(edges):o.append(tuple(arr));return
        rec(i+1,used,arr)
        e=edges[i]
        if used.isdisjoint(e):rec(i+1, used|set(e), arr+[e])
    rec(0,set(),[])
    return o


def projection(x, Cs, edge_index):
    y=x.copy()
    for C in Cs:
        d=F(1,2*len(C))
        for e in C:y[edge_index[e]]-=d
    return y


def checks(G, numeric=False):
    E=sorted(tuple(sorted(e)) for e in G.edges())
    if not E:return 0,0,0,F(0)
    ei={e:i for i,e in enumerate(E)}
    Cs=cycles(G)
    packs=disjoint_packs(Cs)
    maxval=max((sum((F(1,4*len(c)) for c in p),F(0)) for p in packs),default=F(0))
    ct=0; num=0
    n=G.number_of_nodes()
    for pack in packs:
        covered=set(u for c in pack for e in c for u in e)
        for M in matchings(G,set(G.nodes)-covered):
            x=[F(0)]*len(E)
            for e in M:x[ei[tuple(sorted(e))]]=F(1)
            for C in pack:
                for e in C:x[ei[e]]=F(1,2)
            y=projection(x,pack,ei)
            target=sum((F(1,4*len(c)) for c in pack),F(0))
            assert sum(((a-b)**2 for a,b in zip(x,y)),F(0))==target
            assert all(a>=0 for a in y)
            # Exact supporting hyperplane lower bounds, independent of numerical solver.
            for C in pack:
                assert sum((y[ei[e]] for e in C),F(0))==F(len(C)-1,2)
                assert sum((x[ei[e]] for e in C),F(0))==F(len(C),2)
            # Every endpoint constraint and every blossom inequality is checked.
            for u in G:
                assert sum((y[ei[tuple(sorted((u,v)))]] for v in G[u]),F(0))<=1
            for k in range(3,n+1,2):
                for sub in combinations(G.nodes,k):
                    S=set(sub)
                    assert sum((y[i] for i,e in enumerate(E) if set(e)<=S),F(0))<=F(k-1,2)
            ct+=1
            if numeric and pack and num<25:
                N=len(E)
                A=[];b=[]
                for v in G:
                    A.append([int(v in e) for e in E]);b.append(1.)
                for k in range(3,n+1,2):
                    for S0 in combinations(G.nodes,k):
                        S=set(S0);A.append([int(set(e)<=S) for e in E]);b.append((k-1)/2)
                A=np.array(A,dtype=float);b=np.array(b)
                xx=np.array([float(a) for a in x]);yy=np.array([float(a) for a in y])
                res=minimize(lambda z:np.dot(z-xx,z-xx),np.zeros(N),method='SLSQP',jac=lambda z:2*(z-xx),bounds=[(0.,1.)]*N,constraints=[{'type':'ineq','fun':lambda z: b-A@z,'jac':lambda z:-A}],options={'maxiter':500,'ftol':1e-11})
                assert res.success or np.linalg.norm(res.x-yy)<2e-5,(res.message, G,pack)
                assert np.linalg.norm(res.x-yy)<2e-5,(np.linalg.norm(res.x-yy),G,pack)
                num+=1
    return len(packs),ct,num,maxval


def main():
    graphs=[]
    def graph(edges,n):
        g=nx.Graph();g.add_nodes_from(range(n));g.add_edges_from(edges);return g
    for n in range(3,7):
        graphs.append((f'complete{n}',nx.complete_graph(n)))
        graphs.append((f'cycle{n}',nx.cycle_graph(n)))
    graphs.append(('two_triangles',graph([(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)],6)))
    graphs.append(('bowtie',graph([(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],5)))
    graphs.append(('triangular_prism',nx.triangular_prism_graph() if hasattr(nx,'triangular_prism_graph') else graph([(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)],6)))
    graphs.append(('bipartite',nx.complete_bipartite_graph(3,4)))
    sums=[0,0,0]
    for name,G in graphs:
        p,v,qp,d=checks(G,numeric=(G.number_of_nodes()<=6))
        sums=[a+b for a,b in zip(sums,[p,v,qp])]
        print(name,'packs',p,'vertices',v,'qp',qp,'Hausdorff_squared',str(d))
        assert d<=F(G.number_of_nodes(),36)
        if G.number_of_nodes()%3==0 and d==F(G.number_of_nodes(),36):
            assert any(len(pack)==G.number_of_nodes()//3 and all(len(c)==3 for c in pack) for pack in disjoint_packs(cycles(G)))
    print('MATCHING_HAUSDORFF_PASS packs=%d vertices=%d independent_QP=%d'%(tuple(sums)))
if __name__=='__main__':main()
