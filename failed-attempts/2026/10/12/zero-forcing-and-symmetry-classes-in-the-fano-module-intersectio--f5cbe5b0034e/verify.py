#!/usr/bin/env python3
from itertools import product, combinations
from fractions import Fraction
from collections import Counter

# Vertices: 0 is the zero subspace. 1..7 are the points of PG(2,2),
# represented by the seven nonzero vectors of F_2^3. 8..14 are the
# two-dimensional subspaces, represented by their nonzero normal vectors.
PTS=sorted(v for v in product((0,1), repeat=3) if v!=(0,0,0))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))%2

def graph():
    N=[set() for _ in range(15)]
    # Point-plane incidence.
    for i,p in enumerate(PTS,1):
        for j,a in enumerate(PTS,8):
            if dot(p,a)==0:
                N[i].add(j);N[j].add(i)
    # Any two distinct planes in F_2^3 intersect in a line.
    for i in range(8,15):
        for j in range(i+1,15):
            N[i].add(j);N[j].add(i)
    # Zero is isolated; points have no mutual edges.
    return N

def zero_trace(S,N):
    blue=set(S); trace=[]
    while len(blue)<len(N):
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=(v,next(iter(W)));break
        if move is None:
            return None
        blue.add(move[1]);trace.append(move)
    return trace

def polynomial(N):
    out={}; mins=[]
    for k in range(len(N)+1):
        arr=[]
        for S in combinations(range(len(N)),k):
            if zero_trace(S,N) is not None:
                arr.append(S)
        if arr:
            out[k]=len(arr)
            if not mins: mins=arr
    return out,mins

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1;continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1;c+=1
    return r

def gram_rank(N):
    # Active Gram vectors in R^7: each point gets e_p; each plane gets its
    # Fano incidence vector. The isolated zero vertex gets the zero vector.
    vec=[[0]*7]
    for i in range(7):
        v=[0]*7;v[i]=1;vec.append(v)
    for a in PTS:
        vec.append([1 if dot(p,a)==0 else 0 for p in PTS])
    M=[[sum(vec[i][k]*vec[j][k] for k in range(7)) for j in range(15)] for i in range(15)]
    for i in range(15):
        for j in range(i+1,15):
            assert ((M[i][j]!=0)==(j in N[i]))
    assert rank_fraction(M)==7
    return 7

def mat_mul(A,x):
    return tuple(sum(A[i][j]*x[j] for j in range(3))%2 for i in range(3))

def inv3(A):
    # Gaussian elimination over F_2.
    M=[list(A[i])+[1 if i==j else 0 for j in range(3)] for i in range(3)]
    r=0
    for c in range(3):
        p=next((i for i in range(r,3) if M[i][c]),None)
        if p is None:return None
        M[r],M[p]=M[p],M[r]
        for i in range(3):
            if i!=r and M[i][c]:
                M[i]=[x^y for x,y in zip(M[i],M[r])]
        r+=1
    return tuple(tuple(M[i][3+j] for j in range(3)) for i in range(3))

def transpose(A):return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))

def gl_actions():
    mats=[]
    for bits in product((0,1), repeat=9):
        A=tuple(tuple(bits[3*i+j] for j in range(3)) for i in range(3))
        Ai=inv3(A)
        if Ai is None:continue
        mats.append((A,Ai))
    assert len(mats)==168
    pos={v:i for i,v in enumerate(PTS)}
    perms=[]
    for A,Ai in mats:
        # Points transform by A; plane normals by A^{-T}.
        Ait=transpose(Ai)
        p=[0]
        p += [1+pos[mat_mul(A,v)] for v in PTS]
        p += [8+pos[mat_mul(Ait,a)] for a in PTS]
        assert sorted(p)==list(range(15))
        perms.append(tuple(p))
    return perms

def orbit_sizes(minsets,perms):
    remaining={tuple(sorted(S)) for S in minsets}
    sizes=[]
    while remaining:
        S=next(iter(remaining))
        O={tuple(sorted(P[v] for v in S)) for P in perms}
        assert O<=remaining|O
        # All images of a minimum forcing set must again be minimum forcing.
        assert O <= {tuple(sorted(T)) for T in minsets}
        remaining-=O
        sizes.append(len(O))
    return sorted(sizes)

N=graph()
assert len(N)==15 and len(N[0])==0
assert [len(N[i]) for i in range(1,8)]==[3]*7
assert [len(N[i]) for i in range(8,15)]==[9]*7

poly,mins=polynomial(N)
expected={8:1204,9:2100,10:1792,11:980,12:364,13:91,14:14,15:1}
assert poly==expected,(poly,expected)
assert len(mins)==1204 and all(0 in S for S in mins)
assert gram_rank(N)==7

# Explicit minimum witness and deterministic force trace.
witness=(0,1,2,3,4,8,9,11)
tr=zero_trace(witness,N)
assert tr==[(1,13),(2,12),(4,10),(3,14),(8,6),(9,5),(10,7)],tr

perms=gl_actions()
sizes=orbit_sizes(mins,perms)
assert sizes==[28,84,84,84,84,168,168,168,168,168],sizes
print('POLYNOMIAL',poly)
print('MINIMUM_SETS',len(mins))
print('EXPLICIT_WITNESS',witness)
print('FORCE_TRACE',tr)
print('GRAM_RANK',7)
print('GL32_ORDER',len(perms))
print('MINIMUM_SET_ORBIT_SIZES',sizes)
print('VERIFY_OK')
