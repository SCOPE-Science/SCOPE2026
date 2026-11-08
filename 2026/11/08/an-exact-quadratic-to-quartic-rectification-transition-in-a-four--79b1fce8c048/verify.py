#!/usr/bin/env python3
"""Exact six-state verification of transport-response coefficients.
Requires Python 3 and SymPy.  Run: python verify.py
"""
import itertools
import sympy as sp

STATES = list(itertools.combinations(range(4), 2))
INDEX = {s: i for i, s in enumerate(STATES)}
ONE = sp.Integer(1)


def matrices(a, b):
    """Column generators Q0,Q1 and bond-current rows F0,F1.

    The full generator is Q0 + epsilon Q1, and current is
    (F0 + epsilon F1) * stationary_distribution.
    """
    weights = (a, b, ONE, ONE)
    n = len(STATES)
    q0, q1 = sp.zeros(n), sp.zeros(n)
    f0, f1 = sp.zeros(1, n), sp.zeros(1, n)
    for j, old in enumerate(STATES):
        old = set(old)
        for origin in old:
            for direction in (-1, 1):
                dest = (origin + direction) % 4
                if dest in old:
                    continue
                new = tuple(sorted((old - {origin}) | {dest}))
                i = INDEX[new]
                rate0 = sp.sympify(weights[origin]) / 2
                rate1 = direction * rate0
                q0[i, j] += rate0
                q0[j, j] -= rate0
                q1[i, j] += rate1
                q1[j, j] -= rate1
                if {origin, dest} == {0, 1}:
                    orientation = 1 if origin == 0 else -1
                    f0[j] += orientation * rate0
                    f1[j] += orientation * rate1
    assert all(sp.simplify(sum(q0[:, j])) == 0 for j in range(n))
    assert all(sp.simplify(sum(q1[:, j])) == 0 for j in range(n))
    return q0, q1, f0, f1


def augmented_inverse(q):
    matrix = q.copy()
    matrix[-1, :] = sp.ones(1, matrix.cols)
    return matrix.inv(method='DM')


def perturbation(a, b, order):
    q0, q1, f0, f1 = matrices(a, b)
    inverse = augmented_inverse(q0)
    q1[-1, :] = sp.zeros(1, q1.cols)
    p = []
    rhs = sp.zeros(6, 1)
    rhs[-1] = 1
    for k in range(order + 1):
        if k:
            rhs = -q1 * p[-1]
            rhs[-1] = 0
        p.append(inverse * rhs)
    coeffs = []
    for k in range(order + 1):
        coeffs.append((f0 * p[k])[0] + ((f1 * p[k-1])[0] if k else 0))
    return coeffs, p


def exact_current(a, b, e):
    q0, q1, f0, f1 = matrices(a, b)
    q = q0 + e*q1
    pinv = augmented_inverse(q)
    rhs = sp.zeros(6, 1)
    rhs[-1] = 1
    pi = pinv*rhs
    return sp.cancel(((f0 + e*f1)*pi)[0]), q, pi


def tree_current(q, f):
    """Independent Markov-chain tree-minor computation for numeric parameters."""
    w = []
    for i in range(6):
        rows = [j for j in range(6) if i != j]
        w.append((-q).extract(rows, rows).det())
    total = sum(w)
    assert total != 0
    return sp.cancel((f*sp.Matrix(w))[0] / total)


def check():
    a, b, e = sp.symbols('a b e', positive=True)
    A = a*b + 2*a + 2*b + 1
    B = a*b + 3*a + 3*b + 1
    c1 = 4*a*b*(a+b+2)/(A*B)
    c2 = 4*a*b*(a-1)*(a-b)*(b-1)*(a*b-3)/(A*A*B*B)
    coeffs, p = perturbation(a, b, 2)
    assert sp.cancel(coeffs[0]) == 0
    assert sp.cancel(coeffs[1] - c1) == 0
    assert sp.cancel(coeffs[2] - c2) == 0
    expected_pi0 = sp.Matrix([1, b, b, a, a, a*b])/A
    assert all(sp.cancel(u-v) == 0 for u,v in zip(p[0],expected_pi0))
    print('PASS: symbolic stationary expansion and linear/quadratic coefficients')

    c4curve = (12*a**2*(a-3)*(a-1)*(a**2-3)
        /((a**2+2*a+3)**2*(3*a**2+4*a+9)**2))
    jcurve, _, _ = exact_current(a, 3/a, e)
    assert sp.cancel(sp.diff(jcurve,e,2).subs(e,0)/2) == 0
    assert sp.cancel(sp.diff(jcurve,e,4).subs(e,0)/24 - c4curve) == 0
    print('PASS: all-parameter quartic onset on the nongeometric cancellation curve')

    wj, _, _ = exact_current(sp.Integer(2), sp.Rational(3,2), e)
    witness = (12*e*(e-11)*(e+11)*(e*e+1)
        /(4*e**5-13*e**4-4*e**3-3486*e**2-3509))
    assert sp.cancel(wj-witness) == 0
    assert sp.cancel(sp.diff(wj,e,4).subs(e,0)/24 + sp.Rational(48,101761)) == 0
    print('PASS: exact nonsymmetric witness with nonzero fourth-order rectification')

    # Check the source's weaker, per-site inversion correspondence (two choices
    # of reflected index for each offset).  The entries A, B, C are distinct.
    pattern = ('A','B','C','C')
    for center in range(4):
        assert not all(pattern[(center+i)%4] in
            (pattern[(center-i)%4],pattern[(center-i+1)%4])
            for i in range(4))
    print('PASS: both symmetry conditions absent in the distinct-rate family')

    tested = 0
    for aa,bb in [(1,2),(2,1),(2,3),(3,2),(2,sp.Rational(3,2)),
                  (sp.Rational(5,4),sp.Rational(9,5))]:
        for eps in (sp.Rational(1,7),sp.Rational(-1,11),sp.Rational(2,5)):
            jj,q,pi=exact_current(aa,bb,eps)
            assert all(sp.cancel(x)==0 for x in q*pi)
            assert sp.cancel(sum(pi)-1)==0
            for i in range(6):
                assert pi[i]>0
            q0,q1,f0,f1=matrices(aa,bb)
            jt=tree_current(q,(f0+eps*f1))
            assert sp.cancel(jt-jj)==0
            tested+=1
    print('PASS: %d independent matrix-tree and stationarity checks'%tested)
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    check()
