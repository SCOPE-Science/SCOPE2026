"""Exact finite rational diagnostics for periodic-renewal MFPT summand modal structure.

This checker verifies finite instances of analytic inequalities. It is not
an exhaustive proof for all parameter values or all sequence indices.
"""
from fractions import Fraction
from math import factorial


def terms(q, x, top):
    assert Fraction(0) < q < 1 and x > 0
    out = [Fraction(1), x]
    for n in range(1, top):
        out.append(out[-1] * x * (1 - q**n) / (n + 1))
    return out


def alpha(q, n):
    return (1 - q**n) / (n + 1)


def modes(vals):
    return [n for n in range(1, len(vals)-1)
            if vals[n] > vals[n-1] and vals[n] > vals[n+1]]


def run():
    checks = 0
    for den in range(3, 18):
        for num in range(1, den):
            q = Fraction(num, den)
            for n in range(1, 60):
                delta = alpha(q, n+1) - alpha(q, n)
                criterion = q**n * ((n+2) - (n+1)*q) - 1
                assert (delta > 0) == (criterion > 0)
                assert (delta < 0) == (criterion < 0)
                checks += 2
            for i in range(1, 40):
                x = Fraction(i, 3)
                vals = terms(q, x, 45)
                assert len(modes(vals)) <= 2
                if q <= Fraction(1,2):
                    assert all(vals[n]**2 >= vals[n-1]*vals[n+1]
                               for n in range(1,44))
                checks += 1
    q=Fraction(3,4); x=Fraction(15,2)
    vals=terms(q, x, 70)
    assert modes(vals)==[1,5], modes(vals)
    assert vals[2]<vals[1] and vals[2]<vals[3] and vals[5]>vals[6]
    assert max(range(70),key=lambda n: vals[n])==5
    checks += 4
    print('exact_rational_checks_passed=', checks)
    print('q=3/4 x=15/2 modes=',modes(vals))
    print('C_0_to_C_7=',[str(v) for v in vals[:8]])
    print('computed_maximum_index=', max(range(70),key=lambda n: vals[n]))

if __name__ == '__main__':
    run()
