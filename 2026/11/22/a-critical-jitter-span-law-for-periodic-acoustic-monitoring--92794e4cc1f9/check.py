"""Reproduce the phase-width detection theorem with standard Python only.

This checker tests the exact integral against independent circular-interval
geometry and checks limiting laws numerically. It is supplementary to proof.
"""
from fractions import Fraction
from math import exp, log
from random import Random


def exact_miss(P, L, W, m):
    assert P > 0 and 0 < L < P and 0 < W <= P and int(m) == m and m >= 1
    a = max(0, W + L - P)
    b = min(W, L)
    rlo = 1 - a / W
    rhi = 1 - b / W
    return (abs(P - W - L) * rlo**m
            + abs(W - L) * rhi**m
            + 2 * W / (m + 1) * (rlo**(m + 1) - rhi**(m + 1))) / P


def hit_given_phase(theta, P, L, W):
    # Independent circular intersection construction, not the trapezoid law.
    size = 0.0
    for k in (-2, -1, 0, 1, 2):
        left, right = theta - L + k * P, theta + k * P
        size += max(0.0, min(W, right) - max(0.0, left))
    return size / W


def integrated_miss(P, L, W, m, cells=8000):
    return sum((1 - hit_given_phase(P*(j+.5)/cells, P, L, W))**m
               for j in range(cells)) / cells


def main():
    rng = Random(20241119)
    assertions = 0
    # Rational exact boundary checks before floating point is invoked.
    for P,L,W in [(Fraction(60),Fraction(10),Fraction(40)),
                  (Fraction(60),Fraction(10),Fraction(50)),
                  (Fraction(60),Fraction(10),Fraction(55)),
                  (Fraction(1),Fraction(3,10),Fraction(1)),
                  (Fraction(1),Fraction(7,10),Fraction(3,5))]:
        for m in [1,2,3,4,10,20]:
            Q=exact_miss(P,L,W,m)
            assert Fraction(0)<=Q<=Fraction(1)
            if m == 1:
                assert Q == 1-L/P
            assertions+=2
    # Check literal circular overlap numerically against integrated formula.
    for _ in range(200):
        P=1.0
        L=rng.uniform(.015,.985)
        W=rng.uniform(.015,1.0)
        m=rng.randint(1,14)
        exact=exact_miss(P,L,W,m)
        direct=integrated_miss(P,L,W,m,4000)
        assert abs(exact-direct)<2e-6,(L,W,m,exact,direct)
        assertions+=1
        assert exact + 1e-12 >= (1-L/P)**m
        assertions+=1
        if m>=2 and W < P - 1e-12:
            assert exact > (1-L/P)**m
            assertions+=1
    # Exact no-detection floor, critical 1/m law, and geometric regime.
    P,L=1.0,.2
    for W in [.15,.5,.799999]:
        floor=max(0,P-W-L)/P
        assert abs(exact_miss(P,L,W,10000)-floor-2*W/(P*10001))<1e-6
        assertions+=1
    W=P-L
    for m in [10000,40000]:
        assert abs(m*exact_miss(P,L,W,m)-2*W/P) < .001
        assertions+=1
    for W in [.81,.9,.99]:
        a=W+L-P
        r=(P-L)/W
        for m in [5000,8000]:
            # Rescale geometric terms to avoid underflow.
            b=min(W,L); h=1-b/W
            # Calculate Q_m/r**m directly from the exact trapezoid integral.
            ratio=(a+abs(W-L)*(h/r)**m
                   +2*W/(m+1)*(r-(h/r)**(m+1)*r))/P
            assert abs(ratio-a/P) < .002
            assertions+=1
    # Near-critical two-sided crossover, including opposite signs.
    for c in [-1.5,-.8,-.2,0.,.2,.7,1.5]:
        W0=1-L
        target=(2*W0+abs(c))*exp(-max(c,0)/W0)
        for m in [10000,40000]:
            W=W0+c/m
            assert abs(m*exact_miss(P,L,W,m)-target)<.002,(c,m)
            assertions+=1
    print(f'PASS: {assertions} analytic-formula, numerical and asymptotic assertions')


if __name__=='__main__':
    main()
