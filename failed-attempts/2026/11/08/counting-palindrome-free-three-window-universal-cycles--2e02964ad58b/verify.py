#!/usr/bin/env python3
"""Independent exact checks for palindrome-free three-window cycle counts."""
from math import factorial
from itertools import product
from fractions import Fraction


def proposed(q):
    assert q>=2
    tau=q**(((q+3)*(q-2))//2) * (q-1)**(q-1) * (q-2)**(((q-1)*(q-2))//2)
    return tau * factorial(q-2)**(q*q)


def graph(q):
    vertices=list(product(range(q), repeat=2))
    arcs=[(a,b,c) for a,b,c in product(range(q),repeat=3) if a !=c]
    return vertices,arcs


def determinant_int(M):
    A=[list(map(int,row)) for row in M]
    n=len(A)
    if not n:return 1
    s=1;prev=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]!=0),None)
            if j is None:return 0
            A[k],A[j]=A[j],A[k];s=-s
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        for i in range(k+1,n):A[i][k]=0
        prev=pivot
    return s*A[n-1][n-1]


def tree(q):
    vs,arcs=graph(q)
    idx={v:i for i,v in enumerate(vs)}
    N=len(vs)
    L=[[0]*N for _ in range(N)]
    for a,b,c in arcs:
        i=idx[a,b];j=idx[b,c]
        L[i][i]+=1
        L[i][j]-=1
    assert all(sum(row)==0 for row in L)
    return determinant_int([row[:-1] for row in L[:-1]])


def direct_cycles(q):
    vs,arcs=graph(q)
    arcidx={e:i for i,e in enumerate(arcs)}
    adj={v:[] for v in vs}
    for i,(a,b,c) in enumerate(arcs):adj[a,b].append((i,(b,c)))
    first=arcs[0]
    head=(first[1],first[2]);start=(first[0],first[1]);target=(1<<len(arcs))-1
    def dfs(v,mask):
        if mask==target:return int(v==start)
        s=0
        for i,w in adj[v]:
            if not mask>>i&1:s+=dfs(w,mask|1<<i)
        return s
    return dfs(head,1<<arcidx[first])


def main():
    for q in range(2,7):
        t=tree(q)
        expected=proposed(q)//(factorial(q-2)**(q*q))
        assert t==expected,(q,t,expected)
        print('TREE',q,t,'CYCLES',proposed(q))
    for q in [2,3]:
        direct=direct_cycles(q)
        assert direct==proposed(q),(q,direct,proposed(q))
        print('DIRECT',q,direct)
    print('VERIFY_OK')

if __name__=='__main__':main()
