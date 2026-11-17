"""Finite numerical diagnostics for factorial-shift secular spectral ladders.

The infinite statements require the analytic proof; these tests are consistency checks.
Run: python check_spectral_ladders.py
"""
import math
import cmath
import numpy as np


def coeff(m, a, j):
    return cmath.exp(j * cmath.log(a) + math.lgamma(m * j) / m - math.lgamma(j + 1))


def test(m, a, alpha, size=50):
    weights = np.array([n ** (-1/m) for n in range(1, size)], dtype=float)
    S = np.zeros((size, size), dtype=complex)
    for n, w in enumerate(weights):
        S[n + 1, n] = w
    gamma = np.zeros(size, dtype=complex)
    for j in range(1, (size - 1)//m + 1):
        gamma[m*j-1] = coeff(m, a, j)
    F = np.outer(np.eye(size, dtype=complex)[:, 0], gamma)
    assert np.linalg.norm(F@F) < 1e-12
    A = S + alpha * F
    sing_s = np.linalg.svd(S, compute_uv=False)
    sing_a = np.linalg.svd(A, compute_uv=False)
    for n in range(2, size):
        assert sing_s[n] - 1e-10 <= sing_a[n-1] <= sing_s[n-2] + 1e-10
    # The truncated secular function is the exact finite matrix determinant condition.
    for z in [0.3, 0.5+0.3j, 1.3-0.4j]:
        poly = sum((a*z**m)**j/math.factorial(j) for j in range(1,(size-1)//m+1))
        assert abs(poly-(cmath.exp(a*z**m)-1)) < 2e-10
        series = sum(gamma[k] * z**(k+1)/math.exp(math.lgamma(k+1)/m) for k in range(size))
        assert abs(poly-series) < 1e-10
        lam=1/z
        detratio=np.linalg.det(lam*np.eye(size)-A)/np.linalg.det(lam*np.eye(size)-S)
        assert abs(detratio-(1-alpha*series)) < 2e-9
    beta=1+1/alpha
    logbeta=cmath.log(beta)
    for k in [-3,-1,0,1,3]:
        z=((logbeta+2j*math.pi*k)/a)**(1/m)
        assert abs(1-alpha*(cmath.exp(a*z**m)-1)) < 1e-9
    for radius in [.08,.1,.15]:
        R=abs(a)*radius**(-m)
        kmax=max(10,math.ceil((R+abs(logbeta))/(2*math.pi))+3)
        count=m*sum(abs(logbeta+2j*math.pi*k)<=R for k in range(-kmax,kmax+1))
        predicted=m*abs(a)*radius**(-m)/math.pi
        assert abs(count-predicted)<4*m
    return float(sing_a[-3]),float(sing_a[-1])


def main():
    completed=0
    for m in (2,3,4):
        for a in (1/(2*m), 1/m):
            for alpha in (1, 2, 0.6+0.5j):
                test(m,a,alpha)
                completed+=1
    for m in range(2,10):
        # boundary coefficient square-summability: asymptotic exponent check.
        arr=[abs(coeff(m,1/m,j)) for j in range(40,101)]
        ratio=arr[-1]/arr[-2]
        expected=(100/99)**(-(m+1)/(2*m))
        assert abs(ratio-expected)<.00015
        completed+=1
    print(f'PASS: {completed} distinct parameter checks; secular equations, rank-one nilpotence, singular interlacing, counting, endpoint coefficient decay.')

if __name__ == '__main__':
    main()
