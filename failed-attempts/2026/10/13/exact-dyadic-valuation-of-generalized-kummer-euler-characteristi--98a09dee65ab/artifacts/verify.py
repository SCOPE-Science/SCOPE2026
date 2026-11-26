from math import isqrt

def v2(n):
    out = 0
    while n and n % 2 == 0:
        out += 1
        n //= 2
    return out

def factorint(n):
    out = {}
    while n % 2 == 0:
        out[2] = out.get(2, 0) + 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def sigma_from_factorization(fac):
    out = 1
    for p, e in fac.items():
        out *= (p ** (e + 1) - 1) // (p - 1)
    return out

def predicted_v2(m):
    fac = factorint(m)
    a = fac.pop(2, 0)
    out = 3 * a
    for p, e in fac.items():
        if e % 2 == 1:
            out += v2(p + 1) + v2(e + 1) - 1
    return out

checks = 0
odd_m = []
for m in range(2, 100001):
    fac = factorint(m)
    sig = sigma_from_factorization(fac)
    chi = m ** 3 * sig
    assert v2(chi) == predicted_v2(m), (m, chi, v2(chi), predicted_v2(m))

    is_odd_square = (m % 2 == 1 and isqrt(m) ** 2 == m)
    assert (chi % 2 == 1) == is_odd_square
    if chi % 2 == 1:
        odd_m.append(m)
    checks += 1

local_checks = 0
for p in range(3, 500, 2):
    # only test primes
    if any(p % q == 0 for q in range(3, isqrt(p) + 1, 2)):
        continue
    for e in range(1, 30):
        sig = (p ** (e + 1) - 1) // (p - 1)
        expected = 0 if e % 2 == 0 else v2(p + 1) + v2(e + 1) - 1
        assert v2(sig) == expected, (p, e, sig, v2(sig), expected)
        local_checks += 1

assert odd_m[:5] == [9, 25, 49, 81, 121]
assert 9 ** 3 * (1 + 3 + 9) == 9477
print("VERIFY_OK", checks, local_checks, len(odd_m), odd_m[:10])
