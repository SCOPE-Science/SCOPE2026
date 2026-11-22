#!/usr/bin/env python3
"""Independent finite diagnostics for Fejer-power Fourier sign and tail formulas.

Only the Python standard library is needed. This is not a proof of the infinite theorem.
"""
import math

PI = math.pi


def exact_integer_coefficients(n, q):
    # F_n(theta) has coefficients (n-|k|)/n, |k|<n.
    coeff = {k: (n-abs(k))/n for k in range(-(n-1), n)}
    cur = {0: 1.0}
    for _ in range(q):
        nxt = {}
        for a, ca in cur.items():
            for b, cb in coeff.items():
                nxt[a+b] = nxt.get(a+b, 0.0) + ca*cb
        cur = nxt
    return cur


def A(n, gamma, residue):
    return sum((n/(4*math.sin(PI*j/n)**2))**gamma *
               math.cos(2*PI*residue*j/n) for j in range(1, n))


def predicted_lead(n, gamma, m):
    return -math.gamma(2*gamma+1) * math.sin(PI*gamma)/PI * A(n,gamma,m%n) / m**(2*gamma+1)


def trapezoidal_coeff(n, gamma, m, points=32768):
    total = 0.0
    for j in range(points):
        x = 2*PI*j/points
        if j == 0:
            value = n**gamma
        else:
            den = math.sin(x/2)
            value = (math.sin(n*x/2)**2 / (n*den*den))**gamma
        total += value*math.cos(m*x)
    return total/points


def exact_n2_noninteger(gamma, m):
    # Gamma quotient, rearranged by reflection so that all gamma calls are positive.
    mag = math.exp(-gamma*math.log(2)+math.lgamma(2*gamma+1)-math.log(PI)
                   +math.lgamma(m-gamma)-math.lgamma(m+gamma+1))
    return (-1)**(m+1) * math.sin(PI*gamma) * mag


def run():
    checks = 0
    for n in range(2, 9):
        for q in range(1, 5):
            c = exact_integer_coefficients(n, q)
            assert len(c) == 2*q*(n-1)+1
            assert all(x >= 0.0 for x in c.values())
            assert abs(sum(c.values()) - n**q) < 1e-7 * n**q
            checks += 3
    for n in range(2, 13):
        for gamma in (0.25, 0.5, 0.8, 1.4, 2.25):
            av = [A(n,gamma,r) for r in range(n)]
            assert av[0] > 0
            assert min(av) < 0
            assert abs(sum(av)) < 1e-10 * sum(abs(x) for x in av)
            checks += 3
    for gamma in (0.25, 0.5, 1.4, 2.25):
        for m in (30, 31, 60, 61):
            exact = exact_n2_noninteger(gamma, m)
            quad = trapezoidal_coeff(2, gamma, m)
            assert abs(quad-exact) < 0.001 * max(abs(exact), 1e-10), (gamma,m,quad,exact)
            lead = predicted_lead(2,gamma,m)
            if abs(lead)>1e-14:
                assert abs(exact/lead-1)<0.06, (gamma,m,exact,lead)
                checks += 1
            checks += 1
    for n,gamma in ((3,.5),(3,1.5),(4,.4),(5,.5)):
        for m in (72, 73, 74, 75):
            if abs(A(n,gamma,m%n)) < 1e-10:
                continue
            approx = trapezoidal_coeff(n,gamma,m)
            lead = predicted_lead(n,gamma,m)
            assert approx*lead>0, (n,gamma,m,approx,lead)
            assert abs(approx/lead-1)<0.12, (n,gamma,m,approx,lead)
            checks += 2
    print(f'PASS: {checks} finite diagnostics; no infinite conclusion inferred')

if __name__=='__main__':
    run()
