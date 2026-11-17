#!/usr/bin/env python3
"""Finite exact checks for coordinate controllability of rook-graph Laplacians.

No external packages. Matrix ranks are computed over a prime larger than
Hadamard bounds for all tested minors, so they agree with rational ranks.
This file checks examples, not the all-size proof in RESULT.md.
"""
from itertools import product, combinations
from math import comb

P=1000003

def rank_mod(rows, k):
    a=[list(map(lambda z:z%P,row)) for row in rows]
    pivot=0
    for col in range(k):
        j=next((j for j in range(pivot,len(a)) if a[j][col]),None)
        if j is None:continue
        a[pivot],a[j]=a[j],a[pivot]
        t=pow(a[pivot][col],-1,P)
        for h in range(col,k):a[pivot][h]=(a[pivot][h]*t)%P
        for j in range(pivot+1,len(a)):
            v=a[j][col]
            if v:
                for h in range(col,k):a[j][h]=(a[j][h]-v*a[pivot][h])%P
        pivot+=1
    return pivot

def eig_restrictions(m,n,selected):
    def U(i,a):return int(i==a)-int(i==m-1)
    def V(j,b):return int(j==b)-int(j==n-1)
    # Disjoint eigenspaces if m!=n; collided middle spaces if m==n.
    e_m=[[U(i,a) for a in range(m-1)] for i,j in selected]
    e_n=[[V(j,b) for b in range(n-1)] for i,j in selected]
    e_top=[[U(i,a)*V(j,b) for a in range(m-1) for b in range(n-1)] for i,j in selected]
    rtop=rank_mod(e_top,(m-1)*(n-1)) == (m-1)*(n-1)
    if m==n:
        middle=[r+s for r,s in zip(e_m,e_n)]
        rmid=rank_mod(middle,2*(n-1)) == 2*(n-1)
    else:
        rmid=rank_mod(e_m,m-1)==m-1 and rank_mod(e_n,n-1)==n-1
    return bool(selected) and rtop and rmid

def comb_criterion(m,n,selected):
    chosen=set(selected)
    # On m+n vertices the edge (i,m+j) represents the rook square (i,j).
    T=[(i,m+j) for i in range(m) for j in range(n) if (i,j) not in chosen]
    parent=list(range(m+n))
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for x,y in T:
        a,b=find(x),find(y)
        if a==b:return False
        parent[a]=b
    if m!=n:return True
    parent=list(range(m+n))
    for i,j in chosen:
        x,y=find_s(i,parent),find_s(m+j,parent)
        if x!=y:parent[x]=y
    comps={}
    for i in range(m+n):
        p=find_s(i,parent)
        if p not in comps:comps[p]=[0,0]
        comps[p][int(i>=m)]+=1
    # With equal sides, vectors of component row/column counts must be independent.
    return rank_mod(list(zip(*comps.values())),len(comps))==len(comps)

def find_s(x,parent):
    while x!=parent[x]:x=parent[x]
    return x

def test(m,n,all_sets=True):
    cells=list(product(range(m),range(n)))
    good=0; total=0; min_good=10**9; mincount=0
    if all_sets:
        masks=range(1<<(m*n))
        for mask in masks:
            S=[cells[k] for k in range(m*n) if mask>>k&1]
            a=eig_restrictions(m,n,S)
            b=comb_criterion(m,n,S)
            assert a==b,(m,n,mask,a,b)
            total+=1
            if a:
                good+=1
                if len(S)<min_good:min_good=len(S);mincount=0
                if len(S)==min_good:mincount+=1
    else:
        size=(m-1)*(n-1)
        for ids in combinations(range(m*n),size):
            S=[cells[k] for k in ids]
            a=eig_restrictions(m,n,S)
            b=comb_criterion(m,n,S)
            assert a==b,(m,n,ids,a,b)
            total+=1
            good+=a
        min_good=size;mincount=good
    expect_size=(2 if m==n==2 else (m-1)*(n-1))
    expect_count=(4 if m==n==2 else (m**(n-1)*n**(m-1) if m!=n else m**(2*m-2)-m*m*((m-1)**2+1)))
    assert min_good==expect_size,(m,n,min_good,expect_size)
    assert mincount==expect_count,(m,n,mincount,expect_count)
    print('board=%dx%d subsets=%d controllable=%d minimum_size=%d minimum_sets=%d OK'%
          (m,n,total,good,min_good,mincount))

if __name__=='__main__':
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4)]:test(m,n)
    test(4,4,False)
    print('PASS: all comparisons exact over F_%d; rational rank equivalent for these dimensions'%P)
