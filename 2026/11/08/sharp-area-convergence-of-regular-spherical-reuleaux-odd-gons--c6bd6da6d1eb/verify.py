"""Independent numerical and symbolic checks for spherical Reuleaux odd-gons.

Run: python verify.py. Numerical sampling supplements, rather than proves, the theorem.
Requires mpmath, sympy and numpy.
"""
from math import pi, sin, cos, acos, sqrt
import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 70
z, c = sp.symbols('z c', positive=True, real=True)
t = sp.symbols('t', real=True)
s2 = 1-c**2
h = sp.asin(sp.sin(t)/c)
formula = s2*sp.cos(t)*(c**2+2*sp.sin(t)**2)/(c**2-sp.sin(t)**2)**sp.Rational(5,2)
assert sp.simplify(sp.diff(h,t,3)-formula)==0
# Strict increase of h''' reduces to positivity of a rational logarithmic derivative.
expr = -1/(2*(1-z)) + 2/(c**2+2*z)+5/(2*(c**2-z))
positive_sum = 2/(c**2+2*z)+2/(c**2-z)+(1-c**2)/(2*(c**2-z)*(1-z))
assert sp.simplify(expr-positive_sum)==0
# In the relevant domain 1/2<=c^2<1 and 0<=z<=1/4,
# 5/(c^2-z)>1/(1-z), so expr>0.

def quantities(n,w):
    w=mp.mpf(w)
    s=mp.sin(w/2);c=mp.cos(w/2)
    t=mp.pi/(2*n)
    alpha=2*mp.asin(mp.sin(t)/c)
    L=n*mp.sin(w)*alpha
    A=2*mp.pi-n*(1+mp.cos(w))*alpha
    Ainf=2*mp.pi*(1-c)
    Linf=2*mp.pi*s
    delta=Ainf-A
    K=mp.pi**3*s**2/(12*c)
    return A,L,Ainf,Linf,delta,K

widths=[mp.mpf('0.13'),mp.mpf('0.58'),mp.mpf('1.1'),mp.pi/2]
count=0
for w in widths:
    oldA=None;oldL=None;oldX=None
    upper=9*quantities(3,w)[4]
    for n in list(range(3,102,2))+[201,501,1001]:
        A,L,Ainf,Linf,delta,K=quantities(n,w)
        assert 0<A<Ainf and Linf<L
        assert mp.almosteq(L, (2*mp.pi-A)*mp.tan(w/2),rel_eps=mp.mpf('1e-55'))
        assert K < n*n*delta <= upper*(1+mp.mpf('1e-50'))
        if oldA is not None:
            assert A>oldA and L<oldL and n*n*delta < oldX
        oldA,oldL,oldX=A,L,n*n*delta
        count+=1
    assert abs((1001**2*quantities(1001,w)[4])/quantities(1001,w)[5]-1)<mp.mpf('0.000003')

# The endpoint w=pi/2 reduces to the known regular spherical polygon formula.
for n in [3,5,7,11,21]:
    A=quantities(n,mp.pi/2)[0]
    A_endpoint=2*mp.pi-2*n*mp.asin(mp.sqrt(2)*mp.sin(mp.pi/(2*n)))
    assert mp.almosteq(A,A_endpoint,rel_eps=mp.mpf('1e-60'))

# The arc aperture is independently recovered from the spherical cosine law.
for n in [3,5,9,15]:
    for w in [0.3,0.8,1.4]:
        s=sin(w/2);T=pi/(2*n);C=cos(w/2)
        rho=np.arcsin(s/cos(T))
        arcside=acos(cos(rho)**2+sin(rho)**2*cos(2*pi/n))
        alpha_direct=acos((cos(arcside)-cos(w)**2)/sin(w)**2)
        alpha_formula=2*np.arcsin(sin(T)/C)
        assert abs(alpha_direct-alpha_formula)<1e-12

# Area by independent uniform area sampling on S^2; no use of Gauss-Bonnet.
rng=np.random.default_rng(73127)
sample=240000
u=rng.uniform(-1,1,sample)
phi=rng.uniform(0,2*pi,sample)
r=np.sqrt(1-u*u)
points=np.column_stack((r*np.cos(phi),r*np.sin(phi),u))
maxdev=0.0
for n,w in [(3,0.8),(5,0.8),(9,1.3),(3,pi/2)]:
    rho=np.arcsin(sin(w/2)/cos(pi/(2*n)))
    angles=np.arange(n)*2*pi/n
    centers=np.column_stack((np.sin(rho)*np.cos(angles),np.sin(rho)*np.sin(angles),np.full(n,np.cos(rho))))
    inside=(points@centers.T >= cos(w)-1e-13).all(axis=1)
    area_emp=inside.mean()*4*pi
    area=float(quantities(n,w)[0])
    dev=abs(area_emp-area)
    maxdev=max(dev,maxdev)
    assert dev<0.028,(n,w,area_emp,area)
print('VERIFY_OK symbolic_third_derivative=1 strict_normalized_cases=%d spherical_arc_cases=12 endpoint_cases=5 monte_carlo_orientation_samples=%d max_area_deviation=%.6g' %(count,sample*4,maxdev))
