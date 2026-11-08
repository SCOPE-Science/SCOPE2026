"""Exact finite checks for a three-block rational Ehrhart-series identity.

These checks corroborate, but do not replace, the all-parameter proof.
Run: python verify.py
Requires Python 3 and SymPy.
"""
from math import comb, factorial
import sympy as sp

z, t, u = sp.symbols('z t u')


def count_from_constraints(a, q):
    """Enumerate block heights and exact composition multiplicities."""
    w = [comb(r + a - 1, a - 1) for r in range(q + 1)]
    return sum(w[i] * w[j] * w[k]
               for i in range(q + 1)
               for j in range(q - i + 1)
               for k in range(min(q-i, q-j) + 1))


def count_from_min_layer(a, q):
    """Independent minimum-block layer decomposition."""
    ans = comb(q + 3*a, 3*a)
    for h in range(1, q//2 + 1):
        v = q - 2*h
        ans += sum(
            comb(h + i + a - 1, a - 1)
            * comb(h + j + a - 1, a - 1)
            * comb(h + v - i - j + a - 1, a - 1)
            for i in range(v + 1) for j in range(v-i+1)
        )
    return ans


def rational_a(a):
    """A_{a,t}(z)=sum_{u>=0} C(t+u+a-1,a-1) z^u."""
    poly = sp.Poly(sp.expand(sp.prod(t + u + k for k in range(1,a))
                             / sp.factorial(a-1)), u)
    moments = [1/(1-z)]
    for k in range(1, a):
        moments.append(sp.cancel(z * sp.diff(moments[-1], z)))
    return sp.cancel(sum(poly.nth(k) * moments[k] for k in range(a)))


def ehrhart_series(a):
    """Build finite rational expression by polynomial-in-t expansion."""
    p = sp.Poly(sp.expand(rational_a(a)**3), t)
    d = 3*a - 3
    sums = [z*z/(1-z*z)]
    for j in range(1, d+1):
        sums.append(sp.cancel(z/2 * sp.diff(sums[-1],z)))
    return sp.factor(1/(1-z)**(3*a+1)
                     + sum(p.nth(j)*sums[j] for j in range(d+1)))


def run():
    count = 0
    for a in range(1, 6):
        for q in range(0, 13):
            assert count_from_constraints(a,q) == count_from_min_layer(a,q)
            count += 1
    for a in (1,2,3):
        F=ehrhart_series(a)
        d=3*a-3
        principal=sp.limit((1+z)**(d+1)*F,z,-1)
        predicted=sp.Rational(factorial(d),
                 factorial(a-1)**3*2**(3*a+1))
        assert sp.simplify(principal-predicted)==0
        count += 1
        # Independently check the entire rational series against lattice counts.
        series=sp.series(F,z,0,13).removeO().expand()
        for q in range(13):
            assert series.coeff(z,q)==count_from_constraints(a,q)
            count += 1
        # Its local pole at z=-1 must have precisely the stated order.
        assert sp.limit((1+z)**(d+1)*F,z,-1)!=0
        count += 1
    print('PASS:',count,'exact assertions')
    print('Series a=2:',ehrhart_series(2))
    print('Series a=3:',ehrhart_series(3))

if __name__=='__main__':
    run()
