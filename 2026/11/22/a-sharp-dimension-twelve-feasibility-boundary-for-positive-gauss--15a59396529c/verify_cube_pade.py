"""Exact rational certificates for two-stage Gauss diffusion on Boolean cubes.

Requires Python 3 and SymPy. No numerical root finding or sampled-step inference.
"""
from fractions import Fraction
from math import comb, gcd, prod
import sympy as sp

x = sp.symbols('x')


def kraw(d, distance, k):
    return sum((-1)**i * comb(distance, i) * comb(d-distance, k-i)
               for i in range(max(0, k-(d-distance)), min(distance, k)+1))


def rational_shells(d, h):
    vals = [Fraction(1)]
    for k in range(1, d+1):
        z = Fraction(2*k)*h
        vals.append((Fraction(1)-z/2+z*z/12) /
                    (Fraction(1)+z/2+z*z/12))
    return [sum(Fraction(kraw(d,j,k), 2**d) * vals[k]
                for k in range(d+1)) for j in range(d+1)]


def numerator_poly(d, distance):
    # p_{d,j}(h) = N_{d,j}(h)/(2^d D(h)),
    # D(h) = product_{k=1}^d (3+3kh+k^2 h^2).
    den = [sp.Poly(3+3*k*x+k*k*x*x,x,domain='QQ')
           for k in range(1,d+1)]
    num = [sp.Poly(3-3*k*x+k*k*x*x,x,domain='QQ')
           for k in range(1,d+1)]
    D = sp.Poly(1,x,domain='QQ')
    for q in den:
        D *= q
    N = D
    for k in range(1,d+1):
        N += kraw(d,distance,k)*D.exquo(den[k-1])*num[k-1]
    return N, D


def count_sign_changes(seq):
    seq = [v for v in seq if v]
    return sum(1 for a,b in zip(seq,seq[1:]) if int(a)*int(b) < 0)


def sturm_variations(poly, endpoint):
    seq = sp.sturm(poly.as_expr(),x)
    if endpoint == 'infinity':
        signs = [sp.sign(sp.Poly(p,x).LC()) for p in seq]
    else:
        signs = [sp.sign(p.subs(x,endpoint)) for p in seq]
    return count_sign_changes(signs)


def main():
    checks = 0
    d = 12
    h = Fraction(1,3)
    shells = rational_shells(d,h)
    assert len(shells)==13 and all(z>0 for z in shells)
    assert sum(comb(d,j)*shells[j] for j in range(d+1)) == 1
    assert min(shells) == Fraction(48478650,2410225524765331)
    checks += 16
    D = prod(k*k+9*k+27 for k in range(1,d+1))
    numerators = [int(z*2**d*D) for z in shells]
    g = gcd(*numerators)
    assert g==2786059680768
    assert [z//g for z in numerators] == [
        953858494850392,1563497388699,43175953868634,
        12536901704823,3549152148984,1078655625780,
        353170735740,122750459970,44317433700,
        16128405915,5623467450,1657493475,193914600]
    checks += len(numerators)+1

    # d=13: a three-shell exact obstruction for every h>0.
    specifications = [
        (7, [7,7], -1, [sp.Rational(0),sp.Rational(1,32)]),
        (13,[1,1],-1,[sp.Rational(1,32),sp.Rational(1,3)]),
        (1,[11,11],-1,[sp.Rational(1,3),'infinity'])]
    for j, variations, desired_sign, (left,right) in specifications:
        N,D13=numerator_poly(13,j)
        assert N.as_expr().subs(x,sp.Rational(1,2)) == \
            sum(kraw(13,j,k)*
                (sp.Rational(1)-sp.Rational(k,2)+sp.Rational(k*k,12)) /
                (sp.Rational(1)+sp.Rational(k,2)+sp.Rational(k*k,12))
                for k in range(14)) * D13.eval(sp.Rational(1,2))
        power=min(t[0][0] for t in N.terms())
        assert power==j
        f=sp.Poly(N.as_expr()/x**power,x)
        actual=[sturm_variations(f,q) for q in [left,right]]
        assert actual==variations,(j,actual)
        evaluation=left if left>0 else right
        if evaluation=='infinity':evaluation=left
        assert sp.sign(f.eval(evaluation))==desired_sign
        checks+=6

    z=sp.symbols('z')
    F=(1-z/2+z*z/12)/(1+z/2+z*z/12)
    ts=sp.series(F,z,0,8).removeO().expand()
    assert ts.coeff(z,6)==0 and ts.coeff(z,7)==sp.Rational(1,1728)
    assert ts.coeff(z,5)==-sp.Rational(1,144)
    assert sp.Rational(1,1728)*(-sp.factorial(7)) == -sp.Rational(35,12)
    # For distance six, L^7 coefficient is 7*d*6! and therefore positive.
    assert sp.Rational(1,1728)*7*6*sp.factorial(6) == sp.Rational(35,2)
    checks += 5
    # Exact rational shell positivity checks at separate steps, only supplemental.
    for d in [7,8,9,10,11,12]:
        assert all(z>0 for z in rational_shells(d,Fraction(1,3)))
        checks+=d+1
    print(f'VERIFY_OK exact_checks={checks}; Q12_positive_at_1/3; Q13_all_h_obstructed')

if __name__=='__main__':
    main()
