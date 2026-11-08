"""Reproducibility checks for a harmonic Gaussian HMC quadratic-correlation design.

The universal statement is proved analytically in RESULT.md. These finite checks
exercise exact weight constraints and numerical Fourier/eigenspace identities.
"""
from fractions import Fraction
from math import cos, pi, isclose


def close(a, b, tol=3e-12):
    assert isclose(a, b, rel_tol=0.0, abs_tol=tol), (a, b)


def check(K):
    N = K + 1
    p = [Fraction(1, K)] * K
    assert sum(p) == 1
    assert sum(Fraction(j, N)*p[j-1] for j in range(1,N)) == Fraction(1,2)
    target = Fraction(K-1, 2*K)
    moments = []
    for j in range(1, N):
        rho = sum(float(p[m-1])*cos(pi*j*m/N)**2 for m in range(1,N))
        close(rho, float(target)); moments.append(rho)
    for i in range(1, N):
        for j in range(i+1,N):
            gamma = sum(float(p[m-1])*cos(pi*i*m/N)*cos(pi*j*m/N) for m in range(1,N))
            assert abs(gamma) <= float(target)+3e-12
            if (i-j)%2:
                close(gamma,0)
            else:
                close(gamma,-1/K)
    tau = (1+float(target))/(1-float(target))
    close(tau, (3*K-1)/(K+1))
    return target


def asymmetric(K):
    # N>=5. Construct the affine line of equal-cost nonsymmetric minimizers.
    assert K >= 4
    N=K+1
    u=Fraction(N-4, 4*K*(N-2))
    delta=[Fraction(0)]*(N+1)
    delta[1]=u; delta[N-1]=-u
    delta[2]=-Fraction(N-2,N-4)*u; delta[N-2]=-delta[2]
    p=[Fraction(1,K)+delta[j] for j in range(1,N)]
    assert min(p)>0
    assert sum(p)==1
    assert sum(Fraction(j,N)*p[j-1] for j in range(1,N)) == Fraction(1,2)
    assert any(p[j]!=Fraction(1,K) for j in range(K))
    for j in range(1,N):
        close(sum(float(p[m-1])*cos(pi*j*m/N)**2 for m in range(1,N)), (K-1)/(2*K))
    for i in range(1,N):
        for j in range(i+1,N):
            gamma=sum(float(p[m-1])*cos(pi*i*m/N)*cos(pi*j*m/N) for m in range(1,N))
            assert abs(gamma)<=(K-1)/(2*K)+3e-12
    return p


def sample_fejer(K, T):
    # Elementary Fejer certificate for a point mass, plus its spectral bound.
    N=K+1
    cs=[cos(2*j*T) for j in range(1,N)]
    f=N+2*sum((N-j)*cs[j-1] for j in range(1,N))
    real=sum(cos(2*j*T) for j in range(N))
    imag=sum(__import__('math').sin(2*j*T) for j in range(N))
    close(f,real*real+imag*imag,2e-11)
    assert max(cs)>= -1/K-3e-12


if __name__=='__main__':
    tests=0
    for K in range(1,19):
        check(K); tests+=1
        for l in range(17):
            sample_fejer(K,pi*(l+0.31)/18); tests+=1
        if K>=4:
            asymmetric(K); tests+=1
    print('PASS: %d deterministic test groups; K=1..18; all-covariance quadratic moments, exact mean and root-of-unity checks.'%tests)
    print('K=2 optimal rho=1/4; maximal integrated autocorrelation=5/3.')
    print('K=3 optimal rho=1/3; maximal integrated autocorrelation=2.')
    print('K=4 optimal rho=3/8; maximal integrated autocorrelation=11/5; nonsymmetric optima exist.')
