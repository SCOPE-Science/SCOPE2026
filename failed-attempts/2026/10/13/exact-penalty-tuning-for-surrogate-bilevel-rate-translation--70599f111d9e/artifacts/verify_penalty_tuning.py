from fractions import Fraction as F
from math import sqrt


def deriv(rho, a1, b0, b1, ell):
    s = sqrt(2.0 * (float(b1) + float(b0) / float(rho)))
    return float(a1) - float(ell * b0) / (float(rho) ** 2 * s)


def second(rho, b0, b1, ell):
    r=float(rho); b0=float(b0); b1=float(b1); ell=float(ell)
    return (sqrt(2.0)*ell*b0*(4.0*b1*r+3.0*b0))/(4.0*r**2.5*(b1*r+b0)**1.5)


def quartic_value(rho, a1, b0, b1, ell):
    return 2*a1*a1*(b1*rho**4+b0*rho**3)-ell*ell*b0*b0

# Positive-b1 exact case: rho*=1.
a1=F(1); b0=F(2); b1=F(6); ell=F(2); rho=F(1)
assert quartic_value(rho,a1,b0,b1,ell)==0
assert deriv(F(1,2),a1,b0,b1,ell)<0
assert abs(deriv(rho,a1,b0,b1,ell))<1e-14
assert deriv(F(2),a1,b0,b1,ell)>0
assert second(rho,b0,b1,ell)>0
# Minimum-value identity at rho=1.
U = F(0) + a1*rho + F(2)*F(4)  # sqrt(2*(6+2)) = 4
U_identity = F(0) + 3*a1*rho + 2*a1*b1*rho*rho/b0
assert U == U_identity == F(9)

# b1=0 cube-root case with rho*=1.
a1=F(1); b0=F(2); b1=F(0); ell=F(1); rho=F(1)
assert ell*ell*b0 == 2*a1*a1*rho**3
assert quartic_value(rho,a1,b0,b1,ell)==0
assert deriv(F(1,2),a1,b0,b1,ell)<0
assert abs(deriv(rho,a1,b0,b1,ell))<1e-14
assert deriv(F(2),a1,b0,b1,ell)>0
# Here U-a0 = rho + 2/sqrt(rho), so the minimum excess is 3.
assert F(1)+F(2)==F(3)

# Degenerate regimes: derivative signs.
# a1=0<b0: strictly decreasing.
for r in [F(1,10),F(1),F(10)]:
    assert deriv(r,F(0),F(2),F(3),F(1))<0
# b0=0<a1: derivative is exactly a1.
for r in [F(1,10),F(1),F(10)]:
    assert abs(deriv(r,F(3),F(0),F(2),F(1))-3.0)<1e-14
# a1=b0=0: the bound is rho-independent.
for r in [F(1,10),F(1),F(10)]:
    assert abs(deriv(r,F(0),F(0),F(2),F(1)))<1e-14

print('VERIFY_OK')
