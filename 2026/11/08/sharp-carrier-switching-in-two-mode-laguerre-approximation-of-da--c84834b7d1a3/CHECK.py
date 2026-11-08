"""Standalone exact-algebra and independent integral checks for a two-mode Laguerre carrier theorem.

Requires sympy and scipy. Run: python CHECK.py
"""
import math
import cmath
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

W,t=sp.symbols('W t',positive=True,real=True)
P=(1+W+t)**2-4*W*t
N=2*t**3+(5-4*W)*t**2+(2*W**2-6*W+4)*t+5*W**2+2*W+1
J=4*N/P**2
Q=t**3+(2-W)*t**2+(1-W**2-12*W)*t+W**3+10*W**2+W
H=(W+1)*t**2-2*(W**2+4*W-1)*t+W**3+7*W**2+3*W+1
assert sp.simplify(J.subs(t,W-1)-(W+1)/W)==0
assert sp.simplify(J-(W+1)/W + (t-W+1)**2*H/(W*P**2))==0
assert sp.simplify(sp.diff(J,t)+8*(t-W+1)*Q/P**3)==0
assert sp.factor(sp.discriminant(H,t))==16*W*(W-3)
assert sp.factor(H.subs(W,3))==4*(t-5)**2
assert sp.simplify(J.subs({W:3,t:2})-sp.Rational(4,3))==0
assert sp.simplify(J.subs({W:3,t:5})-sp.Rational(4,3))==0
u=sp.symbols('u',real=True)
assert sp.expand(Q.subs(t,W+u))==sp.expand((2*u*u-8*u+2)*W+u**3+2*u*u+u)

# Direct real-half-line numerical quadratures of both complex Laguerre inner products.
def energy_integrated(s, omega, carrier):
    def integ(n):
        def component(x):
            f=math.exp(-s*x/2)*2*math.cos(omega*x)
            phi=math.sqrt(s)*math.exp(-s*x/2)*(1 if n==0 else (1-s*x))
            return f*phi*cmath.exp(-1j*carrier*x)
        r=quad(lambda x:component(x).real,0,math.inf,epsabs=2e-11,limit=250)[0]
        im=quad(lambda x:component(x).imag,0,math.inf,epsabs=2e-11,limit=250)[0]
        return complex(r,im)
    return abs(integ(0))**2+abs(integ(1))**2

def energy_rational(s,omega,carrier):
    w=omega/s;z=carrier/s
    return float(J.subs({W:w*w,t:z*z}))/s

for w,z in [(1,0),(1.2,math.sqrt(1.2**2-1)),(math.sqrt(3),math.sqrt(2)),
            (math.sqrt(3),math.sqrt(5)),(2,2.49817),(3,3.4397)]:
    for s in (1.0,1.8):
        a=energy_integrated(s,s*w,s*z)
        b=energy_rational(s,s*w,s*z)
        assert abs(a-b)<2e-8,(s,w,z,a,b)

jfunc=sp.lambdify((W,t),J,modules="math")
qfunc=sp.lambdify((W,t),Q,modules="math")
for w in (1.0,1.1,1.25,1.5,1.7,math.sqrt(3)-1e-5,math.sqrt(3),math.sqrt(3)+1e-5,1.8,2,2.5,4,10):
    w2=w*w
    j=lambda xx:jfunc(w2,xx)
    if w2<=3:
        candidates=[max(0,w2-1)]
        if abs(w2-3)<1e-10:candidates.append(5)
    else:
        lo=(w2*w2+4*w2-1-2*math.sqrt(w2*(w2-3)))/(w2+1)
        hi=(w2*w2+4*w2-1+2*math.sqrt(w2*(w2-3)))/(w2+1)
        qr=lambda xx:qfunc(w2,xx)
        rt=brentq(qr,lo,hi,xtol=1e-12)
        candidates=[rt]
    predicted=max(j(xx) for xx in candidates)
    brute=minimize_scalar(lambda zz:-j(zz*zz),bounds=(0,max(25,2*w)),method='bounded',options={'xatol':1e-10})
    # Bound-based minimization may identify only a local maximum; densely check all centers.
    scan=max(j((k/1400*max(20,2*w))**2) for k in range(1401))
    assert scan<=predicted+1e-6,(w,scan,predicted)
    assert -brute.fun<=predicted+1e-8,(w,-brute.fun,predicted)

print('TWO_MODE_LAGUERRE_CARRIER_EXACT_AND_INTEGRAL_CHECKS_PASSED')
