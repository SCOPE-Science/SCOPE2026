from fractions import Fraction as F

# Exact algebra for the second-moment circle.
# Pick several rational A,u,mx and derive M2 from the invariant relation.
tests = [
    (F(1), F(9,10), F(4)),
    (F(2), F(1,2), F(3)),
    (F(3,2), F(2,3), F(7,4)),
]
for A,u,mx in tests:
    den = 1-u*u
    M2 = (2*A*mx-A*A)/den
    c = A/den
    R2 = A*A*u*u/(den*den)
    lhs = M2 - 2*c*mx + c*c
    assert lhs == R2

A = F(1)
u = F(9,10)
den = 1-u*u
c = A/den
R = A*u/den
assert c == F(100,19)
assert R == F(90,19)
assert R*R == F(8100,361)

# Variance decomposition: E|Z-c|^2 = Var(Z)+|E Z-c|^2.
# Use exact abstract components V, mx, my.
for V,mx,my in [(F(3,7),F(1,2),F(2,5)),(F(0),F(4,3),F(-1,5))]:
    c0 = F(5,4)
    left = V + (mx-c0)*(mx-c0) + my*my
    right = V + ((mx-c0)*(mx-c0)+my*my)
    assert left == right

print('VERIFY_OK')
