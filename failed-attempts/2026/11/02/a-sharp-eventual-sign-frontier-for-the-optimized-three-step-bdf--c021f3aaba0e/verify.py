#!/usr/bin/env python3
"""Exact algebra and supplementary numerical checks for a cubic causal Green sequence.

Requires Python 3 and SymPy. Run: python3 verify.py
"""
import sympy as sp

mu, s, z, R = sp.symbols('mu s z R', positive=True)
P = z**3 - sp.Rational(3, 2)*s*z**2 + sp.Rational(3, 5)*s*z - sp.Rational(1, 10)*s
D = 15*R**2 - 6*R + 1
sR = 10*R**3 / D

checks = 0
def check(expr):
    global checks
    assert sp.simplify(expr) == 0, sp.factor(expr)
    checks += 1

def verify():
    # Exact stability-polynomial structure, root parameterization, and crossing.
    check(sp.discriminant(P, z) + sp.Rational(27, 500)*s**2*(10*s**2-14*s+5))
    check(P.subs(z,R).subs(s,sR))
    check(sp.diff(sR,R)-10*R**2*(15*R**2-12*R+3)/D**2)
    check(sp.factor(sR.subs(R,sp.Rational(2,5)))-sp.Rational(16,25))
    check(D-1-3*R*(5*R-2))
    check(sp.factor((D-R**2)-(14*R**2-6*R+1)))
    check(sp.factor(P.subs(s,sp.Rational(16,25))-(z-sp.Rational(2,5))*(z**2-sp.Rational(14,25)*z+sp.Rational(4,25))))

    root_real = sp.Rational(2,5)
    root_complex = (7+sp.I*sp.sqrt(51))/25
    dist2 = sp.simplify((root_real-root_complex)*(root_real-sp.conjugate(root_complex)))
    A = root_real**2 / dist2
    B = root_complex**2 / ((root_complex-root_real)*(root_complex-sp.conjugate(root_complex)))
    check(A-sp.Rational(5,3))
    check(sp.simplify((4*B*sp.conjugate(B))/(A*A))-sp.Rational(20,17))
    check((root_complex + sp.conjugate(root_complex))/(2*root_real)-sp.Rational(7,10))

    # Independently regenerate Green coefficients from the recurrence and generating function.
    a = sp.Rational(15,2)/(5+3*mu)
    b = -3/(5+3*mu)
    c = sp.Rational(1,2)/(5+3*mu)
    coefficients = [sp.Integer(1)]
    for n in range(1, 14):
        term = a*coefficients[n-1]
        if n >= 2:
            term += b*coefficients[n-2]
        if n >= 3:
            term += c*coefficients[n-3]
        coefficients.append(sp.factor(term))
    G6 = (1296*mu**4-154656*mu**3+1440720*mu**2-2997300*mu+1667125)/(64*(5+3*mu)**6)
    check(coefficients[6]-G6)
    check(coefficients[6].subs(mu,sp.Rational(187,200)) + sp.Rational(1262437317590000,14468297105020833361))
    check(sp.factor(1-a-b-c-3*mu/(5+3*mu)))
    for n in range(14):
        check(coefficients[n] - sp.diff(1/(1-a*z-b*z**2-c*z**3),z,n).subs(z,0)/sp.factorial(n))

    # Numerical checks are illustrative only and cannot establish an infinite-index claim.
    sample_mu = [sp.Rational(1,20),sp.Rational(1,2),sp.Rational(9,10),
                 sp.Rational(187,200),sp.Rational(15,16),sp.Rational(1),sp.Rational(2),sp.Integer(6)]
    for t in sample_mu:
        sv = sp.Rational(5)/(5+3*t)
        roots = [complex(v) for v in sp.nroots(P.subs(s,sv), n=40, maxsteps=100)]
        real_roots = [x for x in roots if abs(x.imag)<1e-25]
        assert len(real_roots)==1
        real_root=real_roots[0].real
        nonreal=[x for x in roots if abs(x.imag)>=1e-25]
        assert len(nonreal)==2
        modulus=abs(nonreal[0])
        if t < sp.Rational(15,16):
            assert real_root>modulus + 1e-12
        elif t > sp.Rational(15,16):
            assert real_root<modulus - 1e-12
        else:
            assert abs(real_root-modulus)<1e-12
        checks_plus = 1
        globals()['checks'] += checks_plus
    print(f'PASS: {checks} algebraic, coefficient and supplementary root checks')

if __name__ == '__main__':
    verify()
