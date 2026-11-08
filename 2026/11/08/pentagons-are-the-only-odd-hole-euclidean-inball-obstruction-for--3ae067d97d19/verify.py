"""Finite checks for the Euclidean inradius theorem on h-perfect stable-set polytopes.

Run: python verify.py (requires numpy and scipy). Finite checks complement the proof.
"""
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.optimize import linprog


def components(*blocks):
    n=sum(sz for sz,_ in blocks)
    adj=[[False]*n for _ in range(n)]
    i0=0
    for sz, kind in blocks:
        if kind=='clique': pairs=combinations(range(sz),2)
        elif kind=='cycle': pairs=((i,(i+1)%sz) for i in range(sz))
        elif kind=='path': pairs=((i,i+1) for i in range(sz-1))
        elif kind=='isolate': pairs=[]
        else: raise ValueError(kind)
        for i,j in pairs:adj[i0+i][i0+j]=adj[i0+j][i0+i]=True
        i0+=sz
    return adj


def all_cliques(adj):
    n=len(adj)
    return [s for m in range(1,1<<n) if (s:=[i for i in range(n) if (m>>i)&1]) and all(adj[i][j] for i,j in combinations(s,2))]


def odd_cycles(adj):
    n=len(adj)
    found=set()
    for s in range(n):
        def dfs(path):
            v=path[-1]
            if len(path)>=3 and len(path)%2==1 and adj[v][s]:
                found.add(tuple(sorted(path)))
            for u in range(s+1,n):
                if adj[v][u] and u not in path:
                    dfs(path+[u])
        dfs([s])
    # Each vertex set can support multiple cycles; for these test graphs, it is enough.
    return [list(c) for c in found]


def theoretical(adj):
    n=len(adj)
    cs=all_cliques(adj)
    q=max(map(len,cs))
    pent=[C for C in odd_cycles(adj) if len(C)==5]
    if q==2 and pent:
        r=2/(5+sqrt(5))
        forced=set().union(*map(set,pent))
        kind='pentagons'
    else:
        r=1/(q+sqrt(q))
        forced=set().union(*(set(C) for C in cs if len(C)==q))
        kind='cliques'
    return r,len(forced),kind,q,len(pent)


def lp_check(adj):
    n=len(adj)
    cs=all_cliques(adj)
    cyc=odd_cycles(adj)
    A=[]; b=[]
    for i in range(n):
        row=[0.]*(n+1);row[i]=-1;row[-1]=1
        A.append(row);b.append(0.)
    for C in cs:
        row=[0.]*(n+1)
        for i in C:row[i]=1
        row[-1]=sqrt(len(C))
        A.append(row);b.append(1.)
    for C in cyc:
        row=[0.]*(n+1)
        for i in C:row[i]=1
        row[-1]=sqrt(len(C))
        A.append(row);b.append((len(C)-1)/2)
    obj=[0.]*n+[-1.]
    res=linprog(obj,A_ub=A,b_ub=b,bounds=[(None,None)]*n+[(0,None)],method='highs')
    assert res.success, res.message
    r,forced,kind,q,num_pents=theoretical(adj)
    assert abs(res.x[-1]-r)<2e-9,(q,num_pents,res.x[-1],r)
    uniform=[r]*n+[r]
    assert max(np.asarray(A) @ np.asarray(uniform)-np.asarray(b))<2e-9
    return len(cs),len(cyc),n,kind


def main():
    profiles=[
        ((3,'clique'),),((5,'cycle'),),((7,'cycle'),),((9,'cycle'),),
        ((3,'clique'),(5,'cycle')),((4,'clique'),(5,'cycle')),
        ((5,'cycle'),(2,'clique')),((7,'cycle'),(1,'isolate')),
        ((5,'path'),),((4,'isolate'),),
        ((5,'cycle'),(1,'isolate')),((3,'clique'),(1,'isolate')),
        ((2,'clique'),(2,'clique')),((6,'cycle'),),
    ]
    totals=[0,0,0]
    for blocks in profiles:
        a=lp_check(components(*blocks))
        totals=[x+y for x,y in zip(totals,a[:3])]
    # Monotonicity of the odd-hole barrier after the pentagon.
    vals=[(l-1)/(2*(l+sqrt(l))) for l in range(5,72,2)]
    assert all(x<y for x,y in zip(vals,vals[1:]))
    assert vals[0]<1/(2+sqrt(2))<vals[1]
    print('HPERFECT_EUCLIDEAN_INBALL_CHECKS_PASSED profiles=',len(profiles),
          'cliques=',totals[0],'odd_cycles=',totals[1], 'coordinates=',totals[2])

if __name__=='__main__':main()
