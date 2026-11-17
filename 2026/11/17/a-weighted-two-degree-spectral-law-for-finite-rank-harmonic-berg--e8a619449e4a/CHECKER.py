"""Finite arithmetic diagnostics for harmonic Bergman monomial Toeplitz commutators.

The infinite-dimensional asymptotic theorem is proved analytically, not by this checker.
Run: python CHECKER.py (only Python standard library is required).
"""
from math import exp, lgamma, sqrt


def moment(beta, j):
    assert j >= 0 and beta > 0
    return exp(lgamma(beta + 1) + lgamma(j + 1) - lgamma(j + beta + 1))


def basis_coeff(beta, degree, index):
    if index >= 0:
        return sqrt(moment(beta, index + degree) / moment(beta, index))
    k = -index
    if k >= degree:
        return sqrt(moment(beta, k) / moment(beta, k - degree))
    return moment(beta, degree) / sqrt(moment(beta, k) * moment(beta, degree - k))


def two_steps(beta, m, n, k):
    return (basis_coeff(beta, n, -k) * basis_coeff(beta, m, n - k)
            - basis_coeff(beta, m, -k) * basis_coeff(beta, n, m - k))


def three_branches(beta, m, n, k):
    M = m + n
    a, b = moment(beta, k), moment(beta, M - k)
    if 1 <= k <= n:
        return sqrt(b/a)*(moment(beta, n)/moment(beta, n-k)
                          -moment(beta, m)/moment(beta, m-k))
    if n < k < m:
        return moment(beta, m)*(sqrt(a/b)/moment(beta, k-n)
                               -sqrt(b/a)/moment(beta, m-k))
    if m <= k < M:
        return sqrt(a/b)*(moment(beta, m)/moment(beta, k-n)
                          -moment(beta, n)/moment(beta, k-m))
    return 0.0


def unweighted_expected(m, n):
    return n*(m-n)/((m+1)**1.5 * (n+1)**0.5)


def test():
    checks = 0
    for beta in (0.4, 1.0, 2.0, 3.5):
        for m in range(2, 24):
            for n in range(1, m):
                for k in range(1, m+n):
                    a, b = two_steps(beta,m,n,k),three_branches(beta,m,n,k)
                    assert abs(a-b) < 2e-10, (beta,m,n,k,a,b)
                    checks += 1
    for m in range(2, 41):
        for n in range(1, m):
            actual=max(abs(two_steps(1,m,n,k)) for k in range(1,m+n))
            target=unweighted_expected(m,n)
            assert abs(actual-target)<2e-11, (m,n,actual,target)
            checks += 1
    print('DOUBLE_MONOMIAL_COMMUTATOR_CHECKS_OK', checks)

if __name__ == '__main__':
    test()
