#!/usr/bin/env python3
"""Exact checks for second-order Padé diffusion on Cartesian products of cliques.
Requires only the Python standard library; finite tests supplement the analytic proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod

checks=0

def ck(b, msg):
    global checks
    checks += 1
    if not b:
        raise AssertionError(msg)

def add_poly(a,b):
    n=max(len(a),len(b));out=[(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def mul_poly(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def deriv(a):return [(i+1)*a[i+1] for i in range(len(a)-1)] or [0]

D=[2,2,1]; Dp=deriv(D)
N=[2]
for k,expected in enumerate(([2],[-4,-4],[8,24,12],[0,-96,-144,-48])):
    ck(N==expected,(k,N,expected))
    N=add_poly(mul_poly(deriv(N),D),[-(k+1)*i for i in mul_poly(N,Dp)])
ck(N[0] == -192,"fourth-derivative sign at zero")
series=[]
for i in range(5):
    v=Q(int(i==0),1)-sum(Q(D[j],2)*series[i-j] for j in range(1,min(i,2)+1))
    series.append(v)
ck(series==[Q(1),Q(-1),Q(1,2),Q(0),Q(-1,4)],"Maclaurin coefficients")

def f(x):return 1/(1+x+x*x/2)

def grid(qs): return list(product(*(range(q) for q in qs)))

def spectral_entry(qs,x,y,h):
    out=Q(0)
    for active in product((0,1),repeat=len(qs)):
        eigen=sum(q*a for q,a in zip(qs,active))
        weight=prod((q-1 if u==v else -1) if a else 1 for q,u,v,a in zip(qs,x,y,active))
        out+=weight*f(h*eigen)
    return out/prod(qs)

def inverse(M):
    n=len(M); A=[[Q(v) for v in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        row=next(i for i in range(j,n) if A[i][j]!=0)
        A[j],A[row]=A[row],A[j]
        d=A[j][j];A[j]=[v/d for v in A[j]]
        for i in range(n):
            if i==j:continue
            c=A[i][j]
            if c: A[i]=[a-c*b for a,b in zip(A[i],A[j])]
    return [row[n:] for row in A]

def laplacian(qs,verts):
    n=len(verts);return [[Q(sum(q-1 for q in qs)) if i==j else Q(-1 if sum(a!=b for a,b in zip(u,v))==1 else 0) for j,v in enumerate(verts)] for i,u in enumerate(verts)]

def multiply(A,B):
    Bt=list(zip(*B));return [[sum(x*y for x,y in zip(row,col)) for col in Bt] for row in A]

for qs in ((2,),(4,),(2,2),(2,3),(3,4),(2,2,2),(2,2,3),(2,3,4),(3,3,3)):
    verts=grid(qs);L=laplacian(qs,verts);L2=multiply(L,L);n=len(verts)
    for h in (Q(1,7),Q(2,3),Q(5)):
        M=[[Q(i==j)+h*L[i][j]+h*h*L2[i][j]/2 for j in range(n)] for i in range(n)]
        T=inverse(M)
        for i,u in enumerate(verts):
            ck(sum(T[i])==1,(qs,h,i,"row sum"))
            for j,v in enumerate(verts):
                w=spectral_entry(qs,u,v,h)
                ck(T[i][j]==w,(qs,h,u,v,"spectral formula",T[i][j],w))
                ck(w>0,(qs,h,u,v,"positive"))

qs=(2,2,2,2); x=(0,0,0,0);y=(1,1,1,1)
for h in (Q(1,1000),Q(1,10000)):
    w=spectral_entry(qs,x,y,h)
    ck(w<0,(h,w,"distance-four counterexample"))
    ck(abs(w/h**4+6) < Q(1,2),(h,w,"-6 coefficient"))
print(f"VERIFY_OK: {checks} exact rational assertions; all true")
