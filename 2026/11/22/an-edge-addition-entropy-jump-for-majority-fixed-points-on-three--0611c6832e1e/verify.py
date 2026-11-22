#!/usr/bin/env python3
"""Independent exact checks for majority fixed configurations on P3 x Cn.
Run: python3 verify.py (Python standard library only).
"""
from itertools import product
from math import gcd

COL=range(8)
def bit(b,r): return (b>>r)&1

def locally_stable(a,b,c):
    for r in range(3):
        t=bit(a,r)+bit(c,r)
        neighbours=2
        for rr in (r-1,r+1):
            if 0<=rr<3:
                t+=bit(b,rr); neighbours+=1
        v=bit(b,r)
        if v and 2*t<neighbours: return False
        if not v and 2*t>neighbours: return False
    return True

T=[[0]*64 for _ in range(64)]
for a,b,c in product(COL, repeat=3):
    if locally_stable(a,b,c):T[8*a+b][8*b+c]=1
assert sum(map(sum,T))==110

def matmul(A,B):
    m=len(A);C=[[0]*m for _ in range(m)]
    for i in range(m):
        for k,v in enumerate(A[i]):
            if v:
                for j,w in enumerate(B[k]):
                    if w:C[i][j]+=v*w
    return C

def tr(A):return sum(A[i][i] for i in range(len(A)))

def charpoly(A):
    m=len(A)
    P=[1]
    B=[r[:] for r in A]; s=[]
    for k in range(1,m+1):
        s.append(tr(B))
        p=-sum(P[k-i]*s[i-1] for i in range(1,k+1))
        assert p%k==0
        P.append(p//k)
        if k<m:B=matmul(B,A)
    return P # descending coefficients, highest first

def poly_mul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B):C[i+j]+=x*y
    return C

# Tarjan SCC: exact integer arithmetic, no numerical eigensolver.
adj=[[j for j,v in enumerate(row) if v] for row in T]
index=0;stack=[];on=set();num={};low={};scc=[]
def dfs(u):
    global index
    num[u]=low[u]=index;index+=1;stack.append(u);on.add(u)
    for v in adj[u]:
        if v not in num:dfs(v);low[u]=min(low[u],low[v])
        elif v in on:low[u]=min(low[u],num[v])
    if low[u]==num[u]:
        comp=[]
        while True:
            v=stack.pop();on.remove(v);comp.append(v)
            if v==u:break
        scc.append(sorted(comp))
for v in range(64):
    if v not in num:dfs(v)
assert sorted(map(len,scc),reverse=True)==[20]+[1]*44
P=[1,-2,0,-1]                  # x^3-2x^2-1
Q=[1,-1,1,1]                  # x^3-x^2+x+1
R=[1,-2,3,-3,0,-1]           # x^5-2x^4+3x^3-3x^2-1
factors=[([1,-1],5),([1,1],2),(P,1),(Q,1),(R,1)]
full=[1]
for f,power in factors:
    for _ in range(power):full=poly_mul(full,f)
full=full+[0]*46
assert len(full)==65
block_polys=[]
for comp in scc:
    M=[[T[i][j] for j in comp] for i in comp]
    block_polys.append(charpoly(M))
characteristic=[1]
for p in block_polys:characteristic=poly_mul(characteristic,p)
assert characteristic==full, (characteristic,full)

# Real-coefficient strict Schur test after substitution x=2z.
def inner_disc(f):
    d=len(f)-1
    g=[f[i]*2**(d-i) for i in range(d+1)]
    cert=[]
    while len(g)>1:
        a,b=g[0],g[-1];cert.append((a,b))
        assert abs(b)<abs(a), ('outside 2-disc',cert)
        h=[a*x-b*y for x,y in zip(g,reversed(g))]
        assert h[-1]==0
        h=h[:-1]
        common=0
        for v in h:common=gcd(common,abs(v))
        assert common
        g=[v//common for v in h]
    return cert
print('Schur Q:',inner_disc(Q))
print('Schur R:',inner_disc(R))
# P has a unique real root rho>2 and two complex roots modulus 1/sqrt(rho)<1.
# derivative 3x^2-4x has its positive critical point at 4/3; both
# critical values are negative, hence only one real root; P(2)=-1,P(3)=8.

# Direct majority map, independent of the transfer graph.
def direct_fixed_count(n):
    vertices=3*n
    nb=[]
    for c in range(n):
        for r in range(3):
            z=[3*((c-1)%n)+r,3*((c+1)%n)+r]
            if r>0:z.append(3*c+r-1)
            if r<2:z.append(3*c+r+1)
            assert len(z)==len(set(z))
            nb.append(z)
    nfixed=0
    for state in range(1<<vertices):
        ok=True
        for i,z in enumerate(nb):
            s=sum((state>>j)&1 for j in z)
            b=(state>>i)&1
            if (b and 2*s<len(z)) or (not b and 2*s>len(z)):
                ok=False;break
        nfixed+=ok
    return nfixed

# n=3 edge case has distinct left/right neighbours despite cycle triangle.
expected={3:8,4:36,5:78,6:146,7:260,8:572,9:1304,10:2848,11:6058,12:13218}
A=[r[:] for r in T]
for n in range(1,max(expected)+1):
    if n in expected:assert tr(A)==expected[n]
    if n<max(expected):A=matmul(A,T)
for n in range(3,7):
    v=direct_fixed_count(n)
    assert v==expected[n],(n,v,expected[n])
    print('Direct fixed n=',n,'count=',v)
print('PASS: all-size transfer characteristic factorization, bound certificates, and direct n=3..6.')
