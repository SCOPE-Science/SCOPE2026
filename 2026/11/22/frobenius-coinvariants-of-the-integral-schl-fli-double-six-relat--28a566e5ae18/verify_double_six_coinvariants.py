#!/usr/bin/env python3
"""Exact integral and modulo-four verification for a cubic-surface incidence quotient.
Python 3 standard library only. All indexing uses six labels 0,...,5.
"""
from itertools import combinations
from collections import Counter
from math import prod

labels = ([('E',i) for i in range(6)] +
          [('L',i,j) for i,j in combinations(range(6),2)] +
          [('Q',i) for i in range(6)])
classes=[]
for lab in labels:
    typ,i=lab[:2]
    if typ=='E': cls=(0,tuple(-int(k==i) for k in range(6)))
    elif typ=='Q': cls=(2,tuple(int(k!=i) for k in range(6)))
    else:
        j=lab[2];cls=(1,tuple(int(k in (i,j)) for k in range(6)))
    classes.append(cls)

def dot(c,r):
    return c[0]*r[0]-sum(x*y for x,y in zip(c[1],r[1]))
roots=[(0,tuple(int(k==i)-int(k==j) for k in range(6)))
       for i,j in combinations(range(6),2)]
roots += [(1,tuple(int(k in t) for k in range(6)))
          for t in combinations(range(6),3)]
roots += [(2,(1,)*6)]
assert len(roots)==36
full=[[int(dot(c,r)!=0) for r in roots] for c in classes]
assert all(sum(full[i][j] for i in range(27))==12 for j in range(36))

pivots=[0,1,2,3,4,6]
rest=[i for i in range(27) if i not in pivots]
assert len(rest)==21

def coeff(c):
    a,b=c
    h=a-3*b[5]
    v=[-b[k]+b[5] for k in range(5)]
    return [v[0]+h,v[1]+h,v[2],v[3],v[4],h]

K=[[0]*21 for _ in range(27)]
for j,i in enumerate(rest):
    K[i][j]=1
    for u,k in enumerate(pivots):K[k][j]=-coeff(classes[i])[u]
B=[[full[i][j] for j in range(36)] for i in rest]
# Validate the entire integer presentation in Picard lattice; not just finite ranks.
for j in range(36):
    for i in range(27):
        assert sum(K[i][k]*B[k][j] for k in range(21))==full[i][j]

def bareiss(a):
    a=[row[:] for row in a];n=len(a);sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            z=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if z is None:return 0
            a[k],a[z]=a[z],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*p-a[i][k]*a[k][j]
                assert z%prev==0
                a[i][j]=z//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sign*a[-1][-1]

# A 21-by-21 exact determinant, no normal-form library.
order=sorted(range(36),key=lambda j:tuple(i for i in range(27) if full[i][j]))
minor=(1,3,5,6,9,10,13,14,16,17,18,19,20,22,23,26,27,29,30,33,35)
det=bareiss([[B[i][order[j]] for j in minor] for i in range(21)])
assert abs(det)==65536,det

# Smith diagonal over Z/4, using invertible row and column operations.
# The exact determinant above, together with the resulting mod-4 diagonal for B,
# proves all integral B invariants (there is no invisible odd or 8-torsion).
def smith_mod4(matrix):
    a=[[int(x)%4 for x in row] for row in matrix]
    n=len(a);m=len(a[0]);d=[];k=0
    while k<n:
        odd=next(((i,j) for i in range(k,n) for j in range(k,m) if a[i][j]&1),None)
        found=odd if odd is not None else next(((i,j) for i in range(k,n) for j in range(k,m) if a[i][j]),None)
        if found is None:break
        i,j=found
        a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        v=a[k][k]
        if v&1:
            for col in range(k,m):a[k][col]=(a[k][col]*v)%4
        # pivot 1 or 2, all later entries divisible by pivot modulo 4
        p=a[k][k]; assert p in (1,2)
        for row in range(k+1,n):
            t=a[row][k] if p==1 else a[row][k]//2
            for col in range(k,m):a[row][col]=(a[row][col]-t*a[k][col])%4
        for col in range(k+1,m):
            t=a[k][col] if p==1 else a[k][col]//2
            for row in range(k,n):a[row][col]=(a[row][col]-t*a[row][k])%4
        assert all(a[i][k]==0 for i in range(k+1,n))
        assert all(a[k][j]==0 for j in range(k+1,m))
        d.append(p);k+=1
    return Counter(d+[0]*(n-len(d)))

# A natural S6-equivariant mod-two map to the 15 unordered index pairs.
pairs=list(combinations(range(6),2))
Phi=[[int((labels[k][0]=='L' and set(labels[k][1:])==set(pair)) or
          (labels[k][0]=='E' and labels[k][1] not in pair))
      for k in range(27)] for pair in pairs]
# It annihilates each double-six sum modulo two.
assert all(sum(Phi[i][k]*full[k][j] for k in range(27))%2==0
           for i in range(15) for j in range(36))
PK=[[sum(Phi[i][k]*K[k][j] for k in range(27))%2
     for j in range(21)] for i in range(15)]
# Explicit full-rank minor uses the first fifteen chosen kernel generators.
def rank_mod2(rows):
    a=[row[:] for row in rows]; n=len(a);m=len(a[0]);t=0
    for j in range(m):
        z=next((i for i in range(t,n) if a[i][j]),None)
        if z is None:continue
        a[t],a[z]=a[z],a[t]
        for i in range(n):
            if i!=t and a[i][j]:
                for h in range(j,m):a[i][h]^=a[t][h]
        t+=1
        if t==n:break
    return t
assert rank_mod2([row[:15] for row in PK])==15
# The integral coordinate-sum map is S6-invariant and kills each
# twelve-line double-six modulo four; it reaches an odd value on K.
assert all(sum(full[i][j] for i in range(27))%4==0 for j in range(36))
assert any(sum(K[i][j] for i in range(27))%2 for j in range(21))

cb=smith_mod4(B)
assert cb==Counter({1:6,2:14,0:1}),cb

def parts(n,m=None):
    if n==0:yield ();return
    if m is None:m=n
    for x in range(min(n,m),0,-1):
        for t in parts(n-x,x):yield (x,)+t

def representative(t):
    p=list(range(6));k=0
    for d in t:
        for i in range(d):p[k+i]=k+(i+1)%d
        k+=d
    return p

def index_map(p):
    lookup={lab:i for i,lab in enumerate(labels)}
    result=[]
    for lab in labels:
        if lab[0]=='L':result.append(lookup[('L',*sorted((p[lab[1]],p[lab[2]])))])
        else:result.append(lookup[(lab[0],p[lab[1]])])
    return result

def action_on_K(p):
    f=index_map(p)
    U=[[K[f.index(rest[i])][j] for j in range(21)] for i in range(21)]
    for i in range(27):
        for j in range(21):
            assert K[f.index(i)][j]==sum(K[i][k]*U[k][j] for k in range(21))
    return U

def subset_orbits(p):
    subsets=list(combinations(range(6),2));idx={s:i for i,s in enumerate(subsets)}
    action=[idx[tuple(sorted((p[i],p[j])))] for i,j in subsets]
    seen=set();n=0
    for i in range(15):
        if i in seen:continue
        n+=1;j=i
        while j not in seen:seen.add(j);j=action[j]
    return n

rows=[]
for typ in parts(6):
    p=representative(typ)
    U=action_on_K(p)
    A=[B[i]+[U[i][j]-int(i==j) for j in range(21)] for i in range(21)]
    c=smith_mod4(A)
    pairs=subset_orbits(p)
    assert c==Counter({1:21-pairs,2:pairs-1,0:1}),(typ,c,pairs)
    rows.append((typ,pairs,c[2],c[0]))
print('type   pair_orbits   Z/2 factors   Z/4 factors')
for t,o,a,b in rows:print(t,o,a,b)
print('DOUBLE_SIX_FROBENIUS_COINVARIANTS_VERIFIED_OK')
# Check equivariance of the pair-valued map for S6 generators.
for t in range(5):
    p=list(range(6));p[t],p[t+1]=p[t+1],p[t]
    f=index_map(p)
    pair_labels=list(combinations(range(6),2))
    pairindex={pair:i for i,pair in enumerate(pair_labels)}
    for i,pair in enumerate(pair_labels):
        moved=pairindex[tuple(sorted(p[k] for k in pair))]
        for k in range(27):assert Phi[moved][f[k]]==Phi[i][k]
