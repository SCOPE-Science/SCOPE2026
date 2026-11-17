"""Independent bounded checks for corrected Catalan prime-power surjectivity.

Proof for all powers uses large-block multiplication and the primitive p-adic
limit of binom(2*p**T,p**T), NOT fixed-window product-of-small-binomial units.
"""
from math import comb


def factorial_valuation(n, p):
    ans = 0
    while n:
        n //= p
        ans += n
    return ans


def modular_unit_factorial(n, p, modulus):
    # For odd p, one complete residue block of units is -1 modulo p**k.
    pref = [1]
    for i in range(1, modulus):
        pref.append(pref[-1] * (i if i % p else 1) % modulus)
    ans = 1
    while n:
        blocks, rem = divmod(n, modulus)
        ans = ans * (-1 if blocks % 2 else 1) * pref[rem] % modulus
        n //= p
    return ans


def central_binomial_mod(n, p, k):
    m = p ** k
    v = factorial_valuation(2*n, p) - 2*factorial_valuation(n, p)
    if v >= k:
        return 0
    unit_2n = modular_unit_factorial(2*n, p, m)
    unit_n = modular_unit_factorial(n, p, m)
    return p**v * unit_2n * pow(unit_n, -2, m) % m


def catalan_mod(n, p, k):
    m = p ** k
    # This modular evaluator only needs cases with p not dividing n+1.
    assert (n + 1) % p
    return central_binomial_mod(n, p, k) * pow(n + 1, -1, m) % m


def verify():
    for p in (3, 5, 11):
        h = (p + 1)//2
        assert pow(2, p-1, p*p) != 1
        assert len({pow(2, a, p) for a in range(p-1)}) == p-1
        for k in (1, 2, 3):
            if p**k > 500:
                continue
            modulus = p**k
            seen = set()
            c = 1
            for n in range(4000):
                seen.add(c % modulus)
                c = c * (4*n+2)//(n+2)
            assert len(seen) == modulus, (p, k, len(seen))
            assert all(central_binomial_mod(n, p, k) == comb(2*n, n) % modulus
                       for n in range(40)), (p, k)
            for v in range(k+1):
                L = 2*k+3
                n = sum(h*p**(j*L) for j in range(1, v+1))
                carries = factorial_valuation(2*n, p)-2*factorial_valuation(n, p)
                assert carries == v and n % modulus == 0, (p, k, v)
                assert catalan_mod(n, p, k) == central_binomial_mod(n, p, k)
            # Very large unit blocks approach one fixed p-adic unit, not
            # necessarily the small binomial coefficient 2 modulo p**k.
            values = [central_binomial_mod(p**T, p, k) for T in range(1,k+4)]
            assert len(set(values[-2:])) == 1, (p, k, values)
            assert values[-1] % p**min(k, 2) == 2 % p**min(k, 2)
    assert catalan_mod(3**9, 3, 3) == 20
    assert catalan_mod(3**9, 3, 3) != 2  # Regression: invalid old lemma.
    print('VERIFY_OK: finite residue coverage, valuation seeds, stable block units, and false-lemma regression')


if __name__ == '__main__':
    verify()
