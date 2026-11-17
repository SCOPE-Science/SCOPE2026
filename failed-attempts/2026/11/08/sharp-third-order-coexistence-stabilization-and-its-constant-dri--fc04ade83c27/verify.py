"""Exact-rational checks for cubic-per-capita Lotka--Volterra stabilization."""
from fractions import Fraction as F
from random import Random


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def build(r, S, p):
    n = len(r)
    a = [[S[i][j] * p[j] for j in range(n)] for i in range(n)]
    w = [-2*r[i] - sum(a[i]) for i in range(n)]
    c = sum(w, F(0))/n
    u = [wi-c for wi in w]
    if all(z == 0 for z in u):
        if c >= 0:
            return None, w, None, None
        H = [[c if i==j else F(0) for j in range(n)] for i in range(n)]
        typ = 'negative_constant'
    else:
        den = sum((z*z for z in u), F(0))
        f = [F(1,n)-(1+c)*u[j]/den for j in range(n)]
        v = [wi+1 for wi in w]
        H = [[(F(-1) if i==j else F(0))+v[i]*f[j] for j in range(n)] for i in range(n)]
        N = [[H[i][j]+(1 if i==j else 0) for j in range(n)] for i in range(n)]
        assert not any(z for row in matmul(N,N) for z in row)
        typ = 'nonconstant'
    q = [-r[i]-sum(a[i]) for i in range(n)]
    g = [[H[i][j]-a[i][j] for j in range(n)] for i in range(n)]
    T = [[[(g[i][j]+g[i][k])/F(2*n)-q[i]/F(n*n) for k in range(n)]
           for j in range(n)] for i in range(n)]
    B = [[[T[i][j][k]/p[j]/p[k] for k in range(n)] for j in range(n)] for i in range(n)]
    for i in range(n):
        assert sum(g[i]) == 2*q[i]
        assert sum((T[i][j][k] for j in range(n) for k in range(n)),F(0)) == q[i]
        for j in range(n):
            assert 2*sum(T[i][j]) == g[i][j]
        G = r[i] + sum(S[i][j]*p[j] for j in range(n)) + sum(B[i][j][k]*p[j]*p[k] for j in range(n) for k in range(n))
        assert G == 0
        for j in range(n):
            J = p[i]*(S[i][j] + 2*sum(B[i][j][k]*p[k] for k in range(n)))
            assert J == p[i]*H[i][j]/p[j]
        assert sum(H[i]) == w[i]
    return H,w,T,typ


def run():
    rng=Random(261109)
    counts={'nonconstant':0,'negative_constant':0,'obstructed':0}
    for n in range(1,7):
        for z in range(160):
            p = [F(rng.randint(1,5),rng.randint(1,5)) for _ in range(n)]
            r = [F(rng.randint(-5,5)) for _ in range(n)]
            S = [[F(rng.randint(-5,5), rng.randint(1,5)) for _ in range(n)] for _ in range(n)]
            if z%10 in (0,1):
                # Enforce w a nonnegative constant or a negative constant.
                c = F(2 if z%10==0 else -2)
                r = [(-c-sum(S[i][j]*p[j] for j in range(n)))/2 for i in range(n)]
            H,w,T,typ=build(r,S,p)
            if H is None:
                assert len(set(w)) == 1 and w[0]>=0
                counts['obstructed'] += 1
            else:
                counts[typ] += 1
    assert sum(counts.values()) == 960
    # Homogeneous example: r=-1, S=0, every w=2; no Hurwitz Jacobian.
    for n in range(1,7):
        assert build([F(-1)]*n, [[F(0)]*n for _ in range(n)],[F(1)]*n)[0] is None
    print('PASS:',counts,'exact-rational cases; 6 explicit nonnegative-constant obstructions')


if __name__=='__main__':
    run()
