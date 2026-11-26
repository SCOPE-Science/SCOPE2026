"""Exact arithmetic checks for the arbitrary-order simplicial SIS construction.

Run: python3 verify.py
Only the Python standard library is required.
Finite checks support, but do not replace, the all-orders proof.
"""
from fractions import Fraction as F
from math import factorial


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for j, v in enumerate(a):
        out[j] += v
    for j, v in enumerate(b):
        out[j] += v
    return out


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i+j] += c*d
    return out


def evaluate(coeffs, x):
    z = F(0)
    for c in coeffs[::-1]:
        z = z*x + c
    return z


def construct(M, eps=F(1, 8)):
    assert M >= 2 and 0 < eps < F(1, 8) + F(1, 1000)
    K = M - 1
    delta = eps / (4*(2*M)**K)
    roots = [F(j, M)*delta for j in range(1, M)]
    Q = [F(1)]
    for r in roots:
        Q = mul(Q, [-r, F(1)])
    P = add([F(1)]*M, [eps*q for q in Q])
    f = add(mul([F(1), F(-1)], P), [F(-1)])
    return delta, roots, P, f


def main():
    for M in range(2, 13):
        delta, roots, P, f = construct(M)
        assert len(P) == M and all(c > 0 for c in P)
        assert all(abs(c - 1) < F(1, 4) for c in P)
        assert len(f) == M+1 and f[-1] < 0
        assert evaluate(f, F(1)) == -1
        K = M-1
        t = [F(2*j+1, 2*M)*delta for j in range(M)]
        signs = [1 if evaluate(f, z) > 0 else -1 for z in t]
        expected = [(-1)**(K-j) for j in range(M)]
        assert signs == expected
        assert signs[-1] == 1 and evaluate(f, F(1)) < 0
        # Check the coefficient map in the complete-simplex mean-field ODE.
        source_coefficients = [P[0] - 1]
        source_coefficients += [P[i] - P[i-1] for i in range(1, M)]
        source_coefficients += [-P[-1]]
        vector_field = mul([F(0), F(1)], f)
        assert vector_field == [F(0)] + source_coefficients
        infection_strengths = [factorial(i)*P[i-1] for i in range(1, M+1)]
        assert all(v > 0 for v in infection_strengths)
        print(f'M={M}: {M} exactly isolated endemic roots, '
              f'{(M+1)//2} stable, normalized rates positive; exact checks OK')
    print('All exact arithmetic certificates passed.')


if __name__ == '__main__':
    main()
