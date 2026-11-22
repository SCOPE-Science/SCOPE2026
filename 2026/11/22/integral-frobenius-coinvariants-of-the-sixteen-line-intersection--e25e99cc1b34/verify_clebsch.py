#!/usr/bin/env python3
"""Exact integral Frobenius-coinvariant census for the sixteen-line intersection graph.

Python >= 3.9; only the standard library. Each Smith reduction is verified
against explicit unimodular row/column operations U and V. No external data.
"""
from collections import Counter, defaultdict
from itertools import permutations, combinations

MASKS = tuple(x for x in range(32) if x.bit_count()%2)
MI = {x:i for i,x in enumerate(MASKS)}
A = [[int((x^y).bit_count()==4) for y in MASKS] for x in MASKS]

def matmul(a,b):
    if not a or not b:return []
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def snf_cert(mat):
    """Return Smith diagonal with a verified unimodular U A V reduction."""
    a=[list(row) for row in mat];m=len(a);n=len(a[0]) if m else 0
    u=ident(m);v=ident(n)
    def rowswap(i,j):
        a[i],a[j]=a[j],a[i];u[i],u[j]=u[j],u[i]
    def colswap(i,j):
        for rr in a:rr[i],rr[j]=rr[j],rr[i]
        for rr in v:rr[i],rr[j]=rr[j],rr[i]
    def rowadd(i,j,mul):
        for t in range(n):a[i][t]+=mul*a[j][t]
        for t in range(m):u[i][t]+=mul*u[j][t]
    def coladd(i,j,mul):
        for t in range(m):a[t][i]+=mul*a[t][j]
        for t in range(n):v[t][i]+=mul*v[t][j]
    def rowneg(i):
        for t in range(n):a[i][t]=-a[i][t]
        for t in range(m):u[i][t]=-u[i][t]
    k=0;count=0
    while k<min(m,n):
        nonzero=[(abs(a[i][j]),i,j) for i in range(k,m) for j in range(k,n) if a[i][j]]
        if not nonzero:break
        _,i,j=min(nonzero);rowswap(k,i);colswap(k,j)
        while True:
            count+=1
            if count>10000:raise AssertionError('Euclidean reduction did not terminate')
            piv=a[k][k]
            ii=next((i for i in range(k+1,m) if a[i][k]%piv),None)
            if ii is not None:
                q=a[ii][k]//piv;rowadd(ii,k,-q);rowswap(ii,k);continue
            jj=next((j for j in range(k+1,n) if a[k][j]%piv),None)
            if jj is not None:
                q=a[k][jj]//piv;coladd(jj,k,-q);colswap(jj,k);continue
            for i in range(k+1,m):
                if a[i][k]:rowadd(i,k,-a[i][k]//piv)
            for j in range(k+1,n):
                if a[k][j]:coladd(j,k,-a[k][j]//piv)
            assert all(a[i][k]==0 for i in range(k+1,m))
            assert all(a[k][j]==0 for j in range(k+1,n))
            bad=next(((i,j) for i in range(k+1,m) for j in range(k+1,n) if a[i][j]%piv),None)
            if bad:
                rowadd(k,bad[0],1);continue
            break
        if a[k][k]<0:rowneg(k)
        k+=1
    assert matmul(matmul(u,mat),v)==a
    diagonal=[a[i][i] for i in range(min(m,n))]
    assert all(a[i][j]==(diagonal[i] if i==j else 0)
               for i in range(m) for j in range(n) if i<min(m,n) or j<min(m,n))
    assert all(diagonal[i]>0 for i in range(k))
    assert all(diagonal[i]==0 for i in range(k,len(diagonal)))
    assert all(diagonal[i+1]%diagonal[i]==0 for i in range(k-1))
    return diagonal

def dot(a,b):return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

# Five disjoint exceptional divisors, ten transforms of joining lines,
# and the strict transform of the conic through all five points.
e=[(0,*(int(j==i) for j in range(5))) for i in range(5)]
lij=[(1,*(-int(k in (i,j)) for k in range(5))) for i,j in combinations(range(5),2)]
c=(2,-1,-1,-1,-1,-1)
classes=e+lij+[c]
class_masks=[1<<i for i in range(5)] + [31^((1<<i)|(1<<j)) for i,j in combinations(range(5),2)] + [31]
assert len(set(class_masks))==16
for i in range(16):
    assert dot(classes[i],classes[i])==-1
    for j in range(16):
        assert (dot(classes[i],classes[j]) if i!=j else 0)==A[MI[class_masks[i]]][MI[class_masks[j]]]
assert all(sum(row)==5 for row in A)
assert all(A[i][j]==A[j][i] for i in range(16) for j in range(16))
assert Counter(snf_cert(A)) == Counter([1]*11+[3]*4+[15])

def signed_type(p,f):
    seen=set();out=[]
    for i in range(5):
        if i in seen:continue
        j=i;l=0;bit=0
        while j not in seen:
            seen.add(j);l+=1;bit^=(f>>j)&1;j=p[j]
        out.append((l,bit))
    return tuple(sorted(out))

def action(p,f):
    perm=[]
    for x in MASKS:
        y=f
        for i in range(5):
            if x&(1<<i):y^=1<<p[i]
        perm.append(MI[y])
    assert sorted(perm)==list(range(16))
    assert all(A[perm[i]][perm[j]]==A[i][j] for i in range(16) for j in range(16))
    return perm

def orbits(g):
    oid=[-1]*len(g);length=[]
    for i in range(len(g)):
        if oid[i]!=-1:continue
        j=i;label=len(length);l=0
        while oid[j]==-1:
            oid[j]=label;l+=1;j=g[j]
        assert j==i
        length.append(l)
    return oid,tuple(sorted(length))

def coinvariants(g):
    oid,profile=orbits(g);n=max(oid)+1
    # The coinvariant free module is on Frobenius orbits of line classes.
    # Every image of a single orbit representative is computed by summing
    # coefficients across each target orbit.
    B=[[0]*n for _ in range(n)]
    for j in range(n):
        rep=oid.index(j)
        for i in range(16):B[oid[i]][j]+=A[i][rep]
        for col in [k for k in range(16) if oid[k]==j]:
            for i in range(n):
                assert B[i][j]==sum(A[k][col] for k in range(16) if oid[k]==i)
    ds=snf_cert(B)
    assert len(ds)==n and all(x>0 for x in ds)
    return tuple(x for x in ds if x>1),profile

EXPECTED={
 ((1,0),(1,0),(1,0),(1,0),(1,0)):(1,(3,3,3,3,15)),
 ((1,0),(1,0),(1,0),(1,1),(1,1)):(10,(3,3,15)),
 ((1,0),(1,0),(1,0),(2,0)):(20,(3,3,3,15)),
 ((1,0),(1,0),(1,1),(2,1)):(60,(3,15)),
 ((1,0),(1,0),(3,0)):(80,(3,3,15)),
 ((1,0),(1,1),(1,1),(1,1),(1,1)):(5,(15,)),
 ((1,0),(1,1),(1,1),(2,0)):(60,(3,15)),
 ((1,0),(1,1),(3,1)):(160,(15,)),
 ((1,0),(2,0),(2,0)):(60,(3,3,15)),
 ((1,0),(2,1),(2,1)):(60,(15,)),
 ((1,0),(4,0)):(240,(3,15)),
 ((1,1),(1,1),(1,1),(2,1)):(20,(5,)),
 ((1,1),(1,1),(3,0)):(80,(15,)),
 ((1,1),(2,0),(2,1)):(120,(15,)),
 ((1,1),(4,1)):(240,(5,)),
 ((2,0),(3,0)):(160,(3,15)),
 ((2,1),(3,1)):(160,(5,)),
 ((5,0),):(384,(15,)),
}
counts=Counter();seen_groups={};profiles=defaultdict(set)
for p in permutations(range(5)):
    for f in range(32):
        if f.bit_count()%2:continue
        typ=signed_type(p,f)
        grp,profile=coinvariants(action(p,f))
        counts[typ]+=1
        if typ in seen_groups:assert seen_groups[typ]==(grp,profile)
        else:seen_groups[typ]=(grp,profile)
        profiles[profile].add(grp)
assert len(counts)==18 and sum(counts.values())==1920 and set(counts)==set(EXPECTED)
for typ,(ct,grp) in EXPECTED.items():
    assert counts[typ]==ct,(typ,counts[typ],ct)
    assert seen_groups[typ][0]==grp,(typ,seen_groups[typ][0],grp)
assert profiles[(4,4,4,4)]=={(3,15),(15,),(5,)}
assert profiles[(2,2,2,2,2,2,2,2)]=={(3,3,15),(3,15),(15,)}
print('Reconstructed blow-up intersection pairing, every degree and W(D5) graph action: PASS')
print('Geometric Smith form: 1^11, 3^4, 15')
print('All 1920 even signed permutations, 18 signed-cycle classes: PASS')
print('Signed cycles (length, negative-bit), group invariants, line orbits, class size:')
for typ in sorted(EXPECTED):
    print('%s %4d %s %s' % (typ,counts[typ],seen_groups[typ][0],seen_groups[typ][1]))
print('Distinct groups for common orbit pattern (4,4,4,4):',sorted(profiles[(4,4,4,4)]))
print('All Smith U*A*V certificates and invariant-factor divisibility checks: PASS')
