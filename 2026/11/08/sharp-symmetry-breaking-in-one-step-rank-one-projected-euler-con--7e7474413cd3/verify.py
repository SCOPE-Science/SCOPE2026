"""Reproducibility checks for the one-step rank-one Euler-retraction theorem.

Run with Python >= 3.9, standard library only: python verify.py
These finite tests supplement, but never replace, the analytic proof.
"""
import math
import random
from fractions import Fraction as Q


def bracket_delta(target, gamma):
    """Unique delta >=1 solving T_gamma(delta)=target, when target>1+gamma/2."""
    if not target > 1 + gamma / 2:
        raise ValueError("outside bifurcated phase")
    def T(d):
        return ((1 + gamma) * d**3 + d*d) / (d*d + 1)
    lo, hi = 1., max(2., target + 1.)
    while T(hi) < target:
        hi *= 2
    for _ in range(95):
        mid = (lo + hi)/2
        if T(mid) <= target:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2


def reduced_cost(u, target, gamma):
    d = math.hypot(1., 2*u)
    return target*target/2 + (1+d)/4 + (1+gamma)*u*u/2 - target*u*u/d


def full_cost(u, target, gamma):
    return (1+target*target)/2 + (1+gamma/2)*u*u


def mat2_frob2(x):
    return sum(v*v for row in x for v in row)


def mat2_det(x):
    return x[0][0]*x[1][1] - x[0][1]*x[1][0]


def exact_svd_checks():
    n = 0
    for i in range(0, 96):
        k = Q(30+i, 31)
        u = (k*k-1)/(4*k)
        d = (k*k+1)/(2*k)
        assert d*d == 1+4*u*u
        lp, lm = (1+d)/2, (1-d)/2
        assert lp > abs(lm)
        # Positive eigenprojector = (A-lm I)/d.
        A = ((Q(1), u), (u, Q(0)))
        P = (((Q(1)-lm)/d, u/d), (u/d, -lm/d))
        Y = tuple(tuple(lp*P[i][j] for j in range(2)) for i in range(2))
        R = tuple(tuple(A[i][j]-Y[i][j] for j in range(2)) for i in range(2))
        assert mat2_det(Y) == 0
        assert mat2_frob2(Y) == lp*lp
        assert mat2_frob2(R) == lm*lm
        assert Y[1][1] == u*u/d
        assert lp-abs(lm) == 1
        for q in (Q(-5),Q(-1),Q(0),Q(1),Q(2),Q(9,2)):
            for gamma in (Q(0),Q(1,2),Q(5)):
                explicit = q*q/2+(1+d)/4+(1+gamma)*u*u/2-q*u*u/d
                direct = (mat2_frob2(((Y[0][0],Y[0][1]),
                         (Y[1][0],Y[1][1]-q)))/2+gamma*u*u/2)
                assert explicit == direct
                n += 1
    return n


def phase_checks():
    random.seed(230417)
    n = 0
    for _ in range(2500):
        gamma = 12*random.random()
        critical = 1+gamma/2
        target = critical + 10**random.uniform(-3.0, 2.0)
        d = bracket_delta(target, gamma)
        ustar = math.sqrt((d*d-1)/4)
        jstar = reduced_cost(ustar,target,gamma)
        jzero = reduced_cost(0,target,gamma)
        assert jstar < jzero + 1e-12*max(1,jzero)
        for scale in (0.05,0.4,0.9,1.1,1.5,2.0,5.):
            assert reduced_cost(scale*ustar,target,gamma) + 5e-12*max(1,jstar) >= jstar
        assert full_cost(ustar,target,gamma)>full_cost(0,target,gamma)
        assert abs(reduced_cost(-ustar,target,gamma)-jstar)<1e-10*max(1,jstar)
        assert (1+gamma)*d**3 + (1-target)*d*d-target < 1e-8*max(1,target**3)
        # For target not exceeding the threshold, the cost increases at all tested amplitudes.
        low_target = critical - 10**random.uniform(-2.,1.)
        baseline=reduced_cost(0,low_target,gamma)
        for u in (.001,.03,.2,1.,4.,20.):
            assert reduced_cost(u,low_target,gamma) >= baseline-1e-11*max(1,baseline)
        n+=1
    return n


def asymptotic_checks():
    n=0
    for gamma in (0., .2, 1., 5.):
        tc=1+gamma/2
        for h in (0.0001,0.00001):
            target=tc+h
            d=bracket_delta(target,gamma)
            s=(d*d-1)/4
            expected=h/(3+2*gamma)
            assert abs(s/expected-1)<.003
            loss=reduced_cost(0,target,gamma)-reduced_cost(math.sqrt(s),target,gamma)
            expected_loss=h*h/(2*(3+2*gamma))
            assert abs(loss/expected_loss-1)<.01
            residual=(d-1)/2
            assert abs(residual/expected-1)<.003
            n+=1
    return n


if __name__ == '__main__':
    a=exact_svd_checks()
    b=phase_checks()
    c=asymptotic_checks()
    print(f'REPRODUCIBILITY_OK: {a} exact rational cost identities; {b} numerical phase cases; {c} critical asymptotics')
