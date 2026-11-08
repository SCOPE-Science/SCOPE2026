#!/usr/bin/env python3
"""Reproduce algebraic identities and finite-sample checks for a randomized Ritz pencil.

No third-party Python dependencies are required. Statistical assertions compare a
reproducible sample with proved distribution formulas; they are not proofs of tails.
"""
import cmath
import math
import random


def det(x, y):
    return x[0]*y[1]-x[1]*y[0]


def pencil_coeff(a, b, c, theta):
    sn, cs = math.sin(theta), math.cos(theta)
    return (sn*det(c,b), cs*det(a,b), cs*det(a,c)+sn*det(b,c))


def near_zero_root(a0, a1, a2):
    disc = cmath.sqrt(a1*a1-4*a2*a0)
    denominator = a1+disc if abs(a1+disc)>=abs(a1-disc) else a1-disc
    return -2*a0/denominator


def slope_value(a, b, c):
    return -det(c,b)/det(a,b)


def slope_vector(a, b, c):
    return -det(a,c)/det(a,b)


def gaussian_vector(rng, complex_field):
    if complex_field:
        return [(rng.gauss(0,1)+1j*rng.gauss(0,1))/math.sqrt(2) for _ in range(2)]
    return [rng.gauss(0,1) for _ in range(2)]


def close(x, y, tol=1e-9):
    assert abs(x-y)<=tol*(1+abs(y)), (x,y)


def algebraic_tests():
    samples = [
        ([1,2],[3,5],[7,11]),
        ([1+1j,2-1j],[3+2j,1-4j],[2-3j,5+1j]),
        ([2,1],[1,-1],[4,5]),
    ]
    checks=0
    for a,b,c in samples:
        assert abs(det(a,b))>0.01
        for theta in [0.01,0.003,0.001,0.0001]:
            sn,cs=math.sin(theta),math.cos(theta)
            a0,a1,a2=pencil_coeff(a,b,c,theta)
            mu=near_zero_root(a0,a1,a2)
            close(a0+a1*mu+a2*mu*mu,0,1e-9)
            lhs=[-sn*c[j]-mu*(cs*a[j]+sn*b[j]) for j in range(2)]
            rhs=[-b[j]-mu*c[j] for j in range(2)]
            j=max(range(2),key=lambda k:abs(rhs[k]))
            z=-lhs[j]/rhs[j]
            close(lhs[0]+z*rhs[0],0,1e-9)
            close(lhs[1]+z*rhs[1],0,1e-9)
            if theta<=0.0001:
                assert abs(mu/theta-slope_value(a,b,c))<0.03
                assert abs(z/theta-slope_vector(a,b,c))<0.03
            # The sine-angle and Rayleigh-quotient identities are exact.
            sin_sq=(sn*sn+abs(z)**2)/(1+abs(z)**2)
            w1=(sn+z)/math.sqrt(2)
            w3=(sn-z)/math.sqrt(2)
            norm=cs*cs+abs(w1)**2+abs(w3)**2
            close(norm,1+abs(z)**2)
            close(sin_sq,1-cs*cs/norm)
            close((abs(w3)**2-abs(w1)**2)/norm,
                  -2*sn*z.real/(1+abs(z)**2))
            checks+=8
    return checks


def distribution_tests():
    rng=random.Random(260401037)
    checks=0
    for complex_field in [False,True]:
        n=24000
        z_abs=[]; infl=[]; ref=[]
        for _ in range(n):
            a,b,c=(gaussian_vector(rng,complex_field) for _ in range(3))
            z=slope_vector(a,b,c)
            z_abs.append(abs(slope_value(a,b,c)))
            infl.append(math.sqrt(1+abs(z)**2))
            ref.append(abs(2*z.real))
        for t in [1,2,4]:
            if complex_field:
                tail=1/(1+t*t)
                infl_tail=1/(t*t)
                ref_tail=1-t/math.sqrt(t*t+4)
            else:
                tail=2/math.pi*math.atan(1/t)
                infl_tail=2/math.pi*math.asin(1/t)
                ref_tail=2/math.pi*math.atan(2/t)
            measured=sum(x>t for x in z_abs)/n
            measured_infl=sum(x>t for x in infl)/n
            measured_ref=sum(x>t for x in ref)/n
            assert abs(measured-tail)<0.025,(complex_field,t,measured,tail)
            assert abs(measured_infl-infl_tail)<0.025
            assert abs(measured_ref-ref_tail)<0.025
            checks+=3
    return checks


if __name__=='__main__':
    a=algebraic_tests()
    b=distribution_tests()
    print(f'PASS: {a} algebraic/numerical checks; {b} distribution checks')
