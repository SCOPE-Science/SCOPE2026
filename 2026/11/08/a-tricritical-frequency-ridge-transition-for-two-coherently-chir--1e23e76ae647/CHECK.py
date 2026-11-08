"""Independent finite checks for the local central-slice spectral-transition formulas.
The analytic proof in RESULT.md, not this finite sampling, proves the theorem.
"""
import math
import cmath
import mpmath as mp
import sympy as sp
mp.mp.dps = 55

print('start integral',flush=True)
# Check normalization by numerical integration of the actual STFT integral.
for a,c,w,xi in [(1.0,0.0,0.55,0.2),(1.4,0.3,0.7,0.36),(.9,-.33,.4,-.2)]:
    a,c,w,xi=map(mp.mpf,(str(a),str(c),str(w),str(xi)))
    fn=lambda t: mp.exp(-mp.pi*a*t*t+mp.pi*1j*c*t*t)*(
             mp.exp(2j*mp.pi*w*t)+mp.exp(-2j*mp.pi*w*t))*mp.exp(-2j*mp.pi*xi*t)
    integral=mp.quad(fn,[-mp.inf,0,mp.inf])
    p=a-1j*c
    closed=(mp.exp(-mp.pi*(xi-w)**2/p)+mp.exp(-mp.pi*(xi+w)**2/p))/mp.sqrt(p)
    assert abs(integral-closed)<mp.mpf('1e-35')
    d=a*a+c*c
    u=2*mp.pi*a/d
    k=4*mp.pi*a*w/d
    mu=4*mp.pi*c*w/d
    intensity=2/mp.sqrt(d)*mp.exp(-u*(xi*xi+w*w))*(mp.cosh(k*xi)+mp.cos(mu*xi))
    assert abs(abs(integral)**2-intensity)<mp.mpf('1e-35')

print('start taylor',flush=True)
# Taylor coefficients of the normalized positive profile, exactly.
r,z=sp.symbols('r z', real=True)
r0=sp.sqrt(2)-1
AA=2/sp.sqrt(1-r*r)
profile=sp.exp(-z*z)*(sp.cosh(AA*z)+sp.cos(r*AA*z))
q=sp.factor(sp.diff(profile,z,4).subs(z,0)/sp.factorial(4))
v=sp.factor(sp.diff(profile,z,6).subs(z,0)/sp.factorial(6))
qexpected=(-1+6*r*r-r**4)/(3*(1-r*r)**2)
assert sp.simplify(q-qexpected)==0
assert sp.simplify(q.subs(r,r0))==0
assert sp.simplify(v.subs(r,r0)+sp.Rational(8,45))==0
qp=sp.simplify(sp.diff(q,r).subs(r,r0))
assert sp.simplify(qp-(4+2*sp.sqrt(2))/3)==0
K=sp.simplify(sp.Rational(15,16)*qp**2)
assert sp.simplify(K-(sp.Rational(5,2)+5*sp.sqrt(2)/3))==0

print('start fold',flush=True)
# Nonzero stationary points, their types, and the fold coefficient.
rt=mp.sqrt(2)-1

def Dprofile(t,rr,e):
    aa=2*mp.sqrt((1+e)/(1-rr*rr))
    bb=rr*aa
    return mp.exp(-t*t)*(aa*mp.sinh(aa*t)-bb*mp.sin(bb*t)-2*t*(mp.cosh(aa*t)+mp.cos(bb*t)))

# At the tricritical point the positive maximum obeys fourth-root law.
for e in [mp.mpf('1e-4'),mp.mpf('1e-5')]:
    z0=(mp.mpf(15)*e/4)**mp.mpf('.25')
    root=mp.findroot(lambda t: Dprofile(t,rt,e), (z0*.9,z0*1.1))
    assert root>0 and abs(root/z0-1)<mp.mpf('.008')
    assert mp.diff(lambda t: Dprofile(t,rt,e),root)<0

# In the subcritical regime the saddle-node is near the predicted scaling.
qpn=mp.mpf(str(qp.evalf(50)))
kn=mp.mpf(str(K.evalf(50)))
for delta in [mp.mpf('0.015'),mp.mpf('0.007')]:
    rr=rt+delta
    guess=mp.sqrt(mp.mpf(15)/8*qpn*delta)
    zf,ef=mp.findroot((lambda x,e:Dprofile(x,rr,e),
                      lambda x,e:mp.diff(lambda t:Dprofile(t,rr,e),x)),
                     (guess,-kn*delta**2), maxsteps=90)
    assert zf>0 and ef<0
    assert abs(-ef/delta**2/kn-1)<mp.mpf('.03')
    assert abs(zf**2/(delta*(mp.mpf(15)/8)*qpn)-1)<mp.mpf('.04')
    # At the middle of the coexistence interval, locate both satellite extrema.
    e=ef/2
    a=mp.findroot(lambda x:Dprofile(x,rr,e), (zf*.4,zf*.85))
    b=mp.findroot(lambda x:Dprofile(x,rr,e), (zf*1.05,zf*1.75))
    assert 0<a<b
    assert mp.diff(lambda x:Dprofile(x,rr,e),a)>0
    assert mp.diff(lambda x:Dprofile(x,rr,e),b)<0
    assert mp.diff(lambda x:Dprofile(x,rr,e),0)<0
print('CHIRPED_TWO_TONE_TRICRITICAL_CHECKS_PASSED')
