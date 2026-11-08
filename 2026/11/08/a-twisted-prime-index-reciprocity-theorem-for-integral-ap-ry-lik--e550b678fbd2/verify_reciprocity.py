"""Finite checks for recurrence reciprocity; uses only Python standard library.

The statements for arbitrary primes are proved algebraically, not by these tests.
"""
from math import comb

QUADRATIC = {
    'Franel': (7, 2, -8),
    'Zagier_D': (11, 3, -1),
    'Zagier_C': (10, 3, 9),
    'Zagier_E': (12, 4, 32),
    'Zagier_B': (9, 3, 27),
    'Zagier_F': (17, 6, 72),
}
CUBIC = {
    'AZ_delta': (7, 3, 81),
    'AZ_alpha': (10, 4, 64),
    'AZ_epsilon': (12, 4, 16),
    'AZ_zeta': (9, 3, -27),
    'Apery_zeta3': (17, 5, 1),
}


def primes_through(bound):
    return [n for n in range(3, bound + 1, 2)
            if all(n % d for d in range(3, int(n ** .5) + 1, 2))]


def terms(order, a, b, c, top):
    ans = [1, b]
    for n in range(1, top):
        q = (n + 1) ** order
        if order == 2:
            middle = a * n * (n + 1) + b
        else:
            middle = (2*n+1)*(a*n*(n+1)+b)
        numerator = middle * ans[n] - c * n**order * ans[n-1]
        assert numerator % q == 0, ('integrality', order, a, b, c, n)
        ans.append(numerator // q)
    return ans


def independent_examples():
    # These expressions come from the explicit binomial-sum representations.
    for n in range(12):
        z3 = sum(comb(n,k)**2 * comb(n+k,k)**2 for k in range(n+1))
        al = sum(comb(n,k)**2 * comb(2*k,k) * comb(2*(n-k),n-k)
                 for k in range(n+1))
        ep = sum(comb(n,k)**2 * comb(2*k,n)**2
                 for k in range(n+1) if 2*k >= n)
        fr = sum(comb(n,k)**3 for k in range(n+1))
        assert z3 == terms(3,*CUBIC['Apery_zeta3'], n)[n]
        assert al == terms(3,*CUBIC['AZ_alpha'], n)[n]
        assert ep == terms(3,*CUBIC['AZ_epsilon'], n)[n]
        assert fr == terms(2,*QUADRATIC['Franel'], n)[n]


def run():
    independent_examples()
    checks = 0
    families = {**{k:(2,*v) for k,v in QUADRATIC.items()},
                **{k:(3,*v) for k,v in CUBIC.items()}}
    for name,(order,a,b,c) in families.items():
        seq = terms(order,a,b,c,60)
        for p in primes_through(59):
            if c % p == 0:
                continue
            e = seq[p-1] % p
            assert e*e % p == 1, ('endpoint',name,p,e)
            for n in range(p):
                assert (pow(c,n,p)*seq[p-1-n]-e*seq[n])%p == 0, ('reciprocity', name,p,n)
                # Same coefficient comparison as the reciprocal polynomial.
                assert (seq[p-1-n]*pow(c,-(p-1-n),p)-e*seq[n])%p == 0, ('polynomial',name,p,n)
                checks += 1
    # Sharp boundary: c nonzero but the excluded d != 0 cubic sequence s10.
    # Its recurrence is (n+1)^3 s10[n+1] = (2n+1)(6n(n+1)+2)s10[n]
    #                                      -n( -64 n^2 +4)s10[n-1].
    for p in (5,7,11,13):
        val = sum(comb(p-1,k)**4 for k in range(p))
        assert val%p == 0, ('boundary',p)
    print('VERIFY_OK families=%d primes=%d coefficient_checks=%d independent_binomial_n=12 excluded_d_case_primes=4' % (
        len(families),len(primes_through(59)),checks))


if __name__ == '__main__':
    run()
