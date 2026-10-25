from fractions import Fraction as F

# Exact rational test data for the stationary raw-moment formulas.
a = F(9, 10)
b = F(-6013, 10000)
c = F(2)
d = F(1, 2)

u = F(7, 20)
v = F(-3, 25)

raw_diff = (1-a)*u - b*v
raw_cross2 = -c*u + (1-d)*v

A = raw_diff - (u*u - v*v)
B = raw_cross2 - 2*u*v

assert A == (1-a)*u - b*v - u*u + v*v
assert B == -c*u + (1-d)*v - 2*u*v

# Choose a trace large enough to define a positive covariance.
# Use exact A,B to synthesize p-r=A and 2q=B.
T = F(20)
p = (T + A) / 2
r = (T - A) / 2
q = B / 2

assert p-r == A
assert 2*q == B

D2 = A*A + B*B
det = p*r - q*q
assert 4*det == T*T - D2

# Centered case.
uc = vc = F(0)
Ac = (1-a)*uc - b*vc - uc*uc + vc*vc
Bc = -c*uc + (1-d)*vc - 2*uc*vc
assert Ac == 0 and Bc == 0

# Classical coefficients.
assert 1-a == F(1,10)
assert -b == F(6013,10000)
assert 1-d == F(1,2)
assert c == F(2)

print("VERIFY_OK")
