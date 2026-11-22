"""Standalone exact and numerical checks for triangular-disk homology polytope metric formulas.

Requires Python 3, NumPy; exact checks use fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import numpy as np

count=0

def check(ok, label):
    global count
    assert ok,label
    count+=1

def inv_rat(M):
    n=len(M)
    A=[[F(M[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if A[j][k]!=0)
        A[k],A[j]=A[j],A[k]
        fac=A[k][k]
        A[k]=[t/fac for t in A[k]]
        for i in range(n):
            if i==k:continue
            fac=A[i][k]
            if fac:A[i]=[a-fac*b for a,b in zip(A[i],A[k])]
    return [r[n:] for r in A]

def matrix(edges,n):
    a=[[0]*n for _ in range(n)]
    for u,v in edges:a[u][v]=a[v][u]=-1
    for u in range(n):a[u][u]=3
    return a

def tree_edges(which,m):
    if which=='path':return [(i,i+1) for i in range(m-1)]
    if which=='binary':return [(i,(i-1)//2) for i in range(1,m)]
    raise ValueError(which)

def triangles_for_tree(edges,m):
    # Recursive ear-gluing yields a triangulated topological disk with the requested dual tree.
    adj=[[] for _ in range(m)]
    for i,j in edges:adj[i].append(j);adj[j].append(i)
    triangles={0:(0,1,2)}
    nextvertex=3
    used=set()
    queue=[0]
    while queue:
        i=queue.pop(0)
        x,y,z=triangles[i]
        for j in adj[i]:
            if j in triangles:continue
            candidates=[tuple(sorted(e)) for e in ((x,y),(x,z),(y,z))]
            candidates=[e for e in candidates if (i,e) not in used]
            assert candidates
            e=candidates[0]
            used.add((i,e))
            triangles[j]=(e[0],e[1],nextvertex)
            used.add((j,e))
            nextvertex+=1
            queue.append(j)
    faces=[triangles[i] for i in range(m)]
    # Genuine simplicial boundary columns, lexicographic orientation.
    edge_index={e:k for k,e in enumerate(sorted({tuple(sorted((t[i],t[j]))) for t in faces for i,j in ((0,1),(0,2),(1,2))}))}
    A=[[0]*m for _ in range(len(edge_index))]
    for i,face in enumerate(faces):
        a,b,c=sorted(face)
        for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:A[edge_index[e]][i]=s
    # Switching columns along the dual tree makes every common-edge dot product -1.
    sign=[0]*m;sign[0]=1
    q=[0]
    while q:
        i=q.pop(0)
        for j in adj[i]:
            if sign[j]:continue
            dot=sum(A[k][i]*A[k][j] for k in range(len(A)))
            check(abs(dot)==1,('shared edge',i,j))
            sign[j]=-sign[i]*dot
            q.append(j)
    B=[[A[k][i]*sign[i] for i in range(m)] for k in range(len(A))]
    G=[[sum(B[k][i]*B[k][j] for k in range(len(A))) for j in range(m)] for i in range(m)]
    check(G==matrix(edges,m),('topological Gram',edges))
    check(len(edge_index)==2*m+1,('edge count',m))
    return B

r=(3-sqrt(5))/2
for m in range(1,11):
    e=tree_edges('path',m)
    B=triangles_for_tree(e,m)
    inv=inv_rat(matrix(e,m))
    for i in range(m):
        for j in range(m):
            check(inv[i][j]>0,('inverse positivity',m,i,j))
    S=sum(sum(row) for row in inv)
    explicit=m-2*r*(1-r**m)/((1-r)*(1+r**(m+1)))
    check(abs(float(S)-explicit)<1e-10,('path formula',m,S,explicit))
    # Verify uniqueness of facet-normal norm maximizers by exhaustive rational signs.
    if m<=9:
        for signs in product([-1,1],repeat=m):
            val=sum(F(signs[i]*signs[j])*inv[i][j] for i in range(m) for j in range(m))
            check((val==S)==(len(set(signs))==1),('active facets',m,signs))
    # Orthogonal-factor check of every signed facet normal using actual boundary columns.
    if m<=7:
        D=np.asarray(B,dtype=float)
        G=np.asarray(matrix(e,m),dtype=float)
        for signs in product([-1,1],repeat=m):
            y=D@np.linalg.solve(G,np.asarray(signs,dtype=float))
            check(np.allclose(D.T@y,signs,atol=1e-11),('facet normal',m))
            check(abs(y@y-sum(F(signs[i]*signs[j])*inv[i][j] for i in range(m) for j in range(m)))<1e-10,('facet norm',m))

for h in range(0,7):
    m=2**(h+1)-1
    edges=tree_edges('binary',m)
    B=triangles_for_tree(edges,m)
    Q=np.asarray(matrix(edges,m),dtype=float)
    S=float(np.ones(m)@np.linalg.solve(Q,np.ones(m)))
    N=2**(h+1)
    explicit=2*m-h-1-(h+2)*(h+1/N)/(2-1/N)
    check(abs(S-explicit)<1e-8*max(1,S),('binary exact formula',h,S,explicit))
    if h<=2:
        Ir=inv_rat(matrix(edges,m))
        check(abs(float(sum(sum(row) for row in Ir))-explicit)<1e-10,('binary rational',h))
    if h<=3:
        check(np.all(np.linalg.eigvalsh(Q)>0),('positive definite',h))

print('PASS',count,'checks; m=1..10 exact path inverses, signed facet normals, geometric boundary constructions; full binary h=0..6')
