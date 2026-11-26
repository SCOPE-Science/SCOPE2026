"""Polynomial identities and finite Cartier checks for a characteristic-two tower."""
from functools import cache
from itertools import product


def xor_sum(parts):
    out = set()
    for part in parts:
        out.symmetric_difference_update(part)
    return frozenset(out)


@cache
def normal(t, c, y, v):
    """Monic reduction in F2[t,c,y,v]/(y²+y+t³,v²+v+y³+c²y)."""
    if v >= 2:
        return xor_sum((normal(t,c,y,v-1), normal(t,c,y+3,v-2),
                        normal(t,c+2,y+1,v-2)))
    if y >= 2:
        return xor_sum((normal(t,c,y-1,v), normal(t+3,c,y-2,v)))
    return frozenset({(t,c,y,v)})


def mul(a, b):
    return xor_sum(normal(*(i+j for i,j in zip(x,z))) for x in a for z in b)


def sq(a):
    return mul(a,a)


T, C, Y, V = (normal(*e) for e in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)])
ty = mul(T,Y)
t3 = mul(T,sq(T))
candidates = (
    (Y, Y, T),
    (ty, sq(T), Y),
    (mul(Y,sq(Y)), xor_sum((Y,t3)), ty),
    (V, xor_sum((V,Y,t3,mul(C,Y))), xor_sum((ty,mul(C,T)))),
)
for target, a, b in candidates:
    assert target == xor_sum((sq(a),mul(T,sq(b))))
print('FORMAL_CHAR2_POLYNOMIAL_IDENTITIES_OK')


def gf_mul(x, y):
    """Field elements are a+b*alpha, alpha^2=alpha+1."""
    ax, bx = x & 1, x >> 1
    ay, by = y & 1, y >> 1
    return ((ax*ay ^ bx*by) | ((ax*by ^ bx*ay ^ bx*by) << 1))


def sqrt(x):
    # Squaring is Frobenius on F_4; its square is the identity.
    return gf_mul(x, x)


assert sqrt(2) == 3 and sqrt(3) == 2
assert all(gf_mul(sqrt(a), sqrt(a)) == a for a in range(4))


def cartier(a, c0):
    """Apply inverse Frobenius on the input coefficients before the matrix."""
    _, x1, x2, _, x4, x5 = map(sqrt, a)
    return (x1, x2 ^ gf_mul(c0, x4), x5, 0, 0, x4)


def ranks(c0):
    # Rank is log base 4 of the image cardinality, even for semilinear maps.
    image = set(product(range(4), repeat=6))
    result = [6]
    for _ in range(5):
        image = {cartier(a, c0) for a in image}
        result.append([4**i for i in range(7)].index(len(image)))
    return tuple(result)


# This input distinguishes the inverse-Frobenius action from F_4-linearity.
assert cartier((0, 2, 0, 0, 0, 0), 0) == (3, 0, 0, 0, 0, 0)
profile = (6, 4, 3, 2, 1, 0)
for c0 in range(4):
    assert ranks(c0) == profile

for lam in range(4):
    b = lam ^ sqrt(lam ^ 1)
    assert ranks(sqrt(b)) == profile

semigroup = {4*a+6*b+9*c for a,b,c in product(range(5), repeat=3)}
gaps = [i for i in range(12) if i not in semigroup]
assert gaps == [1, 2, 3, 5, 7, 11]
assert all(i in semigroup for i in range(12,16))  # closure under addition of 4
print('GF4_CARTIER_POWER_RANKS_OK 6,4,3,2,1,0 (all four c0 and all four lambda)')
print('WEIERSTRASS_SEMIGROUP_GAPS_OK 1,2,3,5,7,11')
print('CERTIFICATE_OK')
