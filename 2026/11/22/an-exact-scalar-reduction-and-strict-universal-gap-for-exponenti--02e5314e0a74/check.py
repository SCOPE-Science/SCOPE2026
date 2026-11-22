#!/usr/bin/env python3
"""Supplementary Jacobian and scalar-bound checks for exponential-cone projection."""
import math
import random


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm_inf(a):
    return max(sum(abs(v) for v in row) for row in a)


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def inverse(a):
    augmented = [[float(a[i][j]) for j in range(3)] + [float(i == j) for j in range(3)] for i in range(3)]
    for j in range(3):
        pivot = max(range(j, 3), key=lambda i: abs(augmented[i][j]))
        augmented[pivot], augmented[j] = augmented[j], augmented[pivot]
        v = augmented[j][j]
        assert abs(v) > 1e-14
        augmented[j] = [x/v for x in augmented[j]]
        for i in range(3):
            if i != j:
                factor = augmented[i][j]
                augmented[i] = [augmented[i][k]-factor*augmented[j][k] for k in range(6)]
    return [row[3:] for row in augmented]


def data(r, t, lam):
    e = math.exp(r)
    p = (r, 1.0, e)
    v = (e, (1-r)*e, -1.0)
    pr = (1.0, 0.0, e)
    vr = (e, -r*e, 0.0)
    pp = dot(p, p)
    vv = dot(v, v)
    q = [pr[i] - dot(pr,p)/pp*p[i] for i in range(3)]
    rho = 1.0/(1.0+lam*e/(t*dot(q,q)))
    R = [[p[i]*p[j]/pp for j in range(3)] for i in range(3)]
    T = [[float(i == j)-v[i]*v[j]/vv for j in range(3)] for i in range(3)]
    J1 = [[R[i][j]+rho*(T[i][j]-R[i][j]) for j in range(3)] for i in range(3)]
    # Direct differentiation of x=t*p(r)+lam*v(r); projected output=t*p(r).
    A = [[p[i],t*pr[i]+lam*vr[i],v[i]] for i in range(3)]
    B = [[p[i],t*pr[i],0.0] for i in range(3)]
    J2 = matmul(B,inverse(A))
    return R,T,J1,J2,rho


def scalar_coefficients(r):
    p = (r, 1.0, math.exp(r))
    v = (math.exp(r), (1-r)*math.exp(r), -1.0)
    ap = [abs(x) for x in p]
    av = [abs(x) for x in v]
    nr = max(ai*sum(ap)/dot(p,p) for ai in ap)
    nt = max(1+ai*(sum(av)-2*ai)/dot(v,v) for ai in av)
    return nr,nt


def main():
    rng = random.Random(20211012)
    count = 0
    for k in range(350):
        r = rng.uniform(-4,4)
        t = math.exp(rng.uniform(-1.6,1.6))
        lam = math.exp(rng.uniform(-4,4))
        R,T,J1,J2,rho = data(r,t,lam)
        assert 0 < rho < 1
        assert max(abs(J1[i][j]-J2[i][j]) for i in range(3) for j in range(3)) < 1e-9
        nr,nt = scalar_coefficients(r)
        assert abs(norm_inf(R)-nr) < 1e-12
        assert abs(norm_inf(T)-nt) < 1e-12
        assert norm_inf(J1) <= max(nr,nt)+1e-12
        count += 1
    rr = 201.0/200.0
    lower = scalar_coefficients(rr)[0]
    upper = (1+math.sqrt(3))/2
    assert 1.3660217 < lower < upper < 1.3660255
    assert scalar_coefficients(1.0)[0] > 1.366018
    assert scalar_coefficients(-0.331)[1] > 1.3658
    # Supplementary grid exploration, not a certificate of the real-line supremum.
    step = 0.002
    grid = [scalar_coefficients(-8+step*k) for k in range(8001)]
    rbest = max(v[0] for v in grid)
    tbest = max(v[1] for v in grid)
    assert lower-0.00002 <= rbest < upper
    assert 1.3658 < tbest < upper
    print('PASS:',count,'direct-Jacobian comparisons; sharpness lower',format(lower,'.12f'))
    print('Exploratory grid: radial',format(rbest,'.9f'),'tangent',format(tbest,'.9f'))
    print('This program does not prove continuous supremum or literature originality.')

if __name__ == '__main__':
    main()
