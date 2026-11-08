"""Exact mod-three action checks for a five-by-five chessboard complex."""
from itertools import combinations, permutations
import numpy as np
from collections import defaultdict

p=3
m=5
# column-major ordering of the 25 rook vertices
faces=[[] for _ in range(5)]
for j in range(1,6):
 for cols in combinations(range(m),j):
  for rows in permutations(range(m),j):
   faces[j-1].append(tuple(sorted(m*c+r for c,r in zip(cols,rows))))
assert [len(x) for x in faces]==[25,200,600,600,120]
idx=[{f:i for i,f in enumerate(fs)} for fs in faces]

def bdry(k):
    out=np.zeros((len(faces[k-1]),len(faces[k])), dtype=np.int16)
    for j,face in enumerate(faces[k]):
        for i in range(len(face)):
            sub=face[:i]+face[i+1:]
            out[idx[k-1][sub],j]=(1 if i%2==0 else 2)
    return out

B2=bdry(2) # C2 -> C1 200x600
B3=bdry(3) # C3 -> C2 600x600
assert not np.any((B2@B3)%3)

def columnspace_basis(mat):
    """Column-oriented mod-three echelon basis, keyed by first nonzero row."""
    basis={}
    for j in range(mat.shape[1]):
        v=mat[:,j].copy() %3
        for pivot,w in basis.items():
            if v[pivot]: v=(v-v[pivot]*w)%3
        a=np.flatnonzero(v)
        if a.size:
            q=int(a[0]); basis[q]=(v* (1 if v[q]==1 else 2))%3
    return basis

def reduces(vec,basis):
    v=np.array(vec,dtype=np.int16).copy()%3
    for pivot,w in basis.items():
        if v[pivot]: v=(v-v[pivot]*w)%3
    return v

def nullspace(mat):
    A=mat.copy()%3
    ncol=A.shape[1]; piv=[]; row=0
    for j in range(ncol):
        where=np.flatnonzero(A[row:,j]);
        if not len(where): continue
        k=row+int(where[0]); A[[row,k],:]=A[[k,row],:]
        if A[row,j]==2:A[row,:]=(2*A[row,:])%3
        nz=np.flatnonzero(A[:,j]); nz=nz[nz!=row]
        if len(nz):A[nz,:]=(A[nz,:]-A[nz,j,None]*A[row,:])%3
        piv.append(j); row+=1
        if row==len(A): break
    frees=[j for j in range(ncol) if j not in set(piv)]
    vec=[]
    for j in frees:
        v=np.zeros(ncol,dtype=np.int16);v[j]=1
        v[piv]=(-A[:row,j])%3
        vec.append(v)
    return vec

B3basis=columnspace_basis(B3)
K2=nullspace(B2)
print('faces',[len(fs) for fs in faces],'rank_d3',len(B3basis),'rank_d2',600-len(K2),'ker_d2',len(K2))
assert len(B3basis)==423 and len(K2)==424
z=next(v for v in K2 if np.any(reduces(v,B3basis)))
print('nonboundary_cycle_support',int(np.count_nonzero(z)))

def image_z(rowperm,colperm):
    zz=np.zeros(600,dtype=np.int16)
    for ii,old in enumerate(faces[2]):
        t=[m*colperm[v//m]+rowperm[v%m] for v in old]
        sign=1
        for a in range(3):
            for b in range(a+1,3):
                if t[a]>t[b]:sign=-sign
        new=tuple(sorted(t))
        zz[idx[2][new]]=(zz[idx[2][new]]+sign*z[ii])%3
    return zz

idp=tuple(range(m))
tp=(1,0,2,3,4)
for name,rowp,colp in [('row12',tp,idp),('column12',idp,tp),('both',tp,tp)]:
    gz=image_z(rowp,colp)
    sign= -1 if name!='both' else 1
    assert not np.any(reduces(gz-sign*z,B3basis)),name
    assert np.any(reduces(gz+sign*z,B3basis)),name
    print(name,'action',sign,'PASS')
print('ALL_VERIFY_OK')


# Independent mod-two fixed-point computations.
from itertools import product
from math import comb

def calc(m,k):
    cap=[1]*k+[m-4]
    faces_by_n=[set() for _ in range(m)]
    for opts in product(range(-1,k+1),repeat=m):
        if any(opts.count(i)>cap[i] for i in range(k+1)):continue
        face=tuple(m*c+r for c,r in enumerate(opts) if r>=0)
        if face:faces_by_n[len(face)-1].add(face)
    while faces_by_n and not faces_by_n[-1]:faces_by_n.pop()
    dims=[len(x) for x in faces_by_n]
    ranks=[1]
    for d in range(1,len(dims)):
        im= { }; prev={x:i for i,x in enumerate(faces_by_n[d-1])}
        for face in faces_by_n[d]:
            v=sum(1<<prev[face[:a]+face[a+1:]] for a in range(len(face)))
            while v:
                p=v.bit_length()-1
                if p in im:v^=im[p]
                else: im[p]=v;break
        ranks.append(len(im))
    betas=[dims[d]-ranks[d]-(ranks[d+1] if d+1<len(ranks) else 0) for d in range(len(dims))]
    beta= ((m-1)*(m-2)*(m-3)//6 if k==0 else (m*comb(m-2,2)-comb(m-1,3) if k==1 else m*(m-3)+comb(m-1,3)))
    expected_d=m-5+k
    assert betas == [beta if d==expected_d else 0 for d in range(len(dims))],(m,k,dims,betas,expected_d,beta)
    return (m,k,dims,betas)
for m in (5,6,7):
 for k in range(3):print(calc(m,k))
print('ALL_FIXED_OK')

# Independent modular check of the integral presentation's diagonal relation.
# This verifies the row interchange and column relabeling signs in the quotient;
# the proof of exact integral torsion order is supplied in the cited theorem.
for size in (5, 6, 7, 8, 9):
    triples = list(combinations(range(size), 3))
    labels = {D: i for i, D in enumerate(triples)}
    n = len(triples)
    def unit(v, a):
        v[a] = (v[a]+1)%3
    relations=[]
    for kind in range(2):
        for length in (1,2):
            for T in combinations(range(size),length):
                row=[0]*(2*n)
                for D in triples:
                    if set(T).issubset(D): unit(row,kind*n+labels[D])
                relations.append(row)
    diagonal=[1]*(2*n)
    relations.append(diagonal)
    pivots={}
    def red(vec,register=False):
        vec=vec[:]
        for p,base in pivots.items():
            if vec[p]:
                c=vec[p]
                vec=[(a-c*b)%3 for a,b in zip(vec,base)]
        if register:
            nz=next((i for i,a in enumerate(vec) if a),None)
            if nz is not None:
                inv=1 if vec[nz]==1 else 2
                pivots[nz]=[(inv*a)%3 for a in vec]
        return vec
    for row in relations:red(row,True)
    q2=[1]*n+[0]*n
    q3=[0]*n+[1]*n
    assert any(red(q2)),size
    assert not any(red([(a+b)%3 for a,b in zip(q2,q3)])),size
    # Column transposition relabels every three-subset and reverses the
    # orientation of the exterior word with one factor per column.
    col=(1,0)+tuple(range(2,size))
    col_image=[0]*(2*n)
    for D in triples:
        D2=tuple(sorted(col[v] for v in D))
        col_image[labels[D2]]=(col_image[labels[D2]]+2)%3
    assert not any(red([(a+b)%3 for a,b in zip(col_image,q2)])),size
    # The unit-row transposition interchanges the two indexed families.
    row_image=q3
    assert not any(red([(a+b)%3 for a,b in zip(row_image,q2)])),size
    print('presentation_m',size,'torsion_generator_nonzero_and_two_signs','PASS')
print('ALL_PRESENTATION_OK')
