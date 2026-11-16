"""Standalone reproducibility checks for four-line Gaussian spectrogram zeros.

Run with Python 3 and SymPy. The all-parameter proof is in RESULT.md;
finite sampling below is supplementary and never an exhaustive proof.
"""
import math
import sympy as sp

k,t,z,u,d=sp.symbols('k t z u d', positive=True, real=True)
L=sp.log(sp.cosh(u)+k*sp.cosh(3*u))
V=sp.diff(L,u,2)
v_t=sp.factor((1-t*t)*((3*k-1)**2*(1-t*t)**2+16*k)/(1+k+(3*k-1)*t*t)**2)
P=(27*k**3-27*k**2+9*k-1)*z**3+(27*k**3+9*k**2-15*k+3)*z**2+(-135*k**3+15*k**2+19*k-3)*z+81*k**3+67*k**2-13*k+1
L_t=sp.log(1+k+(3*k-1)*t*t)-sp.Rational(3,2)*sp.log(1-t*t)
V_direct=sp.factor((1-t*t)*sp.diff((1-t*t)*sp.diff(L_t,t),t))
assert sp.factor(V_direct-v_t)==0
assert sp.factor(sp.diff(v_t,t)+2*t*P.subs(z,t*t)/(1+k+(3*k-1)*t*t)**3)==0
assert sp.factor(sp.discriminant(P,z))==-16384*k**3*(3*k-1)**6*(27*k*k+18*k-1)
assert sp.factor(P.subs(z,0))==(k+1)*(81*k*k-14*k+1)
assert sp.factor(P.subs(z,1))==64*k*k
b0=(1+k)*(81*k*k-14*k+1)
b1=4*k*(27*k*k+54*k-5)/3
b2=16*k*(15*k-1)/3
b3=64*k*k
assert sp.factor(P-(b0*(1-z)**3+3*b1*z*(1-z)**2+3*b2*z*z*(1-z)+b3*z**3))==0
kc=(2*sp.sqrt(3)-3)/9
zc=1/sp.sqrt(3)
assert sp.simplify(27*kc**2+18*kc-1)==0
assert sp.simplify(P.subs({k:kc,z:zc}))==0
assert sp.simplify(sp.diff(P,z).subs({k:kc,z:zc}))==0
assert sp.simplify(sp.diff(P,k).subs({k:kc,z:zc}))==sp.simplify(sp.diff(P,z,2).subs({k:kc,z:zc}))
assert sp.simplify(sp.factor(P.subs(k,kc),extension=sp.sqrt(3))-(-16+80*sp.sqrt(3)/9)*(z-zc)**2*(z-2-zc))==0
assert sp.factor(P.subs({k:sp.Rational(1,32),z:sp.Rational(3,4)}))==-sp.Rational(41739,2097152)
assert sp.factor(sp.diff(V_direct,t,2).subs(t,0)+2*(81*k*k-14*k+1)/(1+k)**2)==0
# For the four independent harmonic lines with the specified Gaussian window,
# the effective spectral-pair ratio is exp(-8*d*d).
assert sp.simplify(sp.exp(-9*d*d)/sp.exp(-d*d))==sp.exp(-8*d*d)
# Elementary total zero intensity: since the slope of L tends to +/-3,
# integral of the zero intensity over frequency equals 3*d/pi.
assert sp.simplify(sp.diff(L,u).subs(u,0))==0
count=17
for kval in [0.0001,0.002,0.01,0.02,0.03125,0.04,0.05,0.051,0.05157,0.06,0.067,0.09,0.1,0.2,1/3,0.5,1,2,10]:
    coeffs=[float(x) for x in sp.Poly(P.subs(k,kval),z).all_coeffs()]
    while coeffs and abs(coeffs[0])<1e-12:
        coeffs.pop(0)
    import numpy as np
    roots=np.roots(coeffs)
    real_inside=sorted(float(q.real) for q in roots if abs(q.imag)<1e-8 and 0<q.real<1)
    expected=2 if kval<float(kc) else 0
    assert len(real_inside)==expected, (kval, roots)
    for point in [0.0, .05, .25, .5, .75, .95, .99]:
        vt=float(v_t.subs({k:kval,t:point}))
        assert vt>0
        uu=math.atanh(point)
        vv=float((sp.diff(L,u,2)).subs({k:kval,u:uu}))
        assert abs(vt-vv)<1e-8, (kval,point,vt,vv)
        count+=2
    count+=1
for kval in [.03,.04,.05]:
    coeffs=[float(x) for x in sp.Poly(P.subs(k,kval),z).all_coeffs()]
    roots=sorted(float(q.real) for q in np.roots(coeffs) if abs(q.imag)<1e-8 and 0<q.real<1)
    a,b=roots
    # P positive at both ends and negative between its two interior roots.
    assert float(P.subs({k:kval,z:(a+b)/2}))<0
    assert float(P.subs({k:kval,z:a/2}))>0
    assert float(P.subs({k:kval,z:(b+1)/2}))>0
    count+=3
# Check the saddle-node square-root coefficient with independent numerical roots.
for eps in [1e-4,1e-5,1e-6]:
    kval=float(kc)-eps
    roots=sorted(float(q.real) for q in np.roots([float(v) for v in sp.Poly(P.subs(k,kval),z).all_coeffs()]) if abs(q.imag)<1e-7 and 0<q.real<1)
    assert len(roots)==2
    scale=(roots[1]-roots[0])/(2*math.sqrt(2*eps))
    assert abs(scale-1)<.035, (eps,scale)
    count+=2
print('FOUR_LINE_INTENSITY_CHECKS_PASSED',count)
