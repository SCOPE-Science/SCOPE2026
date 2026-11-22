"""Finite diagnostics for the analytic annular Szego decorrelation-distance law.

These checks do not establish the all-parameter theta-product zero classification
or global hyperbolic inequality, which are proved symbolically in RESULT.md.
"""
import math
import mpmath as mp
mp.mp.dps = 75


def unique_interior_zero(q, r):
    x = mp.log(r)/(2*mp.log(q))
    if abs(x-mp.nint(x)) < mp.mpf("1e-65"):
        return None
    k = int(mp.ceil(x))
    s = q**(2*k)/r
    assert q*q < s < 1
    return s


def closed_distance(q, r):
    x = mp.log(r)/(2*mp.log(q))
    if abs(x-mp.nint(x)) < mp.mpf("1e-65"):
        return mp.inf
    L = -mp.log(q)
    sigma = mp.pi**2/(2*L)
    return 2*mp.asinh(mp.sinh(sigma)/mp.sin(mp.pi*(x-mp.floor(x))))


def strip_coshed(q, s, h):
    L = -mp.log(q)
    theta0 = mp.pi*mp.log(s/(q*q))/(2*L)
    theta1 = theta0+h
    theta2 = theta0-h
    delta = mp.pi**2/L
    return (mp.cosh(delta)-mp.cos(theta1)*mp.cos(theta2))/(mp.sin(theta1)*mp.sin(theta2))

checks = 0
for q0 in ('0.1','0.3','0.6'):
    q=mp.mpf(q0); L=-mp.log(q)
    for shift in ('-1.23','-0.21','0.14','0.37','0.5','0.82','1.26','2.65'):
        xi=mp.mpf(shift)
        r=q**(2*xi)
        s=unique_interior_zero(q,r)
        assert s is not None
        d=closed_distance(q,r)
        dperiod=closed_distance(q,r*q*q)
        assert abs(d-dperiod)<mp.mpf('1e-60')
        checks+=1
        t0=mp.pi*mp.log(s/(q*q))/(2*L)
        assert abs(mp.acosh(strip_coshed(q,s,mp.mpf('0')))-d)<mp.mpf('1e-60')
        checks+=1
        hmax=min(t0,mp.pi-t0)
        for fac in ('0.12','0.49','0.91'):
            hh=hmax*mp.mpf(fac)
            dplus=mp.acosh(strip_coshed(q,s,hh))
            dminus=mp.acosh(strip_coshed(q,s,-hh))
            assert dplus>d
            assert abs(dplus-dminus)<mp.mpf('1e-60')
            checks+=1
        assert d>=mp.pi**2/L-mp.mpf('1e-60')
        checks+=1

# Fourier-Laurent covariance checks for genuinely non-core zeros.
for q0,r0 in [('0.3','0.5'),('0.2','0.7'),('0.4','0.8'),('0.55','0.25')]:
    q=mp.mpf(q0);r=mp.mpf(r0)
    s=unique_interior_zero(q,r)
    value=sum((-s)**n/(1+r*q**(2*n)) for n in range(-700,701))
    assert abs(value)<mp.mpf('1e-32'), (q,r,mp.nstr(value,12))
    checks+=1

for q0 in ('0.1','0.3','0.6'):
    q=mp.mpf(q0);L=-mp.log(q)
    for m in range(-2,3):
        r=q**(2*m)
        assert unique_interior_zero(q,r) is None
        assert closed_distance(q,r)==mp.inf
        checks+=1
        center=q**(2*m+1)
        assert abs(closed_distance(q,center)-mp.pi**2/L)<mp.mpf('1e-60')
        checks+=1

# Divergence normalization near exceptional weights; estimate remainder at
# an explicit small fractional log-weight gap.
for q0 in ('0.2','0.4'):
    q=mp.mpf(q0);L=-mp.log(q)
    eps=mp.mpf('1e-7')
    r=q**(2*eps)
    d=closed_distance(q,r)
    asym=2*mp.log(2*mp.sinh(mp.pi**2/(2*L))/(mp.pi*eps))
    assert abs(d-asym)<mp.mpf('1e-9')
    checks+=1
print(f'PASS {checks} finite diagnostics (75-digit precision)')
