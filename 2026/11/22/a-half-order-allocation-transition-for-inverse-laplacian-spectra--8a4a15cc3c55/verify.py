"""Reproducible numerical diagnostics for inverse spectral moments on cyclic prisms.

Dependencies: Python 3.10+, NumPy and SciPy. This script checks finite examples;
the statements for infinite graph families are proved analytically in RESULT.md.
"""
from math import pi, sin, sqrt, gamma, log, isclose
import numpy as np
from scipy.optimize import brentq
from scipy.special import zeta
from scipy.integrate import quad

checks = 0

def ck(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1


def wavelengths(m):
    return np.array([4*sin(pi*k/m)**2 for k in range(m)],dtype=float)


def stationarity(m,p,t):
    z=wavelengths(m)
    S=np.sum(z[1:]**(-p))
    R=np.sum((4-z)/(z+2*t)**(p+1))
    return R-S


def optimal_ratio(m,p):
    return brentq(lambda t: stationarity(m,p,t), 1e-13, 100.,xtol=1e-14)


def objective(m,p,t):
    z=wavelengths(m)
    return (m*(2+t))**p*(np.sum(z[1:]**(-p))+np.sum((z+2*t)**(-p)))


def matrix_laplacian(m,t):
    a=1/(m*(2+t)); b=t*a
    L=np.zeros((2*m,2*m))
    for i in range(m):
        for layer in range(2):
            j=(i+1)%m
            u=layer*m+i; v=layer*m+j
            L[u,u]+=a; L[v,v]+=a
            L[u,v]-=a; L[v,u]-=a
        u=i; v=m+i
        L[u,u]+=b; L[v,v]+=b
        L[u,v]-=b; L[v,u]-=b
    return L


def continuum_limit(p):
    I=4**(-p)*gamma(.5-p)/(sqrt(pi)*gamma(1-p))
    def rhs(t):
        def f(x):
            lam=4*sin(pi*x)**2
            return (4-lam)/(lam+2*t)**(p+1)
        return quad(f,0,.5,epsabs=1e-11,epsrel=1e-11)[0]*2
    return brentq(lambda t: rhs(t)-I,1e-9,100)


def high_order_constant(p):
    C=2*zeta(2*p)/(4*pi*pi)**p
    D=2**(.5-p)*gamma(p+.5)/(sqrt(pi)*gamma(p+1))
    beta=(2*p-1)/(p+.5)
    return beta, (D/C)**(1/(p+.5))

# Exact spectral representation and global one-dimensional minimizer.
for m in range(3,17):
    for p in (.1,.25,.5,.75,1,1.5,2,3,5):
        t=optimal_ratio(m,p)
        ck(t>0, f'nonpositive t: m={m},p={p}')
        ck(abs(stationarity(m,p,t)) < 1e-6*sum(wavelengths(m)[1:]**(-p)), 'stationarity')
        for tt in (t/3.,t/2.,t*1.5,t*3.):
            ck(objective(m,p,t)<objective(m,p,tt), 'unique minimum finite check')
    for t in (.05,.2,.7,1.3,5.):
        L=matrix_laplacian(m,t)
        ev=np.linalg.eigvalsh(L)
        a=1/(m*(2+t))
        z=wavelengths(m)
        expected=sorted(list(a*z[1:])+list(a*(z+2*t)))
        ck(np.allclose(ev[1:],expected,atol=1e-11,rtol=1e-10), 'spectrum check')
        for p in (.5,1,2,3):
            ck(isclose(np.sum(ev[1:]**(-p)),objective(m,p,t),rel_tol=2e-8), 'trace check')

# Finite-difference derivative vs exact stationarity equation.
for m in (3,4,5,7,11,17):
    for p in (.1,.5,1,2,3):
        for t in (.25,.7,1.4):
            h=1e-5*min(1.,t)
            D=(objective(m,p,t+h)-objective(m,p,t-h))/(2*h)
            z=wavelengths(m)
            S=np.sum(z[1:]**(-p))
            H=np.sum((z+2*t)**(-p))
            exact=p*(m*(2+t))**p/(2+t)*(S+H-2*(2+t)*np.sum((z+2*t)**(-p-1)))
            ck(isclose(D,exact,rel_tol=1e-5,abs_tol=1e-5),'derivative')

# Asymptotics in the three regimes, without confusing finite checks with proofs.
for p in (.1,.25):
    target=continuum_limit(p)
    ck(abs(optimal_ratio(12000,p)/target-1)<.03,'subcritical asymptotic')
for m in (10000,25000):
    s=optimal_ratio(m,.5)*log(m)/2
    ck(.80<s<1.05,'critical logarithmic scale')
for p in (.75,1,1.5,2,3,4):
    beta,c=high_order_constant(p)
    m=10000
    ck(abs(optimal_ratio(m,p)*m**beta/c-1)<.015,'supercritical asymptotic')
ck(isclose(high_order_constant(1)[1],18**(1/3),rel_tol=1e-13),'p=1 exact constant')
ck(isclose(high_order_constant(2)[1],540**(.4)/2,rel_tol=1e-13),'p=2 exact constant')
ck(abs(continuum_limit(.499)/(2*(1-2*.499))-1)<.045,'near-critical continuum amplitude')

# Check the actual full Laplacian objective against random asymmetric competitors.
rng=np.random.default_rng(1047)
for m in (3,4,5,7):
    for p in (.5,1,2):
        t=optimal_ratio(m,p)
        opt=objective(m,p,t)
        for _ in range(16):
            weights=rng.random(3*m)+.002
            weights/=weights.sum()
            L=np.zeros((2*m,2*m))
            idx=0
            for i in range(m):
                for layer in range(2):
                    u=layer*m+i; v=layer*m+(i+1)%m; w=weights[idx];idx+=1
                    L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
                u=i;v=m+i;w=weights[idx];idx+=1
                L[u,u]+=w; L[v,v]+=w; L[u,v]-=w; L[v,u]-=w
            ev=np.linalg.eigvalsh(L)
            ck(np.sum(ev[1:]**(-p))>=opt*(1-2e-9),'asymmetric challenger')
print('PASS',checks,'finite diagnostics')
