"""Exact-arithmetic checks for path Chebyshev quadratic-form covariance.

No external packages. Execute: python verify_path_chebyshev_covariance.py
Finite checks corroborate, but do not replace, the all-order proof.
"""
from fractions import Fraction
from itertools import product


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matrices(n):
    adj = [[int(abs(i-j) == 1) for j in range(n)] for i in range(n)]
    old = [[2 * int(i == j) for j in range(n)] for i in range(n)]
    cur = adj
    out = [None, cur]
    for _ in range(2, n + 1):
        prod = matmul(adj, cur)
        nxt = [[prod[i][j] - old[i][j] for j in range(n)] for i in range(n)]
        out.append(nxt)
        old, cur = cur, nxt
    return out


def matrix_entry_formula(n, m, i, j):
    # One-based vertex labels; returns entry of 2 T_m(A).
    a, b = i + 1, j + 1
    N = n + 1
    return (int(abs(a-b) == m)
            - int(a+b == m)
            - int(a+b == 2*N-m))


def predicted_cov(n, j, k):
    if j == k:
        return n-1 if j % 2 else n-2
    return -2 if (j-k) % 2 == 0 else 0


def direct_cov(mats, j, k):
    n = len(mats[j])
    return sum(mats[j][a][b] * mats[k][a][b]
               for a in range(n) for b in range(a + 1, n))


def exact_sign_cov(mats, j, k):
    n = len(mats[j])
    samples = []
    for z in product((-1, 1), repeat=n):
        def score(m):
            return Fraction(sum(z[a]*m[a][b]*z[b]
                                for a in range(n) for b in range(n)), 2)
        samples.append((score(mats[j]), score(mats[k])))
    count = len(samples)
    mean_j = sum(x for x, _ in samples)/count
    mean_k = sum(y for _, y in samples)/count
    return sum((x-mean_j)*(y-mean_k) for x, y in samples)/count


def check():
    entry_cases = covariance_cases = sign_cases = identities = 0
    for n in range(2, 31):
        mats = matrices(n)
        for m in range(1, n+1):
            for a in range(n):
                for b in range(n):
                    assert mats[m][a][b] == matrix_entry_formula(n, m, a, b), (n,m,a,b)
                    entry_cases += 1
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                assert direct_cov(mats, j, k) == predicted_cov(n, j, k), (n,j,k)
                covariance_cases += 1
        matching = [m for m in range(1, n+1) if m%2 == n%2]
        target = -int(n%2 == 0)
        for i in range(n):
            for j in range(n):
                actual = sum(mats[m][i][j] for m in matching)
                assert actual == target * int(i == j), (n, i, j, actual)
                identities += 1
        if n <= 8:
            for j in range(1, n+1):
                for k in range(1, n+1):
                    assert exact_sign_cov(mats,j,k) == predicted_cov(n,j,k), (n,j,k)
                    sign_cases += 1
    print('PASS exact matrix entries:', entry_cases)
    print('PASS independent pair-covariance comparisons:', covariance_cases)
    print('PASS exact sign-space covariance enumerations:', sign_cases)
    print('PASS polynomial identity matrix entries:', identities)
    print('Finite checks passed; infinite-n proof is separate.')

if __name__ == '__main__':
    check()
