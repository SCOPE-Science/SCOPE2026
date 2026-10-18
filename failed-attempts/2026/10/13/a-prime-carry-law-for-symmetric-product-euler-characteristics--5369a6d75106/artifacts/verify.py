from math import comb, gcd

def digit_sum(n, p):
    s = 0
    while n:
        s += n % p
        n //= p
    return s

def vp(n, p):
    if n == 0:
        raise ValueError("valuation of zero is not tested")
    n = abs(n)
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def carry_count(a, b, p):
    carry = 0
    count = 0
    while a or b or carry:
        da = a % p
        db = b % p
        total = da + db + carry
        new_carry = 1 if total >= p else 0
        count += new_carry
        carry = new_carry
        a //= p
        b //= p
    return count

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

primes = [p for p in range(2, 100) if is_prime(p)]

positive_checks = 0
for c in range(1, 81):
    for n in range(0, 121):
        E = comb(c + n - 1, n)
        for p in primes:
            direct = vp(E, p)
            digits = (digit_sum(n, p) + digit_sum(c - 1, p) - digit_sum(c + n - 1, p)) // (p - 1)
            carries = carry_count(n, c - 1, p)
            assert direct == digits == carries, (c, n, p, E, direct, digits, carries)
            positive_checks += 1

negative_checks = 0
for m in range(1, 121):
    for n in range(0, m + 1):
        E = (-1) ** n * comb(m, n)
        for p in primes:
            direct = vp(E, p)
            digits = (digit_sum(n, p) + digit_sum(m - n, p) - digit_sum(m, p)) // (p - 1)
            carries = carry_count(n, m - n, p)
            assert direct == digits == carries, (m, n, p, E, direct, digits, carries)
            negative_checks += 1

curve_checks = 0
for g in range(2, 501):
    m = 2 * g - 2
    vals = [comb(m, n) for n in range(1, m)]
    G = 0
    for x in vals:
        G = gcd(G, x)

    h = g - 1
    dyadic = h > 0 and (h & (h - 1)) == 0
    expected = 2 if dyadic else 1
    assert G == expected, (g, m, G, expected)

    # Carry-free parity count among all nonzero positive symmetric powers n=1..m.
    odd_count = sum(1 for n in range(1, m + 1) if comb(m, n) % 2 == 1)
    expected_odd = (1 << bin(m).count("1")) - 1
    assert odd_count == expected_odd, (g, odd_count, expected_odd)
    curve_checks += 1

print("VERIFY_OK", positive_checks, negative_checks, curve_checks)
