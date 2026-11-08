#!/usr/bin/env python3
"""Exact finite-field census and projective orbit calculation.
Requires Python 3 and NumPy. Runs from any working directory.
F4=F2[a]/(a*a+a+1), elements 0,1,a,a+1 encoded 0,1,2,3.
"""
import itertools
import numpy as np
from collections import deque

M = np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]], dtype=np.uint8)
INV=(0,1,3,2)

def mul(a,b): return int(M[int(a),int(b)])
def power(a,n):
    r=1
    for _ in range(n): r=mul(r,a)
    return r

def dot(a,b):
    r=0
    for x,y in zip(a,b): r ^= mul(x,y)
    return r

def matvec(A,x): return tuple(dot(row,x) for row in A)

def matinv(A):
    n=len(A)
    aug=[[int(v) for v in row]+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        k=next((j for j in range(i,n) if aug[j][i]),None)
        if k is None: raise ValueError('singular matrix')
        aug[i],aug[k]=aug[k],aug[i]
        v=INV[aug[i][i]]
        aug[i]=[mul(v,x) for x in aug[i]]
        for j in range(n):
            if j!=i and aug[j][i]:
                v=aug[j][i]
                aug[j]=[x^mul(v,y) for x,y in zip(aug[j],aug[i])]
    return [row[n:] for row in aug]

def rank(A):
    B=[list(map(int,row)) for row in A]
    h=0
    for col in range(len(B[0])):
        k=next((i for i in range(h,len(B)) if B[i][col]),None)
        if k is None: continue
        B[h],B[k]=B[k],B[h]
        v=INV[B[h][col]]
        B[h]=[mul(v,x) for x in B[h]]
        for j in range(len(B)):
            if j!=h and B[j][col]:
                v=B[j][col]
                B[j]=[x^mul(v,y) for x,y in zip(B[j],B[h])]
        h+=1
        if h==len(B): break
    return h

def det3(A):
    v=0
    for p in itertools.permutations(range(3)):
        v ^= mul(mul(A[0][p[0]],A[1][p[1]]),A[2][p[2]])
    return v

points=[(1,y,z) for y in range(4) for z in range(4)] + [(0,1,z) for z in range(4)]+[(0,0,1)]
assert len(points)==21
mons=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]
assert len(mons)==10

def form0(x):
    u,v,w=x
    return mul(mul(u,v),mul(w,power(u,3)^power(v,3)^power(w,3)))

def evalmon(x):
    u,v,w=[power(t,2) for t in x]
    return [mul(mul(power(u,i),power(v,j)),power(w,k)) for i,j,k in mons]
E=np.array([evalmon(p) for p in points],dtype=np.uint8)
f0=np.array([form0(p) for p in points],dtype=np.uint8)

N=4**10
indices=np.arange(N,dtype=np.uint32)
coef=np.array([((indices>>(2*i))&3).astype(np.uint8) for i in range(10)])
smooth=np.ones(N,dtype=bool)
for i in range(21):
    v=np.full(N,int(f0[i]),dtype=np.uint8)
    for j in range(10):
        if E[i,j]: v ^= M[coef[j],E[i,j]]
    smooth &= (v!=0)
IDs={int(v) for v in np.flatnonzero(smooth)}
assert len(IDs)==960, len(IDs)
assert all(form0(p)^dot(evalmon(p),[(262275>>(2*i))&3 for i in range(10)]) for p in points)
print('TOTAL_NORMED_FORMS:',N,'SMOOTH:',len(IDs))

basis=[]
for i,row in enumerate(E):
    if rank([E[j] for j in basis]+[row])>len(basis): basis.append(i)
    if len(basis)==10: break
assert len(basis)==10
V=matinv([list(map(int,E[j])) for j in basis])

# Maps using A in GL3(F4): F -> det(A)^(-1) F(A X).
# This normalization is valid because F0(A X) - det(A)*F0(X)
# is a square of a homogeneous cubic over F4.
generators=[]
for i,j in ((0,1),(1,2),(2,0)):
    for a in (1,2):
        g=[[int(u==v) for v in range(3)] for u in range(3)]
        g[i][j]=a
        generators.append(g)
g=[[1,0,0],[0,1,0],[0,0,1]];g[0][0]=2;generators.append(g)
g=[[0,1,0],[1,0,0],[0,0,1]];generators.append(g)

def affine_map(A):
    d=det3(A)
    assert d in (1,2,3)
    invd=INV[d]
    rows=[matvec(A,points[i]) for i in basis]
    cols=[]
    for j in range(10):
        y=[mul(invd,evalmon(row)[j]) for row in rows]
        cols.append([dot(v,y) for v in V])
    b=[dot(v,[mul(invd,form0(row))^int(f0[basis[i]]) for i,row in enumerate(rows)]) for v in V]
    B=[[cols[k][j] for k in range(10)] for j in range(10)]
    # Check transformation agrees at all 21 projective points for 0 and each basis monomial.
    for p in points:
        at=matvec(A,p)
        e=evalmon(p);e2=evalmon(at)
        assert dot(b,e)==(mul(invd,form0(at))^form0(p))
        for k in range(10):
            assert dot([B[j][k] for j in range(10)],e)==mul(invd,e2[k])
    return B,b

T=[affine_map(A) for A in generators]
def action(idx,B,b):
    a=[(idx>>(2*i))&3 for i in range(10)]
    out=[v^dot(row,a) for row,v in zip(B,b)]
    return sum(int(x)<<(2*i) for i,x in enumerate(out))

for B,b in T:
    assert all(action(i,B,b) in IDs for i in IDs)
seed=min(IDs)
seen={seed};queue=deque([seed])
while queue:
    x=queue.popleft()
    for B,b in T:
        y=action(x,B,b)
        if y not in seen:
            seen.add(y);queue.append(y)
assert seen==IDs and len(seen)==960
# |PGL3(F4)|=|GL3(F4)|/(4-1)=60480.
PGL=(4**3-1)*(4**3-4)*(4**3-4**2)//3
assert PGL==60480 and PGL%len(seen)==0
print('PGL3_F4_ORDER:',PGL,'ORBIT_SIZE:',len(seen),'STABILIZER_ORDER:',PGL//len(seen))
print('CANONICAL_REPRESENTATIVE_COEFFICIENTS:',[(seed>>(2*i))&3 for i in range(10)])
print('SMOOTH_F4_FNC_SEXTIC_UNIQUE_ORBIT_PASS')
