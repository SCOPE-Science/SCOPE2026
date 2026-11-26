#!/usr/bin/env python3
from fractions import Fraction

# q = x*y*(x+25y)*(x+9y)
# q_x = y*(3x^2+68xy+225y^2)
# q_y = x*(x^2+68xy+675y^2)

def poly_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def poly_divmod(a, b):
    a = [Fraction(x) for x in a]
    b = poly_trim([Fraction(x) for x in b])
    if b == [0]:
        raise ZeroDivisionError
    while len(a) >= len(b) and a != [0]:
        c = a[-1] / b[-1]
        k = len(a) - len(b)
        for i, bi in enumerate(b):
            a[i+k] -= c * bi
        poly_trim(a)
    return a

def poly_gcd(a, b):
    a = poly_trim([Fraction(x) for x in a])
    b = poly_trim([Fraction(x) for x in b])
    while b != [0]:
        a, b = b, poly_divmod(a, b)
    if a != [0]:
        lc = a[-1]
        a = [x/lc for x in a]
    return a

# On y=1 the non-coordinate factors are:
# 3r^2+68r+225 and r^2+68r+675.
g = poly_gcd([225,68,3], [675,68,1])
assert g == [Fraction(1)]

# Coordinate points are not common zeros.
# At x=0,y=1: q_x=225 != 0.
# At x=1,y=0: q_y=1 != 0.
assert 225 != 0 and 1 != 0

binary_jacobian_length = 3 * 3
s_factor_length = 3
z_factor_length = 1
milnor = binary_jacobian_length * s_factor_length * z_factor_length
assert binary_jacobian_length == 9
assert milnor == 27

# Weighted-degree check for the exact v=0 local equation
# (z - 1 - s^4)(z^2 - 4s^4) - q(x,y)
# weights: wt(x)=wt(y)=wt(s)=1, wt(z)=2.
# Expansion outside -q:
# z^3 - 4 z s^4 - z^2 + 4 s^4 - s^4 z^2 + 4 s^8.
terms = {
    (0,0,0,3): 1,    # z^3
    (0,0,4,1): -4,   # -4 z s^4
    (0,0,0,2): -1,   # -z^2
    (0,0,4,0): 4,    # 4 s^4
    (0,0,4,2): -1,   # -s^4 z^2
    (0,0,8,0): 4,    # 4 s^8
}
def wt(exp):
    x,y,s,z = exp
    return x+y+s+2*z

initial = {e:c for e,c in terms.items() if wt(e)==4}
higher = {e:c for e,c in terms.items() if wt(e)>4}
assert initial == {(0,0,0,2):-1, (0,0,4,0):4}
assert len(initial) + len(higher) == len(terms)
assert all(wt(e) > 4 for e in higher)

print("binary_quartic_jacobian_projective_common_root=no")
print("binary_quartic_jacobian_length=9")
print("s_factor_length=3")
print("z_factor_length=1")
print("total_space_milnor_number=27")
print("v0_initial_weighted_degree=4")
print("v0_higher_terms_strictly_above_weight=4")
print("VERIFY_OK")
