"""Independent direct-matrix and reentrant-phase checks.
Run with: python verify_numeric.py (requires NumPy, SciPy).
"""
import numpy as np
from scipy.optimize import brentq

def T(u,k):
    return u*((u*u-k)**2+2*k)/(u*u+k)
def G(u,k):
    return u*u*(u*u-k-1)**2*((u*u-k)**2+2*k+2*u*u)/(u*u+k)**2

def full_H(m,t,g):
    H=np.zeros((m+1,m+1),complex)
    H[0,0]=1j*g; H[1,1]=-1j*g
    H[0,1]=H[1,0]=t
    for j in [0,1]+list(range(3,m+1)):
        H[2,j]=H[j,2]=1
    return H

for m in range(3,17):
    k=m-2
    y=-k+np.sqrt(k*(4*k+2)/3)
    ustar=np.sqrt(y)
    tstar=4*y**1.5
    t_low=np.sqrt(k)
    assert t_low<tstar
    # Select a coupling in the nonempty universal reentrant interval.
    t=(t_low+min(tstar,np.sqrt(k+1)))/2
    u1=brentq(lambda u:T(u,k)-t,1e-10,ustar)
    u2=brentq(lambda u:T(u,k)-t,ustar,np.sqrt(k))
    umax=max(2*t+2,2*np.sqrt(k)+2)
    u3=brentq(lambda u:T(u,k)-t,np.sqrt(k),umax)
    gs=sorted(np.sqrt([G(z,k) for z in (u1,u2,u3)]))
    assert gs[0]>0 and gs[1]-gs[0]>1e-6 and gs[2]-gs[1]>1e-6,(m,gs)
    probes=[0,(gs[0]+gs[1])/2,(gs[1]+gs[2])/2,gs[2]+1]
    expected=[m+1,m-1,m+1,m-1]
    for g,count in zip(probes,expected):
        vals=np.linalg.eigvals(full_H(m,t,g))
        num=np.count_nonzero(np.abs(vals.imag)<1e-6)
        assert num==count,(m,g,count,num)
        p=lambda x:x**4+(g*g-t*t-m)*x*x-2*t*x+(m-2)*(t*t-g*g)
        # Every eigenvalue obeys the exact full characteristic polynomial.
        assert max(abs((v**(m-3))*p(v)) for v in vals)<3e-4*(1+max(abs(vals))**(m+1))
    # Third-order point: cubic factorization and a one-dimensional eigenspace.
    gstar=np.sqrt(16*y**3+m-6*y)
    H=full_H(m,tstar,gstar)
    singular=np.linalg.svd(H+np.sqrt(y)*np.eye(m+1))[1]
    # m-3 dark directions are not at the nonzero exceptional eigenvalue.
    assert np.sum(singular<1e-7)==1,(m,singular)
    # Characteristic coefficients on bright block agree with exact cubic factor.
    a=np.poly([-np.sqrt(y)]*3+[3*np.sqrt(y)])
    b=[1,0,gstar*gstar-tstar*tstar-m,-2*tstar,(m-2)*(tstar*tstar-gstar*gstar)]
    assert np.allclose(a,b,rtol=1e-8,atol=1e-7),(m,a,b)
print('PASS: direct Hamiltonians m=3..16 have four-two-four-two phase pattern, unique EP3 eigendirection and cubic coefficients')
