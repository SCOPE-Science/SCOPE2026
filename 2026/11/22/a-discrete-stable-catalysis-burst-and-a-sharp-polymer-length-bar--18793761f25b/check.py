#!/usr/bin/env python3
"""Finite checks of a Pareto-catalysis polymer-length calculation.

Only Python's standard library is required. Finite arithmetic is illustrative;
the convergence claims are proved analytically in the accompanying article.
"""
import math


def molecule_count(k, m):
    return sum(k ** j for j in range(1, m + 1))


def reaction_count(k, m):
    return sum((j - 1) * (k ** j) for j in range(2, m + 1))


def q_half(u):
    """Exact probability a Pareto-half catalyst hits any of R reactions,
    when u=lambda*R/N and conditional hit probability is 1-exp(-uW/R).
    """
    return -math.expm1(-u) + math.sqrt(math.pi * u) * math.erfc(math.sqrt(u))


def simpson(func, a, b, steps=150000):
    assert steps % 2 == 0
    h = (b - a) / steps
    acc = func(a) + func(b)
    for i in range(1, steps):
        acc += (4 if i % 2 else 2) * func(a + i * h)
    return acc * h / 3


def exact_short_edge_probability(n, ell, k=2, alpha=.5, beta=.5):
    assert alpha == .5
    N = molecule_count(k, n)
    L = molecule_count(k, ell)
    R = reaction_count(k, ell)
    lam = N ** (-beta)
    u = lam * R / N
    q = q_half(u)
    return -math.expm1(L * math.log1p(-q)), L * q


def asymptotic_intensity(n, ell, k=2, alpha=.5, beta=.5):
    theta = alpha * (1 + beta) / (1 + alpha)
    b = theta*n - alpha/(1 + alpha)*math.log(n, k)
    C = (math.gamma(1-alpha) * theta**alpha *
         (k-1)**(alpha*beta-1) * k**(1-alpha*beta))
    return C * k**((1+alpha)*(ell-b))


def main():
    # Every word of a fixed length has (length-1) ordered cuts.
    for k in (2, 3, 4):
        for ell in range(2, 7):
            direct = sum(sum(1 for cut in range(1, j)) * k**j
                         for j in range(2, ell+1))
            assert direct == reaction_count(k, ell)
            assert molecule_count(k, ell) == k*(k**ell-1)//(k-1)

    # A separate uniform-change-of-variables integral for the Pareto-half
    # W=U^(-2) checks the exact Laplace transform used in the proof.
    for u in (.003, .03, .15):
        numerical = simpson(lambda v: 1 - math.exp(-u/(v*v)) if v else 1.0, 0, 1)
        assert abs(numerical - q_half(u)) < 3e-8, (u, numerical, q_half(u))

    theta = (.5*(1+.5))/(1+.5)
    assert theta == .5
    data = ((60, 28, .8504251760823844),
            (120, 57, .6235606282690702),
            (240, 117, .7565240654996834))
    for n, ell, expected_probability in data:
        finite_probability, mu = exact_short_edge_probability(n, ell)
        assert abs(finite_probability-expected_probability) < 2e-8
        approximate_mu = asymptotic_intensity(n, ell)
        assert 0 < finite_probability < 1
        assert abs(mu/approximate_mu-1) < .08
        print('n=', n, 'ell=', ell, 'exact incidence probability=',
              f'{finite_probability:.10f}', 'Poisson intensity=', f'{mu:.9f}')

    # The Sibuya(alpha) mark probability has coefficients
    # p_1=alpha, p_{j+1}/p_j=(j-alpha)/(j+1).
    alpha = .5
    probs = [alpha]
    for j in range(1, 10):
        probs.append(probs[-1] * (j-alpha)/(j+1))
    assert all(x > 0 for x in probs)
    assert abs(probs[0]-.5) < 1e-15
    assert abs(probs[1]-.125) < 1e-15
    assert abs(probs[2]-.0625) < 1e-15
    z = .5
    partial_pgf = sum(p*z**(j+1) for j,p in enumerate(probs))
    true_pgf = 1-math.sqrt(1-z)
    assert 0 < true_pgf-partial_pgf < 1e-5

    print('checks passed')


if __name__ == '__main__':
    main()
