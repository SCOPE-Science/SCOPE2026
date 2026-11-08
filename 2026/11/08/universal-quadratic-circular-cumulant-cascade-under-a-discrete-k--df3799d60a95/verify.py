#!/usr/bin/env python3
"""Exact moment/cumulant coefficient tests and independent circle quadrature."""
from fractions import Fraction as Q
from math import comb, sin, cos, pi
import cmath


def add(p, q):
    return tuple(p[i] + q[i] for i in range(3))


def mul(p, q):
    return tuple(sum(p[j] * q[i-j] for j in range(i+1)) for i in range(3))


def scalar(c, p):
    return tuple(c*v for v in p)


def moment_poly(m, a):
    if m == 0:
        return (Q(1), Q(0), Q(0))
    initial = a**m
    first = Q(m,2)*(a**(m-1)-a**(m+1))
    if m == 1:
        second = Q(1,8)*(a-2*a+a**3)  # real a, E[W^-1]=a
    else:
        second = Q(m*m,8)*(a**(m-2)-2*a**m+a**(m+2))
    return (initial, first, second)

count=0
for a in (Q(0), Q(1,5), Q(1,2), Q(-2,5), Q(3,4)):
    M=[moment_poly(m,a) for m in range(13)]
    P=[(Q(1),Q(0),Q(0))]
    for m in range(1,13):
        P.append(mul(P[-1],M[1]))
    for m in range(2,13):
        defect=add(M[m],scalar(-1,P[m]))
        assert defect[:2] == (0,0)
        assert defect[2] == Q(m,8)*(1-a*a)*a**(m-2)
        count+=1
    C=[(Q(0),Q(0),Q(0)) for _ in range(13)]
    for m in range(1,13):
        value=M[m]
        for j in range(1,m):
            value=add(value,scalar(-comb(m-1,j-1),mul(C[j],M[m-j])))
        C[m]=value
    assert C[1] == M[1]
    for m in range(2,13):
        assert C[m][:2]==(0,0)
        assert C[m][2] == Q(m*(-1)**m,8)*(1-a*a)*a**(m-2)
        count+=1

# Independent direct quadrature: exact nonlinear sine-circle kick, no use of
# Fourier/Taylor coefficient formulas to calculate the integrals.
quad_cases=0
N=8192
for a, phase, omega in ((0.3+0.2j, 0.4, 0.7),(-0.2+0.45j,-0.3,0.24), (0.0+0j, 1.2,1.1), (0.6+0j, 0.9,-0.8)):
    points=[2*pi*(j+0.5)/N for j in range(N)]
    weights=[(1-abs(a)**2)/(N*abs(cmath.exp(1j*t)-a)**2) for t in points]
    assert abs(sum(weights)-1)<2e-13
    for rho in (0.014,0.007):
        H=rho*cmath.exp(1j*phase)
        M=[sum(w*cmath.exp(1j*m*(theta+omega+(H*cmath.exp(-1j*theta)).imag)) for theta,w in zip(points,weights)) for m in range(1,7)]
        for m in range(2,7):
            measured=(M[m-1]-M[0]**m)/(H**2)
            predicted=(m/8)*(1-abs(a)**2)*(a**(m-2))*cmath.exp(1j*m*omega)
            assert abs(measured-predicted) < 14*rho, (a,m,rho,measured,predicted)
            quad_cases+=1
print(f'VERIFY_OK exact_fraction_moment_cumulant_checks={count} direct_quadrature_checks={quad_cases} quadrature_nodes={N}')
