#!/usr/bin/env python3
"""Exact standalone checks of binary universal cycles with <=2 internal bit changes."""
from itertools import product
from math import comb

def transitions(word):
    return sum(a!=b for a,b in zip(word,word[1:]))

def edges(n):
    return [''.join(x) for x in product('01',repeat=n) if transitions(x)<=2]

def determinant_bareiss(matrix):
    a=[list(row) for row in matrix]; m=len(a)
    d=1; sign=1
    for k in range(m-1):
        if a[k][k]==0:
            q=next((j for j in range(k+1,m) if a[j][k]),None)
            if q is None:return 0
            a[k],a[q]=a[q],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,m):
            for j in range(k+1,m):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%d==0
                a[i][j]=num//d
            a[i][k]=0
        d=pivot
    return sign*a[-1][-1] if m else 1

def rooted_tree_count(n):
    es=edges(n)
    vs=sorted(set(x[:-1] for x in es)|set(x[1:] for x in es)); ids={v:i for i,v in enumerate(vs)}
    assert vs[0]=='0'*(n-1)
    L=[[0]*len(vs) for _ in vs]
    for e in es:
        i=ids[e[:-1]];j=ids[e[1:]];L[i][i]+=1;L[i][j]-=1
    M=[row[1:] for row in L[1:]]
    return determinant_bareiss(M)

def enumerate_euler(n):
    es=edges(n); N=len(es); ids={e:i for i,e in enumerate(es)}
    out={w:[] for w in {e[:-1] for e in es}}
    for e in es:out[e[:-1]].append(ids[e])
    start='0'*n
    assert start in ids
    used=[False]*N;used[ids[start]]=True
    count=0; sample=None
    def walk(v, t, output):
        nonlocal count,sample
        if t==N:
            if v!='0'*(n-1):return
            s=output[:N]
            windows={''.join(s[(i+j)%N] for j in range(n)) for i in range(N)}
            assert windows==set(es), (n, windows^set(es))
            count+=1
            if sample is None:sample=s
            return
        for eid in out[v]:
            if not used[eid]:
                used[eid]=True
                w=es[eid];walk(w[1:],t+1,output+w[-1]);used[eid]=False
    walk(start[1:],1,start)
    return count, sample

def verify_reduction(n):
    m=n-1
    es=edges(n)
    adj={}
    for e in es:
        adj.setdefault(e[:-1],[]).append(e[1:])
    branching={v for v in adj if transitions(v)<=1}
    assert len(branching)==2*m
    A=['0'*(m-j)+'1'*j for j in range(m+1)]
    B={j:'1'*(m-j)+'0'*j for j in range(1,m)}
    B[m]=A[0]
    assert branching==set(A)|set(B.values())
    reduced={v:[] for v in branching}
    for v in branching:
        for nxt in adj[v]:
            x=nxt
            seen=set()
            while x not in branching:
                assert x not in seen
                seen.add(x)
                assert len(adj[x])==1
                x=adj[x][0]
            reduced[v].append(x)
    for j,v in enumerate(A):
        expected=[A[0],A[1]] if j==0 else ([A[m],B[1]] if j==m else [A[j+1],B[m-j]])
        assert sorted(reduced[v])==sorted(expected), (n,v,reduced[v],expected)
    for j in range(1,m):
        v=B[j]
        expected=[B[j+1],A[m-j]]
        assert sorted(reduced[v])==sorted(expected), (n,v,reduced[v],expected)

if __name__=='__main__':
    for n in range(2,11):
        verify_reduction(n)
        t=rooted_tree_count(n)
        assert t==2**(n-2), (n,t)
        assert len(edges(n))==n*n-n+2
        if n<=7:
            c,s=enumerate_euler(n)
            assert c==t,(n,c,t)
            print('n=%d windows=%d Euler=%d in_trees=%d sample=%s'%(n,len(edges(n)),c,t,s))
        else:
            print('n=%d windows=%d in_trees=%d'%(n,len(edges(n)),t))
    print('VERIFY_OK')
