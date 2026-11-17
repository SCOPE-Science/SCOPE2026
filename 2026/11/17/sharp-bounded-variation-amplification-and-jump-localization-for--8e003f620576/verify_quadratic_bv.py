#!/usr/bin/env python3
"""Reproduce exact finite-grid BV norms of quadratic least-squares projection.

Python 3 standard library only. The infinite-grid theorem requires the accompanying
analytical proof; finitely many checks do not certify an asymptotic statement.
"""
from fractions import Fraction as Q
from math import sqrt


def solve_linear(matrix, rhs):
    n = len(rhs)
    a = [[Q(x) for x in matrix[i]] + [Q(rhs[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        t = a[j][j]
        a[j] = [x / t for x in a[j]]
        for i in range(n):
            if i != j:
                t = a[i][j]
                a[i] = [a[i][l] - t * a[j][l] for l in range(n+1)]
    return [a[i][-1] for i in range(n)]


def direct_project(n, y):
    # An independent, exact 3-by-3 moment-Gram solve in the monomial basis.
    assert n >= 3 and len(y) == n
    nodes = [Q(j, n-1) for j in range(n)]
    G = [[sum(x**(a+b) for x in nodes) for b in range(3)] for a in range(3)]
    rhs = [sum(Q(y[j]) * nodes[j]**a for j in range(n)) for a in range(3)]
    coef = solve_linear(G, rhs)
    return [sum(coef[a] * x**a for a in range(3)) for x in nodes]


def variation(y):
    return sum(abs(y[i+1]-y[i]) for i in range(len(y)-1))


def explicit_step_variation(n, k):
    # Formula derived using orthogonal polynomials 1, t, t^2-mean(t^2).
    a = Q(6*k*(n-k),n*(n*n-1))
    return a * sum(abs(1 + Q(5*(2*k-n)*(2*j-n+2),n*n-4))
                   for j in range(n-1))


def norm_exact(n):
    values = [explicit_step_variation(n,k) for k in range(1,n)]
    c = max(values)
    return c, [k for k in range(1,n) if values[k-1] == c]


def continuum_tv(t):
    t = Q(t)
    t = min(t, 1-t)
    if not t:
        return Q(0)
    if t <= Q(2,5):
        return 6*t*(t-1)*(50*t*t-50*t+13)/(5*(2*t-1))
    return 6*t*(1-t)


def polynomial_step(t):
    t = Q(t)
    return [(1-t)*(10*t*t-8*t+1), 12*t*(1-t)*(3-5*t),
            30*t*(1-t)*(2*t-1)]


def run():
    tested = 0
    for n in range(3,32):
        for k in range(1,n):
            y = [Q(j>=k) for j in range(n)]
            lhs = variation(direct_project(n,y))
            rhs = explicit_step_variation(n,k)
            assert lhs == rhs,(n,k,lhs,rhs)
            tested += 1
    print('DIRECT_GRAM_VERSUS_CLOSED_EXACT_STEP_TESTS_PASS', tested)
    expected = {3:Q(1),4:Q(13,10),5:Q(44,35),6:Q(9,7),
                7:Q(55,42),8:Q(29,21),9:Q(227,165),
                10:Q(76,55),11:Q(92,65),12:Q(2889,2002)}
    for n,v in expected.items():
        assert norm_exact(n)[0] == v, n
    print('EXACT_FIRST_TEN_DIMENSION_COEFFICIENTS_PASS')
    for n in range(3,26):
        C,_ = norm_exact(n)
        for seed in range(6):
            y = [Q(((j*29+seed*7)*(j+2)+3*seed)%41 - 20, 13) for j in range(n)]
            assert variation(direct_project(n,y)) <= C*variation(y),(n,seed)
    print('EXACT_ARBITRARY_INPUT_COMPARISON_PASS')
    # Exact orthogonality to 1,x,x^2 for polynomial fits to continuum steps.
    for t in [Q(1,8),Q(1,4),Q(1,3),Q(2,5),Q(1,2),Q(5,7)]:
        a,b,c=polynomial_step(t)
        for power in range(3):
            integral = a/Q(power+1)+b/Q(power+2)+c/Q(power+3)
            right = (1-t**(power+1))/Q(power+1)
            assert integral == right,(t,power)
        # Exhaustive rational test of continuous TV expression for a quadratic.
        if t in (Q(1,8),Q(1,4),Q(1,3)):
            z=-b/(2*c)
            q=lambda x: a+b*x+c*x*x
            assert 0<z<1
            assert 2*q(z)-q(0)-q(1)==continuum_tv(t)
    print('EXACT_CONTINUOUS_STEP_MOMENTS_AND_VARIATION_PASS')
    r=sqrt(3)*sqrt(12+sqrt(69))/30
    tstar=.5-r
    F=lambda t: float(continuum_tv(Q(str(t))))
    val=F(tstar)
    assert .2398<tstar<.2399 and 1.6331<val<1.6333
    for n in [20,50,100,200]:
        C,ks=norm_exact(n)
        assert abs(float(C)-val)<7/n
        assert min(min(abs(k/n-tstar),abs(k/n-(1-tstar))) for k in ks)<4/n
    print('ASYMPTOTIC_FORMULA_NUMERIC_DIAGNOSTICS_PASS')
    print('CONTINUOUS_MAXIMIZER', format(tstar,'.12f'), 'LIMIT',format(val,'.12f'))
    print('ALL_QUADRATIC_BV_CHECKS_PASS')

if __name__=='__main__': run()
