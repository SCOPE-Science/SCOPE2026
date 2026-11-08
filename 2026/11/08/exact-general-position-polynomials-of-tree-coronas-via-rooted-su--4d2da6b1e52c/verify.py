#!/usr/bin/env python3
"""Exact reproducibility checks for tree-corona general-position enumeration.
Only Python standard library is needed. No file or network input."""
from itertools import product
from math import comb

def add(a,b):
    o=[0]*max(len(a),len(b))
    for k,v in enumerate(a):o[k]+=v
    for k,v in enumerate(b):o[k]+=v
    return trim(o)
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return trim(o)
def subtree_formula(n,edges):
    assert n>=3 and len(edges)==n-1
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    parents=[-1]*n;order=[0]
    for v in order:
        for u in adj[v]:
            if u!=parents[v]:
                assert u not in order
                parents[u]=v;order.append(u)
    assert len(order)==n
    branch=[None]*n; ans=[1]
    for v in reversed(order):
        cs=[u for u in adj[v] if parents[u]==v]
        prod=[1];singleton_branches=[0]
        for u in cs:
            prod=mul(prod,add([1],branch[u]))
            singleton_branches=add(singleton_branches,branch[u])
        twoz=[0,2]; oneplus=[1,1]
        # upward branch: parent is present, v is leaf iff no child branches
        nonempty=add(prod,[-1])
        branch[v]=add(twoz,mul(oneplus,nonempty))
        # topmost vertex v: degree zero or one gives root a leaf
        root_poly=add(mul(twoz,add([1],singleton_branches)),
                      mul(oneplus,add(add(prod,[-1]),[-v for v in singleton_branches])))
        ans=add(ans,root_poly)
    ans=add(ans,[0,0,n])
    return trim(ans)

def all_pairs_distance(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    d=[]
    for v in range(n):
        row=[-1]*n;row[v]=0;queue=[v]
        for u in queue:
            for w in adj[u]:
                if row[w]<0:row[w]=row[u]+1;queue.append(w)
        assert min(row)>=0
        d.append(row)
    return d

def direct_gp(n,edges):
    d=all_pairs_distance(n,edges)
    forb=[[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(a+1,n):
            for c in range(n):
                if c in (a,b):continue
                if (d[a][b]==d[a][c]+d[c][b] or
                    d[a][c]==d[a][b]+d[b][c] or
                    d[b][c]==d[b][a]+d[a][c]):
                    forb[a][b]|=1<<c
    out=[0]*(n+1)
    def enumerate_sets(S,F,lo,k):
        out[k]+=1
        for v in range(lo,n):
            if (F>>v)&1:continue
            nf=F;mask=S
            while mask:
                bit=mask&-mask;u=bit.bit_length()-1;mask^=bit
                nf|=forb[min(u,v)][max(u,v)]
            enumerate_sets(S|(1<<v),nf,v+1,k+1)
    enumerate_sets(0,0,0,0)
    return trim(out)

def corona_edges(n,edges):return edges+[(i,n+i) for i in range(n)]
def prufer_edges(seq):
    n=len(seq)+2;deg=[1]*n
    for v in seq:deg[v]+=1
    edges=[]
    for v in seq:
        a=next(i for i in range(n) if deg[i]==1)
        edges.append((a,v));deg[a]-=1;deg[v]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    edges.append((a,b))
    return edges

def simplicials(n,edges):
    A=[[False]*n for _ in range(n)]
    for a,b in edges:A[a][b]=A[b][a]=True
    return sum(1 for v in range(n) if all(A[x][y] for i,x in enumerate(range(n)) if A[v][x] for y in range(x+1,n) if A[v][y]))

def main():
    checks=0; subsets=0
    for n in range(3,6):
        for seq in product(range(n),repeat=n-2):
            edges=prufer_edges(seq)
            got=subtree_formula(n,edges)
            direct=direct_gp(2*n,corona_edges(n,edges))
            assert got==direct,(n,seq,got,direct)
            assert got[-1]==2**sum(1 for v in range(n) if sum(v in e for e in edges)==1)
            checks+=1;subsets+=1<<(2*n)
    cases=[(6,[(0,1),(1,2),(2,3),(3,4),(4,5)]),
           (6,[(0,i) for i in range(1,6)]),
           (7,[(0,i) for i in range(1,5)]+[(4,5),(5,6)]),
           (8,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7)]),
           (8,[(0,1),(1,2),(1,3),(3,4),(3,5),(5,6),(5,7)])]
    for n,edges in cases:
        got=subtree_formula(n,edges); direct=direct_gp(2*n,corona_edges(n,edges))
        assert got==direct,(n,edges,got,direct)
        checks+=1;subsets+=1<<(2*n)
    # Full root-projection formula independently tested on non-trees.
    for n,edges in [(4,[(0,1),(1,2),(2,3),(3,0)]),
                    (4,[(i,j) for i in range(4) for j in range(i+1,4)]),
                    (5,[(i,(i+1)%5) for i in range(5)]),
                    (6,[(i,(i+1)%6) for i in range(6)])]:
        d=all_pairs_distance(n,edges);expected=[0]*(n+1)
        for mask in range(1<<n):
            U=[v for v in range(n) if mask>>v&1]
            e=sum(1 for v in U if not any(d[a][b]==d[a][v]+d[v][b]
                     for ix,a in enumerate(U) for b in U[ix+1:] if v not in (a,b)))
            expected[len(U)]+=2**e
        expected[2]+=n
        got=direct_gp(2*n,corona_edges(n,edges))
        assert trim(expected)==got,(n,edges,expected,got)
        assert got[-1]==2**simplicials(n,edges)
        checks+=1;subsets+=1<<(2*n)
    print(f'VERIFY_OK graph_cases={checks} enumerated_vertex_subsets={subsets} '
          'tree_corona_recurrence=PASS root_projection=PASS top_simplicial=PASS')
if __name__=='__main__':main()
