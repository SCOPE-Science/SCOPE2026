"""Independent numerical/identity checks for a fixed-area radial Fock minimax theorem.

All analytic universal statements are proved in RESULT.md; these finite tests
probe signs, endpoint reduction, unique placement and asymptotic constants.
Requires Python 3, scipy, numpy, and mpmath.
"""
from math import exp, e, factorial, lgamma, log, pi
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

COUNT=0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def mass(n, a, L):
    # Nonnegative numerical integrand; stable even for fairly large n.
    return exp(-a)*quad(lambda s: exp(n*log(a+s)-lgamma(n+1)-s) if a+s>0 else 0, 0, L, epsabs=1e-12, epsrel=2e-12)[0]

def cross(N,L):
    C=-np.expm1(-L)
    def ratio(a):
        return quad(lambda s: exp(N*log(a+s)-lgamma(N+1)-s) if a+s>0 else 0,0,L,epsabs=1e-12,epsrel=2e-12)[0]/C-1
    return brentq(ratio,0,max(N+3,L+3),xtol=1e-12)

for N in range(1,13):
    for L in (0.08,0.2,0.7,1.5,3,5,9):
        a=cross(N,L)
        c=L/np.expm1(L/N)
        check(a>0 and a<=c+1e-9, f'location N={N},L={L}')
        check(abs(mass(N,a,L)-mass(0,a,L))<2e-9, f'endpoint equality N={N},L={L}')
        seq=[mass(n,a,L) for n in range(N+1)]
        check(all(x>=seq[0]-2e-9 for x in seq),f'all-mode bottleneck N={N},L={L}')
        for u in (0,0.3*a,0.7*a,1.4*a,a+c+0.1,2*c+1):
            test=[mass(n,u,L) for n in range(N+1)]
            check(min(test) <= seq[0]+2e-9,f'global bound N={N},L={L},a={u}')
        # Recurrence gives the exact eigenvalue differences; verify quadrature.
        for k in range(1,N+1):
            rhs=exp(-a)*a**k/factorial(k)-exp(-(a+L))*(a+L)**k/factorial(k)
            check(abs(seq[k]-seq[k-1]-rhs)<3e-9,f'recurrence N={N},L={L},k={k}')

for L in (0.2,1.,4.):
    J=np.expm1((e-1)*L)/((e-1)*(-np.expm1(-L)))
    for N in (50,100,500):
        a=cross(N,L)
        approx=N/e+log(2*pi*N)/(2*e)-log(J)/e
        check(abs(a-approx)<0.5, f'asymptotic numeric N={N},L={L}')
        if N==500:
            check(abs(a-approx)<0.03,f'large index sharpness L={L}')

for N in (1,2,3,5,10):
    L=0.001
    a=cross(N,L)
    approx=factorial(N)**(1/N)-L/2
    check(abs(a-approx)<1e-5,f'small area N={N}')

print(f'PASS: {COUNT} deterministic exact-identity/numerical consistency assertions')
