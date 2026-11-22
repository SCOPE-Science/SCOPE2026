#!/usr/bin/env python3
"""Standalone cross-check: affine projective-plane coordinates, pure Python, no dependencies."""
from math import gcd

def line_incidences(p):
    pts=[('a',x,y) for x in range(p) for y in range(p)]+[('i',m) for m in range(p)]+[('i','vert')]
    lines=[('s',m,b) for m in range(p) for b in range(p)]+[('v',c) for c in range(p)]+[('inf',)]
    N=len(pts); assert N==p*p+p+1==len(lines)
    nbr=[[] for _ in range(2*N)]
    for i,pt in enumerate(pts):
        for j,l in enumerate(lines):
            incident=False
            if pt[0]=='a':
                _,x,y=pt
                if l[0]=='s':incident=(y-l[1]*x-l[2])%p==0
                if l[0]=='v':incident=(x==l[1])
            else:
                if l[0]=='inf':incident=True
                if l[0]=='s':incident=(pt[1]==l[1])
                if l[0]=='v':incident=(pt[1]=='vert')
            if incident:
                nbr[i].append(N+j);nbr[N+j].append(i)
    assert all(len(ns)==p+1 for ns in nbr)
    for a in range(N):
        for b in range(a+1,N):
            assert len(set(nbr[a])&set(nbr[b]))==1
    return nbr

def apply(nbr,x):
    n=len(nbr);u=x[:n];w=x[n:]
    return [(sum(u[j] for j in nbr[i])-w[i])%3 for i in range(n)]+u

def nullity(M):
    # Rows of an integer mod-3 matrix, reduced with integer-only elimination.
    A=[[x%3 for x in r] for r in M]
    rows=len(A);cols=len(A[0]);rank=0
    for c in range(cols):
        k=next((i for i in range(rank,rows) if A[i][c]),None)
        if k is None:continue
        A[k],A[rank]=A[rank],A[k]
        if A[rank][c]==2:A[rank]=[(2*x)%3 for x in A[rank]]
        for i in range(rank+1,rows):
            z=A[i][c]
            if z:
                R=A[rank];row=A[i]
                for j in range(c,cols):row[j]=(row[j]-z*R[j])%3
        rank+=1
        if rank==rows:break
    return cols-rank

def exp(p,v,rho,t):
    a=1;r=t
    while r%3==0:a*=3;r//=3
    if p%3==2:
        if t%8==0:return 4*v
        if t%4==0:return 4
        return 0
    if p%3==1:return (1+(t%2==0))*(min(a,4)+(v-2)*min(a,2))
    return (1+(t%2==0))*min(a,2)+(4*(v-1) if t%3==0 else 4*(v-rho))*(t%4==0)

def check(p,rho):
    nbr=line_incidences(p);n=len(nbr);v=n//2;N=2*n
    L={0:12,1:18,2:8}[p%3]
    columns=[]
    for i in range(N):
        unit=[int(j==i) for j in range(N)]
        trajectory=[];z=unit
        for t in range(1,L+1):
            z=apply(nbr,z)
            if L%t==0:trajectory.append((t,z[:]))
        assert z==unit
        columns.append(trajectory)
    for idx,(t,_) in enumerate(columns[0]):
        matrix=[[columns[j][idx][1][i]-int(i==j) for j in range(N)] for i in range(N)]
        got=nullity(matrix);want=exp(p,v,rho,t)
        print('affine PG(2,%d): t=%d dim=%d predicted=%d'%(p,t,got,want))
        assert got==want
    print('verified',p,'order',L)

for p,r in [(2,6),(3,7),(5,30)]:check(p,r)
