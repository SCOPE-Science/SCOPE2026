"""Self-contained exact and quadrature checks of the two-disc discotope moment theorem.
Run: python twodisc_isotropic_check.py (requires sympy and numpy).
"""
import numpy as np
import sympy as s
from numpy.polynomial.legendre import leggauss

a,b,u=s.symbols('a b u',positive=True)
pi=s.pi
# Moments computed by elementary beta integrals of h(y,z)=sqrt(a^2-y^2)+sqrt(b^2-z^2)
I=lambda k,r: s.simplify(r**(k+1)*s.gamma(s.Rational(1,2))*s.gamma(s.Rational(k,2)+1)/s.gamma(s.Rational(k,2)+s.Rational(3,2)))
for k,expect in [(0,lambda r:2*r),(1,lambda r:pi*r**2/2),(2,lambda r:4*r**3/3),(3,lambda r:3*pi*r**4/8)]:
    assert s.simplify(I(k,a)-expect(a))==0
    assert s.simplify(I(k,b)-expect(b))==0
V=2*(I(1,a)*I(0,b)+I(0,a)*I(1,b))
Mx=s.Rational(2,3)*sum(s.binomial(3,k)*I(k,a)*I(3-k,b) for k in range(4))
Iy2=lambda k,r: s.simplify(r**(k+3)*s.gamma(s.Rational(3,2))*s.gamma(s.Rational(k,2)+1)/s.gamma(s.Rational(k,2)+s.Rational(5,2)))
My=2*(Iy2(1,a)*I(0,b)+Iy2(0,a)*I(1,b))
Mz=2*(I(1,a)*Iy2(0,b)+I(0,a)*Iy2(1,b))
Sx=(a*a+b*b)/4+5*a*b/12
Sy=a*a*(3*a+4*b)/(12*(a+b))
Sz=b*b*(3*b+4*a)/(12*(a+b))
for l,r in [(V,2*pi*a*b*(a+b)),(Mx/V,Sx),(My/V,Sy),(Mz/V,Sz)]:
    assert s.simplify(s.expand_func(l-r))==0,(l,r)
expr=s.factor(Sx*Sy*Sz/V**2)
expected=s.factor((49-u*u)*(11+u*u)/(110592*pi*pi))
assert s.simplify(expr.subs({a:1+u,b:1-u})-expected)==0
assert s.simplify(s.diff((49-u*u)*(11+u*u),u)-4*u*(19-u*u))==0
# Numerical quadrature independent of symbolic beta integrals: tensor Gauss-Legendre.
x,w=leggauss(160)
for aa,bb in [(1.,1.),(.31,2.7),(3.2,.82),(1.02,1.03)]:
    yy=aa*x[:,None];zz=bb*x[None,:]
    ww=(aa*bb)*w[:,None]*w[None,:]
    hh=np.sqrt(np.maximum(0,aa**2-yy**2))+np.sqrt(np.maximum(0,bb**2-zz**2))
    numer=np.array([np.sum(ww*(2./3.)*hh**3),np.sum(ww*2*yy**2*hh),np.sum(ww*2*zz**2*hh)])
    vol=np.sum(ww*2*hh)
    got=numer/vol
    wanted=np.array([(aa*aa+bb*bb)/4+5*aa*bb/12, aa*aa*(3*aa+4*bb)/(12*(aa+bb)),bb*bb*(3*bb+4*aa)/(12*(aa+bb))])
    assert np.max(np.abs(got-wanted))<6e-5,(aa,bb,got,wanted)
    assert abs(vol-2*np.pi*aa*bb*(aa+bb))<3e-5
    # Nonorthogonal affine transformation: determinant-covariance divided by volume^2.
    for angle in [.18,.75,1.48]:
        T=np.array([[1.,0.,0.],[0.,1.,np.cos(angle)],[0.,0.,np.sin(angle)]])
        cov=T@np.diag(got)@T.T
        q=np.linalg.det(cov)/(vol*np.linalg.det(T))**2
        ut=(aa-bb)/(aa+bb)
        exact=(49-ut*ut)*(11+ut*ut)/(110592*np.pi*np.pi)
        assert abs(q-exact)<2e-8,(q,exact)
print('PASS: 14 analytic identities, complete symbolic quotient, derivative, 4x160^2 independent quadrature, 12 nonorthogonal affine tests')
