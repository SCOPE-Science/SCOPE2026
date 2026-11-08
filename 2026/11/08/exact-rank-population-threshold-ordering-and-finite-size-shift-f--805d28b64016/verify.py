"""Independent numeric checks for the finite-population first-passage sensitivity law.

Run: python verify.py. Requires scipy, numpy, mpmath. Numeric checks are not a proof.
"""
import math
import numpy as np
from scipy.special import erfinv, erfc, roots_jacobi
from scipy.optimize import brentq
import mpmath as mp
mp.mp.dps = 42

def H_mp(t):
    z=mp.sqrt(t)
    return (2*z/mp.sqrt(mp.pi)*(mp.exp(-1/(4*t))-mp.exp(-1/t))
       -(t+1)*mp.erfc(1/(2*z))+(t+2)*mp.erfc(1/z))

def Hp_mp(t):
    return (-mp.erfc(1/(2*mp.sqrt(t)))+mp.erfc(1/mp.sqrt(t))
            +mp.exp(-1/(4*t))/(2*mp.sqrt(mp.pi*t)))

def Hpp_mp(t):
    return (mp.exp(-1/(4*t))/(2*mp.sqrt(mp.pi)*t**mp.mpf('1.5'))
         *(1/(4*t)-mp.mpf('1.5')+2*mp.exp(-3/(4*t))))

def a_mp(t):
    return mp.exp(-1/(4*t))/(2*mp.sqrt(mp.pi)*t**mp.mpf('1.5'))

def G_np(q):
    x=np.asarray(q)
    t=1/(4*erfinv(x)**2)
    z=np.sqrt(t)
    h=(2*z/np.sqrt(np.pi)*(np.exp(-1/(4*t))-np.exp(-1/t))
       -(t+1)*erfc(1/(2*z))+(t+2)*erfc(1/z))
    a=np.exp(-1/(4*t))/(2*np.sqrt(np.pi)*t**1.5)
    return np.where(a>1e-270,h/a,0.0)

def S(N,k,nodes=144):
    # Inverse-Beta change of variable. Gaussian Jacobi quadrature with
    # density proportional to (1-x)^(k-1)*(1+x)^(N-k).
    x,w=roots_jacobi(nodes, k-1, N-k)
    return float(np.sum(w*G_np((x+1)/2))/np.sum(w))

u=mp.findroot(H_mp, (mp.mpf('.65'),mp.mpf('.85')))
assert mp.mpf('.74')<u<mp.mpf('.75')
phi=mp.erfc(1/(2*mp.sqrt(u)))
a=a_mp(u)
ap=a*(-mp.mpf('1.5')/u+1/(4*u**2))
g2_g1=-Hpp_mp(u)/(a*Hp_mp(u))+3*ap/(a*a)
c=phi+phi*(1-phi)*g2_g1/2
assert abs(u-mp.mpf('0.7439043428067804761276974841'))<mp.mpf('1e-25')
assert abs(phi-mp.mpf('0.4123101754587192744883896745'))<mp.mpf('1e-25')
assert abs(c+mp.mpf('2.076367087943007658049552994'))<mp.mpf('1e-23')
for N in (20,50,100,200):
    kstar=brentq(lambda k:S(N,k),phi*float(N)-3.5,phi*float(N)-.5,xtol=1e-10)
    delta=kstar-float(phi)*N
    assert abs(delta-float(c)) < 1/N, (N,delta,c)
    print('N =',N,'k-critical =',f'{kstar:.10f}','offset =',f'{delta:.10f}')
for N in (9,20,40):
    vals=[S(N,k) for k in range(1,N-3)]
    signs=[x>0 for x in vals]
    assert signs==sorted(signs,reverse=True), (N,vals)
# Independent finite difference of the renewal transform for the first-passage
# survival; the convolution formula supplies H = q*q-u q.
for t in (0.3,0.8,2.0):
    q=lambda s: mp.erf(1/(2*mp.sqrt(s))) if s>0 else mp.mpf(1)
    conv=mp.quad(lambda s:q(s)*q(t-s),[0,t/2,t])
    assert abs((conv-t*q(t))-H_mp(mp.mpf(t)))<mp.mpf('1e-18')
print('H-root',mp.nstr(u,25),'phi',mp.nstr(phi,25),'offset',mp.nstr(c,25))
print('PASS: root, shift, Beta quadratures, sign-staircase and renewal derivative')
