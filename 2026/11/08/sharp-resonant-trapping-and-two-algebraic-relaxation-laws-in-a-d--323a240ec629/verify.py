"""Reproducible symbolic and numerical checks of a resonant dissipative circle map.

Requires Python 3, sympy, and mpmath. The finite tests supplement the
analytic argument; they do not certify infinite quantifiers.
"""
import math
import mpmath as mp
import sympy as sp

x=sp.symbols('x',real=True)
f=sp.sin(2*sp.pi*x)+sp.sin(6*sp.pi*x)
assert sp.simplify(sp.expand_trig(f)-4*sp.sin(2*sp.pi*x)*sp.cos(2*sp.pi*x)**2)==0
roots=[sp.Rational(k,4) for k in range(4)]
assert all(sp.simplify(f.subs(x,z))==0 for z in roots)
first=[sp.simplify(sp.diff(f,x).subs(x,z)) for z in roots]
second=[sp.simplify(sp.diff(f,x,2).subs(x,z)/2) for z in roots]
assert first==[8*sp.pi,0,-8*sp.pi,0], first
assert second[1]==16*sp.pi**2 and second[3]==-16*sp.pi**2, second

mp.mp.dps=55
H=lambda t:2*t*mp.cot(t)-4*t*mp.tan(t)-1
t0=mp.findroot(H,(mp.mpf('0.40'),mp.mpf('0.50')))
assert 0<t0<mp.pi/4
rmax=32*mp.pi*mp.sin(t0)**2*mp.cos(t0)**4/t0
bstar=1/mp.sqrt(rmax)
assert mp.mpf('0.18970')<bstar<mp.mpf('0.18972')
assert rmax>27 and mp.mpf(512)/27<27
u0=t0/(2*mp.pi)
assert (u0-bstar**2*(mp.sin(2*mp.pi*u0)+mp.sin(6*mp.pi*u0))**2) < mp.mpf('1e-45')
assert (u0-(bstar+mp.mpf('1e-4'))**2*(mp.sin(2*mp.pi*u0)+mp.sin(6*mp.pi*u0))**2)<0
# The leak interval opens with an explicit square-root coefficient.
hprime=mp.diff(H,t0)
assert hprime<0
leak_coefficient=(2/mp.pi)*mp.sqrt(t0/(-bstar*hprime))
for delta in (mp.mpf('1e-4'),mp.mpf('1e-5'),mp.mpf('1e-6')):
    b=bstar+delta
    def phi(u):
        return u-b*b*(mp.sin(2*mp.pi*u)+mp.sin(6*mp.pi*u))**2
    uleft=mp.findroot(phi,(u0-mp.sqrt(delta),u0-mp.sqrt(delta)/2))
    uright=mp.findroot(phi,(u0+mp.sqrt(delta)/2,u0+mp.sqrt(delta)))
    assert uleft<u0<uright
    assert abs((uright-uleft)/mp.sqrt(delta)/leak_coefficient-1)<mp.mpf('0.002')

for b in [0.02,0.10,0.18]:
    for k in range(4):
        l=k/4
        for j in range(1,500):
            u=j/2000
            z=l+u
            val=u-b*b*(math.sin(2*math.pi*z)+math.sin(6*math.pi*z))**2
            assert 0<val<u

# Actual trajectories and the two distinct algebraic exponents.
b=.1
N=400000
for k in range(4):
    l=k/4
    z=l+.075
    for n in range(N):
        fval=math.sin(2*math.pi*z)+math.sin(6*math.pi*z)
        z=z-b*b*fval*fval
    u=z-l
    if k%2==0:
        target=1/(64*math.pi**2*b*b)
        observed=N*u
    else:
        target=1/(768*math.pi**4*b*b)
        observed=N*u**3
    assert abs(observed/target-1)<.045,(k,observed,target)
print('VERIFY_OK harmonics=1 fixed_phase_zeros=4 exact_jets=8 sharp_threshold=1 leak_onset_cases=3 branch_samples=5988 orbit_classes=4')
print('b_star=',mp.nstr(bstar,24),'t_star=',mp.nstr(t0,24),'one_sector_leak_coefficient=',mp.nstr(leak_coefficient,24))
