"""Exact rational finite checks for the balanced-axis simplex constructions.
The all-dimensional extremal statement is proved analytically, not by this finite check.
Run: python3 centered_simplex_checker.py
"""
from fractions import Fraction as F
from math import factorial


def det(rows):
    a = [row[:] for row in rows]
    n = len(a)
    out = F(1)
    for k in range(n):
        z = next((j for j in range(k, n) if a[j][k] != 0), None)
        assert z is not None
        if z != k:
            a[k], a[z] = a[z], a[k]
            out = -out
        p = a[k][k]
        out *= p
        for j in range(k + 1, n):
            f = a[j][k] / p
            for s in range(k + 1, n):
                a[j][s] -= f * a[k][s]
            a[j][k] = 0
    return out


def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def verify(n, t, kind):
    m = n + 1
    assert n % 2 == 1 and n >= 5 and 0 < t <= 1
    signs = [1]*(m//2) + [-1]*(m//2)
    v = [[F(i==j) - F(1,m) for i in range(m)] for j in range(m)]
    proj = [[F(signs[i]*signs[j],m) for j in range(m)] for i in range(m)]
    if kind == 'min':
        B = [[t*F(i==j) + (1-t)*proj[i][j] for j in range(m)] for i in range(m)]
        Binv = [[F(1,t)*F(i==j) + (1-F(1,t))*proj[i][j] for j in range(m)] for i in range(m)]
        a = 1 + (n-1)*t*t
        expected = t**(2*(n-1)) * (F(n)/a)**n
    else:
        B = [[F(i==j) + (t-1)*proj[i][j] for j in range(m)] for i in range(m)]
        Binv = [[F(i==j) + (F(1,t)-1)*proj[i][j] for j in range(m)] for i in range(m)]
        a = n - 1 + t*t
        expected = t*t * (F(n)/a)**n
    scale2 = a / m
    u = [[sum((B[i][k]*v[j][k] for k in range(m)),F(0)) for i in range(m)] for j in range(m)]
    w = [[sum((Binv[i][k]*v[j][k] for k in range(m)),F(0)) for i in range(m)] for j in range(m)]
    assert all(dot(s,s) == scale2 for s in u)
    linvr = [dot(s,s) for s in w]
    assert len(set(linvr)) == 1
    h2 = 1/(m*m*scale2*linvr[0])
    assert h2 == 1/(n*n+(n-1)*(t-F(1,t))**2)
    edges = [[u[j][k]-u[0][k] for k in range(m)] for j in range(1,m)]
    gram = [[dot(s,w)/scale2 for w in edges] for s in edges]
    volume2 = det(gram)/(factorial(n)**2)
    regvolume2 = F(m, factorial(n)**2) * F(m,n)**n
    assert volume2 == regvolume2 * expected
    return {'n':n,'t':str(t),'kind':kind,'h_squared':str(h2),'volume_squared':str(volume2)}

if __name__ == '__main__':
    for n in (5, 7, 9):
        for t in (F(1,2),F(2,3),F(3,4)):
            for kind in ('min','max'):
                print(verify(n,t,kind))
    print('PASS: 18 exact rational construction, inradius and volume checks')
