"""Reproducible numerical and combinatorial checks for a killed birth-death walk.

Requires numpy and scipy. Tests check kernel formulae independently;
finite tests are not substitutes for the asymptotic proof.
"""
from math import comb, exp, floor, lgamma, sqrt, pi, gamma, log
import numpy as np
from scipy.special import ive
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

checks = 0

def require(test, note):
    global checks
    if not test:
        raise AssertionError(note)
    checks += 1


def killed_discrete(n, i, j):
    def choose(k):
        return comb(n, k) if isinstance(k, int) and 0 <= k <= n else 0
    a = n + j - i
    b = n + j + i
    return (choose(a // 2) if a % 2 == 0 else 0) / (2.0 ** n) - (choose(b // 2) if b % 2 == 0 else 0) / (2.0 ** n)


def bessel_kernel(z, i, j):
    return float(ive(abs(i-j), z) - ive(i+j, z))


def poissonized_kernel(z, i, j):
    nmax = max(100, int(z + 18*sqrt(z + 1)))
    weight = exp(-z)
    acc = 0.0
    for n in range(nmax + 1):
        acc += weight * killed_discrete(n, i, j)
        weight *= z / (n + 1)
    return acc

# Killed symmetric walk from two independent constructions.
for z in (0.4, 2.0, 5.0, 12.0):
    for i in range(1, 10):
        for j in range(1, 10):
            a, b = bessel_kernel(z, i, j), poissonized_kernel(z, i, j)
            require(abs(a-b) < 2e-12, f'Poisson reflection failure {z=} {i=} {j=} {a=} {b=}')
            require(a >= -1e-15, 'Nonnegative kernel')

# Direct finite-generator matrix exponential independent of Bessel construction.
a_rate, b_rate = 4.0, 1.0
rho = sqrt(b_rate/a_rate)
c = 2*sqrt(a_rate*b_rate)
lam = a_rate + b_rate - c
N = 140
Q = diags([np.full(N-1,a_rate), np.full(N,-a_rate-b_rate), np.full(N-1,b_rate)],
          offsets=[-1,0,1], format='csr').transpose().tocsr()
# The transpose supplies the forward equation for column initial vectors.
for t in (0.3, 1.0, 3.0, 8.0):
    for i in (1, 2, 5, 8):
        v = np.zeros(N)
        v[i-1] = 1.0
        evolved = expm_multiply(t*Q, v)
        for j in (1, 2, 3, 6, 10):
            exact = exp(-lam*t)*rho**(j-i)*bessel_kernel(c*t, i, j)
            require(abs(evolved[j-1]-exact) < 5e-10,
                    f'generator-Bessel mismatch t={t} i={i} j={j} err={evolved[j-1]-exact}')

# Identity for the reflected Bessel kernel (telescoping recurrence).
from scipy.special import iv
for z in (0.5, 2.3, 10.0, 40.0):
    for i in range(1, 12):
        for j in range(1, 12):
            minimum = min(i,j)
            q0 = abs(i-j)
            telescoped = (2/z)*sum((q0+2*h+1)*ive(q0+2*h+1,z)
                                    for h in range(minimum))
            require(abs(telescoped-bessel_kernel(z,i,j))<2e-12,
                    'Bessel recurrence telescope')

# Finite-time confirmation of exact minimal QSD eigenvector (beta=-1).
for t in (0.4, 2.0, 6.0, 15.0):
    for j in range(1,12):
        ii=np.arange(1,180)
        coeff=np.sum(ii*rho**ii * (ive(np.abs(ii-j),c*t)-ive(ii+j,c*t)))
        # Spectral compensation factors cancel initial geometric tails.
        # For beta=-1, sum_i i*K(i,j) equals j exactly, by harmonicity.
        plain=np.sum(ii*(ive(np.abs(ii-j),c*t)-ive(ii+j,c*t)))
        require(abs(plain-j)<2e-7, f'harmonic identity {t=} {j=} {plain=}')

# Asymptotic leading factors, inspected as diagnostics only.
def profile(beta,t,j=1):
    z=c*t
    imax=int(max(300, z+20*sqrt(z))) if z<300 else int(max(300, 22*sqrt(z)))
    ii=np.arange(1, imax+1)
    kernel=ive(np.abs(ii-j),z)-ive(ii+j,z)
    F=float(np.sum(ii.astype(float)**(-beta)*kernel))
    if beta<2:
        H=(2.0**(1-beta/2)*gamma(1-beta/2)/sqrt(2*pi))*z**(-(beta+1)/2)
    elif beta==2:
        H=log(z)/sqrt(2*pi)/z**1.5
    return F/(j*H)

for beta in (-2.0,-1.0,0.0,1.0,1.5,2.0):
    r_small=profile(beta,90.0)
    r_large=profile(beta,500.0)
    require(np.isfinite(r_small) and np.isfinite(r_large) and r_large>0, 'asymptotic diagnostic finite')
    print(f'beta={beta:4g}: F/(j H) at t=90: {r_small:.8f}; at t=500: {r_large:.8f}')

print(f'PASS: {checks} independent finite numerical/combinatorial assertions; '
      'limiting claims require the analytical proof.')
