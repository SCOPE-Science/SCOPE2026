"""Reproducible numerical and symbolic checks of the stated Gaussian sketch identity.

All mathematical assertions about arbitrary dimensions and limits require the proof
in RESULT.md; these computations are independent finite cross-checks.
"""
from fractions import Fraction
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 65
rng = np.random.default_rng(20261102)
checks = 0

def verify(ok, label):
    global checks
    if not ok:
        raise AssertionError(label)
    checks += 1

def exact_excess(d,k,q,kappa):
    a=mp.mpf(k)/2; b=mp.mpf(d-k)/2
    t=mp.mpf(kappa)**(4*q+2)
    return (mp.mpf(kappa)**2-1)*b/(a+b)*mp.hyp2f1(1,a,a+b+1,1-t)

for d,k,q,c in [(2,1,0,5),(3,1,0,3),(3,2,1,2),(5,3,0,5),(7,2,1,3),(8,4,1,2),(5,1,2,2),(10,7,0,4)]:
    A=np.diag([c]+[1]*(d-1)).astype(float)
    for _ in range(55):
        omega=rng.normal(size=(d,k))
        Y=np.diag([c**(2*q+1)]+[1]*(d-1))@omega
        Q=np.linalg.qr(Y,mode='reduced')[0]
        err=np.linalg.norm(A-Q@(Q.T@A),ord='fro')**2
        g=omega[0,:]
        H=omega[1:,:]
        W=H.T@H
        gamma=g@np.linalg.solve(W,g)
        predicted=d-k+(c*c-1)/(1+c**(4*q+2)*gamma)
        verify(abs(err-predicted)<1e-7*max(1,err),f'projection {d,k,q,c}')

for c,q in [(1,0),(2,0),(5,0),(8,1),(3,3),(100,2)]:
    predicted=(mp.mpf(c)**2-1)/(1+mp.mpf(c)**(2*q+1))
    got=exact_excess(2,1,q,c)
    verify(abs(predicted-got)<mp.mpf('1e-42'),f'dimension two special {c,q}')

for d,k in [(3,1),(5,2),(10,3),(7,6)]:
    verify(exact_excess(d,k,0,1)==0,'isotropic matrix exact')

# Large-spike rates, all three sampling dimensions and both power-iteration regimes.
for d,k,q,c in [(7,1,0,10**6),(7,2,0,10**6),(7,3,0,10**6),
                (7,1,1,10**5),(7,2,1,10**5),(7,3,1,10**5)]:
    val=exact_excess(d,k,q,c)
    if k==1:
        constant=mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d)/2)/mp.gamma(mp.mpf(d-1)/2)
        expected=constant*mp.mpf(c)**(1-2*q)
    elif k==2:
        expected=(d-2)*(2*q+1)*mp.mpf(c)**(-4*q)*mp.log(c)
    else:
        expected=mp.mpf(d-k)/(k-2)*mp.mpf(c)**(-4*q)
    verify(abs(val/expected-1)<mp.mpf('0.12'),f'spike asymptotic {d,k,q,c}: ratio {val/expected}')
    print(f'asymptotic d={d} k={k} q={q} ratio={mp.nstr(val/expected,13)}')

# Independent quadrature against the hypergeometric closed form.
for d,k,q,c in [(2,1,1,3),(5,2,0,5),(6,3,1,2),(10,8,0,3)]:
    a=mp.mpf(k)/2; b=mp.mpf(d-k)/2
    t=mp.mpf(c)**(4*q+2)
    integrand=lambda x: x**(a-1)*(1-x)**b/(1+(t-1)*x)
    split=min(mp.mpf('0.5'),1/t)
    direct=(c*c-1)/mp.beta(a,b)*(mp.quad(integrand,[0,split])+mp.quad(integrand,[split,1]))
    formula=exact_excess(d,k,q,c)
    verify(abs(direct-formula)<mp.mpf('1e-28')*max(1,abs(direct)),f'integral {d,k,q,c}')

print(f'PASS: {checks} checks; analytic proof in RESULT.md supplies all-dimensional conclusions.')
