#!/usr/bin/env python3
"""Exact finite certificate for the centered A_{5,2} hypergraphic zonotope.
All computation uses only the Python standard library and integer/rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd, lcm
from collections import Counter, defaultdict

N=5
EDGES=list(combinations(range(N),2))
TRIPLES=list(combinations(range(N),3))
edge_index={e:i for i,e in enumerate(EDGES)}
triple_index={t:i for i,t in enumerate(TRIPLES)}
PERMS=list(permutations(range(N)))
B=[]
for a,b,c in TRIPLES:
    v=[0]*10
    v[edge_index[(b,c)]]=1
    v[edge_index[(a,c)]]=-1
    v[edge_index[(a,b)]]=1
    B.append(tuple(v))

def rref(rows,ncol):
    A=[[F(v) for v in row] for row in rows]
    pivots=[]
    for col in range(ncol):
        where=next((i for i in range(len(pivots),len(A)) if A[i][col]),None)
        if where is None: continue
        k=len(pivots); A[k],A[where]=A[where],A[k]
        scale=A[k][col];A[k]=[v/scale for v in A[k]]
        for i in range(len(A)):
            if i!=k and A[i][col]:
                t=A[i][col];A[i]=[A[i][j]-t*A[k][j] for j in range(ncol)]
        pivots.append(col)
    return A,pivots

def rank(rows,ncol):return len(rref(rows,ncol)[1])

def kernel_one(rows,ncol):
    A,piv=rref(rows,ncol)
    assert len(piv)==ncol-1
    f=next(i for i in range(ncol) if i not in piv)
    out=[F(0)]*ncol;out[f]=F(1)
    for i,p in enumerate(piv):out[p]=-A[i][f]
    return out

def primitive(v):
    den=lcm(*(x.denominator for x in v))
    out=[int(x*den) for x in v]
    g=gcd(*out)
    out=tuple(x//g for x in out)
    if next(x for x in out if x)!=abs(next(x for x in out if x)):
        out=tuple(-x for x in out)
    return out

def scalar(v,w): return sum(x*y for x,y in zip(v,w))

# Linear span of triangle boundaries in oriented-edge coordinates.
basis=[]
for row in B:
    if rank(basis+[row],10)>len(basis):basis.append(row)
assert len(basis)==6 and rank(B,10)==6

def null_normal(indices):
    A=[[scalar(B[i],basis[j]) for j in range(6)] for i in indices]
    if rank(A,6)!=5:return None
    z=kernel_one(A,6)
    return primitive([sum(z[j]*basis[j][k] for j in range(6)) for k in range(10)])

def permed_edge_vector(v,perm):
    out=[0]*10
    for j,(a,b) in enumerate(EDGES):
        c,d=perm[a],perm[b]
        if c>d:out[edge_index[(d,c)]]-=v[j]
        else:out[edge_index[(c,d)]]+=v[j]
    return tuple(out)

def perm_triple_indices(indices,perm):
    return tuple(sorted(triple_index[tuple(sorted(perm[i] for i in TRIPLES[j]))] for j in indices))

# Every facet has five linearly independent generating directions in its plane;
# conversely, each independent 5-subset defines exactly one pair of facets.
normal_to_zero_sets=defaultdict(list)
for indices in combinations(range(10),5):
    normal=null_normal(indices)
    if normal is not None:normal_to_zero_sets[normal].append(indices)
assert len(normal_to_zero_sets)==37
facets=defaultdict(list)
for normal in normal_to_zero_sets:
    proj=[scalar(normal,b) for b in B]
    n2=scalar(normal,normal)
    s=sum(abs(x) for x in proj)
    dist2=F(s*s,4*n2)
    facets[dist2].append(normal)
assert {k:len(v) for k,v in facets.items()}=={F(15,4):10,F(5):15,F(25,4):12}
assert {k:rank(v,10) for k,v in facets.items()}=={F(15,4):6,F(5):6,F(25,4):6}
for q,normals in facets.items():
    for v in normals:
        proj=[scalar(v,b) for b in B]
        assert q==F(sum(abs(x) for x in proj)**2,4*scalar(v,v))
        assert rank([B[i] for i in range(10) if proj[i]==0],10)==5

# Independent symmetry-orbit check of all candidate 5-element zero sets.
remaining=set(combinations(range(10),5))
sub_orbits=[]
while remaining:
    representative=min(remaining)
    orb={perm_triple_indices(representative,p) for p in PERMS}
    remaining.difference_update(orb)
    sub_orbits.append((representative,len(orb),rank([B[i] for i in representative],10)))
assert sorted((m,sz,r) for m,sz,r in sub_orbits)==[
    ((0,1,2,3,4),30,5),
    ((0,1,2,3,6),30,4),
    ((0,1,2,3,7),60,5),
    ((0,1,2,3,9),60,5),
    ((0,1,3,7,8),60,5),
    ((0,1,4,8,9),12,5),
]
assert sum(sz for _,sz,r in sub_orbits if r==5)==222

# Each facet distance class is a complete S5 orbit up to sign.
for q, normals in facets.items():
    rep=normals[0]
    orbit={primitive([F(a) for a in permed_edge_vector(rep,p)]) for p in PERMS}
    assert orbit==set(normals),(q,len(orbit),len(normals))

# The endpoints of the generator cube contain all vertices and are sufficient
# for exact maximum-distance certification (convexity of squared distance).
radial=Counter(); outer=[]
for sig in product((-1,1),repeat=10):
    doubled=tuple(sum(sig[i]*B[i][j] for i in range(10)) for j in range(10))
    length2=scalar(doubled,doubled)
    radial[length2]+=1
    if length2==50:outer.append(doubled)
assert dict(radial)=={10:120,18:120,26:240,34:240,42:280,50:24}
assert len(outer)==len(set(outer))==24
all_positive=tuple(sum(b[j] for b in B) for j in range(10))
assert {permed_edge_vector(all_positive,p) for p in PERMS}==set(outer)
assert all(tuple(-x for x in v) in set(outer) for v in outer)

print('certified ambient edge dimension 10; polytope dimension 6')
print('facet count:',2*sum(len(v) for v in facets.values()))
print('facet distance squared -> number:',sorted((str(k),2*len(v)) for k,v in facets.items()))
print('five-subset symmetry orbits:',sub_orbits)
print('five-subsets of full facet rank:',222)
print('radial norm squared of doubled endpoints:',sorted(radial.items()))
print('circumsphere squared radius: 25/2; outer vertices: 24; antipodal diameter pairs: 12')
print('inradius squared: 15/4; inball-tangent facets: 20; tangent normals span rank 6')
print('complete exact enumeration PASS')
