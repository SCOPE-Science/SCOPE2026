from fractions import Fraction
from math import factorial
from collections import Counter


def partitions(n, mx=None):
    if n == 0:
        yield ()
        return
    if mx is None or mx > n:
        mx = n
    for first in range(mx, 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


def aut_order_type(partition, p):
    """Automorphism order for the abelian p-group of partition type."""
    if not partition:
        return 1
    h = max(partition)
    conjugate = [sum(x >= i for x in partition) for i in range(1, h+1)]
    val = Fraction(p ** sum(c*c for c in conjugate), 1)
    for multiplicity in Counter(partition).values():
        for j in range(1, multiplicity+1):
            val *= Fraction(p**j - 1, p**j)
    assert val.denominator == 1
    return val.numerator


def all_mass_by_partitions(a, p):
    return sum(Fraction(1, aut_order_type(lam, p)) for lam in partitions(a))


def hall_mass_closed(a, p):
    qpoch = Fraction(1, 1)
    for j in range(1, a+1):
        qpoch *= Fraction(p**j - 1, p**j)
    return Fraction(1, p**a) / qpoch


def homocyclic_mass(a, p):
    total = Fraction(0, 1)
    for m in range(1, a+1):
        if a % m:
            continue
        qpoch = Fraction(1, 1)
        for j in range(1, m+1):
            qpoch *= Fraction(p**j - 1, p**j)
        total += Fraction(1, p**(m*a)) / qpoch
    return total


def density_formula(a, p):
    total = Fraction(0, 1)
    for m in range(1, a+1):
        if a % m:
            continue
        tail = Fraction(1, 1)
        for j in range(m+1, a+1):
            tail *= Fraction(p**j - 1, p**j)
        total += Fraction(1, p**((m-1)*a)) * tail
    return total


def finite_limit_product(p, N=200):
    x = 1.0
    for j in range(2, N+1):
        x *= 1.0 - p**(-j)
    return x


def main():
    checks = 0
    for p in (2, 3, 5, 7):
        for a in range(1, 9):
            brute_mass = all_mass_by_partitions(a, p)
            closed_mass = hall_mass_closed(a, p)
            assert brute_mass == closed_mass
            q = homocyclic_mass(a, p)
            rho = density_formula(a, p)
            assert rho == q / closed_mass
            if p**a <= 256:
                total_laws = factorial(p**a) * closed_mass
                good_laws = factorial(p**a) * q
                assert total_laws.denominator == 1
                assert good_laws.denominator == 1
            assert 0 < rho <= 1
            checks += 1

    # Exact sample values.
    samples_2 = [density_formula(a, 2) for a in range(1, 7)]
    assert samples_2 == [
        Fraction(1), Fraction(1), Fraction(43,64), Fraction(2731,4096),
        Fraction(624961,1048576), Fraction(643318201,1073741824)
    ]

    # Remainder from noncyclic homocyclic types is bounded by tau(a) p^{-a}.
    for p in (2, 3, 5):
        for a in range(2, 25):
            main_term = Fraction(1, 1)
            for j in range(2, a+1):
                main_term *= Fraction(p**j - 1, p**j)
            rho = density_formula(a, p)
            tau = sum(a % d == 0 for d in range(1, a+1))
            assert Fraction(0) <= rho - main_term <= Fraction(tau, p**a)
            checks += 1

    print('VERIFY_OK')
    print('exact_checks=', checks)
    for p in (2,3,5):
        vals = [str(density_formula(a,p)) for a in range(1,7)]
        print(f'p={p} rho_1..6={vals}')
        print(f'p={p} limiting_density~{finite_limit_product(p):.15f}')

if __name__ == '__main__':
    main()
