"""Numerical corroboration of the stated high-energy integrals.

Requires numpy and scipy. These samples corroborate, but do not replace,
the analytic high-energy expansion.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import beta

I = beta(0.25, 0.5)/4

def check(k1, k2, h, f, E=1e6):
    # V-E=(x-lo)(x-hi)Q(x), Q>0 between roots.
    # Original-time full-period quadrature is sqrt(2)*int dtheta/sqrt(Q).
    coeff = np.array([h/4,k2/3,k1/2,f,-E],float)
    roots = np.roots(coeff)
    real_roots = sorted(z.real for z in roots if abs(z.imag)<1e-7)
    assert len(real_roots)==2
    lo,hi=real_roots
    qpoly,rem=np.polydiv(coeff,np.poly([lo,hi]))
    assert np.max(np.abs(rem))<1e-3
    m,d=(hi+lo)/2,(hi-lo)/2
    w=lambda t: 1/np.sqrt(np.polyval(qpoly,m+d*np.sin(t)))
    J=quad(w,-np.pi/2,np.pi/2,epsabs=1e-12)[0]
    jplus=quad(w,np.arcsin(-m/d),np.pi/2,epsabs=1e-12)[0]
    mean=quad(lambda t:(m+d*np.sin(t))*w(t),-np.pi/2,np.pi/2)[0]/J
    T=np.sqrt(2)*J
    a=(4/h)**.25
    s=-k2/(3*h)
    L=2*np.sqrt(2)*a*I
    R=s/(a*I)
    Lhat=E**.25*T
    Rhat=E**.25*(2*jplus/J-1)
    assert abs(Lhat-L)<0.003, (Lhat,L)
    assert abs(Rhat-R)<0.006, (Rhat,R)
    assert abs(mean-s)<0.006, (mean,s)
    ahat=L/(2*np.sqrt(2)*I)
    hhat=4/ahat**4
    shat=ahat*I*R
    k2hat=-3*hhat*shat
    assert abs(h-hhat)<1e-10 and abs(k2-k2hat)<1e-10
    print(f'case={(k1,k2,h,f)}  scaled_period={Lhat:.9f} expected={L:.9f}; '
          f'scaled_signed_residence={Rhat:.9f} expected={R:.9f}; mean={mean:.9f} expected={s:.9f}')

if __name__=='__main__':
    check(-1,3,2,5)
    check(2,-2,3,-1)
    check(1,0,1,3)
    print('QUARTIC_SIGNED_RESIDENCE_INVERSE_CHECK_OK')
