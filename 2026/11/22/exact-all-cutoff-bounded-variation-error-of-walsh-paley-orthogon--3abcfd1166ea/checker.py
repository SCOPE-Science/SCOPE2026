#!/usr/bin/env python3
"""Exact rational tests for a sharp BV-to-L2 Walsh-Paley projection estimate.
No symbolic or numerical experiment is used as an infinite-dimensional proof.
"""
from fractions import Fraction as F
from random import Random


def paley(k, cell, L):
    """The k-th Paley-Walsh character on a dyadic 2**L grid cell."""
    p=0
    while k:
        low = k & -k
        j = low.bit_length()-1
        p ^= (cell >> (L-1-j)) & 1
        k ^= low
    return -1 if p else 1


def jump_residual_direct(N, t):
    L=(N-1).bit_length()
    B=1<<L
    coeff=[]
    for k in range(N):
        c=F(0)
        for cell in range(B):
            start=F(cell,B)
            end=F(cell+1,B)
            length=max(F(0), end-max(t,start))
            if length:
                c += paley(k,cell,L)*length
        coeff.append(c)
    return 1-t-sum((c*c for c in coeff),F(0))


def jump_residual_formula(N,t):
    M=1<<(N.bit_length()-1)
    j=min(int(M*t),M-1)
    q=M*t-j
    d=min(q,1-q)
    return (q*(1-q)-F(N-M,M)*d*d)/M


def test():
    rnd=Random(241126)
    count=0
    for N in range(1,41):
        M=1<<(N.bit_length()-1)
        r=N-M
        for j in sorted(set([0,M//2,M-1])):
            qs={F(0),F(1,3),F(1,2),F(2,3),F(1)}
            for _ in range(1): qs.add(F(rnd.randint(1,24),25))
            for q in qs:
                t=(F(j)+q)/M
                direct=jump_residual_direct(N,t)
                formula=jump_residual_formula(N,t)
                assert direct==formula,(N,j,q,direct,formula)
                assert formula<=F(1,4*N),(N,j,q,formula)
                count+=2
        for j in sorted(set([0,M//2,M-1])):
            q=F(M,2*N)
            ts={(F(j)+q)/M,(F(j+1)-q)/M}
            for t in ts:
                assert jump_residual_direct(N,t)==F(1,4*N),(N,t)
                count+=1
        if r:
            qstar=F(M,2*N)
            assert F(1,4) < qstar < F(1,2)
            count+=1
        else:
            assert F(M,2*N)==F(1,2)
            count+=1
    # An explicit check of the step-basis triangle bound for sample atomic derivatives.
    # The above exact identities are finite checks; the proof covers arbitrary BV derivatives.
    for N in [1,2,3,5,6,9,11,17,31]:
        grid=1<<(N-1).bit_length()
        ts=[F(1,13),F(7,19),F(5,11)]
        weights=[F(1,3),F(-2,5),F(3,7)]
        coeff=[]
        for k in range(N):
            ck=F(0)
            for w,t in zip(weights,ts):
                for cell in range(grid):
                    st=F(cell,grid); en=F(cell+1,grid)
                    ck+=w*paley(k,cell,(grid.bit_length()-1))*max(F(0),en-max(st,t))
            coeff.append(ck)
        # Integrate the quadratic polynomial of the piecewise constant step function.
        z=sorted(set([F(0),F(1)]+ts))
        full=F(0)
        for a,b in zip(z,z[1:]):
            mid=(a+b)/2
            f=sum((w for w,t in zip(weights,ts) if t<mid),F(0))
            full+=(b-a)*f*f
        residual=full-sum((c*c for c in coeff),F(0))
        tv=sum(map(abs,weights),F(0))
        assert residual <= tv*tv/F(4*N),(N,residual,tv)
        count+=1
    print('PASS exact rational assertions:',count)

if __name__=='__main__':test()
