"""Supplementary small-matrix numerical checks for the four-vertex fractional heat theorem.

Python 3, standard library only. The theorem is proved analytically in RESULT.md;
these finite tests are supplementary, not an infinite-domain certificate.
"""
import math
import random


def jacobi_eigh(matrix):
    n = len(matrix)
    a = [list(map(float, row)) for row in matrix]
    v = [[float(i == j) for j in range(n)] for i in range(n)]
    for _ in range(150):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 1e-14:
            break
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        angle = 0.5 * math.atan2(2 * apq, aqq - app)
        c, s = math.cos(angle), math.sin(angle)
        for k in range(n):
            if k not in (p, q):
                x, y = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c * x - s * y
                a[k][q] = a[q][k] = s * x + c * y
        a[p][p] = c*c*app - 2*c*s*apq + s*s*aqq
        a[q][q] = s*s*app + 2*c*s*apq + c*c*aqq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            x, y = v[k][p], v[k][q]
            v[k][p], v[k][q] = c*x - s*y, s*x + c*y
    else:
        raise AssertionError('Jacobi diagonalization did not converge')
    return [max(0.0, a[i][i]) for i in range(n)], v


def heat_from_jacobi(a, b, alpha, t):
    L = [[0.0]*4 for _ in range(4)]
    for i, j, w in [(0, 1, a), (2, 3, a), (0, 2, b), (1, 3, b)]:
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    eig, U = jacobi_eigh(L)
    # Remove the exactly zero constant mode after finite-precision diagonalization.
    eig = [0.0 if z < 1e-12 else z for z in eig]
    expv = [math.exp(-t * z**alpha) for z in eig]
    return [[sum(U[i][k]*U[j][k]*expv[k] for k in range(4))
             for j in range(4)] for i in range(4)]


def heat_from_formula(a, b, alpha, t):
    x = math.exp(-t*(2*a)**alpha)
    y = math.exp(-t*(2*b)**alpha)
    z = math.exp(-t*(2*(a+b))**alpha)
    d = (1+x+y+z)/4
    ka = (1-x+y-z)/4
    kb = (1+x-y-z)/4
    q = (1-x-y+z)/4
    return [[d,ka,kb,q],[ka,d,q,kb],[kb,q,d,ka],[q,kb,ka,d]]


def dimless_q(t, r, alpha):
    u = r**alpha
    delta = math.expm1(alpha*math.log1p(r))
    return -math.expm1(-u*t) + math.exp(-t)*math.expm1(-delta*t)


def dimless_qprime(t, r, alpha):
    u = r**alpha
    delta = math.expm1(alpha*math.log1p(r))
    return u*math.exp(-u*t)+math.exp(-t)-(1+delta)*math.exp(-(1+delta)*t)


def bisect(fn, lo, hi):
    flo, fhi = fn(lo), fn(hi)
    assert flo < 0 < fhi, (lo, hi, flo, fhi)
    for _ in range(110):
        mid = (lo+hi)/2
        if fn(mid) < 0: lo = mid
        else: hi = mid
    return (lo+hi)/2


def check():
    count = 0
    random.seed(17439)
    for alpha in [.45,.8,1,1.1,1.3,1.8,2,3,4.5]:
        for _ in range(35):
            a = math.exp(random.uniform(-2, 2))
            b = math.exp(random.uniform(-2, 2))
            t = math.exp(random.uniform(-5, 1))
            X = heat_from_jacobi(a,b,alpha,t)
            Y = heat_from_formula(a,b,alpha,t)
            assert max(abs(X[i][j]-Y[i][j]) for i in range(4) for j in range(4)) < 4e-11
            assert max(abs(sum(row)-1.0) for row in X) < 1e-10
            assert all(Y[i][j]>-1e-12 for i in range(4) for j in range(4) if i==j or (i+j!=3))
            count += 1
    for alpha in [1.01,1.2,1.7,2.,3.,5.]:
        for r in [.01,.03,.1,.4,1.]:
            delta = math.expm1(alpha*math.log1p(r))
            L0 = math.log(delta/r**alpha)
            peak = bisect(lambda s:dimless_qprime(s,r,alpha), 0, 10.)
            root = bisect(lambda s:dimless_q(s,r,alpha), peak, L0)
            assert L0/(1+delta) < root < L0
            assert dimless_q(peak,r,alpha) < 0
            assert dimless_q(root*1.01,r,alpha)>0
            assert dimless_q(root*.99,r,alpha)<0
            count += 1
    alpha = 1.75
    for r in [0.002,0.0002,0.00002]:
        delta = math.expm1(alpha*math.log1p(r))
        L0 = math.log(delta/r**alpha)
        peak = bisect(lambda s:dimless_qprime(s,r,alpha),0,10)
        root = bisect(lambda s:dimless_q(s,r,alpha),peak,L0)
        target = (alpha-1)*math.log(1/r)+math.log(alpha)
        assert abs(root-target)<.02
        assert abs(peak-1)<.05
        amplification = -dimless_q(peak,r,alpha)/2
        assert abs(amplification/(alpha*r/(2*math.e))-1)<.06
        count += 1
    print(f'PASS: {count} cases; separate Jacobi diagonalization, exact kernel, positivity, threshold bounds and asymptotics checked')


if __name__ == '__main__':
    check()
