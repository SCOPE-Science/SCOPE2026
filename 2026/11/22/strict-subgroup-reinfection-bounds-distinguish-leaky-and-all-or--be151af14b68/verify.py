#!/usr/bin/env python3
"""Numerical consistency checks for reinfection-allocation inequalities.

Uses only Python standard library; all universal claims are proved in RESULT.md,
not inferred from finite simulations. Finite infectious seeds approximate the
vanishing-seed epidemic branch.
"""
import math


def solve(reproduction, coverage, vaccinated_primary, postinfection,
          seed=1e-8, dt=0.02, time_end=320.0):
    # compartments S_U,S_V,I_U,I_V,R_U,R_V,
    # cumulative primary_U,V, cumulative repeat_U,V
    y = [1.0 - coverage - seed/2, coverage - seed/2,
         seed/2, seed/2, 0., 0., 0., 0., 0., 0.]
    def rhs(y):
        su, sv, iu, iv, ru, rv, pu, pv, qu, qv = y
        force = reproduction * (iu + iv)
        pu_rate = force * su
        pv_rate = force * vaccinated_primary * sv
        qu_rate = force * postinfection * ru
        qv_rate = force * postinfection * rv
        return [-pu_rate, -pv_rate,
                pu_rate + qu_rate - iu, pv_rate + qv_rate - iv,
                iu - qu_rate, iv - qv_rate,
                pu_rate, pv_rate, qu_rate, qv_rate]
    n = round(time_end / dt)
    for _ in range(n):
        k1 = rhs(y)
        k2 = rhs([u + dt*v/2 for u,v in zip(y,k1)])
        k3 = rhs([u + dt*v/2 for u,v in zip(y,k2)])
        k4 = rhs([u + dt*v for u,v in zip(y,k3)])
        y = [u + dt*(v1+2*v2+2*v3+v4)/6
             for u,v1,v2,v3,v4 in zip(y,k1,k2,k3,k4)]
    su, sv, iu, iv, ru, rv, pu, pv, qu, qv = y
    assert abs(su + ru + iu - (1-coverage)) < 3e-8
    assert abs(sv + rv + iv - coverage) < 3e-8
    assert abs(iu + iv) < 5e-8
    h = math.log((1.0-coverage-seed/2)/su)
    rho = -math.expm1(-vaccinated_primary*h) / -math.expm1(-h)
    qratio = (qv/coverage)/(qu/(1-coverage))
    repeated = qu+qv
    lower = coverage*vaccinated_primary / (1-coverage+coverage*vaccinated_primary) * repeated
    upper = coverage*rho / (1-coverage+coverage*rho) * repeated
    assert 0 < postinfection <= vaccinated_primary < 1
    assert reproduction*postinfection < 1
    assert reproduction*(1-coverage+coverage*vaccinated_primary)>1
    assert vaccinated_primary < qratio < rho < 1
    assert qv/pv < qu/pu
    assert lower < qv < upper
    # Unlike a simulation, the paper's total-count identity is exact in the limit seed->0.
    source_total = h/reproduction - ((1-coverage)-su + coverage-sv)
    assert abs(repeated - source_total) <= seed*1.01
    return (qratio, rho, qu, qv, lower, upper, h)

if __name__ == '__main__':
    cases=[(2,.5,.5,.25), (1.8,.25,.8,.3), (2.1,.6,.65,.15),
           (1.5,.3,.9,.25), (3,.4,.9,.2), (1.5,.8,.9,.3)]
    for a,b,c,d in cases:
        x=solve(a,b,c,d)
        print('R0=%s c=%s theta=%s phi=%s ratio=%.9f rho=%.9f QU=%.9f QV=%.9f bounds=(%.9f, %.9f) H=%.9f' % ((a,b,c,d)+x))
    print('PASS: six parameter scenarios, exact algebraic residual and strict bounds.')
