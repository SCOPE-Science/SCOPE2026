#!/usr/bin/env python3
"""Exact finite integer-chain verification for an octagonal chord complex.

No external dependencies. Vertices are admissible chords of the 8-gon.
Relative two-cells correspond to pairwise nonconsecutive triples.
"""
from itertools import combinations
from math import gcd

N=8
chords=[(a,b) for a,b in combinations(range(N),2)
        if (b-a) not in (1,N-1)]
chord_index={e:i for i,e in enumerate(chords)}
triangles=[t for t in combinations(range(N),3)
           if all(e in chord_index for e in combinations(t,2))]
tri_index={t:i for i,t in enumerate(triangles)}
assert len(chords)==20 and len(triangles)==16

# Classify all faces of the full independence complex directly by DFS.
faces=[]
def visit(selected, start):
    if selected: faces.append(tuple(selected))
    for j in range(start,len(chords)):
        a,b=chords[j]
        if all((a in chords[i] or b in chords[i]) for i in selected):
            visit(selected+[j],j+1)
visit([],0)
assert len(faces)==244, len(faces)
faces_outside_stars=[]
for face in faces:
    common=set(chords[face[0]])
    for i in face[1:]:common.intersection_update(chords[i])
    if not common: faces_outside_stars.append(face)
assert len(faces_outside_stars)==16
for face in faces_outside_stars:
    t=tuple(sorted(set().union(*(set(chords[i]) for i in face))))
    assert len(face)==3 and t in tri_index
assert len({tuple(sorted(set().union(*(set(chords[i]) for i in f))))
             for f in faces_outside_stars})==16

# Signed triangle-to-chord boundary in the graph of octagonal chords.
D=[[0]*len(triangles) for _ in chords]
for j,t in enumerate(triangles):
    a,b,c=t
    for edge,coeff in [((a,b),1),((a,c),-1),((b,c),1)]:
        D[chord_index[edge]][j]=coeff
basis_columns=[
    [-1,0,1,0,0,-1,0,0,0,0,0,0,1,0,0,0],
    [1,-1,0,1,-1,1,-1,1,0,-1,1,-1,0,-1,1,0],
    [0,0,0,0,0,0,-1,0,1,0,0,-1,0,0,0,1],
]
B=[[basis_columns[j][i] for j in range(3)] for i in range(16)]
for i in range(20):
    for j in range(3):
        assert sum(D[i][k]*B[k][j] for k in range(16))==0
assert [B[j] for j in (12,14,15)]==[[1,0,0],[0,1,0],[0,0,1]]

def determinant_integer(A):
    """Bareiss determinant; exact division checked at each step."""
    a=[row[:] for row in A]; n=len(a); sign=1; prior=1
    if n==0:return 1
    for k in range(n-1):
        if a[k][k]==0:
            nxt=next((i for i in range(k+1,n) if a[i][k]),None)
            if nxt is None:return 0
            a[k],a[nxt]=a[nxt],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=pivot*a[i][j]-a[i][k]*a[k][j]
                assert v%prior==0
                a[i][j]=v//prior
        for i in range(k+1,n):a[i][k]=0
        prior=pivot
    return sign*a[-1][-1]

rows=[0,1,2,3,5,6,7,8,10,11,12,14,15]
cols=[0,1,2,3,4,5,6,7,8,9,10,11,13]
assert abs(determinant_integer([[D[i][j] for j in cols] for i in rows]))==1
# Independent bound: Euler formula yields rank 13 and no remaining kernel basis.
# The unimodular nonzero 13-minor gives rank >= 13. A 3-vector kernel gives <=13.

R=[[0,-1,-1],[0,-1,0],[1,0,0]]
S=[[-1,0,0],[0,-1,0],[0,1,1]]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def action(offset,reflection):
    out=[[0]*16 for _ in range(16)]
    for j,face in enumerate(triangles):
        moved=[(offset-x if reflection else offset+x)%N for x in face]
        dest=tuple(sorted(moved))
        inv=sum(moved[a]>moved[b] for a,b in combinations(range(3),2))
        out[tri_index[dest]][j]=(-1)**inv
    return out
for matrix,off,refl in ((R,1,False),(S,0,True)):
    assert matmul(action(off,refl),B)==matmul(B,matrix)
I=[[int(i==j) for j in range(3)] for i in range(3)]
assert matmul(matmul(R,R),matmul(R,R))==I
assert matmul(S,S)==I
# Check srs=r^{-1} via sr s r=identity.
assert matmul(matmul(matmul(S,R),S),R)==I

def mv(A,v):return [sum(a*b for a,b in zip(row,v)) for row in A]
v=[-1,-1,0];orbit=[];w=v
for _ in range(4):orbit.append(w);w=mv(R,w)
assert w==v
assert [sum(o[j] for o in orbit) for j in range(3)]==[0,0,0]
assert abs(determinant_integer([[orbit[j][i] for j in range(3)] for i in range(3)]))==1
assert mv(S,v)==orbit[1]
for i in range(4):assert mv(S,orbit[i])==orbit[(1-i)%4]

# Smith invariants for R-I from gcd of minors (no Smith library dependency).
T=[[R[i][j]-I[i][j] for j in range(3)] for i in range(3)]
g1=0
for row in T:
    for a in row:g1=gcd(g1,abs(a))
g2=0
for rr in combinations(range(3),2):
    for cc in combinations(range(3),2):
        g2=gcd(g2,abs(determinant_integer([[T[i][j] for j in cc] for i in rr])))
assert (g1,g2,abs(determinant_integer(T)))==(1,1,4)

def binary_rank(A):
    piv={}
    for row in A:
        v=sum((a%2)<<j for j,a in enumerate(row))
        while v:
            b=v.bit_length()-1
            if b not in piv:piv[b]=v;break
            v^=piv[b]
    return len(piv)
assert [binary_rank(T),binary_rank(matmul(T,T)),binary_rank(matmul(matmul(T,T),T))]==[2,1,0]

# Direct Lefschetz on all nonempty simplices for all 16 symmetries,
# crosschecked against trace of the proven integral representation.
def face_trace(off,refl):
    total=0
    for face in faces:
        moved=[]
        for index in face:
            a,b=chords[index]
            pair=tuple(sorted(((off-a if refl else off+a)%N,
                               (off-b if refl else off+b)%N)))
            moved.append(chord_index[pair])
        if set(moved)==set(face):
            sign=(-1)**sum(moved[a]>moved[b] for a,b in combinations(range(len(moved)),2))
            total+=(-1)**(len(face)-1)*sign
    return total-1 # reduced Lefschetz subtract H0=1.
for refl in (False,True):
    for offset in range(8):
        op=I
        for _ in range(offset):op=matmul(op,R)
        if refl:op=matmul(op,S)
        assert sum(op[i][i] for i in range(3))==face_trace(offset,refl), (offset,refl)

print('OCTAGON_CHORDS',len(chords),'ADMISSIBLE_TRIPLES',len(triangles))
print('K_NONEMPTY_FACES',len(faces),'EXCEPTIONAL_2_FACES',len(faces_outside_stars))
print('RELATIVE_BOUNDARY_RANK',13,'KERNEL_Z_RANK',3)
print('BASIS_PRIMITIVE_MINOR_ROWS',12,14,15)
print('ROTATION_MATRIX',R,'REFLECTION_MATRIX',S)
print('PRIMITIVE_ORBIT',orbit,'RELATION_SUM_ZERO',True)
print('SMITH_R_MINUS_I',(1,1,4),'ROTATION_COINVARIANTS_Z4',True)
print('MOD2_JORDAN_RANKS',(2,1,0))
print('DIRECT_LEFSCHETZ_SYMMETRIES',16)
print('STABLE_KNESER_2_4_INTEGRAL_DIHEDRAL_LATTICE_PASS')
