#!/usr/bin/env python3
"""Finite reproducibility checks for low-rank positive mass--moment feasibility.

The analytical proof is in RESULT.md. Finite LP tests are not a proof of the
universal statements. Requires NumPy and SciPy.
"""
from fractions import Fraction
from random import Random
import numpy as np
from scipy.optimize import linprog


def lp_ok(A_ub, b_ub, A_eq, b_eq, number_of_variables):
    result = linprog(
        np.zeros(number_of_variables), A_ub=A_ub, b_ub=b_ub,
        A_eq=A_eq, b_eq=b_eq, bounds=[(None, None)]*number_of_variables,
        method="highs",
    )
    return bool(result.success)


def direct_core_feasible(X, V, velocities, mu, a=None, b=None):
    m, r = X.shape
    n = V.shape[0]
    K = np.kron(X, V)  # row-major vec(X S V^T) = K row-major vec(S)
    a = np.ones(m) if a is None else np.asarray(a)
    b = np.ones(n) if b is None else np.asarray(b)
    mass = np.kron(a,b)
    momentum = mass*np.tile(velocities,m)
    return lp_ok(-K, np.zeros(m*n), np.vstack((mass @ K, momentum @ K)),
                 [1., mu], r*r)


def factor_feasible(X, V, velocities, mu, a=None, b=None):
    m, r = X.shape
    n = V.shape[0]
    a = np.ones(m) if a is None else np.asarray(a)
    b = np.ones(n) if b is None else np.asarray(b)
    u = lp_ok(-X, np.zeros(m), [a @ X], [1.], r)
    w = lp_ok(-V, np.zeros(n), np.vstack((b @ V, (b*velocities) @ V)),
              [1., mu], r)
    return u and w


def canonical_example():
    # W = span((1,1,1),(-1,0,1)) = (1,-2,1)^perp
    X = np.array([[1., 1.], [1., -1.], [1., 0.]])
    V = np.array([[1., -1.], [1., 0.], [1., 1.]])
    v = np.array([-1., 0., 1.])
    for p, q in [(-1,1), (-2,3), (-1,2), (0,1), (1,2), (2,3), (3,4), (1,1)]:
        mu = Fraction(p,q)
        predicted = Fraction(-2,3) <= mu <= Fraction(2,3)
        assert direct_core_feasible(X, V, v, float(mu)) == predicted
        assert factor_feasible(X, V, v, float(mu)) == predicted
    # An explicit positive rank-one witness at mu=1/2 and mass M=1.
    u = np.array([1.,1.,1.])
    w = np.array([float(Fraction(1,12)), float(Fraction(1,3)),
                  float(Fraction(7,12))])
    F = np.outer(u/3., w)
    assert np.all(F > 0.) and abs(F.sum()-1.) < 1.e-13
    assert abs(F.sum(axis=0) @ v - 0.5) < 1.e-13
    assert np.allclose(F, X @ np.array([[1./9.,1./12.],[0.,0.]]) @ V.T)
    # Physical mean 3/4 exists but is not feasible in W; one-vector completion.
    w_new = np.array([1./12., 1./12., 5./6.])
    assert abs(w_new @ v - 0.75) < 1.e-13
    assert np.linalg.matrix_rank(np.column_stack((V,w_new))) == 3
    assert not direct_core_feasible(X,V,v,0.75)
    F_new = np.outer(u/3., w_new)
    assert np.all(F_new > 0.) and abs(F_new.sum()-1.) < 1.e-13
    assert abs(F_new.sum(axis=0) @ v - 0.75) < 1.e-13
    return 8


def random_feasibility_tests():
    rng = Random(7181327)
    valid = 0
    for _ in range(400):
        m, n, r = 3, 4, 2
        X = np.array([[rng.randrange(-3,4) for k in range(r)]
                      for j in range(m)],dtype=float)
        V = np.array([[rng.randrange(-3,4) for k in range(r)]
                      for j in range(n)],dtype=float)
        if np.linalg.matrix_rank(X)<r or np.linalg.matrix_rank(V)<r:
            continue
        velocities = np.array([-2., -1., 1., 2.])
        mu = float(rng.choice([-2, -1, 0, 1, 2]))
        assert direct_core_feasible(X,V,velocities,mu) == factor_feasible(X,V,velocities,mu)
        valid += 1
    # Repeat with nonuniform positive quadrature weights on both factors.
    weighted = 0
    for _ in range(160):
        m,n,r = 3,4,2
        X = np.array([[rng.randrange(-3,4) for k in range(r)]
                       for j in range(m)],dtype=float)
        V = np.array([[rng.randrange(-3,4) for k in range(r)]
                       for j in range(n)],dtype=float)
        if np.linalg.matrix_rank(X)<r or np.linalg.matrix_rank(V)<r:
            continue
        a = np.array([rng.randrange(1,4) for _ in range(m)],float)
        b = np.array([rng.randrange(1,4) for _ in range(n)],float)
        vel = np.array([-2.,-1.,1.,2.])
        mu = float(rng.choice([-2,-1,0,1,2]))
        assert direct_core_feasible(X,V,vel,mu,a,b) == factor_feasible(X,V,vel,mu,a,b)
        weighted += 1
    return valid,weighted


def codim_one_exact_checks():
    tested = 0
    c = [Fraction(1),Fraction(-2),Fraction(1)]
    velocity = [Fraction(-1),Fraction(0),Fraction(1)]
    pair_means = []
    for i,ci in enumerate(c):
        for j,cj in enumerate(c):
            if ci > 0 and cj < 0:
                wi, wj = (-cj)/(ci-cj), ci/(ci-cj)
                assert wi>=0 and wj>=0 and wi+wj==1
                assert ci*wi+cj*wj==0
                pair_means.append(wi*velocity[i]+wj*velocity[j])
                tested += 4
    assert sorted(pair_means)==[Fraction(-2,3),Fraction(2,3)]
    tested += 1
    return tested


if __name__ == '__main__':
    a = canonical_example()
    b, w = random_feasibility_tests()
    c = codim_one_exact_checks()
    print(f'VERIFY_OK canonical_means={a} random_full_core_vs_factor={b} '
          f'weighted_LP_matches={w} exact_pair_checks={c}')
