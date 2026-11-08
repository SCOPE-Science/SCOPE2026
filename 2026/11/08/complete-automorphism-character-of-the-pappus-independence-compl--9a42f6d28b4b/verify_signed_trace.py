#!/usr/bin/env python3
"""Independent verification: recursive face enumeration, GF(2) boundaries, signed chain Lefschetz traces.
Only the Python standard library is needed.
"""
from collections import Counter

N=18
OFF=[5,7,-7,7,-7,-5]*3
edges=set()
for i in range(N):
    edges.add(frozenset((i,(i+1)%N)))
    edges.add(frozenset((i,(i+OFF[i])%N)))
assert len(edges)==27
adj=[set() for _ in range(N)]
for a,b in (tuple(x) for x in edges):
    adj[a].add(b);adj[b].add(a)

# Recursive enumeration checks inclusion against earlier chosen vertices,
# independent from the bitset dynamic-programming enumerator.
faces_by_dim={d:[] for d in range(-1,9)}
faces_by_dim[-1].append(())
def search(i,selected):
    if i==N:
        if selected:faces_by_dim[len(selected)-1].append(tuple(selected))
        return
    search(i+1,selected)
    if not any(j in adj[i] for j in selected):search(i+1,selected+[i])
search(0,[])
fvector=[len(faces_by_dim[d]) for d in range(9)]
assert fvector==[18,126,438,801,756,348,90,18,2]
assert sum(fvector)==2597

# Check reduced mod-2 Betti dimensions by actual boundary-matrix reduction.
def rank_boundary(d):
    rows={f:i for i,f in enumerate(faces_by_dim[d-1])}
    pivots={}
    for face in faces_by_dim[d]:
        b=0
        for j in range(len(face)):
            boundary=face[:j]+face[j+1:]
            b ^= 1<<rows[boundary]
        while b:
            k=b.bit_length()-1
            if k in pivots:b^=pivots[k]
            else:pivots[k]=b;break
    return len(pivots)
ranks={d:rank_boundary(d) for d in range(9)}
reduced=[len(faces_by_dim[d])-ranks[d]-ranks.get(d+1,0) for d in range(9)]
assert reduced==[0,0,0,0,10,0,0,0,0],reduced
print('RECURSIVE_FACE_ENUMERATION total=2597 fvector='+str(fvector))
print('MOD2_REDUCED_BETTI '+str(reduced))

# Fixed representative list from separate group-theoretic certificate;
# independently verify each preserves all graph edges.
DATA=[
(1,1,10,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]),
(9,2,-2,[0,1,8,9,16,17,12,13,2,3,10,11,6,7,14,15,4,5]),
(18,2,0,[1,0,5,4,3,2,13,12,17,16,15,14,7,6,11,10,9,8]),
(18,2,2,[0,1,2,13,12,17,16,9,8,7,14,15,4,3,10,11,6,5]),
(2,3,1,[10,11,6,7,8,9,16,17,12,13,14,15,4,5,0,1,2,3]),
(12,3,-2,[2,3,4,5,0,1,8,9,10,11,6,7,14,15,16,17,12,13]),
(12,3,1,[0,5,6,11,12,17,16,15,4,3,10,9,8,7,14,13,2,1]),
(18,4,2,[1,0,5,6,7,8,9,16,17,12,11,10,3,4,15,14,13,2]),
(18,6,1,[2,3,10,11,12,13,14,15,4,5,6,7,8,9,16,17,0,1]),
(36,6,-1,[0,5,4,15,16,17,12,11,6,7,14,13,2,3,10,9,8,1]),
(36,6,0,[1,2,3,4,5,0,17,12,13,14,15,16,9,10,11,6,7,8]),
(18,12,-1,[1,2,3,10,9,8,7,14,13,12,11,6,5,4,15,16,17,0]),
(18,12,-1,[3,4,5,6,11,10,9,16,15,14,7,8,1,0,17,12,13,2]),
]
assert sum(x[0] for x in DATA)==216

def sign_perm(a):
    inv=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
    return -1 if inv%2 else 1

def lef_trace(p):
    total=0
    for d in range(9):
        s=0
        for face in faces_by_dim[d]:
            img=[p[v] for v in face]
            if set(img)==set(face):s+=sign_perm(img)
        total+=s*(-1 if d%2 else 1)
    # Nonempty Lefschetz - H_0 trace gives rational H_4 trace.
    return total-1
for idx,(clsize,ord_,expected,p) in enumerate(DATA):
    assert len(set(p))==N and set(p)==set(range(N))
    assert {frozenset((p[a],p[b])) for a,b in (tuple(x) for x in edges)}==edges
    got=lef_trace(p)
    assert got==expected,(idx,got,expected)
    print('SIGNED_TRACE class=%02d size=%d order=%d trace=%d'%(idx,clsize,ord_,got))
assert sum(s*v for s,_,v,_ in DATA)==0
assert sum(s*v*v for s,_,v,_ in DATA)==432
print('DIRECT_SIGNED_LEFSCHETZ_CHECK_PASS')
