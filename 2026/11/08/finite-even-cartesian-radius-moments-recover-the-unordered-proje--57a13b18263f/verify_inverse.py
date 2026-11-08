"""Supplementary numerical diagnostics for finite unitary phase-gap moment identities.

This is not a proof of finite determinacy. Run: python verify_inverse.py
"""
from math import pi, sin, cos, comb
import random


def moment_from_gaps(gaps, k):
    return comb(2*k, k)/4**k + 2/(pi*4**k)*sum(
        comb(2*k, k-j)*sum(sin(j*g) for g in gaps)/j
        for j in range(1, k+1))


def moment_quadrature(gaps, k, n=24000):
    angles = [0.]
    for g in gaps[:-1]:
        angles.append(angles[-1]+g)
    return sum(max(abs(cos(pi*(a+.5)/n-b)) for b in angles)**(2*k)
               for a in range(n))/n


def reconstruct_sine_moments(moments):
    out=[]
    for k, mk in enumerate(moments, 1):
        s = (pi*4**k/2)*(mk-comb(2*k,k)/4**k)
        s -= sum(comb(2*k,k-j)*out[j-1]/j for j in range(1,k))
        out.append(k*s)
    return out


def cheb_u(j, x):
    if j==0:return 1.
    if j==1:return 2*x
    a,b=1.,2*x
    for _ in range(2,j+1):a,b=b,2*x*b-a
    return b


def checks():
    trials=0
    rng=random.Random(72641)
    for m in range(1,8):
        for _ in range(14):
            x=[rng.random()+.08 for j in range(m)]
            gaps=[pi*t/sum(x) for t in x]
            moments=[moment_from_gaps(gaps,k) for k in range(1,min(9,2*m+1))]
            reconstructed=reconstruct_sine_moments(moments)
            for j,s in enumerate(reconstructed, 1):
                expected=sum(sin(j*g) for g in gaps)
                assert abs(s-expected)<1e-6*(1+abs(expected)), (m,j,s,expected)
                moment=sum(sin(g)*cheb_u(j-1,cos(g)) for g in gaps)
                assert abs(moment-expected)<1e-6*(1+abs(expected))
                trials+=2
            for k in (1,2,3,4):
                analytic=moment_from_gaps(gaps,k)
                numerical=moment_quadrature(gaps,k,n=3000)
                assert abs(analytic-numerical)<1e-5, (m,k,analytic,numerical)
                trials+=1
    a=[pi/10,2*pi/10,3*pi/10,4*pi/10]
    b=[pi/10,3*pi/10,2*pi/10,4*pi/10]
    for k in range(1,13):
        assert abs(moment_from_gaps(a,k)-moment_from_gaps(b,k))<1e-12
        trials+=1
    aa={0,1,3,6};bb={0,1,4,6}
    assert all({(sgn*j+shift)%10 for j in aa}!=bb
               for sgn in [-1,1] for shift in range(10))
    trials+=1
    print(f"PASS: {trials} numerical and algebraic consistency assertions")

if __name__=='__main__':checks()
