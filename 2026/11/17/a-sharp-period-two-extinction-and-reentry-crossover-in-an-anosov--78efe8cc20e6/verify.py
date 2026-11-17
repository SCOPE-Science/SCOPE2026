#!/usr/bin/env python3
"""Independent numerical checks of the exact period-two phase diagram.

The proof is in RESULT.md; these checks test its matrix algebra, base orbit
exhaustion, fixed-point classification, and sharp parameter crossover.
Requires only the Python 3 standard library.
"""
import cmath
import math
from fractions import Fraction

PI = math.pi
S_H = math.sin(2 * PI / 5)
S_L = math.sin(PI / 5)


def cat_step(t, s):
    return ((2*t+s) % 1, (t+s) % 1)


def base_points():
    # Solve (A^2-I)v = k over the torus using the exact inverse / 5.
    pts = set()
    for k in range(-5, 6):
        for l in range(-5, 6):
            pts.add((Fraction(-k+3*l, 5) % 1,
                     Fraction(3*k-4*l, 5) % 1))
    return pts


def multiply(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def matrix_one_step(shift, epsilon):
    z = cmath.exp(1j * PI * shift)
    t = 1 / math.sqrt(1 - epsilon*epsilon)
    return ((t*z, t*epsilon*z),
            (t*epsilon/z, t/z))


def return_matrix(r, mu, epsilon, sigma):
    M1 = matrix_one_step(r+mu*sigma, epsilon)
    M2 = matrix_one_step(r-mu*sigma, epsilon)
    return multiply(M2, M1)


def matrix_trace(r, mu, epsilon, sigma):
    M = return_matrix(r, mu, epsilon, sigma)
    return M[0][0]+M[1][1]


def trace_formula(r, mu, epsilon, sigma):
    return 2*(math.cos(2*PI*r) + epsilon**2 * math.cos(2*PI*mu*sigma))/(1-epsilon**2)


def thresholds(mu, epsilon):
    uh, ul = PI*mu*S_H, PI*mu*S_L
    return (math.asin(epsilon*math.cos(uh))/PI,
            math.asin(epsilon*math.cos(ul))/PI,
            0.5-math.asin(epsilon*math.sin(uh))/PI,
            0.5-math.asin(epsilon*math.sin(ul))/PI)


def critical(mu):
    uh, ul = PI*mu*S_H, PI*mu*S_L
    return 1/math.sqrt(math.cos(ul)**2 + math.sin(uh)**2)


def branch_count(r, mu, epsilon, sigma):
    h = trace_formula(r, mu, epsilon, sigma)/2
    if abs(abs(h)-1)<1e-9:
        return 1
    return 2 if abs(h)>1 else 0


def number_of_unit_roots(M):
    # Boundary fixed points of the fractional linear action of SU(1,1).
    a, b = M[0]
    c, d = M[1]
    disc = (d-a)**2 + 4*c*b
    z1 = (a-d+cmath.sqrt(disc))/(2*c)
    z2 = (a-d-cmath.sqrt(disc))/(2*c)
    return sum(abs(abs(z)-1)<5e-7 for z in (z1,z2))


def main():
    points = base_points()
    assert len(points) == 5
    assert {cat_step(*pt) for pt in points} == points
    fixed = {pt for pt in points if cat_step(*pt) == pt}
    assert fixed == {(Fraction(0),Fraction(0))}
    assert {(Fraction(1,5),Fraction(2,5)),(Fraction(4,5),Fraction(3,5)),
            (Fraction(2,5),Fraction(4,5)),(Fraction(3,5),Fraction(1,5))} == points-fixed
    assert abs((S_H/S_L)-(1+math.sqrt(5))/2)<1e-14

    mu = 0.3
    star = critical(mu)
    assert 0 < star < 1
    for epsilon in (0.65,star,0.98):
        lh,ll,uh,ul = thresholds(mu, epsilon)
        assert 0 < lh < ll < ul < 0.5 and lh < uh < ul
        if epsilon < star-1e-8:
            assert ll < uh
        if epsilon > star+1e-8:
            assert uh < ll
        if abs(epsilon-star)<1e-12:
            assert abs(uh-ll)<1e-12
        # Threshold and midpoint tests, plus independent circle-root test.
        for r in (0.0,lh/2,(lh+ll)/2,(ll+uh)/2,(uh+ul)/2,(ul+.5)/2):
            for sigma in (S_H,S_L):
                M = return_matrix(r,mu,epsilon,sigma)
                assert abs(matrix_trace(r,mu,epsilon,sigma)-trace_formula(r,mu,epsilon,sigma))<1e-10
                assert abs((M[0][0]*M[1][1]-M[0][1]*M[1][0])-1)<1e-10
                # Exclude numerical near-parabolic cases here.
                if abs(abs(trace_formula(r,mu,epsilon,sigma))-2)>1e-5:
                    assert number_of_unit_roots(M)==branch_count(r,mu,epsilon,sigma)
        for r, sigma in ((lh,S_H),(ll,S_L),(uh,S_H),(ul,S_L)):
            assert abs(abs(trace_formula(r,mu,epsilon,sigma))-2)<1e-10
            M=return_matrix(r,mu,epsilon,sigma)
            assert abs(M[0][1])>1e-6  # Hence parabolic, never identity.
    # Parametric sweep: verify ordering and analytic crossover at 400 samples.
    for i in range(1,201):
        mu = .5*i/201
        star=critical(mu)
        assert 0 < star < 1
        for e in (star/2, (1+star)/2):
            lh,ll,uh,ul=thresholds(mu,e)
            assert 0<lh<ll<ul<.5 and lh<uh<ul
            assert (ll<uh) == (e<star)
    # Analytic slope of the overlap length at the crossover.
    mu = .3
    uH,uL=PI*mu*S_H,PI*mu*S_L
    a,b=math.cos(uL),math.sin(uH)
    K=math.hypot(a,b)
    slope=K**3/(PI*a*b)
    h=1e-5
    numerical=( (thresholds(mu,critical(mu)+h)[1]-thresholds(mu,critical(mu)+h)[2])
                -(thresholds(mu,critical(mu)-h)[1]-thresholds(mu,critical(mu)-h)[2]))/(2*h)
    assert abs(numerical-slope)<1e-7
    print('CHECK_OK base=5 period_two_base_cycles=2 threshold_sweep=400 crossover_slope=verified')
    print('example_mu=0.3 epsilon_star=%.12f' % critical(.3))

if __name__ == '__main__':
    main()
