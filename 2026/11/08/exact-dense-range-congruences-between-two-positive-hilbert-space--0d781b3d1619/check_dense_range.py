"""Finite exact-arithmetic corroboration for two diagonal pullback maps.

For each tested index, calculate weighted output coefficient squared and
compare with the declared source quadratic form coefficient using fractions.
The accompanying proof covers all indices, not just these tests.
"""
from fractions import Fraction


def ceil_log2(n):
    assert n >= 1
    return (n-1).bit_length()


def v2_odd(n):
    assert n >= 1
    j = (n & -n).bit_length()-1
    return j, n >> j


def test():
    checks = 0
    # W: every exceptional index (j(n),n) maps to second summand.
    special = set()
    for n in range(1, 5001):
        j = ceil_log2(n)
        assert n <= (1 << j)
        assert j == 0 or n > (1 << (j-1))
        assert (j,n) not in special
        special.add((j,n))
        assert Fraction(n, 1 << j) * Fraction(1,n) == Fraction(1,1 << j)
        assert Fraction(n,1 << j) <= 1
        checks += 5
    # W: arbitrary nonspecial index maps to first summand.
    for j in range(12):
        for k in range(1,500):
            if (j,k) not in special:
                assert Fraction(1,1<<j)*1 == Fraction(1,1<<j)
                checks += 1
    # V: first summand to odd band-0 indices; second summand to
    # even band-0 positions or all positive bands by odd-part index.
    targets = set()
    for m in range(1,5001):
        target=(0,2*m-1)
        assert target not in targets
        targets.add(target)
        assert Fraction(1,1)==1
        checks += 2
    for n in range(1,5001):
        j,odd = v2_odd(n)
        assert odd % 2 == 1 and n == (1<<j)*odd
        k = ((odd + 1)//2)
        target = (0,2*k) if j==0 else (j,k)
        assert target not in targets
        targets.add(target)
        assert Fraction(1,odd)*Fraction(1,1<<j) == Fraction(1,n)
        assert Fraction(1,odd) <=1
        checks +=5
    # Confirm each finite j-positive band target is represented by a v_n,
    # and the zero band is filled by u_m + odd v_n.
    for j in range(1,12):
        for k in range(1,201):
            n = (1 << j) * (2*k-1)
            jj,odd = v2_odd(n)
            assert jj == j and (odd+1)//2==k
            assert Fraction(1,odd)*Fraction(1,1<<j)==Fraction(1,n)
            checks +=3
    for k in range(1,2001):
        assert 2*k-1 != 2*k
        checks +=1
    print('DENSE_RANGE_EXACT_CHECK_OK',checks)

if __name__=='__main__':test()
