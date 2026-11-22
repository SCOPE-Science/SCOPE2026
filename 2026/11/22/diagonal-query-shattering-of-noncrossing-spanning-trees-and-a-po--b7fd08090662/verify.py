#!/usr/bin/env python3
"""Reproduce the diagonal-query noncrossing-forest shattering certificates.

Only standard Python 3 library required. No external data files are read.
"""
from collections import Counter, defaultdict
from itertools import combinations


def crosses(e, f):
    a,b=e; c,d=f
    return len({a,b,c,d})==4 and ((a<c<b)!=(a<d<b)) and ((c<a<d)!=(c<b<d))


def diagonals(n):
    return [(a,b) for a,b in combinations(range(n),2) if b-a>1 and (a,b)!=(0,n-1)]


def forest_histogram(n):
    es=diagonals(n); m=len(es)
    conflict=[sum(1<<j for j in range(i+1,m) if crosses(es[i],es[j])) for i in range(m)]
    out=Counter()
    def visit(start,allowed,parents,k):
        out[k]+=1
        for i in range(start,m):
            if not (allowed>>i)&1: continue
            a,b=es[i]
            while parents[a]!=a:a=parents[a]
            while parents[b]!=b:b=parents[b]
            if a==b:continue
            nxt=parents.copy();nxt[a]=b
            visit(i+1,allowed & ~(1<<i) & ~conflict[i],nxt,k+1)
    visit(0,(1<<m)-1,list(range(n)),0)
    return [out[i] for i in range(n-2)]


def series_counts(max_n):
    bound=max_n-1
    def add(a,b,sgn=1):
        ans=a.copy()
        for t,v in b.items():ans[t]=ans.get(t,0)+sgn*v
        return {t:v for t,v in ans.items() if v}
    def times(a,b):
        c=defaultdict(int)
        for (i,j),v in a.items():
            for (ii,jj),w in b.items():
                if i+ii<=bound: c[i+ii,j+jj]+=v*w
        return dict(c)
    def geo2(a):
        ans={};p={(0,0):1}
        for _ in range(bound):
            p=times(p,a)
            if _>=1:ans=add(ans,p)
        return ans
    x={(1,0):1}; z={(0,1):1}; G={}
    for _ in range(bound+3):
        d=times(z,G); new=add(geo2(add(x,d)),geo2(d),-1)
        if new==G:break
        G=new
    else:raise AssertionError('formal fixed point did not stabilize')
    F=geo2(add(x,times(z,G)))
    return {n:[F.get((n-1,k),0) for k in range(n-2)] for n in range(3,max_n+1)}


def trace_test(n):
    edges=list(combinations(range(n),2))
    diag=diagonals(n)
    idx={e:i for i,e in enumerate(edges)}
    trees=[]
    for indices in combinations(range(len(edges)),n-1):
        if any(crosses(edges[a],edges[b]) for a,b in combinations(indices,2)):continue
        parent=list(range(n))
        def root(a):
            while parent[a]!=a:a=parent[a]
            return a
        for i in indices:
            a,b=edges[i];parent[root(a)]=root(b)
        if len({root(a) for a in range(n)})==1:
            full=sum(1<<i for i in indices)
            trees.append(full)
    assert trees
    order=[idx[e] for e in diag]
    projected=[sum(((tree>>i)&1)<<j for j,i in enumerate(order)) for tree in trees]
    hist=Counter()
    for support in range(1<<len(diag)):
        selected=[j for j in range(len(diag)) if support>>j&1]
        valid=True
        par=list(range(n))
        def root(a):
            while par[a]!=a:a=par[a]
            return a
        for a,b in combinations(selected,2):
            if crosses(diag[a],diag[b]):valid=False;break
        if valid:
            for j in selected:
                a,b=diag[j];ra,rb=root(a),root(b)
                if ra==rb:valid=False;break
                par[ra]=rb
        signatures=set()
        for tree in projected:
            signatures.add(sum(((tree>>j)&1)<<i for i,j in enumerate(selected)))
            if len(signatures)==1<<len(selected):break
        is_shattered=len(signatures)==1<<len(selected)
        assert is_shattered==valid, (n, support, is_shattered, valid)
        if valid:hist[len(selected)]+=1
    return len(trees),[hist[i] for i in range(n-2)]


def main():
    algebra=series_counts(12)
    direct=0
    for n in range(3,13):
        forest=forest_histogram(n)
        assert forest==algebra[n],(n,forest,algebra[n])
        assert forest[0]==1
        if n>=4: assert forest[-1]==n*2**(n-5)
        print('forest and algebraic series',n,forest)
        if n<=6:
            nt,trace=trace_test(n)
            assert trace==forest,(n,trace,forest)
            direct+=1<<(n*(n-3)//2)
            print('exhaustive spanning-tree trace',n,'noncrossing trees',nt,'support subsets',1<<(n*(n-3)//2))
    print('SUCCESS: diagonal forest and series counts n=3..12; exact query shattering on',direct,'support instances n=3..6')


if __name__=='__main__':main()
