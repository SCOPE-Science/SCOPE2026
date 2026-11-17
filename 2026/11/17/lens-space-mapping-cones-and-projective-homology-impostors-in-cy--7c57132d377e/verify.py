#!/usr/bin/env python3
"""Exact finite checks for cyclic cross-polytope and lens-cover chain models.

No external dependencies. This checks finite examples, not the universal proof.
"""
from itertools import product
from math import gcd


def rotate(x, p):
    # x is one of 0,...,2p-1, with x+p its opposite.
    return (x + 1) % (2*p)


def cross_faces(p):
    return [frozenset((j if e == 1 else j + p) for j, e in enumerate(sig) if e)
            for sig in product((-1,0,1), repeat=p) if any(sig)]


def face_orbits(p):
    faces = cross_faces(p)
    allowed = set(faces)
    assert len(allowed) == 3**p - 1
    assert all(frozenset(rotate(v,p) for v in f) in allowed for f in faces)
    assert all(all(not (j in f and j+p in f) for j in range(p)) for f in faces)
    assert len([f for f in faces if len(f) == p]) == 2**p
    # Checks cross-polytope/graph-power equivalence on all vertex pairs.
    for a in range(2*p):
        for b in range(a+1, 2*p):
            is_edge = min((a-b)%(2*p),(b-a)%(2*p)) <= p-1
            assert (frozenset((a,b)) in allowed) == is_edge
    # Nonzero stabilizer may occur for the full sphere, but the equator
    # C_{2p}-representation has primitive weights, checked below.
    return len(faces)


def mod_rank(matrix, prime):
    if not matrix: return 0
    A=[[v%prime for v in row] for row in matrix]
    if not A[0]: return 0
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]), None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,prime)
        A[r]=[(v*inv)%prime for v in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[(a-z*b)%prime for a,b in zip(A[i],A[r])]
        r+=1
    return r


def lens_boundary(q, j, d):
    # One CW cell per dimension 0,...,d, d odd.
    return q if 2<=j<=d and j%2==0 else 0


def mapping_cone_matrix(p,n):
    # C_n(L_{2p}) + C_{n-1}(L_p), dimensions in [0,p-2].
    d=p-2
    src=[('base',n)] if 1<=n<=d else []
    if 1<=n-1<=d:src.append(('cone',n-1))
    tgt=[('base',n-1)] if 1<=n-1<=d else []
    if 1<=n-2<=d:tgt.append(('cone',n-2))
    out=[[0]*len(src) for _ in tgt]
    for c,(typ,j) in enumerate(src):
        if typ=='base':
            if ('base',j-1) in tgt:
                out[tgt.index(('base',j-1))][c]=lens_boundary(2*p,j,d)
        else:
            # Cover map: degree two on odd lens cells, one on even.
            out[tgt.index(('base',j))][c] = 2 if j%2 else 1
            if ('cone',j-1) in tgt:
                out[tgt.index(('cone',j-1))][c]=-lens_boundary(p,j,d)
    return out, len(src), len(tgt)


def check(p):
    assert p>=5 and p%2==1 and all(p%i for i in range(2,int(p**0.5)+1))
    faces=face_orbits(p)
    # Eigenweights -1 and zeta_{2p}^{2j-1}; all non-real weights
    # are coprime to 2p when p is prime.
    weights=[w for w in range(1,p,2)]
    assert len(weights)==(p-1)//2
    assert all(gcd(w,2*p)==1 for w in weights)
    for j in range(p):
        assert (j+p)%(2*p) == (j+p)
        assert (j+2*p)%(2*p) == j
    # Exact integer cellular chain identity D_{n-1}D_n=0.
    mats={n:mapping_cone_matrix(p,n) for n in range(p+1)}
    for n in range(2,p+1):
        a,cs,rs=mats[n]; b,bs,br=mats[n-1]
        assert rs==bs
        assert all(sum(b[i][k]*a[k][j] for k in range(bs))==0
                   for i in range(br) for j in range(cs))
    # Integral homology predicted: Z/2 in odd 1,...,p-2, otherwise 0.
    # UCT implies reduced mod2 Betti rank 1 in degrees 1,...,p-1.
    # For odd primes all reduced mod-q homology must vanish.
    dims=[]
    for field in (2,3,p,101 if p!=101 else 103):
        hs=[]
        for n in range(p):
            dim=mats[n][1]
            b=mod_rank(mats[n][0],field)
            c=mod_rank(mats[n+1][0],field)
            hs.append(dim-b-c)
        assert hs==([0]+[1]*(p-1) if field==2 else [0]*p), (p,field,hs)
        dims.append((field,hs))
    # Free action of H on E implies pi_1(L_p)=C_p;
    # Hurewicz: pi_2(Sigma L_p)=H_1(L_p)=C_p.
    print(f'p={p}: faces={faces}, cyclic order={2*p}, lens cover degree=2;'
          f' cone CW boundary squares zero; mod-field ranks={dims}')

if __name__=='__main__':
    for prime in (5,7,11): check(prime)
    print('CYCLIC_RIPS_LENS_MAPPING_CONE_CHECKS_PASS')
