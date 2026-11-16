#!/usr/bin/env python3
"""Independent integer determinant verifier for 4 by 4 domino Walsh spectrum."""
from collections import Counter
from fractions import Fraction

# For each edge: (cell_u, cell_v), vertices indexed 4*r+c.
edges = []
for r in range(4):
    for c in range(4):
        u=4*r+c
        if c<3: edges.append((u,u+1))
        if r<3: edges.append((u,u+4))
assert len(edges)==24

# Deterministic Kruskal tree; nine non-tree edges provide independent gauge coordinates.
roots=list(range(16))
def find(x):
    while roots[x]!=x:
        x=roots[x]
    return x
chords=[]
for j,(u,v) in enumerate(edges):
    a,b=find(u),find(v)
    if a!=b: roots[a]=b
    else: chords.append(j)
assert chords==[7,9,11,14,16,18,21,22,23]
black=[4*r+c for r in range(4) for c in range(4) if (r+c)%2==0]
white=[4*r+c for r in range(4) for c in range(4) if (r+c)%2==1]
bi={b:i for i,b in enumerate(black)}
wi={w:i for i,w in enumerate(white)}

def det_exact(mat):
    """Fraction-free Bareiss elimination with deterministic pivoting."""
    A=[row[:] for row in mat]; n=len(A); sign=1; previous=1
    for k in range(n-1):
        p=next((r for r in range(k,n) if A[r][k]),None)
        if p is None:return 0
        if p!=k: A[k],A[p]=A[p],A[k];sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*piv-A[i][k]*A[k][j]
                assert num%previous==0
                A[i][j]=num//previous
            A[i][k]=0
        previous=piv
    return sign*A[n-1][n-1]

chord_pos={e:j for j,e in enumerate(chords)}
def signed_matrix(s):
    A=[[0]*8 for _ in range(8)]
    for e,(u,v) in enumerate(edges):
        r1,c1=divmod(u,4);r2,c2=divmod(v,4)
        # Real Kasteleyn signing: one negative vertical edge per unit-square face.
        weight=-1 if (c1==c2 and c1%2==0) else 1
        if e in chord_pos and (s>>chord_pos[e])&1: weight=-weight
        b,w=(u,v) if u in bi else (v,u)
        A[bi[b]][wi[w]]=weight
    return A
raw=[det_exact(signed_matrix(s)) for s in range(512)]
assert abs(raw[0])==36
W=[z*(1 if raw[0]>0 else -1) for z in raw]
expect_abs={0:233,4:177,8:72,12:12,16:6,20:2,24:8,32:1,36:1}
assert dict(Counter(map(abs,W)))==expect_abs
assert sum(v*v for v in W)==512*36

def had(a):
    a=list(a)
    p=1
    while p<len(a):
        for start in range(0,len(a),2*p):
            for q in range(p):
                x=a[start+q];y=a[start+q+p]
                a[start+q]=x+y; a[start+q+p]=x-y
        p*=2
    return a

H=had([int(t!=0) for t in W])
assert sum(map(abs,H))==3698
assert Fraction(sum(map(abs,H)),512)==Fraction(1849,256)
assert sum(int(w==0) for w in W)==233
assert sum(int(w==0 and i.bit_count()==1) for i,w in enumerate(W))==2
print('PASS: 512 exact 8x8 Kasteleyn determinants, spectrum, Parseval and endpoint norm.')
