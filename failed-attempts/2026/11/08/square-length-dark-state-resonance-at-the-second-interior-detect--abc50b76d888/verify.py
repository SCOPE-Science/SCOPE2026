#!/usr/bin/env python3
"""Exact arithmetic and independently constructed spectral spot checks for a spin-transfer chain."""
from math import comb, isqrt
from fractions import Fraction

def K2(d,k):
    return ((d-2*k)**2-d)//2

def Kraw(d,j,k):
    return sum((-1)**a*comb(k,a)*comb(d-k,j-a) for a in range(max(0,j-(d-k)), min(j,k)+1))

def check_spectral(d):
    # Unitary eigenbasis: v_k(j) = sqrt(C(d,k)/(2^d*C(d,j)))*K_j(k).
    # Rational identity: sum_j K_j(k)K_j(l)/C(d,j) = (2^d/C(d,k))*[k=l]
    K=[[Kraw(d,j,k) for k in range(d+1)] for j in range(d+1)]
    for k in range(d+1):
        assert K[0][k]==1
        for j in range(d+1):
            lhs=(d-j)*(Fraction(K[j+1][k],comb(d,j+1)) if j<d else 0) + j*(Fraction(K[j-1][k],comb(d,j-1)) if j>0 else 0)
            assert lhs==(d-2*k)*Fraction(K[j][k],comb(d,j)),(d,j,k,lhs)
        assert K[2][k] == K2(d,k)
    if d<=18:
        for k in range(d+1):
            for ell in range(d+1):
                lhs=sum(Fraction(K[j][k]*K[j][ell],comb(d,j)) for j in range(d+1))
                rhs=Fraction(2**d,comb(d,k)) if k==ell else 0
                assert lhs==rhs,(d,k,ell,lhs,rhs)
    zero1=[k for k in range(d+1) if K[1][k]==0]
    assert zero1==([d//2] if d%2==0 else []),(d,zero1)
    zero=[k for k in range(d+1) if K[2][k]==0]
    assert not set(zero1).intersection(zero),(d,zero1,zero)
    if d%2==0:
        p1=Fraction(comb(d,d//2),2**d)
        assert p1==Fraction(comb(d,zero1[0]),2**d)
    square=isqrt(d)**2==d
    assert zero==([(d-isqrt(d))//2,(d+isqrt(d))//2] if square else []),(d,zero)
    if square:
        survival=sum(Fraction(comb(d,k),2**d) for k in zero)
        assert survival==Fraction(2*comb(d,(d-isqrt(d))//2),2**d)
    return len(zero)

def main():
    for d in range(2,61):
        check_spectral(d)
    print('EXACT_KRAWTCHOUK_OK dimensions=2..60 orthogonality_dimensions=2..18')
    import numpy as np
    for d in (3,4,5,8,9,10,15,16):
        H=np.zeros((d+1,d+1),dtype=complex)
        for j in range(d):
            H[j,j+1]=H[j+1,j]=np.sqrt((j+1)*(d-j))
        for gamma in (0.2,1.7,10.):
            for sites in ((1,),(2,),(1,2)):
                M=H.copy()
                for a in sites: M[a,a]-=1j*gamma
                ev=np.linalg.eigvals(M)
                count=sum(abs(x.imag)<2e-7 for x in ev)
                expected= int(d%2==0) if sites==(1,) else 2*int(isqrt(d)**2==d) if sites==(2,) else 0
                assert count==expected,(d,sites,gamma,ev,count,expected)
    print('INDEPENDENT_DISSIPATIVE_SPECTRUM_OK 72 test matrices')
    from math import pi,exp,sqrt
    for s in (4,5,6,10,20):
        d=s*s
        p=float(Fraction(2*comb(d,(d-s)//2),2**d))
        asym=2*sqrt(2/(pi*d))*exp(-0.5)
        print(f'endpoint_survival d={d} exact={p:.12g} asym={asym:.12g}')
if __name__=='__main__': main()
