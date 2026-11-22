"""Standalone exact-rational checks for the wheel spectral-moment comparison.

The finite assertions are reproducibility checks, not replacements for the
all-size convexity and Fourier arguments in RESULT.md. Python 3 standard library.
"""
from fractions import Fraction as Q
from math import cos, pi, sqrt

CASES = {
    4: (Q(119, 200), +1, -1),
    5: (Q(16, 25), +1, -1),
    6: (Q(643, 1000), +1, -1),
    7: (Q(57, 100), -1, +1),
    8: (Q(1, 2), -1, +1),
    9: (Q(9, 20), -1, +1),
    10: (Q(21, 50), -1, +1),
}


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def product(a, b):
    n, h, m = len(a), len(b), len(b[0])
    return [[sum((a[i][k] * b[k][j] for k in range(h)), Q(0))
             for j in range(m)] for i in range(n)]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def inverse(a):
    n = len(a)
    v = [list(a[i]) + eye(n)[i] for i in range(n)]
    for i in range(n):
        k = next(k for k in range(i, n) if v[k][i] != 0)
        v[i], v[k] = v[k], v[i]
        h = v[i][i]
        v[i] = [x / h for x in v[i]]
        for j in range(n):
            if j == i:
                continue
            h = v[j][i]
            if h:
                v[j] = [x - h * y for x, y in zip(v[j], v[i])]
    return [r[n:] for r in v]


def cycle_laplacian(m):
    c = [[Q(0) for j in range(m)] for i in range(m)]
    for i in range(m):
        c[i][i] += 2
        c[i][(i + 1) % m] -= 1
        c[i][(i - 1) % m] -= 1
    return c


def derivative_signs(m, u):
    c = cycle_laplacian(m)
    a = [[(1-u if i == j else Q(0)) + u*c[i][j]
          for j in range(m)] for i in range(m)]
    ai = inverse(a)
    e = [[c[i][j] - (Q(1) if i == j else Q(0))
          for j in range(m)] for i in range(m)]
    b2 = product(ai, ai)
    b3 = product(b2, ai)
    d1 = -tr(product(b2, e))-(1-Q(1, m+1))/(1-u)**2
    d2 = -tr(product(b3, e))-(1-Q(1, (m+1)**2))/(1-u)**3
    return d1, d2


def full_laplacian(m, u):
    n = m+1
    a, b = (1-u)/m, u/m
    L = [[Q(0) for j in range(n)] for i in range(n)]
    for i in range(m):
        L[0][0] += a
        L[0][i+1] -= a
        L[i+1][0] -= a
        L[i+1][i+1] += a
    for i in range(m):
        j, k = i+1, (i+1)%m+1
        L[j][j] += b; L[k][k] += b
        L[j][k] -= b; L[k][j] -= b
    return L


def pseudoinverse_power_traces(m, u):
    n = m+1
    L = full_laplacian(m, u)
    M = [[L[i][j]+Q(1, n) for j in range(n)] for i in range(n)]
    P = inverse(M)
    return tr(P)-1, tr(product(P, P))-1


def formula_power_traces(m, u):
    c = cycle_laplacian(m)
    A = [[(1-u if i == j else Q(0))+u*c[i][j] for j in range(m)] for i in range(m)]
    B = inverse(A)
    x1 = (1-u)**(-1)/(m+1)+tr(B)-(1-u)**(-1)
    x2 = (1-u)**(-2)/(m+1)**2+tr(product(B,B))-(1-u)**(-2)
    return m*x1, m*m*x2


def dp_float(m, u, p):
    mu = [2-2*cos(2*pi*k/m) for k in range(1,m)]
    return p*((m+1)**(-p)*(1-u)**(-p-1) -
              sum((x-1)/(1-u+u*x)**(p+1) for x in mu))


def root(m, p):
    lo, hi = 0.0, 1.0-1e-12
    assert dp_float(m,lo,p) < 0 and dp_float(m,hi,p)>0
    for _ in range(75):
        mid=(lo+hi)/2
        if dp_float(m,mid,p)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def main():
    count = 0
    for m,(u,s1,s2) in CASES.items():
        d1,d2=derivative_signs(m,u)
        assert (1 if d1>0 else -1)==s1
        assert (1 if d2>0 else -1)==s2
        count += 2
    for m,u in [(3,Q(1,2)),(4,Q(2,5)),(7,Q(57,100)),(10,Q(21,50))]:
        a,b=pseudoinverse_power_traces(m,u)
        c,d=formula_power_traces(m,u)
        assert (a,b)==(c,d)
        count += 2
    x1=root(3,1); x2=root(3,2)
    assert abs(x1-.5)<1e-12 and abs(x2-.5)<1e-12
    count+=2
    for m in range(4,101):
        a,b=root(m,1),root(m,2)
        if 4<=m<=6: assert b>a
        else: assert b<a
        count+=1
    q1=1/3
    q2=(sqrt(7)-2)/3
    for m in [256,1024,4096]:
        assert abs(root(m,1)-q1)<.01
        assert abs(root(m,2)-q2)<.01
        count+=2
    print('PASS',count,'checks')
    print('Exact finite separator signs:',{m:(str(u),s1,s2) for m,(u,s1,s2) in CASES.items()})
    print('Limiting allocations',q1,q2)

if __name__=='__main__':
    main()
