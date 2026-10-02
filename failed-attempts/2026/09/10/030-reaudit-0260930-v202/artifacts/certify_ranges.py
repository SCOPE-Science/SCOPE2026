"""Certify elementary ranges for E(x)=exp(x)+x^2+1 on I=(-1,1).
Stdlib only. Prints enclosures; ends with CERT_RANGES_OK if all checks pass.
Uses interval arithmetic with explicit exp monotonicity bounds:
for interval [a,b], exp([a,b]) subset [e(a_low), e(b_high)] via math.exp on
endpoints (sound up to float rounding; we add explicit padding 1e-12 and
verify margins >> padding so conclusion is robust).
"""
import math

PAD = 1e-9

def exp_lo(x):
    return math.exp(x) * (1 - 1e-15) - 1e-15

def exp_hi(x):
    return math.exp(x) * (1 + 1e-15) + 1e-15

# --- E' zero enclosure: E'(x)=e^x+2x strictly increasing (E''=e^x+2>=2)
# E'(-1)=1/e-2 <0 ; E'(0)=1>0
assert exp_hi(-1) + 2*(-1) < 0, "E'(-1)<0"
assert exp_lo(0) + 2*0 > 0, "E'(0)>0"
lo, hi = -1.0, 0.0
for _ in range(300):
    m = (lo + hi) / 2
    # upper bound of E'(m): if <0 then xc>m? E' increasing: E'(m)<0 => m<xc => lo=m
    if exp_hi(m) + 2*m < 0:
        lo = m
    elif exp_lo(m) + 2*m > 0:
        hi = m
    else:
        break
print("xc in [%.12f, %.12f]" % (lo, hi))
assert hi - lo < 1e-9
assert -0.6 < lo and hi < -0.2, "xc location sanity"

# --- E range: E decreasing on (-1,xc), increasing on (xc,1); E''>=2
# Emin = E(xc) in [E(hi), E(lo)] modulo exp padding
Emin_lo = exp_lo(hi) + hi*hi + 1 - PAD
Emin_hi = exp_hi(lo) + lo*lo + 1 + PAD
print("Emin in [%.10f, %.10f]" % (Emin_lo, Emin_hi))
assert 1.80 < Emin_lo and Emin_hi < 1.95
Emax_hi = exp_hi(0.9999999) + 1 + 1 + PAD
print("Emax < %.10f" % Emax_hi)
assert Emax_hi < 4.72
Emin = Emin_lo  # safe lower bound
Emax = Emax_hi  # safe upper bound

# --- monotonicity margins away from xc: I1=[-0.999, xc-0.05], I2=[xc+0.05, 0.999]
d = 0.05
x1r = hi - d  # right end of I1 (use hi so bound is safe: E' increasing, most negative at left)
x2l = lo + d
# On I1, E'<0: max (closest to 0) at right end
m1 = -(exp_hi(x1r) + 2*x1r)  # |E'| >= m1 on I1 (since E'(x)<=E'(x1r)<0)
# On I2, E'>0: min at left end
m2 = exp_lo(x2l) + 2*x2l
print("m0_I1 >= %.6f, m0_I2 >= %.6f" % (m1, m2))
assert m1 > 0.13 and m2 > 0.13, "uniform slope margin"

# --- wp' bound on X: w in [Emin,Emax] real; |wp'|^2=|4w^3-8|<=4*Emax^3+8
B = math.sqrt(4*Emax**3 + 8) + PAD
print("|wp'| on X <= %.6f" % B)
assert B < 22.0

# --- smooth point: (0,z0) with wp(z0)=2=E(0) exists since wp onto P1; dF/dx=1
assert abs((math.exp(0.0) + 0.0) - 1.0) < 1e-12
print("smooth point derivative dF/dx(0,.)=1 confirmed")
print("CERT_RANGES_OK")
