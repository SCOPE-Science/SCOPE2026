#!/usr/bin/env python3
"""Reproducibility checks for a four-site Euclidean distance-energy theorem."""
import math
import random


def solve(matrix, rhs):
    n = len(rhs)
    a = [list(map(float, matrix[i])) + [float(rhs[i])] for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[p][k]) < 1e-13:
            raise ArithmeticError('singular system')
        a[k], a[p] = a[p], a[k]
        z = a[k][k]
        for j in range(k, n+1):
            a[k][j] /= z
        for i in range(n):
            if i == k:
                continue
            z = a[i][k]
            for j in range(k, n+1):
                a[i][j] -= z*a[k][j]
    return [a[i][n] for i in range(n)]


def distance_matrix(points):
    return [[math.dist(x,y) for y in points] for x in points]


def gauging(points):
    d = distance_matrix(points)
    n = len(points)
    b = [row + [1.] for row in d] + [[1.]*n + [0.]]
    z = solve(b, [0.]*n + [1.])
    return z[:n], -z[-1]


def predicted_weight(triangle, fourth):
    v, lam = gauging(triangle)
    r = [math.dist(a, fourth) for a in triangle]
    phi = sum(x*y for x, y in zip(v, r))
    d = distance_matrix(triangle)
    q = solve(d, [phi-z for z in r])
    assert abs(sum(q)) < 1e-9
    Q = 2*phi-lam-sum(x*y for x,y in zip(r,q))
    assert Q>0
    return (phi-lam)/Q, phi, lam, Q


def check():
    p = [(0., 0.), (2., 0.), (1., math.sqrt(3))]
    y = (1., -0.1)
    w, lam4 = gauging(p + [y])
    formula, phi, lam3, Q = predicted_weight(p, y)
    assert formula < 0 and w[-1] < 0 and abs(formula-w[-1]) < 1e-11
    assert abs(lam3 - 4/3) < 1e-13
    assert math.sqrt(101)/5 + math.sqrt(3) + .1 < 4
    assert w[0]>0 and w[1]>0 and w[2]>0
    rng = random.Random(130719)
    checked = 0
    for i in range(400):
        p = [(rng.uniform(-2,2), rng.uniform(-2,2)) for _ in range(3)]
        x1,y1=p[0]; x2,y2=p[1]; x3,y3=p[2]
        twice_area=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
        if abs(twice_area)<.15:
            continue
        y=(rng.uniform(-3,3),rng.uniform(-3,3))
        if min(math.dist(y,a) for a in p)<.15:
            continue
        v, _=gauging(p)
        assert min(v)>0
        val, phi, lam, Q = predicted_weight(p,y)
        w, _=gauging(p+[y])
        assert abs(val-w[-1])<2e-8
        assert (w[-1]>0)==(phi>lam)
        checked+=1
    assert checked>=250
    # Each open original side lies strictly inside the sign oval.
    for i in range(3):
        for t in (0.15,0.5,0.85):
            y = tuple((1-t)*a+t*b for a,b in zip(p[i],p[(i+1)%3]))
            _,phi,lam,_=predicted_weight(p,y)
            assert phi<lam
    print('PASS: explicit exposed negative site; %d independent random four-site checks; open-edge checks' % checked)


if __name__ == '__main__':
    check()
