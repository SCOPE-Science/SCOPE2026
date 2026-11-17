"""Numerical checks of conservative radial/complex rocking resonance laws.

Run: python verify_rocking_resonance.py
Dependency: mpmath (tested with 1.3.0).

The infinite-parameter statements are proved analytically in RESULT.md;
these are finite, independently evaluated quadrature checks.
"""
import mpmath as mp
mp.mp.dps = 45
BC = mp.mpf(27) / 256


def bisect(fn, lo, hi, steps=160):
    fl = fn(lo)
    assert fl * fn(hi) < 0
    for _ in range(steps):
        mid = (lo+hi)/2
        fm = fn(mid)
        if fl*fm <= 0:
            hi = mid
        else:
            lo, fl = mid, fm
    return (lo+hi)/2


def potential(r,beta):
    return -r*r/2 + r + beta/(2*r*r)


def periodic_quantities(beta,u):
    assert 0 < beta < BC and 0 < u < 1
    h = lambda r: r**3*(1-r)-beta
    center = bisect(h,mp.mpf('0'),mp.mpf('0.75'))
    saddle = bisect(h,mp.mpf('0.75'),mp.mpf('1'))
    Emin, Emax = potential(center,beta),potential(saddle,beta)
    E = Emin+u*(Emax-Emin)
    f = lambda r: potential(r,beta)-E
    left = bisect(f,center/mp.mpf(1000),center)
    right = bisect(f,center,saddle)
    outer = bisect(f,saddle,mp.mpf(10))
    negative = 2-left-right-outer
    assert negative<0<left<right<outer
    def integrands(t):
        radius = left+(right-left)*mp.sin(t)**2
        d = mp.sqrt((radius-negative)*(outer-radius))
        return radius/d,1/(radius*d)
    time = 4*mp.quad(lambda t:integrands(t)[0],[0,mp.pi/4,mp.pi/2])
    angle = 4*mp.sqrt(beta)*mp.quad(lambda t:integrands(t)[1],[0,mp.pi/4,mp.pi/2])
    return time,angle,center,saddle,Emax-Emin


def theoretical_time(u):
    a=2*mp.sqrt(2)/3
    F=lambda z:mp.mpf(64)/27*z-mp.mpf(8)/9*z**3
    e=(2*u-1)*F(a)
    # Exact cubic roots from trigonometric formula, avoiding repeated-root issues.
    C=mp.mpf(8)/9
    A=mp.mpf(64)/27
    s=mp.sqrt(A/(3*C))
    th=mp.acos(-e/(2*C*s**3))/3
    z=sorted([2*s*mp.cos(th-2*mp.pi*k/3) for k in range(3)])
    z1,z2,z3=z
    ellip_m=(z2-z1)/(z3-z1)
    return 3*mp.ellipk(ellip_m)/mp.sqrt(z3-z1)


for u in [mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75')]:
    expected=theoretical_time(u)
    for d in [mp.mpf('1e-4'),mp.mpf('1e-6')]:
        T,phi,_,_,_=periodic_quantities(BC-d,u)
        assert abs(T*d**mp.mpf('.25')/expected-1)<mp.mpf('.06')
        assert abs(phi*d**mp.mpf('.25')/(expected/mp.sqrt(3))-1)<mp.mpf('.06')

u=mp.mpf('0.5')
coefficient=(theoretical_time(u)/(2*mp.pi*mp.sqrt(3)))**4
for winding in [3,5,8,12]:
    target=2*mp.pi*winding
    def g(d):return periodic_quantities(BC-d,u)[1]-target
    d=bisect(g,mp.mpf('1e-11'),mp.mpf('.002'),steps=48)
    residual=abs(g(d))
    assert residual < mp.mpf('1e-9')
    assert abs((d*winding**4)/coefficient-1) < mp.mpf('.05')
    print('winding',winding,'beta_gap',mp.nstr(d,15),'normalized_m4_gap',mp.nstr(d*winding**4,15))

# Fixed beta: logarithmic exponent of phase advance towards the saddle.
beta=mp.mpf('.06')
_,_,center,saddle,_=periodic_quantities(beta,mp.mpf('.5'))
lam=mp.sqrt(4-3/saddle)
omega=mp.sqrt(beta)/saddle**2
phase_values = []
for eta in [mp.mpf('1e-6'),mp.mpf('1e-8')]:
    _,phase,_,_,_=periodic_quantities(beta,1-eta)
    phase_values.append(phase)
observed_slope = (phase_values[1]-phase_values[0])/mp.log(mp.mpf(100))
assert abs(observed_slope/(omega/lam)-1) < mp.mpf('1e-4')
print('fixed_beta_log_slope',mp.nstr(observed_slope,16),'analytic',mp.nstr(omega/lam,16))

# Exact circular linear frequencies provide a separate check on the normalizations.
for winding in [1,2,4,10,20]:
    r=mp.mpf(3*winding**2-1)/(4*winding**2-1)
    b=r**3*(1-r)
    ang=mp.sqrt(b)/r**2
    rad=mp.sqrt(3/r-4)
    assert abs(ang/rad-winding)<mp.mpf('1e-36')
print('VERIFY_OK scaled_period_and_phase_cases=6 nonlinear_closed_resonances=4 fixed_beta_log_tests=2 linear_frequency_checks=5')
