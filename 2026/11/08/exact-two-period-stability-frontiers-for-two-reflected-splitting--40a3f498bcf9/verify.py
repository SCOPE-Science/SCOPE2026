#!/usr/bin/env python3
"""Reproduce two-period skew-resolvent stability identities (SymPy + Python stdlib)."""
import cmath
import math
import sympy as s

a, b = s.symbols('a b', positive=True, real=True)
I = s.I
D = (1+I*a)*(1+I*b)

def current(t):
    return s.Matrix([[(1-2*I*t)/(1+I*t), I*t/(1+I*t)], [1,0]])

def history(t, u):
    return s.Matrix([[(1-I*(t+u))/(1+I*t), I*u/(1+I*t)], [1,0]])

C = current(b)*current(a)
H = history(b,a)*history(a,b)

expected = {
    'current': (C, (1-I*(a+b)-6*a*b)/D,
                8*a*b*(1-4*a*b)*(1+2*(a+b)**2)/((1+a*a)**2*(1+b*b)**2),
                2*(1-4*a*b)/D),
    'history': (H, (1-I*(a+b)-2*(a*a+a*b+b*b))/D,
                4*(1-(a+b)**2)*((a+b)**4+a*a+b*b)/((1+a*a)**2*(1+b*b)**2),
                2*(1-(a+b)**2)/D)
}
checks = 0
for name, (M, tr_ref, delta_ref, m1_ref) in expected.items():
    tr = s.trace(M)
    det = M.det()
    schur_gap = (1-det*s.conjugate(det))**2 - (tr - s.conjugate(tr)*det)*(s.conjugate(tr)-tr*s.conjugate(det))
    for lhs, rhs in [(tr,tr_ref), (det,-a*b/D), (schur_gap,delta_ref), ((M+s.eye(2)).det(), m1_ref)]:
        assert s.factor(s.together(lhs-rhs)) == 0, (name, s.factor(s.together(lhs-rhs)))
        checks += 1

# The initial two-step state (z_0,z_{-1})=(1,1) cannot lie in a strictly decaying eigenspace
# at/beyond the boundary: z_1=(1-ia)/(1+ia) lies on the unit circle, while the
# putative decaying eigenvalue of the two-step map is strictly inside the unit circle.
for aa in [0.001,0.01,0.1,0.2,0.4,0.5,0.8,1.1,2.,3.]:
    for bb in [0.001,0.01,0.1,0.2,0.4,0.5,0.8,1.1,2.,3.]:
        for name, (M, tr, _, _) in expected.items():
            t = complex(tr.subs({a:aa,b:bb}))
            d = complex((-a*b/D).subs({a:aa,b:bb}))
            disc = cmath.sqrt(t*t - 4*d)
            r1, r2 = (t+disc)/2, (t-disc)/2
            rho = max(abs(r1),abs(r2))
            assert abs(abs((1-1j*aa)/(1+1j*aa))-1)<1e-12
            critical = 4*aa*bb-1 if name=='current' else (aa+bb)**2-1
            if critical < -1e-11: assert rho < 1 - 1e-10, (name,aa,bb,rho)
            elif critical > 1e-11: assert rho > 1 + 1e-10, (name,aa,bb,rho)
            else: assert abs(rho-1)<1e-10, (name,aa,bb,rho)
            checks += 1

for aa, bb in [(0.1,2.5),(.25,1),(.5,.5),(.2,.8),(.1,.9)]:
    for name, (M, tr, _, _) in expected.items():
        crit = 4*aa*bb-1 if name=='current' else (aa+bb)**2-1
        if abs(crit)<1e-10:
            t = complex(tr.subs({a:aa,b:bb}));d=complex((-a*b/D).subs({a:aa,b:bb}))
            assert abs(1+t+d)<1e-10 and abs(d)<1
            checks += 1
assert 4*.1*2 < 1 and (.1+2)>1
print('PASS',checks,'symbolic and numerical checks')
