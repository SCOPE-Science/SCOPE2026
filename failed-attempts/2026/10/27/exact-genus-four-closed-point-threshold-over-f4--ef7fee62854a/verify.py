"""Exact finite-field check for C: y^2 + y = x^9 + omega over F_4.

The mathematical proof in RESULT.md explains why the trace identities hold
for every point.  This script independently checks the finite-field model,
trace values, and resulting point counts using only Python integers.
"""
MOD = 0b1000011  # t^6 + t + 1
DEG = 6
MASK = (1 << DEG) - 1


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << DEG):
            a ^= MOD
    return out


def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


def poly_mod(a, b):
    db = b.bit_length() - 1
    while a and a.bit_length() - 1 >= db:
        a ^= b << (a.bit_length() - 1 - db)
    return a


def poly_gcd(a, b):
    while b:
        a, b = b, poly_mod(a, b)
    return a


def irreducible_degree_six():
    # Rabin test for degree 6: x^(2^6)=x and gcd(x^(2^(6/p))-x,f)=1
    # for the prime divisors p=2,3 of 6.
    x = 2
    if power(x, 1 << DEG) != x:
        return False
    for p in (2, 3):
        y = x
        for _ in range(DEG // p):
            y = mul(y, y)
        if poly_gcd(y ^ x, MOD) != 1:
            return False
    return True


def trace(a):
    total = 0
    z = a
    for _ in range(DEG):
        total ^= z
        z = mul(z, z)
    assert total in (0, 1)
    return total


assert irreducible_degree_six()
omega = 58
omega2 = mul(omega, omega)
assert omega2 == 59
assert (omega2 ^ omega ^ 1) == 0
F4 = (0, 1, omega, omega2)
assert len(set(F4)) == 4
assert trace(omega) == 1
assert trace(omega2) == 1

# In F_4, x^9 is 0 for x=0 and 1 for x!=0; the absolute trace of
# x^9+omega is therefore 1 for all four x, so there are no affine points.
for x in F4:
    rhs = power(x, 9) ^ omega
    assert trace(rhs) == 1
N1 = 1  # the unique point above infinity

# For every x in F_64, x^9 lies in the unique subgroup of order 7, hence
# in F_8.  The trace F_64 -> F_2 of every F_8 element is zero because
# [F_64:F_8]=2.  Adding omega, whose absolute trace is 1, gives trace 1.
for x in range(1 << DEG):
    x9 = power(x, 9)
    assert power(x9, 8) == x9  # x^9 belongs to F_8
    assert trace(x9) == 0
    assert trace(x9 ^ omega) == 1
N3 = 1  # no affine points over F_64; one point above infinity
B3 = (N3 - N1) // 3
assert N1 == 1 and N3 == 1 and B3 == 0
print(f"N1={N1}; N3={N3}; B3={B3}; VERIFY_OK")
