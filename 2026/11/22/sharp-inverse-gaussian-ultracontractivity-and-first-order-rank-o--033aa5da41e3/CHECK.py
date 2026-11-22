import math
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.integrate import quad
rng=np.random.default_rng(418)
for case in range(300):
 n=1+case%4
 A=rng.normal(size=(n,n)); B=-np.eye(n)*(0.5+rng.random())+0.1*(A-A.T)
 V=rng.normal(size=(n,n)); Q=V@V.T +np.eye(n)*0.4
 Qinf=solve_continuous_lyapunov(B,-Q)
 t=0.01+3*rng.random(); S=expm(t*B); Qt=Qinf-S@Qinf@S.T
 p=1.05+7*rng.random(); pp=p/(p-1)
 M=S.T@np.linalg.inv(Qt)@S+np.linalg.inv(Qinf)/p
 detM=np.linalg.det(M)
 detAlt=np.linalg.det(Qinf-Qt/pp)/(np.linalg.det(Qt)*np.linalg.det(Qinf))
 assert np.allclose(detM,detAlt,rtol=1e-7)
 c=(2*math.pi)**(-n/2)*np.linalg.det(Qt)**(-0.5)*np.linalg.det(S)
 norm1=c*(2*math.pi/pp)**(n/(2*pp))*detM**(-1/(2*pp))
 cp=(2*math.pi)**(-n/(2*p))*pp**(-n/(2*pp))*np.linalg.det(Qt)**(-1/(2*p))*np.linalg.det(S)**(1/p)
 norm2=cp*(np.linalg.det(Qinf-Qt)/np.linalg.det(Qinf-Qt/pp))**(1/(2*pp))
 assert np.allclose(norm1,norm2,rtol=1e-7)
 assert norm1 < cp
print('300 anisotropic determinant/normalization checks passed')
for p in [1.5,2,3,5]:
 t=.73; s=math.exp(-t); qt=1-s*s; pp=p/(p-1)
 c=(2*math.pi)**(-.5)*qt**(-.5)*s
 row0=quad(lambda u: math.exp(-pp*(s*u)**2/(2*qt)-(pp-1)*u*u/2),-12,12,epsabs=1e-12)[0]**(1/pp)*c
 M=s*s/qt+1/p
 exact=c*(2*math.pi/pp/M)**(1/(2*pp))
 assert abs(row0-exact)<1e-12
 print('p',p,'quadrature',row0,'formula',exact)
print('sharp row via independent quadrature passed')

# One-dimensional Gaussian point-evaluation profile for nonzero x.
for p in [1.25,2.,4.]:
    r=p/(p-1); t=.8; s=math.exp(-t); qt=1-s*s
    c=(2*math.pi)**(-.5)*qt**(-.5)*s
    for x in [0.,.5,1.5,3.]:
        f=lambda u: math.exp(-r*(s*u-x)**2/(2*qt)-(r-1)*u*u/2)
        observed=c*quad(f,-35,35,epsabs=1e-13)[0]**(1/r)
        m=s*s/qt+1/p
        n0=c*(2*math.pi/(r*m))**(1/(2*r))
        expected=n0*math.exp(-x*x/(2*(qt+p*s*s)))
        assert math.isclose(observed,expected,rel_tol=1e-9,abs_tol=1e-12)
print('12 exact point-profile quadrature checks passed')
# Sharp first-order normal form in one dimension at p=2: error constant.
from scipy.optimize import minimize_scalar
C2=(2*math.pi)**(-.25)*(2.-1.)**(-.25)
kap=math.exp(-.5)
for t in [3.,4.,5.]:
    s=math.exp(-t); qt=1-s*s
    c=(2*math.pi)**(-.5)*qt**(-.5)
    def row_error(x):
        fun=lambda u: (c*math.exp(-(s*u-x)**2/(2*qt)-u*u/2)-(2*math.pi)**(-.5)*math.exp(-x*x/2-u*u/2))**2*math.exp(u*u/2)
        return math.sqrt(quad(fun,-16,16,epsabs=1e-13,limit=150)[0])
    z=minimize_scalar(lambda x:-row_error(x),bounds=(0,2),method='bounded',options={'xatol':1e-9})
    ratio=-z.fun/s
    assert abs(ratio-C2*kap) < 3*s*s
print('First-order normalized p=2 rank-one error checks passed')
