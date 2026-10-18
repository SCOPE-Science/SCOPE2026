from fractions import Fraction
from math import factorial

def deg_type_c(n, r):
    # Highest weight omega_r for type C_n, paired with positive coroots.
    D = 2*r*(n-r) + r*(r+1)//2
    prod = Fraction(1, 1)

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # coroot e_i - e_j
            num = (1 if i <= r else 0) - (1 if j <= r else 0)
            den = j - i
            if num:
                prod *= Fraction(num, den)

            # coroot e_i + e_j
            num = (1 if i <= r else 0) + (1 if j <= r else 0)
            den = 2*n - i - j + 2
            if num:
                prod *= Fraction(num, den)

        # coroot e_i
        num = 1 if i <= r else 0
        den = n - i + 1
        if num:
            prod *= Fraction(num, den)

    val = factorial(D) * prod
    assert val.denominator == 1
    return val.numerator

def deg_type_b(n, r):
    # Highest weight omega_r for r<n in type B_n, paired with positive coroots.
    D = 2*r*(n-r) + r*(r+1)//2
    prod = Fraction(1, 1)

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # long-root coroot e_i - e_j
            num = (1 if i <= r else 0) - (1 if j <= r else 0)
            den = j - i
            if num:
                prod *= Fraction(num, den)

            # long-root coroot e_i + e_j
            num = (1 if i <= r else 0) + (1 if j <= r else 0)
            den = 2*n - i - j + 1
            if num:
                prod *= Fraction(num, den)

        # short-root coroot 2e_i
        num = 2 if i <= r else 0
        den = 2*n - 2*i + 1
        if num:
            prod *= Fraction(num, den)

    val = factorial(D) * prod
    assert val.denominator == 1
    return val.numerator

pairs = 0
for n in range(2, 19):
    for r in range(1, n):
        c = deg_type_c(n, r)
        b = deg_type_b(n, r)
        assert b == (2 ** r) * c, (n, r, b, c)

        t = n - r
        top = tuple(2*n - r - i for i in range(r))
        D = 2*r*(n-r) + r*(r+1)//2
        assert sum(top) == D
        assert sum(1 for x in top if x > t) == r
        pairs += 1

print("VERIFY_OK", pairs)
