#!/usr/bin/env python3
"""Reproduce finite-field conic ambiguity support and Gabor lifting ranks."""
import cmath
import math
from collections import Counter


def legendre(a,p):
    a %= p
    if not a: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def conic(p):
    assert p > 2 and all(p%d for d in range(2, math.isqrt(p)+1))
    S={(x,y) for x in range(p) for y in range(p) if (x*x+y*y)%p==1}
    eps=legendre(-1,p)
    assert len(S)==p-eps
    shifts=Counter()
    for a in range(p):
        for b in range(p):
            K=[(x,y) for x,y in S if ((x+a)%p,(y+b)%p) in S]
            c=len(K)
            assert c in (0,1,2,len(S))
            shifts[c]+=1
            if a or b:
                Q=(a*a+b*b)%p
                expected=(1+legendre(Q*(4-Q),p)) if Q else 0
                assert c==expected, (p,a,b,c,expected)
                if c==2:
                    # A two-point sum of odd-order roots of unity cannot vanish.
                    assert len(K)==2
    expected_support=1+(p-eps)**2//2
    assert sum(shifts[k] for k in (1,2,len(S)))==expected_support
    expected_rank=p*p*expected_support
    # Direct complex ambiguity transform for every spatial shift / frequency.
    zeta=cmath.exp(-2j*math.pi/p)
    active=0
    for a in range(p):
        for b in range(p):
            K=[(x,y) for x,y in S if ((x+a)%p,(y+b)%p) in S]
            for u in range(p):
                for v in range(p):
                    val=sum(zeta**((u*x+v*y)%p) for x,y in K)
                    if abs(val)>1e-8: active+=1
                    else: assert not K, (p,a,b,u,v,val)
    assert active==expected_rank,(p,active,expected_rank)
    print(f'p={p} conic_size={len(S)} shift_support={expected_support} '
          f'pair_counts={dict(sorted(shifts.items()))} '
          f'Gabor_rank={active} nullity={p**4-active}')


if __name__=='__main__':
    for p in (3,5,7,11): conic(p)
    print('CONIC_GABOR_AMBIGUITY_RANK_CHECKS_OK')


def direct_lifting_svd(p=3):
    import numpy as np
    N=p*p
    xy=[(i,j) for i in range(p) for j in range(p)]
    idx={v:i for i,v in enumerate(xy)}
    S={(i,j) for i,j in xy if (i*i+j*j)%p==1}
    zeta=np.exp(2j*np.pi/p)
    rows=[]
    for a in xy:
        for b in xy:
            w=np.zeros(N,dtype=complex)
            for x in S:
                y=((x[0]+a[0])%p,(x[1]+a[1])%p)
                w[idx[y]]=zeta**((b[0]*y[0]+b[1]*y[1])%p)
            P=np.outer(w,w.conjugate())
            rows.append(P.reshape(N*N))
    mat=np.array(rows)
    values=np.linalg.svd(mat,compute_uv=False)
    predicted=[]
    for a in xy:
        K=[x for x in S if ((x[0]+a[0])%p,(x[1]+a[1])%p) in S]
        for b in xy:
            amplitude=sum(zeta**((b[0]*x[0]+b[1]*x[1])%p) for x in K)
            predicted.append(p*abs(amplitude))
    assert np.max(abs(np.array(sorted(values))-np.array(sorted(predicted)))) < 1e-8
    print('DIRECT_COMPLEX_LIFTING_SVD_OK')


if __name__=='__main__':
    direct_lifting_svd(3)
