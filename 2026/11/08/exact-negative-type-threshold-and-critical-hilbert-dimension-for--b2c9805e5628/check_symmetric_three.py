#!/usr/bin/env python3
"""Independent finite-prime-field test of the symmetric-form character table.

Requires NumPy; finite Fourier transforms are floating-point corroboration,
not a proof. Fourier convention: exp(-2*pi*i*tr(AB)/p).
"""
import argparse
import numpy as np
from collections import Counter

def rank_and_type(A,p):
    a,b,c,d,e,f=A
    det=(a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)%p
    if det:
        return (3, None)
    minors=(a*d-b*b,a*f-c*c,d*f-e*e,a*e-b*c,b*e-d*c,b*f-c*e)
    if any(x%p for x in minors):
        return (2,None)
    if any(x%p for x in A):
        return (1,None)
    return (0,None)

def binary_isotropic_count(A,p):
    a,b,c,d,e,f=A
    rank,_=rank_and_type(A,p)
    if rank!=2:raise ValueError('rank not 2')
    # Determine split of induced binary form by projective zeros excluding radical.
    # count all isotropic projective points: 1+q*z2, where z2=0 or 2.
    zero=0
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if x==y==z==0:continue
                if x and x!=1:continue
                if not x and y and y!=1:continue
                if not x and not y and z!=1:continue
                v=(x,y,z)
                Q=(a*x*x+2*b*x*y+2*c*x*z+d*y*y+2*e*y*z+f*z*z)%p
                if Q==0:zero+=1
    assert zero in (1,1+2*p), (zero,A,p)
    return zero

def expected(r,typ,p):
    if r==1:return -1,p*p*(p-1)
    if r==2 and typ=='split': return p*p-1,p*p*(p-2)
    if r==2 and typ=='anisotropic': return -p*p-1,p**3
    if r==3:return -1,-p*p
    if r==0:return None,None

def test_prime(p):
    if p<3 or p%2==0 or any(p%d==0 for d in range(3,int(p**0.5)+1,2)):
        raise ValueError("each field order must be an odd prime")
    sh=(p,)*6
    grids=np.indices(sh,dtype=np.int64)
    a,b,c,d,e,f=(grids[i] for i in range(6))
    det=(a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)%p
    m2=[(a*d-b*b)%p,(a*f-c*c)%p,(d*f-e*e)%p,(a*e-b*c)%p,(b*e-d*c)%p,(b*f-c*e)%p]
    r2= (det==0) & np.logical_or.reduce([u!=0 for u in m2]);r3=det!=0
    r1=(det==0)&(~r2)&((a!=0)|(b!=0)|(c!=0)|(d!=0)|(e!=0)|(f!=0))
    assert int(np.sum(r1)+np.sum(r2)+np.sum(r3))==p**6-1
    # FFT under coordinate pairing tr(AB): 1 on diag, 2 on three off-diag.
    c1=np.rint(np.fft.fftn(r1.astype(float)).real).astype(np.int64)
    c2=np.rint(np.fft.fftn(r2.astype(float)).real).astype(np.int64)
    assert np.max(np.abs(np.fft.fftn(r1.astype(float)).imag)) < 1e-6
    assert np.max(np.abs(np.fft.fftn(r2.astype(float)).imag)) < 1e-6
    stats=Counter()
    for A in np.ndindex(sh):
        # Fourier coefficient at frequency coords A: use offdiagonal index = 2b etc.
        freq=(A[0],(2*A[1])%p,(2*A[2])%p,A[3],(2*A[4])%p,A[5])
        rank,_=rank_and_type(A,p)
        if rank==0:continue
        typ=None
        if rank==2:typ='split' if binary_isotropic_count(A,p)>1 else 'anisotropic'
        s1,s2=expected(rank,typ,p)
        assert (int(c1[freq]),int(c2[freq]))==(s1,s2), (p,A,rank,typ,c1[freq],c2[freq],s1,s2)
        stats[(rank,typ)]+=1
    assert stats[(1,None)] == p**3-1
    assert stats[(2,'split')]+stats[(2,'anisotropic')]==p*p*(p**3-1)
    assert stats[(3,None)]==p*p*(p-1)*(p**3-1)
    print('PASS',p,'strata',sorted((str(k),v) for k,v in stats.items()),'spectrum S1,S2')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--primes',type=int,nargs='+',default=[3,5]); args=parser.parse_args()
    for p in args.primes:test_prime(p)
    print('SYMMETRIC_THREE_RANK_NEGATIVE_TYPE_PASS')
