"""Reproducibility checks for the finite-horizon fully actuated theta heat Gramian.
Uses Python standard library only. Finite tests supplement, not replace, the proof.
"""
from fractions import Fraction as F
from math import sin, pi, exp, expm1, log1p, isfinite


def exact_scalar_weights(lam, T, N, theta):
    k = T / N
    z = lam * k
    p = F(1, 1) + theta * z
    q = F(1, 1) - (F(1, 1) - theta) * z
    r = q / p
    direct = k / (p * p) * sum(r**(2 * j) for j in range(N))
    closed = (1-r**(2*N)) / (lam * (2+(2*theta-1)*z))
    return direct, closed


def discrete_ratio(lam, T, N, theta):
    k = T/N
    z = lam*k
    a = (2*theta-1)*z
    r = (1-(1-theta)*z)/(1+theta*z)
    # r might be negative; abs(r)<1. log(|r|) is safe for |r|>0.
    q = 0. if r==0 else -expm1(2*N*log1p(abs(r)-1))
    return 2*q / ((2+a)*(-expm1(-2*lam*T)))


def exact_spatial_lam(m,j):
    return 4*m*m*sin(j*pi/(2*m))**2


def critical_ratio(a,b,T=1.):
    return 2/(2+a)*(1-exp(-4*T*(2+a)/b)) if b>0 else 2/(2+a)


def check():
    count=0
    for lam in [F(1,2),F(3,1),F(23,7),F(113,5)]:
        for n in [1,2,3,4,5,11]:
            for theta in [F(1,2),F(3,4),F(1)]:
                d,c=exact_scalar_weights(lam,F(3,2),n,theta)
                assert d==c,(lam,n,theta,d,c)
                assert c>0
                count+=1
    for m in [32,64,128,256,512,1024,2048]:
        lam=exact_spatial_lam(m,m-1)
        cn=discrete_ratio(lam,1.,m,.5)
        assert isfinite(cn) and cn>0
        if m>=512:assert abs(cn-critical_ratio(0,4))<0.01
        be=discrete_ratio(lam,1.,m*m,1.)
        if m>=512:assert abs(be-F(1,3))<0.01
        mix=discrete_ratio(lam,1.,m,.5+1./m)
        if m>=512:assert abs(mix-critical_ratio(8,4))<0.01
        count+=3
    # Necessary collapse for a rapidly growing theta-damping parameter or CN-time step.
    for m in [512,2048,8192]:
        lam=exact_spatial_lam(m,m-1)
        cna=discrete_ratio(lam,1.,round(m**.5),.5)
        bed=discrete_ratio(lam,1.,m,1.)
        assert cna>=0 and bed>=0
        if m==8192:assert cna<0.04 and bed<0.001
        count+=2
    # Separate finite-dimensional terminal-control minimum energy: for each real
    # scalar target d, Cauchy--Schwarz minimum is d^2/W, where W is direct sum.
    for lam in [F(1,1),F(3,2),F(9,1)]:
        d=F(7,3)
        for n in [2,3,7]:
            T=F(2,1);theta=F(1,2)
            k=T/n;z=lam*k;p=1+theta*z;r=(1-(1-theta)*z)/p
            taps=[k/p*r**j for j in range(n)]
            W=sum(b*b/k for b in taps)
            u=[(d/W)*b/k for b in taps]
            end=sum(b*v for b,v in zip(taps,u))
            energy=k*sum(v*v for v in u)
            assert end==d and energy==d*d/W
            count+=1
    print('VERIFY_OK',count,'exact/modal/asymptotic/control checks')
    print('LIMIT_CN_b4',critical_ratio(0,4))
    print('LIMIT_BE_a4',critical_ratio(4,0))
    print('LIMIT_MIX_a8_b4',critical_ratio(8,4))

if __name__=='__main__':check()
