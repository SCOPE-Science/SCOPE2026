#!/usr/bin/env python3
"""Reproduce the exact stationary first-absorption-time fluctuation threshold.

This program needs only the Python standard library.
It implements two independent calculations: a Taylor expansion of the
absorption-time transform, and a backwards-generator moment boundary
calculation. All main comparisons use exact rational arithmetic.
"""
from fractions import Fraction as F
from random import Random

def core(a, k, g):
    a, k, g = F(a), F(k), F(g)
    if min(a,k,g) < 0 or k == 0:
        raise ValueError("Require a,g >= 0 and k > 0")
    B = 1+k+2*g
    H = B+k*a
    C = 1+(k+2*g)/3
    E = 1+k/2
    A2 = k*a*a/6+C*a+E
    mean = H/k
    moment2_transform = 2*(mean*mean - A2/k)
    variance = moment2_transform-mean*mean
    cv2 = variance/(mean*mean)
    Q = C*B-2*k*E
    optimum = F(3)*Q/(2*k)
    return dict(B=B,H=H,C=C,E=E,A2=A2,mean=mean,
                moment2_transform=moment2_transform,
                variance=variance,cv2=cv2,Q=Q,optimum=optimum)

def second_moment_from_backward_equations(a,k,g):
    """Independent solution of generator moment ODE with wall condition.

    The space is [-1,1], speed 1. For moment n=1:
      G1(x)=-x, M1(x)=m-a*x*x.
    For n=2:
      G2(x)=-2*m*x+(2*a/3)*x**3,
      M2(x)=m2+(1-2*a*m)*x*x+(a*a/3)*x**4.
    At x=1, outward moment is the bound-wall moment:
      (k+g)*(M2+G2)=2*m1_bound+g*(M2-G2).
    """
    a,k,g=F(a),F(k),F(g)
    m=a+1+(2*g+1)/k
    bound_first=(2*g+1)/k
    G2_at_right=-2*m+2*a/3
    other_in_M2=1-2*a*m+a*a/3
    return (2*bound_first-(k+2*g)*G2_at_right)/k-other_in_M2

def phase_derivative_numerator(a,k,g):
    a,k,g=F(a),F(k),F(g)
    B=1+k+2*g
    C=1+(k+2*g)/3
    E=1+k/2
    A2=k*a*a/6+C*a+E
    # Quotient rule applied directly, without using the reduced Q identity.
    return (k*a/3+C)*(B+k*a)-2*k*A2

def run():
    cases=0
    vals=[F(1,10), F(1,2),F(1),F(2), F(7,2),F(10)]
    for k in vals:
        for g in [F(0),F(1,10),F(1),F(5)]:
            for a in [F(0),F(1,10),F(1),F(2),F(15,2),F(20)]:
                t=core(a,k,g)
                assert t['moment2_transform']==second_moment_from_backward_equations(a,k,g)
                assert t['variance']>=0
                assert t['Q'] == F(4*g*g+4*g*k+8*g-2*k*k-2*k+3,3)
                assert phase_derivative_numerator(a,k,g)==t['Q']-2*k*a/3
                cases += 1
            t0=core(0,k,g)
            astar=t0['optimum']
            if astar>0:
                p=core(astar,k,g)
                assert p['cv2']<t0['cv2']
                assert p['cv2']<F(2,3)
                assert p['cv2']==F(2,3)-F(2,3)/p['H']
                assert core(astar/2,k,g)['cv2']>p['cv2']
                assert core(2*astar,k,g)['cv2']>p['cv2']
            else:
                assert core(1,k,g)['cv2']>t0['cv2']
                assert core(10,k,g)['cv2']>core(1,k,g)['cv2']
    # Fully exact advertised point.
    p=core(F(15,2),1,1)
    assert p['Q']==5 and p['optimum']==F(15,2)
    assert p['mean']==F(23,2)
    assert p['cv2']==F(14,23)
    assert p['variance']==F(161,2)
    # Regression tests at random rational parameters:
    rng=Random(410351)
    for _ in range(150):
        a=F(rng.randint(0,75),rng.randint(1,15))
        k=F(rng.randint(1,75),rng.randint(1,15))
        g=F(rng.randint(0,75),rng.randint(1,15))
        p=core(a,k,g)
        assert p['moment2_transform']==second_moment_from_backward_equations(a,k,g)
        assert phase_derivative_numerator(a,k,g)==p['Q']-F(2,3)*k*a
        assert p['cv2']>0
        cases += 1
    print(f"PASS: {cases} exact-rational moment and slope comparisons; distinct backward-generator calculation")
    print(f"Example k=g=1: a*=15/2, mean=23/2, variance=161/2, CV^2=14/23")
    print("Independent scientific or computer-assisted proof certification not asserted.")
if __name__ == '__main__':
    run()
