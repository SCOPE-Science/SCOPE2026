#!/usr/bin/env python3
"""Finite, exact checks for the C9 action on the rank-three binary symplectic building."""
from itertools import combinations
from collections import Counter

POLY = 0b1000011

def mult(a, b):
    out = 0
    while b:
        if b & 1: out ^= a
        b >>= 1
        a <<= 1
        if a & 64: a ^= POLY
    return out

def fpow(a, exp):
    out = 1
    while exp:
        if exp & 1: out = mult(out, a)
        a = mult(a, a); exp >>= 1
    return out

def trace8(z): return z ^ fpow(z, 2) ^ fpow(z, 4)

def bform(x, y):
    return trace8(mult(x, fpow(y, 8)) ^ mult(fpow(x, 8), y))

alpha = fpow(2, 7)
assert fpow(2, 63) == 1 and all(fpow(2, 63 // p) != 1 for p in (3, 7))
assert fpow(alpha, 9) == 1 and fpow(alpha, 3) != 1
assert all(bform(x, x) == 0 for x in range(64))
assert all(bform(mult(alpha,x), mult(alpha,y)) == bform(x,y) for x in range(64) for y in range(64))

points = sorted((x,) for x in range(1, 64))
lines = sorted({tuple(sorted((x,y,x^y))) for x in range(1,64) for y in range(x+1,64) if bform(x,y) == 0})
lagrangians = sorted({tuple(sorted(set(line) | {z} | {z^x for x in line}))
                    for line in lines for z in range(1,64)
                    if z not in line and all(bform(z,x)==0 for x in line)})
assert (len(points),len(lines),len(lagrangians)) == (63,315,135)
assert all(len(v)==7 for v in lagrangians)

families=[points,lines,lagrangians]
sets=[list(map(frozenset,F)) for F in families]
index=[{v:i for i,v in enumerate(F)} for F in sets]
perms=[]
for kind in range(3):
    action=[index[kind][frozenset(mult(alpha,x) for x in v)] for v in sets[kind]]
    assert sorted(action)==list(range(len(action)))
    perms.append(action)

fixed = {}
for exponent in range(9):
    fixed[exponent]=[]
    for kind in range(3):
        count=0
        a=fpow(alpha,exponent)
        for v in sets[kind]:
            if frozenset(mult(a,x) for x in v)==v: count+=1
        fixed[exponent].append(count)
assert fixed[0]==[63,315,135]
assert all(fixed[j]==[0,9,0] for j in (3,6))
assert all(fixed[j]==[0,0,0] for j in (1,2,4,5,7,8))

# The ordered flags' orbit cells are honest regular cells of a quotient Delta complex.
# A flag consists of one object in each rank; no nontrivial group element
# can invert its orientation, since group actions preserve rank.

def orbit_indices(items, f):
    seen=set(); reps=[]; to_orbit={}
    for z in items:
        if z in seen: continue
        orbit=[]; y=z
        while y not in seen:
            seen.add(y); orbit.append(y);y=f(y)
        ident=len(reps); reps.append(z)
        for w in orbit:to_orbit[w]=ident
    assert len(seen)==len(items)
    return reps,to_orbit

vertex_reps=[]; vert_orbit=[]
for j,perm in enumerate(perms):
    reps,mapping=orbit_indices(list(range(len(sets[j]))),lambda i:perm[i])
    vertex_reps.append(reps)
    vert_orbit.append(mapping)
assert list(map(len,vertex_reps)) == [7,37,15]

# incidences P-L, P-M, L-M, and chambers P-L-M.
flags1=[]
for i,p in enumerate(sets[0]):
    for j,l in enumerate(sets[1]):
        if p<=l:flags1.append(((0,i),(1,j)))
    for k,m in enumerate(sets[2]):
        if p<=m:flags1.append(((0,i),(2,k)))
for j,l in enumerate(sets[1]):
    for k,m in enumerate(sets[2]):
        if l<=m:flags1.append(((1,j),(2,k)))
assert len(flags1)==2835
flags2=[]
for i,p in enumerate(sets[0]):
    for j,l in enumerate(sets[1]):
        if p<=l:
            for k,m in enumerate(sets[2]):
                if l<=m:flags2.append(((0,i),(1,j),(2,k)))
assert len(flags2)==2835

def rotate_flag(flag):return tuple((kind,perms[kind][i]) for kind,i in flag)
reps1,orbs1=orbit_indices(flags1, rotate_flag)
reps2,orbs2=orbit_indices(flags2, rotate_flag)
assert (len(reps1),len(reps2))==(315,315)
assert len(vertex_reps[0])+len(vertex_reps[1])+len(vertex_reps[2])==59
assert all(len(set([f,rotate_flag(f),rotate_flag(rotate_flag(f))]))==3 for f in reps2)

def reduced_mod_p_rank(matrix, p):
    A=[r[:] for r in matrix]
    rows=len(A); cols=len(A[0]); pivot=0
    for col in range(cols):
        loc=next((i for i in range(pivot,rows) if A[i][col]%p),None)
        if loc is None:continue
        A[loc],A[pivot]=A[pivot],A[loc]
        inverse=pow(A[pivot][col]%p,-1,p)
        A[pivot]=[(z*inverse)%p for z in A[pivot]]
        for i in range(pivot+1,rows):
            fac=A[i][col]%p
            if fac:
                A[i]=[(u-fac*v)%p for u,v in zip(A[i],A[pivot])]
        pivot+=1
        if pivot==rows:break
    return pivot

# 59 vertices, 315 edges, 315 chambers.
vertex_coord={}
start=0
for rank,reps in enumerate(vertex_reps):
    for i in range(len(reps)):vertex_coord[(rank,i)]=start+i
    start+=len(reps)
C1=[[0]*315 for _ in range(59)]
for j,flag in enumerate(reps1):
    (rank0,a),(rank1,b)=flag
    C1[vertex_coord[(rank0,vert_orbit[rank0][a])]][j]-=1
    C1[vertex_coord[(rank1,vert_orbit[rank1][b])]][j]+=1
C2=[[0]*315 for _ in range(315)]
for j,(p,l,m) in enumerate(reps2):
    for edge,sgn in [((p,l),1),((p,m),-1),((l,m),1)]:
        C2[orbs1[edge]][j]+=sgn
# explicit chain-complex test
assert all(sum(C1[v][i]*C2[i][j] for i in range(315))==0 for v in range(59) for j in range(315))
# A connected graph has rank 58, and H_1 with F3-coefficients gains one dimension.
r1 = reduced_mod_p_rank(C1, 2)
r2_2 = reduced_mod_p_rank(C2, 2)
r2_3 = reduced_mod_p_rank(C2, 3)
r2_5 = reduced_mod_p_rank(C2, 5)
assert (r1,r2_2,r2_3,r2_5)==(58,257,256,257), (r1,r2_2,r2_3,r2_5)
print('SYMPLECTIC_C9_BUILDING_VERIFIED')
print('poly=0b1000011, alpha=2^7, alpha-order=9')
print('building cells=',tuple(map(len,families)),len(flags1),len(flags2))
print('stabilizer fixed counts=',fixed)
print('quotient vertices by rank=',list(map(len,vertex_reps)))
print('quotient cell counts=',(59,315,315),'Euler=',59)
print('boundary ranks F2, F3, F5=',r2_2,r2_3,r2_5,'rank d1=',r1)
print('H1(quotient; F2)=0, H1(quotient; F3)=1, H1(quotient; F5)=0')
