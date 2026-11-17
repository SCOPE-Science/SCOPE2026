#!/usr/bin/env python3
"""Reproduce finite checks for a critical density-dependent patch population map.
The theorem itself is proved analytically; finite tests are not an infinite proof.
"""
from fractions import Fraction as Q
from math import isclose
from random import Random


def update(x, matrix, competition, cost):
    n = len(x)
    return [sum(matrix[i][j] * x[j] /
                ((1 + competition[j] * x[j]) * (1 + cost[i][j] * x[j]))
                for j in range(n)) for i in range(n)]


def quadratic_coeff(matrix, competition, cost, right, left):
    return sum(left[i] * matrix[i][j] * (competition[j] + cost[i][j]) * right[j]**2
               for i in range(len(matrix)) for j in range(len(matrix)))


def exact_family():
    # Baseline positive mixing matrix, rho=1, eigenvalues 1 and 1/3.
    M = [[Q(2, 3), Q(1, 3)], [Q(1, 3), Q(2, 3)]]
    a = [Q(1), Q(1)]
    v = [Q(1, 2), Q(1, 2)]
    w = [Q(1), Q(1)]
    b0 = [[Q(0), Q(0)], [Q(0), Q(0)]]
    b1 = [[Q(0), Q(1)], [Q(2), Q(3)]]
    assert all(sum(M[i][j]*v[j] for j in range(2)) == v[i] for i in range(2))
    assert all(sum(w[i]*M[i][j] for i in range(2)) == w[j] for j in range(2))
    assert sum(w[i]*v[i] for i in range(2)) == 1
    alpha0 = quadratic_coeff(M, a, b0, v, w)
    alpha1 = quadratic_coeff(M, a, b1, v, w)
    assert alpha0 == Q(1, 2), alpha0
    assert alpha1 == Q(5, 4), alpha1
    assert alpha0 / alpha1 == Q(2, 5)
    # The density-dependent movement matrix is P_ij/(1+b_ij*x_j),
    # with P = (3/4) M and R_j = 4/3; all columns of P sum to 3/4.
    P = [[Q(3, 4)*M[i][j] for j in range(2)] for i in range(2)]
    assert all(sum(P[i][j] for i in range(2)) == Q(3, 4) for j in range(2))
    xinit = [Q(3, 5), Q(1, 5)]
    for b in (b0, b1):
        x = xinit
        for _ in range(4):
            y = update(x, M, a, b)
            assert y[0] > 0 and y[1] > 0
            assert sum(y) < sum(x)
            x = y
    return M, a, b0, b1


def asymptotic_test(M, a, costs):
    # The test uses floats to illustrate, not certify, the asymptotic theorem.
    mf = [[float(t) for t in row] for row in M]
    af = [float(t) for t in a]
    b = [[float(t) for t in row] for row in costs]
    x = [0.7, 0.15]
    for _ in range(180000):
        x = update(x, mf, af, b)
    alpha = float(quadratic_coeff(M, a, costs, [Q(1,2)]*2, [Q(1)]*2))
    target = 0.5/alpha
    assert all(abs(180000*t-target) < 0.00025 for t in x), (x, target)
    return tuple(180000*t for t in x), target


def random_exact_checks():
    rng = Random(6448)
    checked = 0
    for n in (2, 3, 4):
        # M is strictly positive, rational, column-stochastic: rho(M)=1.
        # Positive p=M/2 with R=2 is a column-substochastic dispersal map.
        for _ in range(65):
            weights = [[Q(rng.randrange(1, 9)) for j in range(n)] for i in range(n)]
            M = [[weights[i][j] / sum(weights[k][j] for k in range(n))
                  for j in range(n)] for i in range(n)]
            a = [Q(rng.randrange(1,5), 3) for j in range(n)]
            b = [[Q(rng.randrange(0,5), 4) for j in range(n)] for i in range(n)]
            x = [Q(rng.randrange(1,5), 5) for j in range(n)]
            y = update(x, M, a, b)
            linear = [sum(M[i][j]*x[j] for j in range(n)) for i in range(n)]
            assert all(Q(0) < y[i] < linear[i] for i in range(n))
            # Tight second-order Taylor bound: remainder is cubic for small epsilon.
            for z in [Q(1,10), Q(1,100), Q(1,1000)]:
                state = [z*t for t in x]
                actual = update(state, M, a, b)
                quadratic = [sum(M[i][j]*(state[j] -(a[j]+b[i][j])*state[j]**2)
                                 for j in range(n)) for i in range(n)]
                # For nonnegative parameters the exact omitted term is nonnegative,
                # and scales at most cubically as z diminishes.
                assert all(actual[i] >= quadratic[i] for i in range(n))
                if z == Q(1,1000):
                    assert max(float(actual[i]-quadratic[i]) for i in range(n)) < 0.0000001
                checked += n
    return checked



def heterogeneous_exact_family():
    # A diagonal similarity of a strictly positive Markov matrix gives a
    # non-stochastic critical mixing matrix and nonuniform Perron vectors.
    d = [Q(1), Q(2), Q(3)]
    q = [Q(1, 2), Q(1, 3), Q(1, 6)]
    M = [[d[i]*q[j]/d[j] for j in range(3)] for i in range(3)]
    v = [value / sum(d) for value in d]
    w = [sum(d)*q[i]/d[i] for i in range(3)]
    assert sum(w[i]*v[i] for i in range(3)) == 1
    assert all(sum(M[i][j]*v[j] for j in range(3)) == v[i] for i in range(3))
    assert all(sum(w[i]*M[i][j] for i in range(3)) == w[j] for j in range(3))
    # Take every regional growth factor equal to ten and p=M/10, giving
    # column dispersal probabilities strictly below one.
    assert all(sum(M[i][j]/10 for i in range(3)) < 1 for j in range(3))
    a = [Q(1), Q(2), Q(3)]
    b = [[Q(i+j,5) for j in range(3)] for i in range(3)]
    alpha = quadratic_coeff(M,a,b,v,w)
    improved = [row[:] for row in b]
    improved[0][1] += 1
    alpha_new = quadratic_coeff(M,a,improved,v,w)
    assert alpha_new-alpha == w[0]*M[0][1]*v[1]**2 > 0
    x = [Q(1, 2), Q(3, 5), Q(1, 7)]
    y = update(x,M,a,b)
    assert all(y[i] < sum(M[i][j]*x[j] for j in range(3)) for i in range(3))
    # Nonuniform Perron-profile check for a genuinely heterogeneous family.
    xf = [0.5, 0.3, 0.4]
    mf = [[float(t) for t in row] for row in M]
    af = [float(t) for t in a]
    bf = [[float(t) for t in row] for row in b]
    for _ in range(100000):
        xf = update(xf,mf,af,bf)
    assert all(abs(100000*xf[i] - float(v[i]/alpha)) < 0.0001 for i in range(3))
    return alpha, alpha_new

def main():
    M,a,b0,b1 = exact_family()
    multi_alpha, multi_alpha_new = heterogeneous_exact_family()
    outputs = [asymptotic_test(M,a,b) for b in (b0,b1)]
    checked = random_exact_checks()
    print('EXACT_ALPHA_BASELINE=1/2')
    print('EXACT_ALPHA_DENSITY_COST=5/4')
    print('EXACT_TAIL_FACTOR=2/5')
    print('HETEROGENEOUS_3_PATCH_ALPHA=', multi_alpha, 'INCREASED=', multi_alpha_new)
    for i, (got,target) in enumerate(outputs):
        print('CASE',i, '180000*x=',got,'predicted=',target)
    print('EXACT_RATIONAL_TAYLOR_COMPONENT_CHECKS=',checked)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
