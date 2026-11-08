"""Exact finite algebra checks for random-step velocity-Verlet on the unit oscillator.

These checks verify identities and selected rational examples; they do not replace
Furstenberg's infinite random-product theorem, used in the mathematical proof.
"""
from fractions import Fraction
from itertools import combinations
from sympy import Matrix, Rational, factor, simplify, symbols


def M(h):
    return Matrix([[1-h*h/2, h], [-h*(1-h*h/4), 1-h*h/2]])


def G(h):
    return Matrix.diag(1-h*h/4, 1)


def main():
    checks = 0
    def check(cond, name):
        nonlocal checks
        assert cond, name
        checks += 1

    a, b = symbols('a b', real=True)
    A, B = M(a), M(b)
    check(simplify(A.det()-1)==0, 'unit determinant')
    check(all(simplify(z)==0 for z in A.T*G(a)*A-G(a)), 'fixed-step invariant energy')
    check(simplify(A.trace()-(2-a*a))==0, 'fixed-step trace')
    K = A*B*A.inv()*B.inv()
    commutator_gap = a*a*b*b*(a-b)**2*(a+b)**2/16
    check(factor(K.trace()-2-commutator_gap)==0, 'commutator exact identity')
    for aa,bb in combinations([Rational(j,10) for j in range(1,20)], 2):
        AA,BB=M(aa),M(bb)
        check(AA.det()==1 and BB.det()==1, 'determinants')
        check(all(z==0 for z in AA.T*G(aa)*AA-G(aa)), 'metric preserved')
        check(all(z==0 for z in BB.T*G(bb)*BB-G(bb)), 'metric preserved other')
        check(K.trace().subs({a:aa,b:bb})-2==commutator_gap.subs({a:aa,b:bb}), 'hyperbolic commutator')
        check(commutator_gap.subs({a:aa,b:bb})>0, 'strict hyperbolicity')
    check((M(Rational(1))*M(Rational(6,5))).trace()==Rational(-347,250), 'bounded period-two example')
    check(Rational(-2) < Rational(-347,250) < Rational(2), 'elliptic period-two example')
    print(f'PASS {checks} symbolic/exact-rational assertions')
    print('commutator trace = 2 + a^2*b^2*(a-b)^2*(a+b)^2/16')
    print('periodic example a=1 b=6/5: two-step trace -347/250 in (-2,2)')
    print('LIMIT: checks do not prove stochastic positivity; analytic argument invokes Furstenberg theorem.')


if __name__ == '__main__':
    main()
