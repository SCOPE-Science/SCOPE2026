"""Independent algebraic and finite quadrature checks for a cubic oscillator.

The numerical experiments support but do not substitute for the proof of uniform
asymptotics and the total-variation convergence in RESULT.md.
"""
from math import exp, expm1, pi, sqrt, sin, cos
from scipy.integrate import quad
import sympy as sp

x, v, h, k = sp.symbols('x v h k', real=True)
y = sp.symbols('y', real=True)
# H=e^{h x^2}y^2+int_0^{x^2}(1+ks)e^{hs}ds.
# Check its gradient relation without introducing a division by h.
H_x = 2*h*x*sp.exp(h*x*x)*y*y + 2*x*(1+k*x*x)*sp.exp(h*x*x)
H_y = 2*sp.exp(h*x*x)*y
assert sp.simplify(H_x*y + H_y*(-x-k*x**3-h*x*y*y)) == 0

# Check the closed form for the squared velocity in the turning-gap variable.
r, A = sp.symbols('r A', positive=True)
F = sp.expm1(h*r) if hasattr(sp,'expm1') else sp.exp(h*r)-1
G = (F-h*r)/h**2
q = (1+k*A*A)*F/h-k*G
assert sp.simplify(sp.diff(q,r) - ((1+k*(A*A-r)) + h*q)) == 0
assert sp.simplify(q.subs(r,0)) == 0


def qval(r,h,k,A):
    if r < 1e-9:
        return r*(1+k*A*A)+(h*(1+k*A*A)-k)*r*r/2
    e=expm1(h*r)
    return (1+k*A*A)*e/h-k*(e-h*r)/(h*h)


def period(h,k,A):
    # r=A^2 cos^2(theta), x=A sin(theta).
    def f(theta):
        s=sin(theta)
        r=A*A*(1-s*s)
        if r<1e-14:
            return 4/sqrt(1+k*A*A)
        return 4*A*cos(theta)/sqrt(qval(r,h,k,A))
    return quad(f,0,pi/2,epsabs=1e-11,epsrel=1e-11,limit=400)[0]


def cdf_r(bound,h,k,A):
    if bound<=0: return 0
    if bound>=A*A: return 1
    def f(z):
        r=z*z
        return 2/sqrt((A*A-r)*qval(r,h,k,A)/r)
    val=quad(f,0,sqrt(bound),epsabs=1e-11,limit=200)[0]
    return val/(period(h,k,A)/2)

# These are independent finite checks; the theorem is established analytically.
for h0 in (.7,2.):
    for k0 in (0.,.1,2.,100.):
        vals=[period(h0,k0,A0)*sqrt(h0)*A0*sqrt(1+k0*A0*A0)/(2*pi)
              for A0 in (6.,9.,12.)]
        assert abs(vals[-1]-1)<.025, (h0,k0,vals)
        assert abs(vals[-1]-1)<abs(vals[0]-1), (h0,k0,vals)
        if h0==.7 and k0 in (0.,2.):
            c=cdf_r(1.0,h0,k0,9.)
            # Limit CDF F_R(r)=2/pi*asin(sqrt(1-exp(-h*r)))
            import math
            limit=2/math.pi*math.asin(sqrt(1-exp(-h0)))
            assert abs(c-limit)<.025,(c,limit)
print('CUBIC_CENTER_UNIFORM_ENDPOINT_LAYER_CHECK_OK')
