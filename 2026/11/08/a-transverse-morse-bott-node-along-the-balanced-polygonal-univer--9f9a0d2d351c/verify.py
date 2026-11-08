"""Exact finite checks for the balanced cyclic universal-adjoint theorem.

Run with Python 3; no external packages are required. These tests corroborate,
but do not replace, the proof for every admissible size and positive weight.
"""
from fractions import Fraction as Q


def rank(rows):
    a = [[Q(z) for z in row] for row in rows]
    nr, nc, j = len(a), len(a[0]), 0
    for col in range(nc):
        pivot = next((i for i in range(j, nr) if a[i][col]), None)
        if pivot is None:
            continue
        a[j], a[pivot] = a[pivot], a[j]
        t = a[j][col]
        a[j] = [v/t for v in a[j]]
        for i in range(nr):
            if i != j and a[i][col]:
                t = a[i][col]
                a[i] = [v-t*w for v,w in zip(a[i], a[j])]
        j += 1
        if j == nr:
            break
    return j


def prod(seq):
    r = Q(1)
    for z in seq:
        r *= z
    return r


def check(n, weights, a=2, b=3):
    assert n >= 8 and n % 4 == 0
    u = list(map(Q, weights))
    assert all(z > 0 for z in u)
    assert prod(u[::2]) == prod(u[1::2])
    x = [Q(a), Q(b)]
    for i in range(n-2):
        x.append(-u[i+1]*x[i]/u[i])
    assert x[0] == -u[-1]*x[-2]/u[-2]
    assert x[1] == -u[0]*x[-1]/u[-1]
    assert all(z != 0 for z in x)

    def included(k):
        return [i for i in range(n) if i != k and i != (k+1)%n]

    F = Q(0)
    grad = [Q(0)] * n
    hess = [[Q(0)] * n for _ in range(n)]
    for k in range(n):
        support = included(k)
        F += u[k]*prod(x[i] for i in support)
        for i in support:
            grad[i] += u[k]*prod(x[j] for j in support if j != i)
        for i in support:
            for j in support:
                if i != j:
                    hess[i][j] += u[k]*prod(x[t] for t in support if t not in (i,j))
    assert F == 0, 'F not zero'
    assert not any(grad), 'gradient not zero'
    assert rank(hess) == n-2, 'incorrect Hessian rank'
    P = prod(x)
    y = [u[i]/(x[i]*x[(i+1)%n]) for i in range(n)]
    assert all(y[i]+y[(i+1)%n] == 0 for i in range(n))
    loghess = [[x[i]*hess[i][j]*x[j] for j in range(n)] for i in range(n)]
    expected = [[P*y[i] if j == (i+1)%n else
                 P*y[j] if i == (j+1)%n else Q(0)
                 for j in range(n)] for i in range(n)]
    assert loghess == expected
    print(f'n={n}: F=gradient=0, Hessian rank={n-2}, log-Hessian certificate PASS')


if __name__ == '__main__':
    for n in (8,12,16):
        check(n, [1]*n)
    check(8, [2,3,5,7,11,13,17,Q(2*5*11*17,3*7*13)])
    print('EXACT_BALANCED_ADJOINT_CHECKS_PASS')
