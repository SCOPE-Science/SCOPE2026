"""Reproduce the covariance inversion and its independent finite-chain checks.

Usage: python verify.py
Core checks use only the Python standard library. NumPy and SciPy enable the
optional independent stationary Lyapunov matrix calculation.
"""
from fractions import Fraction as F
import math


def lam(r, m=1.0, k=1.0):
    h = math.sqrt(k/m)
    return ((math.hypot(r, 2*h) - r)/(2*h))**2


def rate(lam_value, m=1.0, k=1.0):
    return math.sqrt(k/m)*(1-lam_value)/math.sqrt(lam_value)


def covariance(d, r1, r2, D=1.0, k=1.0, m=1.0, gamma=1.0):
    return (D*k/gamma)*sum(
        lam(r,m,k)**(d+1)/(1-lam(r,m,k)**2) for r in (r1,r2)
    )


def invert(C0,C1,D=1.0,k=1.0,m=1.0,gamma=1.0):
    K=D*k/gamma
    s,t=C0/K,C1/K
    lower=math.hypot(1,s)-1
    upper=(math.hypot(1,2*s)-1)/2
    assert s>0 and lower-1e-12<=t<upper+1e-12
    c=math.atanh(s/(1+t))
    h=math.acosh(max(1.,math.sqrt((1+t)**2-s*s)))
    lams=[math.tanh((c+h)/2),math.tanh((c-h)/2)]
    return sorted(rate(l,m,k) for l in lams)


def integrate(f, n=16000):
    assert n%2==0
    step=math.pi/n
    return step/3*(f(0)+f(math.pi)+sum(
        (4 if j%2 else 2)*f(j*step) for j in range(1,n)))


def checks():
    # Exact rational identities in the exponential-mode parameterization.
    for a,b in [(F(1,4),F(3,4)),(F(1,2),F(1,2)),
                (F(1,3),F(5,7)),(F(1,10),F(9,10))]:
        coeff=lambda l: l/(1-l*l)
        for d in range(7):
            expected=sum((l**(d+1)/(1-l*l) for l in (a,b)),F(0))
            calculated=coeff(a)*a**d+coeff(b)*b**d
            assert expected==calculated

    # Global inversion, equal-rate boundary and the full feasible corridor.
    cases=0
    for r1 in [0.03,0.2,0.5,1.2,2.0,10.,50.]:
        for r2 in [0.06,0.2,1.7,3.7,12.,50.]:
            C0,C1=covariance(0,r1,r2),covariance(1,r1,r2)
            rates=invert(C0,C1)
            for recovered, true in zip(rates,sorted((r1,r2))):
                assert abs(recovered-true)<2e-6*true
            s,t=C0,C1
            assert math.hypot(1,s)-1-1e-10<=t
            assert t<(math.hypot(1,2*s)-1)/2+1e-10
            cases+=1
    for r in [0.2,0.5,1.,3.,10.]:
        s,t=covariance(0,r,r),covariance(1,r,r)
        assert abs(t-(math.hypot(1,s)-1))<1e-12
    for r in [.2,1.,10.]:
        q=lam(r)
        for d in [0,1,2,3,5]:
            numerical=integrate(lambda z: math.cos(d*z)/(r*r+2-2*math.cos(z)))
            formula=math.pi*q**d/(r*math.sqrt(r*r+4))
            assert abs(numerical-formula)<2e-10

    print('PASS: exact rational mode coefficients,',cases,
          'inverse rate pairs, sharp corridor and Fourier quadratures')
    try:
        import numpy as np
        from scipy.linalg import solve_continuous_lyapunov
    except ImportError:
        print('SKIP: optional finite-chain Lyapunov check requires numpy, scipy')
        return
    N=50
    r1,r2=1.2,3.7
    M=np.zeros((2*N+2,2*N+2))
    M[:N,N:2*N]=np.eye(N)
    stiffness=2*np.eye(N)-np.eye(N,k=1)-np.eye(N,k=-1)
    M[N:2*N,:N]=-stiffness
    M[N,N]=-1; M[2*N-1,2*N-1]=-1
    M[N,2*N]=1; M[2*N-1,2*N+1]=1
    M[2*N,2*N]=-r1; M[2*N+1,2*N+1]=-r2
    Q=np.zeros_like(M)
    Q[2*N,2*N]=4; Q[2*N+1,2*N+1]=4
    # Brownian resetting walls and these OU walls have the same two-time
    # covariance; this is sufficient for all linear-chain second moments.
    Sigma=solve_continuous_lyapunov(M,-Q)
    error=0.
    for d in (0,1,2,3,5,8):
        error=max(error,abs(Sigma[N+N//2,N+N//2+d]-covariance(d,r1,r2)))
    assert error<1e-6,error
    print('PASS: independent 50-site stationary Lyapunov comparison; max error',error)

if __name__=='__main__':
    checks()
