#!/usr/bin/env python3
"""Independent direct conjugation-orbit enumeration for all rank components over GF(2), m=2."""
from itertools import product

idx={(1,1):3,(1,2):4,(2,1):5,(2,2):6}
def mul(a,b):
    v=0
    for i in range(7):
        if a&(1<<i):
            for j in range(7):
                if b&(1<<j):
                    if i==0:v^=1<<j
                    elif j==0:v^=1<<i
                    elif (i,j) in idx:v^=1<<idx[i,j]
    return v

def act(matrix,vector):
    out=0
    for i in range(7):
        if vector&(1<<i):out^=matrix[i]
    return out

def automorphisms():
    for u,v in product(range(4),repeat=2):
        if u==0 or v==0 or u==v:continue
        for s,t in product(range(16),repeat=2):
            gx=((u&1)<<1)|(((u>>1)&1)<<2)|(s<<3)
            gy=((v&1)<<1)|(((v>>1)&1)<<2)|(t<<3)
            mat=[1,gx,gy,mul(gx,gx),mul(gx,gy),mul(gy,gx),mul(gy,gy)]
            preimage={act(mat,a):a for a in range(128)}
            assert len(preimage)==128
            yield mat,preimage

def standard_D(r):
    ds=[0, (1<<1) if r>=1 else 0, (1<<2) if r>=2 else 0]
    for a,b in [(1,1),(1,2),(2,1),(2,2)]:
        d=(int(a<=r)+int(b<=r))%2
        ds.append(d<<idx[(a,b)])
    return ds

def test():
    auts=list(automorphisms())
    assert len(auts)==1536
    expected=[1,96,256]
    for r in range(3):
        D=standard_D(r)
        images=set()
        for phi,inv in auts:
            dx=act(phi,act(D,inv[1<<1]))
            dy=act(phi,act(D,inv[1<<2]))
            images.add((dx,dy))
        assert len(images)==expected[r],(r,len(images))
        print('GF2_CONJUGACY_ORBIT',r,len(images))
    print('ALL_IDEMPOTENT_DERIVATION_ORBIT_CHECKS_PASS')

if __name__=='__main__':test()
