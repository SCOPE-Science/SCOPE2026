#!/usr/bin/env python3
"""Finite checks for an equivariant graph-product independence-complex theorem.
Runs independently of the paper's topological homotopy classification.
No external packages required.
"""
from itertools import permutations
from collections import defaultdict

def cycles(p):
    remain = set(range(len(p)))
    sizes=[]
    while remain:
        a=min(remain); b=a; k=0
        while b in remain:
            remain.remove(b); k+=1; b=p[b]
        assert b==a
        sizes.append(k)
    return tuple(sorted(sizes))

def representatives(n):
    return {cycles(p):p for p in permutations(range(n))}

def expected(m,n,p,q):
    f=sum(i==p[i] for i in range(m))
    h=sum(j==q[j] for j in range(n))
    s=cycles(p).count(2); t=cycles(q).count(2)
    return ((f-1)*(h-1)*(f*h-2))//2 + 2*s*t

def signed_simplex_trace(m,n,p,q):
    """Signed orbit sum over faces of the cross-cover complex Y."""
    N=m*n
    dest=[p[i]*n+q[j] for i in range(m) for j in range(n)]
    orbits=[]; seen=0
    for k in range(N):
        if seen>>k&1: continue
        u=k; mask=0
        while not (mask>>u&1):
            assert not (seen>>u&1)
            mask |=1<<u;seen|=1<<u;u=dest[u]
        assert u==k
        orbits.append(mask)
    total=0
    for S in range(1<<len(orbits)):
        chosen=0
        for i,orb in enumerate(orbits):
            if (S>>i)&1:chosen|=orb
        # U fits in a row plus a column precisely if some cross contains it.
        valid=False
        for i in range(m):
            rowmask=((1<<n)-1)<<(i*n)
            for j in range(n):
                colmask=sum(1<<(a*n+j) for a in range(m))
                if chosen & ~(rowmask|colmask)==0:
                    valid=True;break
            if valid:break
        if valid:total += -1 if S.bit_count()%2 else 1
    return -total  # H_2(Y) character, because Y is connected with H_q only q=2

def direct_full_trace(m,n,p,q):
    """Independent signed simplicial-chain Lefschetz computation on X itself."""
    N=2*m*n
    images=[]
    for a in range(2):
        for i in range(m):
            for j in range(n):
                images.append(a*m*n+p[i]*n+q[j])
    # incompatibility bitset of each vertex in opposite bipartition
    forb=[]
    for a in range(2):
        for i in range(m):
            for j in range(n):
                x=0
                for k in range(m):
                    for l in range(n):
                        if k!=i and l!=j:
                            x|=1<<((1-a)*m*n+k*n+l)
                forb.append(x)
    seen=0;orbs=[]
    for v in range(N):
        if (seen>>v)&1: continue
        u=v;mask=0
        while not (mask>>u)&1:
            assert not (seen>>u)&1
            mask|=1<<u;seen|=1<<u;u=images[u]
        assert u==v
        orbs.append(mask)
    masks=[]
    for orb in orbs:
        forbidden=0;z=orb
        while z:
            bit=z&-z; forbidden|=forb[bit.bit_length()-1]; z-=bit
        masks.append((orb,forbidden))
    Z=0
    # Enumerating orbit unions, checking independence directly
    for S in range(1<<len(masks)):
        selected=0;bad=0
        for k,(mask,forbidden) in enumerate(masks):
            if (S>>k)&1:
                selected|=mask;bad|=forbidden
        if selected&bad==0:
            Z+=-1 if S.bit_count()%2 else 1
    return Z # odd-degree reduced character: (-1)^3 tr = -tr, Z= -L, so tr=Z

def gf2_ranks(m,n):
    """Independent mod-two boundary rank computation for small X."""
    N=2*m*n;forb=[]
    for a in range(2):
        for i in range(m):
            for j in range(n):
                mask=0
                for k in range(m):
                    for l in range(n):
                        if k!=i and l!=j: mask |= 1<<((1-a)*m*n+k*n+l)
                forb.append(mask)
    faces=[[] for _ in range(N+1)];faces[0].append(0)
    for v in range(N):
        for level in range(v,-1,-1):
            for s in list(faces[level]):
                if all((forb[v]>>u)&1==0 for u in range(v) if (s>>u)&1):
                    faces[level+1].append(s|(1<<v))
    while faces and not faces[-1]:faces.pop()
    ranks=[0]*len(faces)
    for k in range(1,len(faces)):
        indices={f:i for i,f in enumerate(faces[k-1])}
        piv={};rank=0
        for f in faces[k]:
            bits=0;z=f
            while z:
                b=z&-z;bits ^= 1<<indices[f^b];z-=b
            while bits:
                i=bits.bit_length()-1
                if i in piv: bits ^= piv[i]
                else: piv[i]=bits;rank+=1;break
        ranks[k]=rank
    # augmented: rank d_1 includes the empty-face row.
    betti={k-1:len(faces[k])-ranks[k]- (ranks[k+1] if k+1<len(ranks) else 0)
           for k in range(1,len(faces))}
    return {k:v for k,v in betti.items() if v},[len(f) for f in faces]

def main():
    cnt=0
    for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)]:
        for p in representatives(m).values():
            for q in representatives(n).values():
                got=signed_simplex_trace(m,n,p,q)
                want=expected(m,n,p,q)
                assert got==want,(m,n,cycles(p),cycles(q),got,want)
                cnt+=1
        print(f'cross-character m={m} n={n} PASS',flush=True)
    direct=0
    for m,n in [(2,2),(2,3),(3,3)]:
        for p in representatives(m).values():
            for q in representatives(n).values():
                got=direct_full_trace(m,n,p,q)
                want=expected(m,n,p,q)
                assert got==want,(m,n,cycles(p),cycles(q),got,want)
                direct+=1
    for m,n in [(2,2),(2,3),(3,3)]:
        betti,counts=gf2_ranks(m,n)
        b=(m-1)*(n-1)*(m*n-2)//2
        assert betti=={3:b},(m,n,betti,b)
        print(f'mod2 ranks m={m} n={n} betti={betti} face-vector={counts}',flush=True)
    print(f'fixed-cross character tests={cnt}; direct-X Lefschetz tests={direct}',flush=True)
    print('VERIFY_OK')
if __name__=='__main__':main()
