"""Exact checks of Jacobsthal reciprocal-square inverse-tail floors.

A truncated sum of positive rational terms gives a rigorous interval for the
infinite inverse tail; this is not used as a proof of the infinite theorem.
"""
from fractions import Fraction


def jacobsthal(k):
    return (2**k - (-1)**k) // 3


def floorq(q):
    return q.numerator // q.denominator


def formula(n):
    return Fraction(3 * 4**n - 4 * (-2)**n, 36)


def rational_brackets(n):
    # K is first omitted index; J_k>2^(k-2) for all k>=3.
    K = 2*n+24
    T = sum((Fraction(1, jacobsthal(k)**2) for k in range(n, K)), Fraction())
    tail = Fraction(64, 3 * 4**K)  # sum of 2^(-2k+4) from k=K to infinity
    return Fraction(1, T+tail), Fraction(1, T)


def proof_constants():
    c = Fraction(128,33)+Fraction(497,72)
    x = Fraction(1,8)
    lower = Fraction(28,45)-Fraction(16,55)*x-c*x*x
    upper = Fraction(28,45)+Fraction(16,55)*x+c*x*x
    assert lower > 0
    assert upper < Fraction(256,243)
    assert Fraction(3456,49)<71
    assert c == Fraction(8539,792)
    return lower, upper


def run():
    lo, hi = proof_constants()
    count=0
    for n in range(1,65):
        low, high = rational_brackets(n)
        f = floorq(formula(n))
        assert floorq(low) == f == floorq(high), (n, f, low, high)
        if n>=3:
            assert low > formula(n)-Fraction(1,9), n
            assert high < formula(n), n
        count+=1
    # Modulo 36, the fractional residues have period 3 for n>=1.
    assert [(3 * 4**n - 4 * (-2)**n) % 36 for n in range(1,10)] == [20,32,8]*3
    # A posteriori bounds from the exact expansion at the worst x=1/8.
    print('VERIFY_OK exact_rational_tail_intervals=',count,'n=1..64','uniform_coefficient_brackets=PASS','mod36_cycle=PASS')

if __name__=='__main__':
    run()
