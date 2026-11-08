"""Reproduce exact rational and symbolic claims for three-species survey completion.
Requires Python 3.10+ and SymPy 1.12+; independent first-step moment recursion.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import sympy as sp


def subset_moments(p):
    one = Fraction(0)
    two = Fraction(0)
    for k in range(1, len(p) + 1):
        for sub in combinations(p, k):
            q = sum(sub)
            sg = 1 if k % 2 else -1
            one += sg / q
            two += sg * (2 - q) / (q*q)
    return one, two - one*one


def markov_moments(p):
    n = len(p)
    @lru_cache(None)
    def solve(mask):
        if mask == (1 << n) - 1:
            return Fraction(0), Fraction(0)
        miss = [i for i in range(n) if not ((mask >> i) & 1)]
        r = sum(p[i] for i in miss)
        futures = [solve(mask | (1 << i)) for i in miss]
        avg_e = sum((p[i] / r) * e for i, (e, _) in zip(miss, futures))
        avg_2 = sum((p[i] / r) * e2 for i, (_, e2) in zip(miss, futures))
        # W ~ Geometric(r) is independent of the identity of the next unseen type.
        mean = Fraction(1, 1)/r + avg_e
        e2 = (2-r)/(r*r) + 2*avg_e/r + avg_2
        return mean, e2
    mean, e2 = solve(0)
    return mean, e2 - mean*mean


def verify():
    a, d, t = sp.symbols('a d t')
    qpoly = 3*a**5 - 12*a**4 + 56*a**3 - 38*a**2 + 45*a - 6
    rpoly = 3*a**7 - 20*a**6 + 149*a**5 - 170*a**4 + 405*a**3 - 152*a**2 + 115*a - 10
    assert qpoly.subs(a, 0) == -6
    assert qpoly.subs(a, sp.Rational(1, 3)) == sp.Rational(544, 81)
    assert qpoly.subs(a, sp.Rational(147, 1000)) < 0
    assert qpoly.subs(a, sp.Rational(148, 1000)) > 0
    # On 0 < a < 1/3, Q'(a) >= 45 - 76/3 - 48/27 > 0.
    assert 45 - sp.Rational(76, 3) - sp.Rational(48, 27) > 0
    # At the unique root, a in (147/1000,148/1000), R(a)>0
    # by retaining its positive terms 115*a and bounding all negative terms.
    lo, hi = sp.Rational(147,1000), sp.Rational(148,1000)
    r_floor = 115*lo - 10 - 20*hi**6 - 170*hi**4 - 152*hi**2
    assert r_floor > 3

    p = (a, (1-a)/2+d, (1-a)/2-d)
    mean = sum((-1)**(k+1)/sum(sub) for k in range(1, 4) for sub in combinations(p, k))
    e2 = sum((-1)**(k+1)*(2-sum(sub))/sum(sub)**2 for k in range(1,4) for sub in combinations(p,k))
    var = sp.factor(e2 - mean*mean)
    second_coeff = sp.factor(sp.diff(var,d,2).subs(d,0)/2)
    assert sp.cancel(second_coeff - 32*qpoly/(1-a*a)**4) == 0

    # Quartic degeneracy: the fourth-order coefficient at Q=0.
    fourth_coeff = sp.factor(sp.diff(var,d,4).subs(d,0)/24)
    # Modulo Q, the quartic coefficient is 128 R/(1-a^2)^6.
    mismatch = sp.cancel(fourth_coeff - 128*rpoly/(1-a*a)**6)
    numer, denom = sp.fraction(mismatch)
    assert sp.rem(numer, qpoly, a) == 0

    p_eq = (Fraction(1,12), Fraction(11,24), Fraction(11,24))
    p_uneq = (Fraction(1,12), Fraction(5,12), Fraction(1,2))
    eq, unequal = subset_moments(p_eq), subset_moments(p_uneq)
    assert eq == markov_moments(p_eq)
    assert unequal == markov_moments(p_uneq)
    assert unequal[0]-eq[0] == Fraction(72,5005)
    assert eq[1]-unequal[1] == Fraction(3564216,25050025)
    # A second independent arithmetic check away from the symmetric section.
    for probs in [(1,2,9),(1,3,8),(2,3,7),(1,4,7),(2,4,6),(3,4,5)]:
        pp = tuple(Fraction(v,sum(probs)) for v in probs)
        assert subset_moments(pp) == markov_moments(pp)
    # Two-type variance expression, t = p(1-p), is decreasing for t in (0,1/4].
    for i in range(1,12):
        x = Fraction(i,24)
        y = (x, 1-x)
        tt = x*(1-x)
        assert subset_moments(y)[1] == 1/tt**2 - 3/tt - 2
    roots = sp.nroots(qpoly, n=25)
    positive = [float(sp.re(z)) for z in roots if abs(float(sp.im(z))) < 1e-15 and 0<float(sp.re(z))<1/3]
    assert len(positive)==1
    print('VERIFICATION_PASS')
    print('critical rare proportion a* =', '{:.15f}'.format(positive[0]))
    print('balanced-mean advantage =', unequal[0]-eq[0])
    print('balanced-variance excess =', eq[1]-unequal[1])
    print('symmetric local quadratic coefficient = 32Q(a)/(1-a^2)^4')
    print('quartic coefficient at Q(a)=0 = 128R(a)/(1-a^2)^6 > 0')


if __name__ == '__main__':
    verify()
