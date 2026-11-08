#!/usr/bin/env python3
"""Independent finite numerical checks of a two-colour Huygens period-two theorem.
Requires Python 3.9+ and NumPy. Computations do not certify all graph sizes.
"""
import math
import numpy as np


def complete_bipartite(p, q):
    assert p >= 1 and q >= 1
    return [(i, p + j) for i in range(p) for j in range(q)], p + q, list(range(p)), list(range(p, p + q)), q, p


def ring(n):
    assert n >= 4 and n % 2 == 0
    return [(i, (i+1) % n) for i in range(n)], n, list(range(0, n, 2)), list(range(1, n, 2)), 2, 2


def cube(d):
    n = 1 << d
    edges = [(i, i ^ (1 << j)) for i in range(n) for j in range(d) if i < (i ^ (1 << j))]
    a = [i for i in range(n) if i.bit_count() % 2 == 0]
    b = [i for i in range(n) if i.bit_count() % 2 == 1]
    return edges, n, a, b, d, d


def laplacian(edges, n):
    L = np.zeros((n, n))
    for i, j in edges:
        L[i, i] += 1
        L[j, j] += 1
        L[i, j] -= 1
        L[j, i] -= 1
    return L


def parameter(a, r, s):
    return 2*a / ((r+s)*math.sin(a))


def update(x, edges, h):
    y = x.copy()
    for i, j in edges:
        delta = h * math.sin(x[i] - x[j])
        y[i] += delta
        y[j] -= delta
    return y


def bisection_decreasing_q(target):
    assert 0 < target < 2
    lo, hi = 1e-12, math.pi/2
    for _ in range(70):
        m = (lo+hi)/2
        if 2*m/math.tan(m) > target:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def main():
    graphs = [complete_bipartite(1, 4), complete_bipartite(2, 3),
              complete_bipartite(4, 4), ring(6), ring(10), cube(3), cube(4)]
    tests = 0
    for edges, n, A, B, r, s in graphs:
        L = laplacian(edges, n)
        eigs = np.linalg.eigvalsh(L)
        lam2, Lam = eigs[1], eigs[-1]
        assert abs(Lam - (r+s)) < 1e-10
        assert lam2 > 0
        for a in (0.05, 0.2, 0.5, 1.0, 1.4, math.pi/2, 1.7, 2.1):
            h = parameter(a, r, s)
            x = np.empty(n)
            x[A], x[B] = math.pi+a, 0.0
            y = update(x, edges, h)
            z = update(y, edges, h)
            assert np.max(abs(z-x)) < 1e-11
            assert np.max(abs(y-x)) > 1e-6
            D = np.eye(n) - h*math.cos(a)*L
            obtained = np.linalg.eigvalsh(D@D)
            expected = np.sort((1-h*math.cos(a)*eigs)**2)
            assert np.max(abs(obtained-expected)) < 1e-11
            transverse = (1-h*math.cos(a)*eigs[1:])**2
            rho = max(transverse)
            boundary = max((1-h*math.cos(a)*lam2)**2, (1-h*math.cos(a)*Lam)**2)
            assert abs(rho-boundary) < 1e-11
            if a < math.pi/2:
                assert rho < 1
            elif a > math.pi/2:
                assert min(transverse) > 1
            else:
                assert max(abs(transverse-1)) < 1e-12
            tests += 1
        qoptimal = 2*Lam/(Lam+lam2)
        aoptimal = bisection_decreasing_q(qoptimal)
        toptimal = parameter(aoptimal,r,s)*math.cos(aoptimal)
        rhomin = max((1-toptimal*lam2)**2, (1-toptimal*Lam)**2)
        assert abs(toptimal - 2/(Lam+lam2)) < 1e-12
        assert abs(rhomin - ((Lam-lam2)/(Lam+lam2))**2) < 1e-12
        for da in (0.01, 0.07, 0.2):
            l = max(1e-5, aoptimal-da)
            u = min(1.56, aoptimal+da)
            for perturbed in (l,u):
                t=parameter(perturbed,r,s)*math.cos(perturbed)
                other=max((1-t*lam2)**2,(1-t*Lam)**2)
                assert other >= rhomin - 1e-11
        tests += 1
        for alpha in (2+1e-4,2+2e-4):
            # Invert alpha(a) with bisection; infer asymptotics of graph modes.
            lo,hi=1e-7,0.2
            for _ in range(60):
                m=(lo+hi)/2
                if 2*m/math.sin(m) < alpha:lo=m
                else:hi=m
            a=(lo+hi)/2
            t=2*a/math.tan(a)/Lam
            rho=max((1-t*lam2)**2,(1-t*Lam)**2)
            assert abs((1-rho)/(alpha-2)-4) < 0.015
            tests+=1
        for upper_gap in (1e-4,2e-4):
            alpha=math.pi-upper_gap
            lo,hi=math.pi/2-0.2,math.pi/2
            for _ in range(60):
                m=(lo+hi)/2
                if 2*m/math.sin(m) < alpha:lo=m
                else:hi=m
            a=(lo+hi)/2
            t=2*a/math.tan(a)/Lam
            rho=max((1-t*lam2)**2,(1-t*Lam)**2)
            assert abs((1-rho)/upper_gap-math.pi*lam2/Lam) < 0.02
            tests+=1
    # On the critical two-colour line, double iterates have cubic damping.
    x = 0.001
    plus = x + math.pi*(1-math.cos(x))
    twice = plus + math.pi*(math.cos(plus)-1)
    assert abs((twice-x)/x**3 + math.pi**2/2) < 0.02
    tests+=1
    print(f'PASS {tests} network, orbit, spectrum, optimum and edge checks')


if __name__ == '__main__':
    main()
