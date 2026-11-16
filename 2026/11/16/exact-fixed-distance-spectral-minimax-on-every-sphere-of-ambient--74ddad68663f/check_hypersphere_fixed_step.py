"""Independent rational verification of a fixed-geodesic spherical averaging theorem.

The finite tests here check exact low-degree identities and the all-dimension
moment bound for a large rational grid. The infinite-degree and unbounded-
dimension conclusions are proved in the accompanying mathematical argument.
"""
from fractions import Fraction


def normalized_multipliers(d, x, count):
    assert d >= 3 and Fraction(-1) <= x <= 1
    p = [Fraction(1), x]
    for n in range(1, count):
        p.append(((2*n+d-2)*x*p[-1] - n*p[-2]) / (n+d-2))
    return p


def fourth_moment(d):
    x = Fraction(1, d)
    s2 = 1-x*x
    return x**4 + 2*x*x*s2/Fraction(d-1) + 3*s2*s2/Fraction((d-1)*(d+1))


def run():
    assertions = 0
    for d in range(5, 101):
        x = Fraction(1,d)
        p = normalized_multipliers(d,x,160)
        assert p[0]==1;assertions+=1
        assert p[1]==x;assertions+=1
        assert p[2]==-x;assertions+=1
        assert p[3]==x*(Fraction(d+2,d*d)-3)/Fraction(d-1);assertions+=1
        assert abs(p[3])<x;assertions+=1
        assert fourth_moment(d)==Fraction(3*d+2,d**3);assertions+=1
        assert fourth_moment(d)<x;assertions+=1
        for degree in range(4,161):
            assert abs(p[degree])<x
            assertions+=1
        pn=normalized_multipliers(d,-x,30)
        for n in range(31):
            assert pn[n]==(-1)**n*p[n]
            assertions+=1
        # Full, exact two-sector lower bound at rational test values.
        for k in range(-2*d,2*d+1):
            y=Fraction(k,2*d*d)
            m=max(abs(y),abs((d*y*y-1)/Fraction(d-1)))
            assert m>=x
            if m==x:assert y in (-x,x)
            assertions+=2
    print('PASS', assertions, 'exact rational assertions for ambient dimensions 5..100')


if __name__=='__main__':
    run()
