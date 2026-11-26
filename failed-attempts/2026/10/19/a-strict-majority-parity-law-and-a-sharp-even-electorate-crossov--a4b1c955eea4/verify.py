"""Exact rational finite checks of a beta-binomial strict-majority theorem.
The theorem for arbitrary positive real shape parameters is proved analytically
in RESULT.md; bounded computations here check the finite identities only.
"""
from fractions import Fraction
from math import comb


def rising(a, n):
    result = Fraction(1)
    for j in range(n):
        result *= a + j
    return result


def beta_ratio(a, b, c, d):
    """B(a+c,b+d)/B(a,b) for positive integral a,b,c,d."""
    return rising(a, c) * rising(b, d) / rising(a+b, c+d)


def pmf(n, k, a, b):
    return Fraction(comb(n, k)) * rising(a, k) * rising(b, n-k) / rising(a+b, n)


def accuracy(n, a, b):
    return sum((pmf(n, k, a, b) for k in range(n//2+1, n+1)), Fraction(0))


def check():
    count = 0
    for a,b in ((2,1),(3,1),(3,2),(5,1),(5,4),(10,9)):
        a,b = Fraction(a),Fraction(b)
        for n in range(1,29):
            assert sum((pmf(n,k,a,b) for k in range(n+1)),Fraction(0)) == 1
            count += 1
        for m in range(1,13):
            lhs = accuracy(2*m+2,a,b)-accuracy(2*m,a,b)
            rhs = (Fraction(comb(2*m,m),m+1)
                   * beta_ratio(a,b,m+1,m)
                   * ((m+1)*a-m*b+2*m+1)/(a+b+2*m+1))
            assert lhs == rhs and lhs > 0
            odd_before = accuracy(2*m-1,a,b)-accuracy(2*m,a,b)
            expected_before = comb(2*m-1,m)*beta_ratio(a,b,m,m)
            assert odd_before == expected_before and odd_before>0
            odd_after = accuracy(2*m+1,a,b)-accuracy(2*m,a,b)
            expected_after = comb(2*m,m)*beta_ratio(a,b,m+1,m)
            assert odd_after == expected_after and odd_after>0
            count += 3
    a,b=Fraction(2),Fraction(1)
    p=Fraction(2,3)
    for m in range(1,16):
        assert accuracy(2*m,a,b)==Fraction(3*m,4*m+2)
        assert accuracy(2*m+1,a,b)==Fraction(3*m+4,4*m+6)
        assert (accuracy(2*m,a,b)>p)==(m>=5)
        assert (accuracy(2*m,a,b)==p)==(m==4)
        count += 4
    assert accuracy(8,a,b)==p
    assert accuracy(10,a,b)==Fraction(15,22)
    print(f"PASS: {count} exact rational checks; A8=2/3, A10=15/22")


if __name__ == '__main__':
    check()
