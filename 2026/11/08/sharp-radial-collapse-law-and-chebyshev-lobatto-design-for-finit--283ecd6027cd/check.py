"""Numerical checks for finite coherent-state radial sampling asymptotics.

Run with: python3 check.py
Requires numpy. These tests support, but do not replace, the analytic proof.
"""
import math
import numpy as np

COUNT = 0

def check(ok, message):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(message)

def matrix(n, t, u, w, eps, M=None):
    M = (2*n-1) if M is None else M
    output=[]
    for j, x in enumerate(t+eps*u):
        for ell in range(M):
            z = np.sqrt(x)*np.exp(2j*np.pi*ell/M)
            v = np.array([z**k/math.sqrt(math.factorial(k)) for k in range(n)])
            row = [abs(v[k])**2 for k in range(n)]
            for d in range(1, n):
                for k in range(n-d):
                    product = v[k].conjugate()*v[k+d]
                    row.extend([math.sqrt(2)*product.real, math.sqrt(2)*product.imag])
            output.append(math.sqrt(w[j]/M)*math.exp(-x)*np.array(row))
    return np.array(output)

def coefficients(n,t):
    return np.array([math.factorial(k)*math.comb(n-1,k)*(-t)**(n-1-k)
                     for k in range(n)], dtype=float)

def asymptotic(n,t,u,w):
    products = np.array([math.prod(u[j]-u[i] for i in range(n) if i!=j)
                         for j in range(n)])
    S=np.linalg.norm(coefficients(n,t))
    A=math.sqrt(sum(t**(2*k)/math.factorial(k)**2 for k in range(n)))
    beta=math.sqrt(sum(1/(w[j]*products[j]**2) for j in range(n)))
    return math.exp(-t)/(S*beta), math.exp(-t)*A

def cheb(n):
    u=np.array(sorted(math.cos(math.pi*j/(n-1)) for j in range(n)))
    w=np.ones(n)/(n-1)
    w[0]*=.5
    w[-1]*=.5
    return u,w

for n in range(2,7):
    t=0.5+0.25*n
    u,w=cheb(n)
    c,top=asymptotic(n,t,u,w)
    ideal=math.exp(-t)*2**(2-n)/np.linalg.norm(coefficients(n,t))
    check(abs(c/ideal-1)<2e-10, f'Chebyshev exact coefficient n={n}')
    check(abs(w.sum()-1)<1e-14, f'weights n={n}')
    for j in range(n):
        check(abs(u[j]-math.cos(math.pi*(n-1-j)/(n-1)))<1e-13, 'extrema')
    # Singular values tested at separations that remain stable in double precision.
    for eps in ([.12, .05, .02] if n<=4 else [.19, .14]):
        sv=np.linalg.svd(matrix(n,t,u,w,eps),compute_uv=False)
        check(len(sv)==n*n and sv[-1]>0, f'rank n={n}')
        ratio=sv[-1]/(eps**(n-1)*c)
        # Relative error is O(eps), and symmetry of this design improves to O(eps^2).
        check(abs(ratio-1)<.15, f'small singular asymptotic n={n} eps={eps} {ratio}')
        check(abs(sv[0]/top-1)<.07, f'largest singular n={n} eps={eps}')
    if n<=4:
        eps=.05
        for a in range(6):
            rng=np.random.default_rng(n*100+a)
            u1=np.sort(rng.uniform(-1,1,n))
            v=rng.uniform(.05,1,n)
            w1=v/v.sum()
            c1,_=asymptotic(n,t,u1,w1)
            check(c1<=ideal*(1+1e-9), 'Chebyshev optimality')
            sv=np.linalg.svd(matrix(n,t,u1,w1,eps),compute_uv=False)
            # Explicit rank and positivity, independent of asymptotics.
            check(sv[-1]>1e-15, 'finite-epsilon informational completeness')

print(f'RADIAL_FOCK_TOMOGRAPHY_CHECKS_PASS {COUNT}')
