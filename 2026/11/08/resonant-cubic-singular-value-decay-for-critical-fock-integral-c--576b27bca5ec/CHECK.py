"""Exact coefficient checks for critical Fock generalized-integral commutators.

Run: python3 CHECK.py. Uses Python's standard library only.
Finite checks corroborate rather than replace the all-parameter analytic proof.
"""
from fractions import Fraction
from math import factorial, prod
from decimal import Decimal, localcontext


def raw(h, j, k):
    """Coefficient of z^(k+2h) in I^(h+j)(z^h D^j z^k)."""
    if k < j:
        return Fraction(0)
    return Fraction(factorial(k), factorial(k-j)) * Fraction(factorial(k-j+h), factorial(k+2*h))


def w_sq(h, j, k):
    if k < j:
        return Fraction(0)
    return Fraction(prod((k-j+r)**2 for r in range(1, h+1)), prod(k+r for r in range(1, 2*h+1)))


def alpha(h, j):
    return Fraction(-h*(h+2*j), 2)


def beta(h, j):
    return Fraction(h*(2*h*h+2*h*j+h-2*j*j+2*j), 4)


def a_sum(h, j):
    return Fraction(sum(r-j for r in range(1,h+1))) - Fraction(sum(range(1,2*h+1)), 2)


def b_sum(h, j):
    return Fraction(-sum((r-j)**2 for r in range(1,h+1)),2) + Fraction(sum(r*r for r in range(1,2*h+1)),4)


def c2(a,b):
    h1,j1=a; h2,j2=b
    return h1*h2*(h1+2*j1-h2-2*j2)


def c3_raw(a,b):
    h1,j1=a; h2,j2=b
    return 4*h2*h2*alpha(h1,j1)-4*h2*beta(h1,j1)-4*h1*h1*alpha(h2,j2)+4*h1*beta(h2,j2)


def c3_resonant(a,b):
    h1,j1=a; h2,j2=b
    assert h1+2*j1 == h2+2*j2
    return Fraction(-h1*h2*(h1*h1-h2*h2),2)


def normalize(h,j,k):
    return raw(h,j,k)**2 * Fraction(factorial(k+2*h), factorial(k))


def decimal_weight(h,j,k):
    f=w_sq(h,j,k)
    return (Decimal(f.numerator)/Decimal(f.denominator)).sqrt()


def test():
    counts={'monomial':0,'log_coefficients':0,'pair_resonance':0,'commutator_numeric':0}
    for h in range(1,8):
        for j in range(0,7):
            assert a_sum(h,j)==alpha(h,j)
            assert b_sum(h,j)==beta(h,j)
            counts['log_coefficients']+=2
            for k in range(0,30):
                assert normalize(h,j,k) == w_sq(h,j,k) if k>=j else raw(h,j,k)==0
                counts['monomial']+=1
    pairs=[(h,j) for h in range(1,8) for j in range(0,7)]
    with localcontext() as context:
        context.prec=90
        for a in pairs:
            for b in pairs:
                if a==b:continue
                h1,j1=a;h2,j2=b
                e2= -2*h2*alpha(h1,j1)+2*h1*alpha(h2,j2)
                assert e2==c2(a,b)
                if h1+2*j1==h2+2*j2:
                    assert c2(a,b)==0
                    assert c3_raw(a,b)==c3_resonant(a,b)!=0
                else:
                    assert c2(a,b)!=0
                counts['pair_resonance']+=1
        for a,b in [((1,0),(1,1)),((2,0),(4,0)),((3,0),(1,1)),((1,1),(3,0)),((4,0),(2,1)),((2,3),(4,2))]:
            h1,j1=a;h2,j2=b
            for k in [10000,1000000]:
                p=decimal_weight(h2,j2,k)*decimal_weight(h1,j1,k+2*h2)
                q=decimal_weight(h1,j1,k)*decimal_weight(h2,j2,k+2*h1)
                degree=3 if c2(a,b)==0 else 2
                value=Decimal(k)**degree*(p-q)
                expected=Decimal(c3_resonant(a,b).numerator)/Decimal(c3_resonant(a,b).denominator) if degree==3 else Decimal(c2(a,b))
                assert abs(value-expected)/abs(expected)<Decimal('0.01')
                counts['commutator_numeric']+=1
    print('FOCK_INTEGRAL_COMMUTATOR_OK',counts)


if __name__=='__main__':test()
