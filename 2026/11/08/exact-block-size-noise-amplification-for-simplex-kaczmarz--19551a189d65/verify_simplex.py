"""Exact small-dimensional checks for uniform-subset simplex Kaczmarz.
Requires SymPy. Run: python verify_simplex.py.
These finite checks supplement, and do not replace, the general proof.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, eye, ones, Rational, zeros, simplify


def verify_dimension(d):
    n = d + 1
    H = eye(n) - ones(n, n) / n
    u = [H[:, i] for i in range(n)]
    for k in range(1, d + 1):
        T = comb(n, k)
        ep = zeros(n)
        ezz = zeros(n)
        ez = zeros(n, 1)
        for S in combinations(range(n), k):
            US = Matrix.vstack(*[u[i].T for i in S])
            G = US * US.T
            P = US.T * G.inv() * US
            su = sum((u[i] for i in S), zeros(n, 1))
            # Unit-normalized simplex rows a_i=sqrt(n/d)*u_i;
            # z_S = d/(d-k+1)*sqrt(n/d)*sum_{i in S}u_i.
            # The squared coefficient below is rational.
            z2coefficient = Rational(n * d, (d - k + 1)**2)
            ep += P
            ezz += z2coefficient * su * su.T
            ez += su
            assert P * P == P
            assert P * su == su
        assert simplify(ep / T - Rational(k, d) * H) == zeros(n)
        assert simplify(ezz / T - Rational(k, d-k+1) * H) == zeros(n)
        assert ez == zeros(n, 1)
        # General exact transient and limiting mean-square coefficients.
        a = Rational(d-k, d)
        floor = Rational(d*d, d-k+1)
        for t in range(0, 12):
            M_t = floor * (1 - a**t)
            if t:
                M_prev = floor * (1 - a**(t-1))
                assert M_t == a * M_prev + Rational(k*d, d-k+1)
        if k < d:
            assert floor < Rational(d*d, d-k)
        print(f"d={d}, k={k}: exact subset identities pass; stationary MSE={floor}")


if __name__ == '__main__':
    for dim in range(2, 8):
        verify_dimension(dim)
    print('ALL EXACT CHECKS PASS')
