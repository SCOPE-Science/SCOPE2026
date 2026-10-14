from math import isqrt

BOUND = 500_000

# Exact divisor sums up to BOUND.
sigma = [0] * (BOUND + 1)
for d in range(1, BOUND + 1):
    for n in range(d, BOUND + 1, d):
        sigma[n] += d

# Smallest-prime-factor table.
spf = list(range(BOUND + 1))
for i in range(2, isqrt(BOUND) + 1):
    if spf[i] == i:
        for n in range(i * i, BOUND + 1, i):
            if spf[n] == n:
                spf[n] = i

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def divisors_from_factorization(f):
    ds = [1]
    for p, e in f:
        old = list(ds)
        mul = 1
        for _ in range(e):
            mul *= p
            ds.extend(d * mul for d in old)
    return ds

def strict_pan_brutal(n, f):
    if sigma[n] <= 2 * n:
        return False
    return all(d == n or sigma[d] < 2 * d for d in divisors_from_factorization(f))

def predicted_two_prime_pan(n, f):
    if len(f) != 2 or f[0][0] != 2:
        return False
    (two, a), (p, b) = f
    return b == 1 and a >= 2 and (1 << a) < p < (1 << (a + 1)) - 1

actual = []
predicted = []
checked_support_two = 0
for n in range(2, BOUND + 1):
    f = factor(n)
    if len(f) != 2:
        continue
    checked_support_two += 1
    a = strict_pan_brutal(n, f)
    b = predicted_two_prime_pan(n, f)
    if a:
        actual.append(n)
    if b:
        predicted.append(n)
    assert a == b, (n, f, sigma[n], a, b)

# Exact phase-count identity on a grid.  The number of excluded Mersenne
# primes is computed directly; primality here is exact by trial division.
def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def primepi_floor(x):
    u = int(x)
    return sum(isprime(k) for k in range(2, u + 1))

def mersenne_primes_leq(x):
    c = 0
    j = 3
    while (1 << j) - 1 <= x:
        if isprime((1 << j) - 1):
            c += 1
        j += 1
    return c

phase_checks = 0
for m in range(2, 9):
    y = 1 << m
    for num, den in [(1,1),(5,4),(3,2),(2,1),(5,2),(3,1),(15,4)]:
        X = (num * (1 << (2*m))) // den
        r_num = X
        # Since all chosen X lie in [4^m,4^(m+1)), this is the phase m.
        U_num = min(X, 2 * y * y)
        U = U_num / y
        exact = sum(1 for n in actual if n <= X)
        formula = primepi_floor(U) - 2 - mersenne_primes_leq(U)
        assert exact == formula, (m, X, U, exact, formula)
        phase_checks += 1

print(
    'VERIFY_OK '
    f'bound={BOUND} support_two_checked={checked_support_two} '
    f'two_prime_pan={len(actual)} phase_identities={phase_checks} '
    f'first={actual[:12]}'
)
