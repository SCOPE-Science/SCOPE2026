from math import comb

def nu2(n):
    assert n > 0
    return (n & -n).bit_length() - 1

def carry_count(a, b):
    carry = 0
    total = 0
    while a or b or carry:
        bit_sum = (a & 1) + (b & 1) + carry
        carry = 1 if bit_sum >= 2 else 0
        if carry:
            total += 1
        a >>= 1
        b >>= 1
    return total

def discriminant_degree(N, c, d):
    n = N - c
    assert N >= 1 and 1 <= c <= N and d >= 2 and n >= 0
    return c * comb(N + 1, c) * d ** (c - 1) * (d - 1) ** (n + 1)

def predicted_valuation(N, c, d):
    n = N - c
    return (
        nu2(N + 1)
        + carry_count(c - 1, n + 1)
        + (c - 1) * nu2(d)
        + (n + 1) * nu2(d - 1)
    )

def predicted_odd(N, c, d):
    return c == 1 and N % 2 == 0 and d % 2 == 0

checks = 0
for N in range(1, 81):
    for c in range(1, N + 1):
        for d in range(2, 65):
            D = discriminant_degree(N, c, d)
            assert nu2(D) == predicted_valuation(N, c, d)
            assert (D % 2 == 1) == predicted_odd(N, c, d)
            if c >= 2:
                assert D % 4 == 0
            checks += 1

assert discriminant_degree(2, 2, 2) == 12
assert nu2(discriminant_degree(2, 2, 2)) == 2
print("VERIFY_OK", checks, discriminant_degree(2, 2, 2))
