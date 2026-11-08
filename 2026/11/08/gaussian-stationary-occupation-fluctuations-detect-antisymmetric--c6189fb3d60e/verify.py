"""Finite independent numerical diagnostics for dense random rate generators.

Usage: python verify.py. Standard library only. Finite checks do not prove
asymptotic Gaussian convergence or a matrix concentration inequality.
"""
from math import sqrt
from random import Random


def solve(a, b):
    """Partial-pivot Gaussian elimination (independent of balance identity)."""
    n = len(b)
    a = [r[:] for r in a]
    b = b[:]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(a[i][k]))
        assert abs(a[p][k]) > 1e-12
        a[k], a[p] = a[p], a[k]
        b[k], b[p] = b[p], b[k]
        pivot = a[k][k]
        for i in range(k+1, n):
            factor = a[i][k] / pivot
            if factor:
                a[i][k] = 0.0
                for j in range(k+1, n):
                    a[i][j] -= factor * a[k][j]
                b[i] -= factor * b[k]
    x = [0.] * n
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(a[i][j]*x[j] for j in range(i+1, n))) / a[i][i]
    return x


def example(n, law, rng):
    x = [[0.]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            v = 1. if rng.randrange(2) == 0 else 3.
            if law == 'symmetric':
                w = v
            elif law == 'independent':
                w = 1. if rng.randrange(2) == 0 else 3.
            elif law == 'anticorrelated':
                w = 4. - v
            else:
                raise ValueError(law)
            x[i][j] = v
            x[j][i] = w
    generator = [row[:] for row in x]
    incoming = [sum(row) for row in x]
    outgoing = [sum(x[i][j] for i in range(n)) for j in range(n)]
    for i in range(n):
        generator[i][i] = -outgoing[i]
    augmented = [row[:] for row in generator]
    augmented[-1] = [1.]*n
    rhs = [0.]*(n-1)+[1.]
    p = solve(augmented, rhs)
    assert abs(sum(p)-1.) < 1e-9
    assert min(p) > 0.
    assert max(abs(sum(generator[i][j]*p[j] for j in range(n))) for i in range(n)) < 1e-8
    s = [incoming[i]-outgoing[i] for i in range(n)]
    assert abs(sum(s)) < 1e-10
    delta = [p[i]-1./n for i in range(n)]
    mu = 2.
    # The exact stationary perturbation identity.
    for i in range(n):
        b_delta = sum((x[i][j]-mu)*delta[j] for j in range(n) if i != j)
        b_delta -= sum(x[j][i]-mu for j in range(n) if i != j)*delta[i]
        approx = s[i]/(mu*n*n)
        assert abs(delta[i] - approx - b_delta/(mu*n)) < 2e-10
    q = n*n*sum(v*v for v in delta)
    if law == 'symmetric':
        assert max(abs(v) for v in delta) < 2e-12
    return q, sqrt(sum((delta[i]-s[i]/(mu*n*n))**2 for i in range(n))) / max(sqrt(sum((s[i]/(mu*n*n))**2 for i in range(n))),1e-12)


def main():
    rng = Random(260614542)
    trials = 0
    for law, limit in [('symmetric',0.), ('independent',0.5), ('anticorrelated',1.)]:
        for n in (12,24,48,72):
            samples = [example(n, law, rng) for _ in range(8)]
            trials += len(samples)
            mean_q = sum(a for a, _ in samples)/len(samples)
            mean_error = sum(e for _, e in samples)/len(samples)
            assert abs(mean_q-limit) < max(0.4,1.0/n**0.5)
            if law!='symmetric' and n == 72:
                assert mean_error < 0.5
            print('%s n=%d: mean susceptibility=%.6f (limit %.6f), mean relative linearization error=%.6f' %(law,n,mean_q,limit,mean_error))
    print('PASS: %d stationary generators, 3 edge couplings; residuals and exact perturbation identities verified.' % trials)


if __name__ == '__main__':
    main()
