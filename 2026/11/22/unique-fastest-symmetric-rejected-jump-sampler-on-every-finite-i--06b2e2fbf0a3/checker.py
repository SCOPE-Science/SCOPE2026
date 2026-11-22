"""Independent exact and numeric checks for rejected-jump mixing on an interval.

Uses only the Python standard library. The checks do not replace the all-n proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def transition(n, weights):
    """weights maps integer displacement to probability; rejects off-grid jumps."""
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    assert sum(weights.values(), F(0)) == 1
    assert all(v >= 0 for v in weights.values())
    assert all(weights.get(s, F(0)) == weights.get(-s, F(0)) for s in weights)
    for i in range(n):
        for s, prob in weights.items():
            j = i + s
            if 0 <= j < n:
                P[i][j] += prob
            else:
                P[i][i] += prob
    return P


def optimal(n):
    w = {s: F(1, 2*(n-1)) for s in range(1, n)}
    w.update({-s: F(1, 2*(n-1)) for s in range(1, n)})
    return w


def jacobi_symmetric(A):
    """Jacobi diagonalization for small symmetric floating-point matrices."""
    a = [[float(x) for x in row] for row in A]
    n = len(a)
    for _ in range(40*n*n):
        i, j = max(((i, j) for i in range(n) for j in range(i+1,n)), key=lambda p: abs(a[p[0]][p[1]]))
        if abs(a[i][j]) < 1.e-12:
            return sorted(a[k][k] for k in range(n))
        import math
        phi = 0.5*math.atan2(2*a[i][j], a[j][j]-a[i][i])
        c, s = math.cos(phi), math.sin(phi)
        # Basis rotation chosen to make off-diagonal zero.
        ai, aj, aij = a[i][i],a[j][j],a[i][j]
        a[i][i]=c*c*ai-2*s*c*aij+s*s*aj
        a[j][j]=s*s*ai+2*s*c*aij+c*c*aj
        a[i][j]=a[j][i]=0.
        for k in range(n):
            if k not in (i,j):
                x,y=a[k][i],a[k][j]
                a[k][i]=a[i][k]=c*x-s*y
                a[k][j]=a[j][k]=s*x+c*y
    raise AssertionError('Jacobi nonconvergence')


def test():
    count=0
    for n in range(2,20):
        P=transition(n,optimal(n))
        lam=F(n-2,2*(n-1))
        for i in range(n):
            assert sum(P[i])==1
            for j in range(n):
                assert P[i][j]==(F(1,2) if i==j else F(1,2*(n-1)))
                assert P[i][j]==P[j][i]
                count+=3
        for j in range(n):
            assert sum(P[i][j] for i in range(n))==1
            count+=1
        for i in range(n):
            for j in range(n):
                assert P[i][j]-(F(1,n))==(lam if i==j else F(0)) - lam*F(1,n)
                count+=1
        accepted=sum(sum(P[i][j] for j in range(n) if j!=i) for i in range(n))/n
        assert accepted == F(1,2)
        count+=1
    rng=Random(20231115)
    for n in range(2,14):
        base=F(n-2,2*(n-1))
        for trial in range(150):
            k=n+2
            raw=[rng.randint(0,20) for _ in range(k)]
            den=2*sum(raw)+rng.randint(0,20)
            if not den: continue
            weights={s+1:F(a,den) for s,a in enumerate(raw)}
            weights.update({-s:v for s,v in list(weights.items())})
            weights[0]=1-sum(weights.values())
            P=transition(n,weights)
            ev=jacobi_symmetric(P)
            mu=max(abs(ev[0]),abs(ev[-2]))
            S=sum(weights[s] for s in range(1,n))
            deviation=sqrt(sum(float(weights[s]-S/(n-1))**2 for s in range(1,n)))
            lower=float(base+F(n,n-1)*(F(1,2)-S)) + n/(4*(n-1)**1.5)*deviation
            assert mu+2e-9>=lower,(n,trial,mu,lower)
            assert mu+2e-9>=float(base)
            assert abs(ev[-1]-1)<1e-9
            count+=3
    print('PASS:', count, 'exact identities or independent numeric inequalities')

if __name__=='__main__': test()
