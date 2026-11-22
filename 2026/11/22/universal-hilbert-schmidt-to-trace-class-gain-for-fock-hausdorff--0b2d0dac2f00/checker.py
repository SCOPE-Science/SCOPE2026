"""Reproducible finite tests for Hausdorff--annihilation commutator formulas.

These tests establish finite matrix identities and consistency of numerical
approximations; they do not replace the infinite-dimensional proofs.
"""
from fractions import Fraction as F
from math import factorial, gamma, lgamma, exp, sqrt


def matmul(a, b):
    d = len(a)
    return [[sum((a[i][h] * b[h][j] for h in range(d)), F(0))
             for j in range(d)] for i in range(d)]


def commutator(a, b):
    ab, ba = matmul(a, b), matmul(b, a)
    return [[ab[i][j] - ba[i][j] for j in range(len(a))]
            for i in range(len(a))]


def beta_integer_moment(n, alpha):
    return F(factorial(alpha) * factorial(n), factorial(alpha + n))


def exact_checks():
    d = 13
    D = [[F(j) if i == j - 1 else F(0) for j in range(d)] for i in range(d)]
    measures = [([(F(1, 5), F(3, 7)), (F(2, 3), F(4, 9)), (F(1), F(5, 6))], None),
                ([(F(1, 17), F(9, 10))], None),
                (None, 1), (None, 2)]
    count = 0
    for atoms, alpha in measures:
        moments = ([sum((weight*s**j for s, weight in atoms), F(0))
                    for j in range(d)] if atoms is not None
                   else [beta_integer_moment(j, alpha) for j in range(d)])
        H = [[moments[i] if i == j else F(0) for j in range(d)] for i in range(d)]
        B = H
        for k in range(1, 5):
            B = commutator(D, B)
            for i in range(d):
                for j in range(d):
                    if j >= k and i == j - k:
                        integral = (sum((weight * s**i * (1-s)**k for s, weight in atoms), F(0))
                                    if atoms is not None else
                                    F(alpha * factorial(i) * factorial(alpha + k - 1),
                                      factorial(i + alpha + k)))
                        predicted = (-1)**k * F(factorial(j), factorial(i)) * integral
                    else:
                        predicted = F(0)
                    assert B[i][j] == predicted, (atoms, alpha, k, i, j, B[i][j], predicted)
                    count += 1
    return count


def numeric_checks():
    atoms = [(0.18, 0.3), (0.76, 0.8), (0.999, 0.2), (1., 0.4)]
    mass = sum(w for s, w in atoms)
    hs2_exact = sum(w*v*(1-s)*(1-t)/(1-s*t)**2
                    for s,w in atoms for t,v in atoms if s < 1 and t < 1)
    hs2_sum = sum((n+1)*sum(w*(1-s)*s**n for s,w in atoms)**2 for n in range(15000))
    assert abs(hs2_exact - hs2_sum) < 2.e-10, (hs2_exact, hs2_sum)
    assert hs2_exact < mass**2
    for k in range(2, 7):
        trace = 0.0
        factor = sqrt(float(factorial(k)))
        for n in range(15000):
            if n:
                factor *= sqrt((n+k)/n)
            val = factor * sum(w * s**n * (1-s)**k for s,w in atoms)
            trace += val
            if n>3000 and val < 1.e-16: break
        assert trace <= sqrt(float(factorial(k))) * mass * (1+1.e-12), (k,trace)
    # Gamma ratios avoid overflow; power-weighted coefficients converge to alpha Gamma(alpha+k).
    for alpha in (0.2,0.7,1.5,2.4):
        for k in (1,2,3):
            constants=[]
            for n in (5000,10000,20000):
                log_w = (0.5*(lgamma(n+k+1)-lgamma(n+1))
                         + lgamma(n+1)-lgamma(n+alpha+k+1)
                         + __import__('math').log(alpha)+lgamma(alpha+k))
                constants.append(exp(log_w+(alpha+k/2)*__import__('math').log(n)))
            target = alpha*gamma(alpha+k)
            assert abs(constants[-1]/target-1)<0.001, (alpha,k,constants,target)
    return hs2_exact


if __name__ == '__main__':
    checks=exact_checks()
    value=numeric_checks()
    print(f'PASS: {checks} exact-rational matrix-entry assertions')
    print(f'PASS: atomic Hilbert--Schmidt kernel check, value {value:.12g}')
    print('PASS: higher commutator trace bounds and beta asymptotics')
