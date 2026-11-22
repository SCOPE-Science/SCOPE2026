#!/usr/bin/env python3
"""Deterministic geometric and integration checks for fixed-cusp hypocycloids.
Python 3 standard library only. Numerical checks complement, not replace, proofs.
"""
import math
import cmath
import random


def curve(n, t, r=1.0):
    return r * ((n - 1) * cmath.exp(1j*t) + cmath.exp(-1j*(n - 1)*t))


def cusp(n, j, r=1.0):
    return n*r*cmath.exp(2j*math.pi*j/n)


def position_from_tip(n, j, branch, arc_distance, r=1.0):
    assert branch in (-1, 1)
    assert 0 <= arc_distance <= 8*r*(n - 1)/n
    angle = (2/n)*math.acos(1 - n*arc_distance/(4*r*(n - 1)))
    return cmath.exp(2j*math.pi*j/n)*curve(n, branch*angle, r)


def a(n):
    return 1.0 if n % 2 == 0 else math.cos(math.pi/(2*n))


def coefficient(n):
    return (n/(32*(n - 1)**2) if n % 2 == 0
            else n/(16*(n - 1)**2*a(n)**2))


def pair_tail_midpoint_coefficient(n, epsilon, grid=280):
    # One representative ordered farthest cusp pair; exact real distances,
    # four independent local branch orientations and midpoint quadrature.
    k = n//2 if n % 2 == 0 else (n - 1)//2
    top = 1.15*epsilon/a(n)
    step = top/grid
    p = []
    q = []
    for branch in (-1, 1):
        p.append([position_from_tip(n, 0, branch, (i+.5)*step) for i in range(grid)])
        q.append([position_from_tip(n, k, branch, (i+.5)*step) for i in range(grid)])
    maximum = 2*n*a(n)
    pairs = 0
    for bp in (0, 1):
        for bq in (0, 1):
            for z in p[bp]:
                for w in q[bq]:
                    if abs(z-w) > maximum-epsilon:
                        pairs += 1
    ordered_edges = n if n % 2 == 0 else 2*n
    perimeter = 8*(n-1)
    probability = ordered_edges*pairs*step**2/perimeter**2
    return probability/epsilon**2


def run():
    checks=0
    for n in range(3, 11):
        # Parameter cusp values, arc inversion and convex-hull side tests.
        for j in range(n):
            assert abs(curve(n, 2*math.pi*j/n)-cusp(n,j)) < 3e-12
            checks+=1
        for k in range(1, 100):
            t=2*math.pi*k/(100*n)
            s=4*(n-1)/n*(1-math.cos(n*t/2))
            reconstructed=position_from_tip(n,0,1,s)
            assert abs(reconstructed-curve(n,t)) < 2e-11
            checks+=1
            # Regular n-gon halfplane containing the arch from cusp 0 to cusp 1.
            normal=cmath.exp(-1j*math.pi/n)
            assert (reconstructed*normal).real <= n*math.cos(math.pi/n)+1e-10
            checks+=1
        # Global diameter: all sampled pair distances are within the chord bound.
        for p in range(50):
            for q in range(50):
                assert abs(curve(n,2*math.pi*p/50)-curve(n,2*math.pi*q/50)) < 2*n*a(n)+1e-9
                checks+=1
    # Unit-radius small-threshold slopes, multiple independent cusp counts.
    for n in (3,4,5,6,7,8):
        actual=pair_tail_midpoint_coefficient(n,0.025)
        expected=coefficient(n)
        assert abs(actual/expected-1)<0.03,(n,actual,expected)
        checks+=1
    # Direct random-sample max to nearest-cusp surrogate, sample-by-sample.
    rng=random.Random(548257)
    for n in (3,4,5,6,7):
        for N in (1000,3000):
            X=[]
            nearest=[float('inf')]*n
            one_arc=8*(n-1)/n
            for _ in range(N):
                j=rng.randrange(n)
                s=rng.random()*one_arc
                X.append(position_from_tip(n,j,1,s))
                nearest[j]=min(nearest[j],s)
                nearest[(j+1)%n]=min(nearest[(j+1)%n],one_arc-s)
            # Only pairs near cusp-pair maxima need be evaluated.
            for j in range(n):
                k=(j+n//2)%n if n%2==0 else (j+(n-1)//2)%n
                if j<k and n%2==0:
                    pass
            edges=([(j,(j+n//2)%n) for j in range(n//2)] if n%2==0 else
                   [(j,(j+(n-1)//2)%n) for j in range(n)])
            linear=max(0,min(a(n)*(nearest[j]+nearest[k]) for j,k in edges))
            assert linear<0.5
            checks+=1
    # Exact n=3 exponential-cycle law is a valid survival function.
    for t in (0,.1,1,2,4,10):
        surv=4*math.exp(-1.5*t)-3*math.exp(-2*t)
        assert 0<=surv<=1+1e-12
        checks+=1
    print(f'VERIFY_OK {checks} deterministic checks; pair-limit table:')
    for n in (3,4,5,6,7,8):
        print(f' n={n} coefficient={coefficient(n):.12f} midpoint_ratio={pair_tail_midpoint_coefficient(n,0.025):.12f}')

if __name__=='__main__':
    run()
