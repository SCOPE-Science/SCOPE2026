"""Numerical and symbolic checks for the coordinate-cap quadratic spectrum.

Requires Python 3, numpy, scipy, sympy, mpmath. Run: python check_axis_caps.py
No sampling test below is used as a substitute for the analytic proof.
"""
import math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.integrate import quad
from scipy.linalg import eigh

checks = 0

def verify(statement, message):
    global checks
    assert bool(statement), message
    checks += 1

# Symbolic recurrence and fourth-moment algebra are checked as identities.
d, q, B, z = sp.symbols('d q B z', positive=True)
I2 = (q+B)/d
I4 = (3*I2+z*B)/(d+2)
I02 = q-2*I2+I4
I21 = I2-I4
a = 2*(I4+3*I02/(d+1))
b = 2*(2*I21/(d-1)+(d-2)*I02/((d-1)*(d+1)))
T = (d+4)*z-3
ld = d*(d+2)*(a-b)/2
lo = d*(d+2)*b
verify(sp.simplify(ld-(2*d*q+d*d*B*T/(d*d-1)))==0, 'diagonal eigenvalue identity')
verify(sp.simplify(lo-(2*d*q-2*d*B*T/(d*d-1)))==0, 'off-diagonal eigenvalue identity')
verify(sp.simplify((d-1)*ld+d*(d-1)*lo/2 -(d*(d+1)/2-1)*2*d*q)==0, 'trace identity')
u = sp.symbols('u', positive=True)
H = u*(1-u*u)**((d-1)/2)*((d+4)*u*u-3)
quartic = (d+2)*(d+4)*u**4-6*(d+2)*u**2+3
verify(sp.simplify(sp.diff(H,u)/(1-u*u)**((d-3)/2)+quartic)==0, 'boundary-derivative identity')

for n in (3, 4, 5, 6, 9):
    cd = math.gamma(n/2)/(math.sqrt(math.pi)*math.gamma((n-1)/2))
    for t in (2**-0.5, .74, .83, .92, .975):
        f = lambda v: cd * (1-v*v)**((n-3)/2)
        J0 = quad(f,t,1,epsabs=2e-13,epsrel=1e-12)[0]
        J2 = quad(lambda v:f(v)*v*v,t,1,epsabs=2e-13,epsrel=1e-12)[0]
        J4 = quad(lambda v:f(v)*v**4,t,1,epsabs=2e-13,epsrel=1e-12)[0]
        Bv = cd*t*(1-t*t)**((n-1)/2)
        Tv = (n+4)*t*t-3
        mu = 2*n*J0
        predictedD = mu+n*n*Bv*Tv/(n*n-1)
        predictedO = mu-2*n*Bv*Tv/(n*n-1)
        # Construct all pairwise fourth moments by integrating each disjoint cap
        # and conditioning the orthogonal coordinates on the remaining sphere.
        M = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                acc = 0.0
                for k in range(n):
                    if i == j == k:
                        term = J4
                    elif i == j:
                        term = 3*(J0-2*J2+J4)/((n-1)*(n+1))
                    elif i == k or j == k:
                        term = (J2-J4)/(n-1)
                    else:
                        term = (J0-2*J2+J4)/((n-1)*(n+1))
                    acc += 2*term
                M[i,j] = acc
        M0 = np.full((n,n),1/(n*(n+2)))
        np.fill_diagonal(M0,3/(n*(n+2)))
        vectors = []
        # Independent full basis for traceless diagonal quadratic polynomials.
        for i in range(n-1):
            e = np.zeros(n);e[i]=1;e[-1]=-1
            vectors.append(('diag',e))
        G = np.array([[float(e@M@v) for _,v in vectors] for _,e in vectors])
        H0= np.array([[float(e@M0@v) for _,v in vectors] for _,e in vectors])
        eigD=eigh(G,H0,eigvals_only=True)
        verify(np.max(abs(eigD-predictedD))<2e-10, f'gram diagonal {n} {t}')
        # Odd sign characters x_i x_j are pairwise orthogonal by symmetry.
        for i in range(n):
            for j in range(i+1,n):
                ev=M[i,j]/M0[i,j]
                verify(abs(ev-predictedO)<2e-10, f'gram off-diagonal {n} {t}')
        verify(0<predictedO<predictedD<1, f'ordering and bounds {n} {t}')
        verify(abs(np.trace(G)/np.trace(H0)-predictedD)<1e-9, 'diagonal gram trace')
        verify(abs(sum(M[i,j] for j in range(n))-mu/n)<1e-10, 'radial sum')
        # Degree-one Gram is exactly mu times the full-sphere Gram.
        verify(abs(n*sum(M[0,j] for j in range(n))-mu)<1e-9, 'linear isotropy')

mp.mp.dps=80
for n in (3,4,8):
    cd=mp.gamma(mp.mpf(n)/2)/(mp.sqrt(mp.pi)*mp.gamma(mp.mpf(n-1)/2))
    for delta in (mp.mpf('1e-4'),mp.mpf('1e-6'),mp.mpf('1e-8')):
        t=mp.sqrt(1-delta);a0=mp.mpf(n-1)/2
        # Incomplete beta is independent of moment recurrence formulas.
        cap=cd/2*mp.betainc(a0,mp.mpf('0.5'),0,delta,regularized=False)
        Bb=cd*t*delta**a0
        TT=(n+4)*t*t-3
        diag=2*n*cap+n*n*Bb*TT/(n*n-1)
        off=2*n*cap-2*n*Bb*TT/(n*n-1)
        exact=diag/off
        expected=(n+1)/(4*delta)
        verify(abs(exact/expected-1)<mp.mpf('0.001'), f'asymptotic {n} {delta}')

# Direct random points on S^2, not cap-moment or incomplete-beta reduction.
rng=np.random.default_rng(78239)
N=400_000
X=rng.normal(size=(N,3));X/=np.linalg.norm(X,axis=1)[:,None]
for t in (0.72,0.84):
    E=np.max(np.abs(X),axis=1)>=t
    C=np.stack((X[:,0]**2-X[:,2]**2,X[:,1]**2-X[:,2]**2,
                X[:,0]*X[:,1],X[:,0]*X[:,2],X[:,1]*X[:,2]),axis=1)
    gram=(C[E].T@C[E])/N
    all_gram=(C.T@C)/N
    numerical=eigh(gram,all_gram,eigvals_only=True)
    n=3;cd=0.5
    cap=(1-t)/2;Bv=cd*t*(1-t*t);Tv=7*t*t-3
    diag=6*cap+9*Bv*Tv/8;off=6*cap-6*Bv*Tv/8
    expected=np.sort(np.array([diag]*2+[off]*3))
    verify(np.max(abs(numerical-expected))<.015, f'full-sphere Monte Carlo {t}')
print(f'AXIS_CAPS_SPECTRUM_CHECKS_PASS {checks}')
