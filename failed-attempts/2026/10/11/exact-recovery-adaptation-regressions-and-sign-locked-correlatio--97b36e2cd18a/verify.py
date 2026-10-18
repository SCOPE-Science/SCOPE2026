from fractions import Fraction as F

# Pointwise residual checks at exact rational values.
x = F(7, 5)
y = F(11, 6)
z = F(13, 7)
a = F(5, 4)
b = F(9, 8)
c = F(17, 6)
d = F(7, 3)
r = F(2, 5)
s = F(11, 4)
xR = F(-8, 5)
I = F(3, 2)

xdot = y - a*x**3 + b*x**2 - z + I
ydot = c - d*x**2 - y
zdot = r*(s*(x-xR)-z)

assert (y-z) - (a*x**3 - b*x**2 - I) == xdot
assert (c-d*x**2) - y == ydot
assert s*(x-xR) - z == zdot/r

# Abstract conditional-regression variance algebra.
EA = F(7, 5)
EB = EA
EB2 = F(19, 6)
EAB = EB2
EA2 = F(23, 5)
assert (EA2 - EA*EA) - (EB2 - EB*EB) == EA2 - 2*EAB + EB2

# Recovery covariance algebra from E[x^2|y]=(c-y)/d.
Ey = F(4, 5)
Ey2 = F(13, 10)
c0 = F(7, 3)
d0 = F(5, 2)
Ex2 = (c0 - Ey)/d0
Ex2y = (c0*Ey - Ey2)/d0
cov_x2_y = Ex2y - Ex2*Ey
var_y = Ey2 - Ey*Ey
assert cov_x2_y == -var_y/d0

# Adaptation covariance algebra from E[x|z]=xR+z/s.
Ez = F(3, 7)
Ez2 = F(5, 6)
s0 = F(9, 4)
xR0 = F(-8, 5)
Ex = xR0 + Ez/s0
Exz = xR0*Ez + Ez2/s0
cov_x_z = Exz - Ex*Ez
var_z = Ez2 - Ez*Ez
assert cov_x_z == var_z/s0

print("VERIFY_OK")
