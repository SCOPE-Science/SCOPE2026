"""Independent elementary algebra and physical-period quadrature checks.
The asymptotic theorem itself is proved analytically in RESULT.md.
"""
import sympy as s
from scipy.integrate import quad
import numpy as np

x,y,lam,a,eta,delta,omega,eps=s.symbols('x y lam a eta delta omega eps', real=True)
r2=x*x+y*y
Qx=lam*x-(a*r2+eta*(x*x-y*y))*x-delta*y*r2-omega*y**3-eps*y*r2
Qy=lam*y-(a*r2+eta*(x*x-y*y))*y+eps*x*r2
rad=s.expand(x*Qx+y*Qy)
ang=s.expand(x*Qy-y*Qx)
assert s.simplify(rad-(lam*r2-(a*r2+eta*(x*x-y*y))*r2-delta*x*y*r2-omega*x*y**3))==0
assert s.simplify(ang-(eps*r2*r2+delta*y*y*r2+omega*y**4))==0

for w,tau in [(1.,0.),(2.,1.),(4.,-1.),(1.,-1.2)]:
    assert tau> -2*np.sqrt(w)
    I,e=quad(lambda v:1/(1+tau*v*v+w*v**4),-np.inf,np.inf,epsabs=1e-11)
    exact=np.pi/np.sqrt(tau+2*np.sqrt(w))
    assert abs(I-exact)<1e-9

# Compute original-time period directly from the exact radial-log balance.
# Its asymptotic ratio must tend to 1 for three physical cusp paths.
for tau in [-1.0,0.0,2.0]:
    lamv,av,etav,w=1.3,3.5,0.7,1.0
    for ep in [1e-3,1e-4,1e-5]:
        dv=tau*np.sqrt(ep)
        def z(th):
            sn=np.sin(th); co=np.cos(th)
            F=av+etav*np.cos(2*th)+dv*co*sn+w*co*sn**3
            g=ep+dv*sn**2+w*sn**4
            return F/g/lamv
        # integrate at two symmetric gates separately with high precision;
        # the odd terms cancel, so the even numerator is enough.
        period=2*quad(lambda th:(av+etav*np.cos(2*th))/(ep+dv*np.sin(th)**2+w*np.sin(th)**4)/lamv,0,np.pi,epsrel=5e-10,limit=300)[0]
        leading=2*np.pi*(av+etav)/(lamv*np.sqrt(tau+2*np.sqrt(w)))*ep**(-.75)
        assert .60 < period/leading < 1.15,(tau,ep,period/leading)
        if ep==1e-5: assert abs(period/leading-1)<0.075,(tau,period/leading)
print('CUBIC_STAR_NODE_QUARTIC_CUSP_CHECK_OK')
