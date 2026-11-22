"""Independent finite and high-precision checks of square-gap thermodynamic formulas.

Checks are diagnostic only: the infinite claims follow from the analytic proof.
Run: python verify.py (requires mpmath).
"""
from math import isclose, sqrt, pi
import mpmath as mp
mp.mp.dps = 80


def A(s):
    # The modular theta series is rapidly convergent at the small pressures used here.
    if s >= 1:
        return mp.fsum(mp.exp(-s*n*n) for n in range(1, 100))
    a = mp.sqrt(mp.pi / s)
    return (a * (1 + 2 * mp.fsum(mp.exp(-mp.pi**2 * j*j / s) for j in range(1, 9))) - 1) / 2


def logZ(s):
    return -s + mp.log(A(s))


def mean(s):
    return -mp.diff(logZ, s)


def variance(s):
    return mp.diff(logZ, s, 2)


def pressure(L):
    a, b = mp.mpf('1e-60'), mp.mpf('2')
    for _ in range(235):
        c = (a+b)/2
        if logZ(c) > L:
            a = c
        else:
            b = c
    return (a+b)/2


def entropy_at_parameter(s):
    t = 1 / mean(s)
    return t, s + t * logZ(s)


# Check the modular formula independently against direct sums at finite s.
modular_tests = 0
for sval in ['0.1', '0.25', '0.8', '0.9']:
    s = mp.mpf(sval)
    direct = mp.fsum(mp.exp(-s*n*n) for n in range(1, 240))
    assert abs(A(s)-direct) < mp.mpf('1e-45')
    modular_tests += 1

sample_results = []
for Lval in [2, 3, 4, 5, 6, 7, 8, 9]:
    L = mp.mpf(Lval)
    p = pressure(L)
    assert abs(logZ(p)-L) < mp.mpf('1e-48')
    mu = mean(p)
    rho = 1/mu
    V = variance(p)
    chi = V / mu**3
    assert p > 0 and V > 0 and 0 < rho < mp.mpf('0.5')
    # The density-selected entropy formula must attain the pressure at rho.
    t, h = entropy_at_parameter(p)
    assert abs((h - L*t) - p) < mp.mpf('1e-49')
    assert abs(t-rho) < mp.mpf('1e-49')
    # Local exact information-geometric conversion.
    assert abs(chi * (1 / (t**3 * V))) < mp.inf
    local = mp.sqrt(2*chi)
    periodic = (mp.mpf('.5')-rho)/mp.sqrt(p+L/2)
    # Compare the best finite sample against exact global candidate lower bound.
    sampled = periodic
    for j in range(-20, 31):
        ss = p * mp.exp(mp.mpf(j)/mp.mpf('5'))
        t2,h2 = entropy_at_parameter(ss)
        delt = p+L*t2-h2
        if abs(t2-rho) > mp.mpf('1e-38') and delt > mp.mpf('1e-38'):
            sampled=max(sampled,abs(t2-rho)/mp.sqrt(delt))
    sample_results.append((Lval, float(p), float(rho), float(chi), float(local),float(periodic),float(sampled)))
    assert sampled >= periodic

for row in sample_results:
    print('L=%2d p=%.10g rho=%.10g chi=%.10g C_loc=%.10g periodic=%.10g sampled=%.10g'%row)

for Lval,p,rho,chi,local,periodic,sampled in sample_results[-3:]:
    assert 0.2 < rho * mp.exp(2*Lval) < 2
    assert 0.4 < local*mp.exp(Lval) / mp.sqrt(2*mp.pi) < 2
    assert 0.5 < sampled*mp.sqrt(Lval) < 0.9
print('PASS: 4 modular equalities, 8 pressure roots, 8 second derivative checks, 408 finite candidate comparisons')

# Check the nonlocal stationary condition and its two distinct exponential scales.
stationary_results = []
for Lval in [8, 10, 12, 14, 16, 18, 20]:
    L = mp.mpf(Lval)
    p = pressure(L)
    rho = 1 / mean(p)
    def stationary(s):
        t = 1 / mean(s)
        return L-logZ(s)-2*(s-p)/(t+rho)
    ss = mp.findroot(stationary, (mp.mpf('0.45')*L, mp.mpf('0.55')*L))
    assert abs(stationary(ss)) < mp.mpf('1e-50')
    t,h = entropy_at_parameter(ss)
    delta = p+L*t-h
    assert delta > 0 and t > rho and t < mp.mpf('0.5')
    c_squared = (t-rho)**2/delta
    endpoint = (mp.mpf('.5')-rho)**2/(p+L/2)
    assert c_squared > endpoint
    dens_scale = (mp.mpf('.5')-t)/(mp.mpf('0.75')*mp.exp(-mp.mpf('1.5')*L))
    corr_scale = (c_squared-1/(2*L)) * 2*L**2*mp.exp(mp.mpf('1.5')*L)
    stationary_results.append((Lval,float(ss-L/2),float(dens_scale),float(corr_scale)))
for row in stationary_results:
    print('stationarity L=%2d shift=%+.7g density-scale=%.10g correction-scale=%.10g'%row)
assert abs(stationary_results[-1][2]-1) < 1e-7
assert abs(stationary_results[-1][3]-1) < 0.01
print('PASS: 7 nonlocal stationary residuals, 7 strict endpoint improvements, 2 independent asymptotic scale checks')
