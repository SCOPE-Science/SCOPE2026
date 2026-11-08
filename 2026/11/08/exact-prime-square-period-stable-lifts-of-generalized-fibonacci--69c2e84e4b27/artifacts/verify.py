"""Exact finite checks for the prime-square recurrence-period lifting theorem."""

PRIMES = (3, 5, 7, 11, 13, 17)
IDENTITY = (1, 0, 0, 1)


def mul(A, B, modulus):
    a, b, c, d = A
    e, f, g, h = B
    return ((a*e + b*g) % modulus, (a*f + b*h) % modulus,
            (c*e + d*g) % modulus, (c*f + d*h) % modulus)


def power(A, exponent, modulus):
    out = IDENTITY
    while exponent:
        if exponent & 1:
            out = mul(out, A, modulus)
        A = mul(A, A, modulus)
        exponent >>= 1
    return out


def companion(a, b):
    return (a, b, 1, 0)


def order_p(a, b, p):
    A = companion(a, b)
    x = IDENTITY
    for h in range(1, 2*p*(p*p-1) + 1):
        x = mul(x, A, p)
        if x == IDENTITY:
            return h
    raise AssertionError('missing matrix period')


def pair_period(a, b, modulus, maximum):
    f0, f1 = 0, 1
    for h in range(1, maximum+1):
        f0, f1 = f1, (a*f1 + b*f0) % modulus
        if (f0, f1) == (0, 1):
            return h
    raise AssertionError('missing recurrence period')


def check():
    matrix_lifts = 0
    sequence_checks = 0
    for p in PRIMES:
        n_regular = n_singular = n_stable = 0
        for a0 in range(p):
            for b0 in range(1, p):
                h = order_p(a0, b0, p)
                singular = (a0*a0 + 4*b0) % p == 0
                found = []
                for x in range(p):
                    for y in range(p):
                        a, b = a0+p*x, b0+p*y
                        M = companion(a, b)
                        stable = power(M, h, p*p) == IDENTITY
                        # Kernel of reduction has exponent p.
                        assert power(M, h*p, p*p) == IDENTITY
                        if stable:
                            found.append((a, b))
                        if p <= 7:
                            assert pair_period(a, b, p*p, h*p) == (h if stable else h*p)
                            sequence_checks += 1
                        matrix_lifts += 1
                expected = (3 if p == 3 else 0) if singular else 1
                assert len(found) == expected, (p, a0, b0, h, found)
                if singular:
                    n_singular += 1
                    if p == 3:
                        assert all((a*a+4*b) % 9 == 6 for a, b in found)
                else:
                    n_regular += 1
                n_stable += len(found)
        assert n_singular == p-1
        assert n_regular == (p-1)*(p-1)
        assert n_stable == (10 if p == 3 else (p-1)*(p-1))
        print(f'p={p} regular_bases={n_regular} singular_bases={n_singular} stable_lifts={n_stable}')
    assert matrix_lifts == sum(p**3*(p-1) for p in PRIMES)
    print(f'VERIFY_OK matrix_lifts={matrix_lifts} recurrence_checks={sequence_checks} primes={PRIMES}')


if __name__ == '__main__':
    check()
