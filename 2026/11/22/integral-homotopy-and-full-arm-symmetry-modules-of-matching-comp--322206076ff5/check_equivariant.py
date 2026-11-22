#!/usr/bin/env python3
"""Independent signed Lefschetz checks on uniform spiders."""
from check_spider import matching_faces
from itertools import permutations

def parity(indices):
    return -1 if sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))%2 else 1

def test(m,a,perm):
    edges=[(i,t) for i in range(a) for t in range(m)]
    idx={e:j for j,e in enumerate(edges)}
    emap=[idx[perm[i],t] for i,t in edges]
    face_groups=matching_faces((m,)*a)
    L=-1
    for d,faces in face_groups.items():
        if d==0:continue
        for face in faces:
            inds=[j for j in range(len(edges)) if face>>j&1]
            mapped=[emap[j] for j in inds]
            if set(mapped)!=set(inds):continue
            ord_mapped=[sorted(inds).index(v) for v in mapped]
            L+=(-1)**(d-1)*parity(ord_mapped)
    if m%3==2:pred=0
    elif m%3==0:pred=(-1)**((m//3)*(sum(perm[i]>perm[j] for i in range(a) for j in range(i+1,a))%2))
    else:
        sgn=(-1)**((m//3)*(sum(perm[i]>perm[j] for i in range(a) for j in range(i+1,a))%2))
        pred=sgn*(sum(perm[i]==i for i in range(a))-1)
    d=a*(m//3)-1 if m%3==0 else a*(m//3)
    trace=((-1)**d)*L
    assert trace==pred,(m,a,perm,trace,pred,L)
    return trace

def main():
    N=0
    for a,m in [(3,1),(4,1),(3,3),(4,3),(3,4),(4,4),(3,6),(3,7),(3,2),(3,5)]:
        for perm in permutations(range(a)):
            test(m,a,perm);N+=1
    print('PASS',N,'equivariant signed-Lefschetz tests across distinct arm lengths and cycle types')
if __name__=='__main__':main()

def test_mixed(ls,perm):
    a=len(ls)
    assert all(ls[i]==ls[perm[i]] for i in range(a))
    edges=[(i,t) for i in range(a) for t in range(ls[i])]
    idx={e:j for j,e in enumerate(edges)}
    emap=[idx[perm[i],t] for i,t in edges]
    face_groups=matching_faces(tuple(ls))
    L=-1
    for d,faces in face_groups.items():
        if not d:continue
        for face in faces:
            inds=[j for j in range(len(edges)) if face>>j&1]
            mapped=[emap[j] for j in inds]
            if set(mapped)!=set(inds):continue
            inv={v:k for k,v in enumerate(inds)}
            L+=(-1)**(d-1)*parity([inv[x] for x in mapped])
    s=sum(x//3 for x in ls);q=sum(x%3==2 for x in ls);r=sum(x%3==1 for x in ls)
    chi=1
    for ell in set(ls):
        ids=[i for i in range(a) if ls[i]==ell]
        local=[ids.index(perm[i]) for i in ids]
        chi*=parity(local)**(ell//3)
    if q>=2 or (q==0 and r==1):expected=0
    elif q==1 or (q==0 and r==0):expected=chi
    else:expected=chi*(sum(perm[i]==i for i in range(a) if ls[i]%3==1)-1)
    d=s-1 if q==0 and r==0 else s
    trace=(-1)**d*L
    assert trace==expected,(ls,perm,trace,expected)
    return trace

if __name__=='__main__':
    mixed=((1,1,3),(1,1,4),(2,3,3),(2,4,4),(3,3,4),(3,4,4),(4,4,6),(3,3,4,4),(1,1,3,3),(2,3,3,3),(4,4,1,1))
    checked=0
    for ls in mixed:
        for p in permutations(range(len(ls))):
            if all(ls[i]==ls[p[i]] for i in range(len(ls))):
                test_mixed(ls,p);checked+=1
    print('PASS',checked,'mixed-length group-action character checks')
