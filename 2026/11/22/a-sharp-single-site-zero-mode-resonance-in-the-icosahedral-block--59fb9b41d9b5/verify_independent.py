#!/usr/bin/env python3
"""Independent graph construction; Newton-trace characteristic polynomial and modular ranks.
Requires Python 3.10+ and networkx. Run: python verify_independent.py
"""
from collections import Counter
import networkx as nx

G=nx.icosahedral_graph()  # Separately generated from the explicit pentagon-and-poles model.
assert (len(G),G.number_of_edges())==(12,30)
E=list(G.edges()); masks=[]
for mask in range(1<<12):
    if not any(((mask>>u)&1) and ((mask>>v)&1) for u,v in E):
        masks.append(mask)
assert Counter(x.bit_count() for x in masks)=={0:1,1:12,2:36,3:20}
L=[x for x in masks if x.bit_count()%2==0]
R=[x for x in masks if x.bit_count()%2==1]
assert (len(L),len(R))==(37,32)

def transfer(a):
    return [[a[(x^y).bit_length()-1] if (x^y).bit_count()==1 else 0 for y in R] for x in L]

def rank_mod(A,p):
    A=[list(map(lambda v:v%p,row)) for row in A];m=len(A);n=len(A[0]);r=0
    for j in range(n):
        k=next((k for k in range(r,m) if A[k][j]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        q=pow(A[r][j],-1,p)
        for h in range(j,n): A[r][h]=A[r][h]*q%p
        for k in range(r+1,m):
            q=A[k][j]
            if q:
                for h in range(j,n): A[k][h]=(A[k][h]-q*A[r][h])%p
        r+=1
    return r

B=transfer([1]*12)
assert rank_mod(B,101)==26
assert rank_mod(transfer([2]+[1]*11),5)==32
assert rank_mod(transfer([0]+[1]*11),5)==32

def multiply(A,B):
    n=len(A); result=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,x in enumerate(A[i]):
            if x:
                for j,y in enumerate(B[k]):
                    result[i][j]+=x*y
    return result
n=len(R)
Gram=[[sum(B[k][i]*B[k][j] for k in range(len(L))) for j in range(n)] for i in range(n)]
X=[[int(i==j) for j in range(n)] for i in range(n)]
traces=[]
for k in range(1,n+1):
    X=multiply(X,Gram)
    traces.append(sum(X[j][j] for j in range(n)))
coeff=[1]
for k in range(1,n+1):
    v=-sum(coeff[k-j]*traces[j-1] for j in range(1,k+1))
    assert v%k==0
    coeff.append(v//k)

def product(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B): C[i+j]+=x*y
    return C
factors=[[0,1]]*6 + [[-3,1]]*4 + [[-1,1]]*4 + \
        [[84,-30,1]] + [[44,-16,1]]*3 + [[12,-10,1]]*5
expected=[1]
for fac in factors:expected=product(expected,fac)
assert coeff==list(reversed(expected))
assert coeff[-1]==0 and expected[:6]==[0]*6 and expected[6]!=0
print('PASS: independent standard icosahedron, parity 37/32')
print('PASS: full exact Gram characteristic via 32 integer traces and Newton identities')
print('PASS: modular ranks 26 at uniform and 32 at single-site drive 0 or 2')
