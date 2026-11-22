#!/usr/bin/env python3
"""Numerical checks for harmonic-copula information and directional dependence.
Analytical identities in the theorem constitute the proof; checks are independent quadratures.
No network access or third-party packages required.
"""
import math

PI = math.pi


def kl_series(theta, terms=120):
    return sum(theta**(2*j) * (math.comb(2*j, j) / 4**j)**2 /
               ((2*j)*(2*j-1)) for j in range(1, terms+1))


def midpoint_integrals(m, n, theta, N=360):
    total_kl = total_tv = total_chi = xi_vu = xi_uv = 0.0
    for i in range(N):
        u = (i + 0.5)/N
        cu, su = math.cos(m*PI*u), math.sin(m*PI*u)
        for k in range(N):
            v = (k + 0.5)/N
            cv, sv = math.cos(n*PI*v), math.sin(n*PI*v)
            density = 1.0 + theta*cu*cv
            total_kl += density * math.log(density)
            total_tv += abs(density - 1)
            total_chi += (density - 1)**2
            xi_vu += (theta * cu * sv / (n*PI))**2
            xi_uv += (theta * cv * su / (m*PI))**2
    divisor = N*N
    return total_kl/divisor, total_tv/(2*divisor), total_chi/divisor, 6*xi_vu/divisor, 6*xi_uv/divisor


def check(m, n, theta):
    assert 0 < theta < 1 and m >= 1 and n >= 1
    kl, tv, chi, xvu, xuv = midpoint_integrals(m,n,theta)
    target = (
        kl_series(theta), 2*theta/PI**2, theta**2/4,
        3*theta**2/(2*n*n*PI**2), 3*theta**2/(2*m*m*PI**2),
    )
    obs = (kl,tv,chi,xvu,xuv)
    for label, actual, expected, tol in zip(
        ('KL', 'TV', 'chi-square', 'xi(V|U)', 'xi(U|V)'),
        obs,target,(0.00005,0.0001,0.00005,0.00005,0.00005)
    ):
        assert abs(actual-expected) < tol, (m,n,label,actual,expected)
    return obs


def main():
    theta = 0.5
    targets = []
    for mn in ((1,1),(2,2),(2,4),(4,2),(4,6),(12,8)):
        vals = check(*mn,theta)
        targets.append(vals)
        print(f'm={mn[0]}, n={mn[1]}: KL={vals[0]:.11f}, TV={vals[1]:.11f}, chi2={vals[2]:.11f}, xiVU={vals[3]:.11f}, xiUV={vals[4]:.11f}')
    # The four even-even cases show equal information and different rank sensitivities.
    for a,b in ((1,2),(2,3),(3,4),(4,5)):
        for idx in (0,1,2):
            assert abs(targets[a][idx]-targets[b][idx]) < 0.00005
    assert kl_series(theta) > 0
    assert abs(kl_series(theta, 60)-kl_series(theta, 120)) < 1e-14
    print('PASS: six frequency cases, five integral identities each, shared information and KL-series convergence')


if __name__ == '__main__':
    main()
