"""Independent finite-residue tests for the odometer roof and time cocycle.

These are finite checks of the exact 2-adic identities, not proofs of infinite laws.
Run: python3 verify_clock.py
"""
from collections import Counter
from fractions import Fraction


def valuation_mod(x: int, precision: int) -> int:
    """Return min(v_2(x),precision) from x modulo 2**precision."""
    residue = x % (1 << precision)
    if residue == 0:
        return precision
    return (residue & -residue).bit_length() - 1


def depth(k: int, j: int, precision: int) -> int:
    return 1 + valuation_mod(k + j + 1, precision)


def count_deep(k: int, n: int, m: int, precision: int) -> int:
    return sum(depth(k, j, precision) >= m for j in range(n))


def run() -> int:
    checks = 0
    precision = 10
    modulus = 1 << precision

    for n in (1, 2, 3, 5, 7, 8, 11, 16, 31, 32, 45):
        for m in range(1, 9):
            p = 1 << (m - 1)
            q, r = divmod(n, p)
            observed = Counter(count_deep(k, n, m, precision) for k in range(modulus))
            expected = {q: modulus * (p-r)//p, q+1: modulus*r//p} if r else {q:modulus}
            expected = {value:cnt for value,cnt in expected.items() if cnt>0}
            assert observed == expected, (n,m,observed,expected)
            checks += 1

    for k in range(0, 7):
        n=1<<k
        frequencies=Counter()
        for start in range(modulus):
            vals=[depth(start,j,precision) for j in range(n)]
            total=4*sum(vals)
            g=(total-(8*n-4))//4
            assert total == 8*n-4+4*g and g>=0
            frequencies[g]+=1
            checks+=1
        for g in range(precision-k):
            assert frequencies[g] == modulus//(1<<(g+1))
            checks+=1

    for n in (1,2,3,5,8,13,32,57):
        for m in range(0,8):
            got=sum(1 for start in range(modulus) if max(depth(start,j,precision) for j in range(n))<=m)
            expected=modulus*max(0,1-Fraction(n,1<<m))
            assert got == expected,(n,m,got,expected)
            checks+=1

    for h in (1,2,3,4,5,6,8,12,16,32):
        z=valuation_mod(h,precision)
        # Check the exact truncated conditional valuation probabilities at each small finite level.
        for a in range(1,7):
            for b in range(1,7):
                nobs=sum(1 for start in range(modulus) if valuation_mod(start+1,precision)>=a and valuation_mod(start+h+1,precision)>=b)
                required=0 if min(a,b)>z else modulus//(1<<max(a,b))
                assert nobs==required,(h,a,b,nobs,required)
                checks+=1
    print('PASS: finite residue assertions:',checks)
    print('Checked exact dyadic-block clock distribution, threshold counts, maximum-depth CDF, and two-lag divisibility intersections.')
    print('Not a proof of unbounded-depth or infinite-Haar identities.')
    return checks


if __name__=='__main__':
    run()
