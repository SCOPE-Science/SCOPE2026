"""Reproduce the finite numerical checks accompanying the sharp right-simplex angle theorem.
Uses only the Python 3 standard library. Numerical tests do not replace the proof.
"""
import math
import random
from math import sqrt, atan


def simpson(f, a, b, n=2000):
    assert n % 2 == 0
    h = (b - a) / n
    return (f(a) + f(b) + 4 * sum(f(a + h * k) for k in range(1, n, 2))
            + 2 * sum(f(a + h * k) for k in range(2, n, 2))) * h / 3


def C(n):
    assert n >= 2
    return n*(n-1)*2**(n/2)*simpson(
        lambda u: (1-u)**(n-2)/(1+u*u)**(n/2), 0, 1)


def apex_angle_3(legs, i):
    t = legs[i]
    others = [legs[j] for j in range(3) if j != i]
    numerator = math.prod(others)
    denominator = math.prod(t + math.hypot(t, b) for b in others)
    return 2*atan(numerator/denominator)


def mu(legs):
    a = sorted(legs, reverse=True)
    return math.prod(legs) / (math.factorial(len(legs)) * (a[0]**2 + a[1]**2)**(len(legs)/2))


def integral_apex_3(legs, i):
    t = legs[i]
    b,c = [legs[j] for j in range(3) if j != i]
    # double integral over triangle {z/b_t+w/c_t <= 1}, gnomonic integrand
    r, s = b/t, c/t
    def outer(u):
        return r*s*(1-u)*simpson(
            lambda v: (1 + (r*u)**2 + (s*(1-u)*v)**2)**(-1.5), 0, 1, 120)
    return simpson(outer,0,1,120)


def ratio_simplex_sample(legs, draws=6500, seed=0):
    # Integration over uniform simplex via sorted gaps of independent uniforms.
    n = len(legs)
    first = max(legs)
    j = legs.index(first)
    r = [b/first for k,b in enumerate(legs) if k != j]
    R=max(r)
    rng = random.Random(seed)
    ss=0.0
    for _ in range(draws):
        cuts = sorted([0.0,1.0]+[rng.random() for _ in range(n-1)])
        U=[cuts[i+1]-cuts[i] for i in range(n-1)]
        ss += (1+sum((a*x)**2 for a,x in zip(r,U)))**(-n/2)
    return n*(1+R*R)**(n/2)*ss/draws


def run():
    checks = 0
    for n in range(2, 13):
        cn=C(n)
        assert n < cn <= n*2**(n/2)
        assert 1-1/(n+1)-1e-12 < cn/(n*2**(n/2)) <= 1+1e-12
        checks+=2
    assert abs(C(2)-math.pi)<2e-8
    assert abs(C(3)-12*(2-sqrt(2)))<2e-8
    checks+=2
    examples = [(1,1,1),(1,2,3),(.01,1,.5),(3,3,.02),(.7,1.1,4),(.2,.2,.2),(2,4,4)]
    for legs in examples:
        ag=[apex_angle_3(legs,i) for i in range(3)]
        for i in range(3):
            if legs[i] == max(legs):
                assert abs(ag[i]-integral_apex_3(legs,i)) < 1e-8, (legs,i)
            for j in range(3):
                assert (ag[i] < ag[j]) == (legs[i] > legs[j]) if legs[i] != legs[j] else abs(ag[i]-ag[j])<1e-14
                checks+=1
            checks+=1
        omega=min(ag)
        ratio=omega/mu(legs)
        assert 3 < ratio <= C(3)+1e-8, (legs,ratio)
        checks+=1
    for n in range(2,7):
        rng=random.Random(5233+n)
        for k in range(12):
            legs=[math.exp(rng.uniform(-2,2)) for _ in range(n)]
            q=ratio_simplex_sample(legs,draws=2000,seed=k+304*n)
            assert n < q < C(n) + .045, (n,legs,q,C(n))
            checks+=1
    # Degenerating extremal families; test ratios using exact n=3 angle.
    for eps in (1e-2,1e-3,1e-4):
        low=(apex_angle_3((1,eps,eps),0)/mu((1,eps,eps)))
        high=(apex_angle_3((1,1,eps),0)/mu((1,1,eps)))
        assert abs(low-3)<3*eps*eps + 0.002, (eps,low)
        assert abs(high-C(3)) < 15*eps, (eps,high)
        checks+=2
    print(f'REPRODUCIBLE_CHECKS_OK {checks}')
    print(f'C2={C(2):.15g}, C3={C(3):.15g}, C4={C(4):.15g}')

if __name__ == '__main__':
    run()
