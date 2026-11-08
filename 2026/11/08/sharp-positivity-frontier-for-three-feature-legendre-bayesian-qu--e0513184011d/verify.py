"""Exact arithmetic checks for the symmetric three-Legendre-feature quadrature frontier.

Run: python verify.py
The infinite-dimensional/design-uniform conclusions use the proof in RESULT.md;
finite checks here are reproducibility tests, not a substitute for that proof.
"""
from fractions import Fraction as F
from random import Random


def z_of(x):
    return (3 * x * x - 1) / 2


def sharp_constant(n):
    assert n >= 2
    if n % 2 == 0:
        return F(n - 2, 4)
    return max(F(n - 1, 16), F(n - 6, 4))


def witness_z(n):
    if n % 2 == 0:
        return [F(1)] * 2 + [F(1, 2)] * (n - 2)
    if F(n - 1, 16) >= F(n - 6, 4):
        return [F(-1, 2)] + [F(-1, 4)] * (n - 1)
    return [F(-1, 2)] + [F(1)] * 2 + [F(1, 2)] * (n - 3)


def ds(z):
    s1, s2 = sum(z), sum(t*t for t in z)
    return [t*s1-s2 for t in z]


def solve(A, b):
    n = len(b)
    B = [[F(A[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if B[j][i])
        B[i], B[pivot] = B[pivot], B[i]
        f = B[i][i]
        B[i] = [v/f for v in B[i]]
        for j in range(n):
            if j != i:
                g = B[j][i]
                B[j] = [B[j][k]-g*B[i][k] for k in range(n+1)]
    return [B[i][-1] for i in range(n)]


def direct_weights(x, a0, a1, a2, eta):
    n = len(x)
    z = [z_of(t) for t in x]
    K = [[a0+a1*x[i]*x[j]+a2*z[i]*z[j]+(eta if i==j else 0)
          for j in range(n)] for i in range(n)]
    return solve(K, [a0]*n)


def formula_weights(x, a0, a2, eta):
    n = len(x)
    z = [z_of(t) for t in x]
    s1, s2 = sum(z), sum(t*t for t in z)
    u = [(1 - a2*s1*t/(eta+a2*s2))/eta for t in z]
    T = sum(u)
    return [(a0/(1+a0*T))*v for v in u]


def main():
    checks = 0
    for n in range(2, 51):
        z = witness_z(n)
        C = sharp_constant(n)
        assert max(ds(z)) == C
        assert sorted(z) == sorted(z)
        assert all(F(-1,2) <= t <= 1 for t in z)
        if n == 2:
            assert C == 0
        else:
            a2 = F(5,3)
            # At the sharp positive ridge floor, a weight is exactly zero.
            q = [a2*(C-t) for t in ds(z)]
            assert min(q) == 0 and all(t >= 0 for t in q)
            for delta in [F(1,1000),F(1,100)]:
                assert min(a2*(C-t)-delta for t in ds(z)) < 0
                assert min(a2*(C-t)+delta for t in ds(z)) > 0
        checks += 1
    rng=Random(147315)
    for n in range(2, 12):
        for j in range(22):
            half=n//2
            y = [F(rng.randrange(0,9),8) for _ in range(half)]
            x=([F(0)] if n%2 else [])+[t for v in y for t in (-v,v)]
            a0,a1,a2=F(2,3),F(11,7),F(13,5)
            eta=F(1+rng.randrange(25),13)
            direct=direct_weights(x,a0,a1,a2,eta)
            formula=formula_weights(x,a0,a2,eta)
            assert direct == formula, (n,x,direct,formula)
            assert all(a>=0 for a in direct) if eta>=a2*sharp_constant(n) else True
            total=sum(direct)
            assert total > 0 and 1-total >= eta/(eta+a0*n)
            checks += 1
    print(f'VERIFY_OK {checks} exact-rational tests')


if __name__ == '__main__':
    main()
