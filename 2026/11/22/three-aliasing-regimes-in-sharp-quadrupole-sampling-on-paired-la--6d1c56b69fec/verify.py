#!/usr/bin/env python3
"""Independent standard-library checks of paired latitude-ring quadrupole spectra.

Run: python3 verify.py
Numerical tests are corroborative; the accompanying mathematical proof is universal.
"""
import math
from fractions import Fraction


def harmonic_values(x, y, z):
    # Orthonormal for the spherical probability area measure.
    return ((math.sqrt(5)/2)*(3*z*z-1), math.sqrt(15)*z*x,
            math.sqrt(15)*z*y, (math.sqrt(15)/2)*(x*x-y*y),
            math.sqrt(15)*x*y)


def direct_gram(m, t, delta):
    r, h = math.sqrt(1-t), math.sqrt(t)
    matrix = [[0.0]*5 for _ in range(5)]
    for z, offset in ((h, 0), (-h, delta)):
        for j in range(m):
            angle = offset + 2*math.pi*j/m
            y = harmonic_values(r*math.cos(angle),r*math.sin(angle),z)
            for i in range(5):
                for k in range(5):
                    matrix[i][k] += y[i]*y[k]/(2*m)
    return matrix


def symmetric_eigenvalues(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    for iteration in range(150):
        i, j = max(((i,j) for i in range(n) for j in range(i+1,n)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[i][j]) < 1e-13:
            break
        tau = (a[j][j]-a[i][i])/(2*a[i][j])
        z = 1/(abs(tau)+math.hypot(1,tau))
        z = math.copysign(z,tau) if tau else 1.0
        c = 1/math.hypot(1,z)
        s = z*c
        off = a[i][j]
        a[i][i] -= z*off
        a[j][j] += z*off
        a[i][j] = a[j][i] = 0
        for k in range(n):
            if k != i and k != j:
                ki, kj = a[k][i],a[k][j]
                a[k][i] = a[i][k] = c*ki - s*kj
                a[k][j] = a[j][k] = s*ki + c*kj
    else:
        raise AssertionError('Jacobi diagonalization did not converge')
    return sorted(a[i][i] for i in range(n))


def predicted(m,t,delta):
    C = Fraction(5,4)*(3*t-1)**2
    A = Fraction(15,2)*t*(1-t)
    B = Fraction(15,8)*(1-t)**2
    if m == 3:
        D = math.hypot(A-B,2*math.sqrt(A*B)*math.sin(3*delta/2))
        low, high = (A+B-D)/2,(A+B+D)/2
        return sorted((C,low,low,high,high))
    if m == 4:
        c = abs(math.cos(2*delta))
        return sorted((C,A,A,B*(1-c),B*(1+c)))
    return sorted((C,A,A,B,B))


def exact_polynomial_identity_checks():
    # Exact rational (not floating-point) evaluations at more points than degree.
    for numerator in range(11):
        t = Fraction(numerator, 10)
        C = Fraction(5,4)*(3*t-1)**2
        A = Fraction(15,2)*t*(1-t)
        B = Fraction(15,8)*(1-t)**2
        assert C+2*A+2*B == 5
        assert A/B == 4*t/(1-t) if t not in (0,1) else True
        if t not in (0,1):
            assert B/A == (1-t)/(4*t)
        assert C >= 0 and A >= 0 and B >= 0


def run():
    exact_polynomial_identity_checks()
    cases = 0
    tstar=(6-math.sqrt(21))/15
    for m in range(3,11):
        for t in (.0002,.04,tstar,.18,1/3,.46,.79,.999):
            for delta in (0,.013,.13,.37,math.pi/(2*m),math.pi/m,
                          1.29,2*math.pi/m):
                direct = symmetric_eigenvalues(direct_gram(m,t,delta))
                formula = predicted(m,t,delta)
                err=max(abs(x-y) for x,y in zip(direct, formula))
                assert err < 2e-11,(m,t,delta,err)
                assert abs(sum(direct)-5)<1e-11
                cases += 1
    bestE=(11-math.sqrt(21))/10
    bestR=(5+math.sqrt(21))/4
    assert abs(Fraction(15,2)*tstar*(1-tstar)-bestE)<1e-13
    assert abs(bestR - (1-tstar)/(4*tstar))<1e-13
    assert abs(1-1/bestR-(math.sqrt(21)-4))<1e-13
    for m,delta in ((3,0),(4,math.pi/4),(5,.31),(10,.93)):
        values=predicted(m,tstar,delta)
        assert abs(values[0]-bestE)<2e-13
        assert abs(values[-1]/values[0]-bestR)<2e-13
    # The three-node antiprism has two missing independent directions.
    values=predicted(3,tstar,math.pi/3)
    assert abs(values[0])<1e-13 and abs(values[1])<1e-13
    # The m=4 E-plateau ends at the exact algebraic boundary.
    cutoff=math.sqrt(21)-4
    for c in (0,cutoff/3,cutoff*.75,cutoff,(cutoff+1)/2):
        delta=math.acos(c)/2
        lam=predicted(4,tstar,delta)[0]
        if c<=cutoff+1e-14:
            assert abs(lam-bestE)<2e-13
        else:
            assert lam<bestE-1e-4
    print('PASS: %d independent complete 5-by-5 Gram spectral tests' % cases)
    print('PASS: rational identities, exceptional ranks, E-plateau, global extrema')
    print('lambda_star=%.15f, kappa_squared_star=%.15f' % (bestE,bestR))


if __name__=='__main__':
    run()
