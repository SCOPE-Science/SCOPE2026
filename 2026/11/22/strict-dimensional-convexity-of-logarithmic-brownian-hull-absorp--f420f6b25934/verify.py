"""Reproducible checks for a logarithmic Brownian-hull absorption-time identity.
Only finite numerical identities are tested; the infinite claims use the separate proof.
Run: python verify.py
Requires: mpmath (tested at 70 decimal digits).
"""
import mpmath as mp
from fractions import Fraction

mp.mp.dps = 70
TOL = mp.mpf('1e-48')
checks = 0

def close(x, y, tol=TOL):
    global checks
    assert abs(x-y) < tol, (x, y, x-y)
    checks += 1

def remainder(d):
    return mp.nsum(lambda k: 1/(k*(k+1)*(2*k+1)**(d-1)), [1, mp.inf])

def log_mean(d):
    return 2*d-1-mp.log(2)-mp.digamma(mp.mpf(d)/2)-remainder(d)

def derivative_gf(w):
    return w*(-2*mp.euler-2*mp.digamma((1-w)/2))/(1-w*w)

# The same quantity follows from coefficient extraction from the published Mellin GF.
for d in range(1, 9):
    via_coefficient = mp.diff(derivative_gf, 0, d-1)/mp.factorial(d-1)
    via_coefficient -= mp.log(2)+mp.digamma(mp.mpf(d)/2)
    close(via_coefficient, log_mean(d))

# Two one- and two-dimensional independent first-passage Mellin formulas.
close(log_mean(1), mp.euler+mp.log(2))
close(log_mean(2), mp.euler+3*mp.log(2))

# Explicit small-dimensional curvature formulas.
close(log_mean(3)-2*log_mean(2)+log_mean(1), mp.pi**2/2-2-4*mp.log(2))
close(log_mean(4)-2*log_mean(3)+log_mean(2), 4*mp.log(2)+mp.mpf(7)/2*mp.zeta(3)+3-mp.pi**2)

for d in range(1, 31):
    m = log_mean(d)
    mnext = log_mean(d+1)
    mnext2 = log_mean(d+2)
    assert mnext > m
    checks += 1
    assert mnext-m < 2
    checks += 1
    assert mnext2-2*mnext+m > 0
    checks += 1
    assert 0 < remainder(d) <= 1
    checks += 1
    if d >= 3:
        # Exact algebraic majorant for the negative curvature contribution.
        upper = Fraction(2,9)*Fraction(1,3)**(d-1)+Fraction(1,2)*Fraction(1,5)**(d-1)
        lower = Fraction(4,d*(d+1)*(d+2))
        assert upper < lower
        checks += 1
    if d >= 2:
        close(remainder(d)-mp.mpf('0.5')*mp.power(3,1-d),
              mp.nsum(lambda k: 1/(k*(k+1)*(2*k+1)**(d-1)), [2,mp.inf]))
        checks += 1

# Rigorous rational margins in the initial curvature inequalities.
assert Fraction(314,100)**2/2-2-4*Fraction(7,10) > 0
checks += 1
assert Fraction(7,2)*Fraction(6,5)+4*Fraction(69,100)+3-Fraction(22,7)**2 > 0
checks += 1
assert sum((Fraction(1,k**3) for k in range(1,17)),Fraction(0))>Fraction(6,5)
checks += 1
print('PASS',checks,'checks')
for d in (1,2,3,4,5,10,20):
    print('d',d,'mean_log_time',mp.nstr(log_mean(d),18),'curvature',mp.nstr(log_mean(d+2)-2*log_mean(d+1)+log_mean(d),12))
