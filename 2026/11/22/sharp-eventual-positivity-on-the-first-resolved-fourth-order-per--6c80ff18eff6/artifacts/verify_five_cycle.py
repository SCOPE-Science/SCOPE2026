"""Reproduce the spectral and entrywise checks for the five-site heat stencil."""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def exact_checks():
    S = sp.zeros(5)
    for j in range(5):
        S[j, (j + 1) % 5] = 1
    I = sp.eye(5)
    D = S + S.T - 2 * I
    Q = D - D**2 / 12
    a = (75 - 17 * sp.sqrt(5)) / 24
    b = (75 + 17 * sp.sqrt(5)) / 24
    phi = (1 + sp.sqrt(5)) / 2
    assert Q == sp.Rational(-5, 2) * I + sp.Rational(4, 3) * (S + S.T) - sp.Rational(1, 12) * (S**2 + (S.T)**2)
    assert Q * sp.ones(5, 1) == sp.zeros(5, 1)
    assert ((Q + a * I) * (Q + b * I) * Q).applyfunc(sp.simplify) == sp.zeros(5)
    assert Q.eigenvals() == {sp.Integer(0): 1, -a: 2, -b: 2}
    P0 = sp.ones(5, 5) / 5
    Pa = -Q * (Q + b*I) / (a*(b-a))
    Pb = Q * (Q + a*I) / (b*(b-a))
    assert sp.simplify(P0 + Pa + Pb - I) == sp.zeros(5)
    assert sp.simplify(P0*Pa) == sp.zeros(5)
    assert sp.simplify(P0*Pb) == sp.zeros(5)
    assert sp.simplify(Pa*Pb) == sp.zeros(5)
    assert sp.simplify(Pa**2 - Pa) == sp.zeros(5)
    assert sp.simplify(Pb**2 - Pb) == sp.zeros(5)
    assert sp.simplify(Pa[0, 0] - sp.Rational(2, 5)) == 0
    assert sp.simplify(Pb[0, 0] - sp.Rational(2, 5)) == 0
    assert sp.simplify(Pa[0, 1] - 1/(5*phi)) == 0
    assert sp.simplify(Pb[0, 1] + phi/5) == 0
    assert sp.simplify(Pa[0, 2] + phi/5) == 0
    assert sp.simplify(Pb[0, 2] - 1/(5*phi)) == 0
    assert sp.simplify(phi*a - b/phi + sp.Rational(5,12)) == 0
    assert sp.simplify(b-a-17*sp.sqrt(5)/12) == 0
    return Q, a, b, phi, (P0, Pa, Pb)


def numerical_checks(Q, a, b, phi, projectors):
    mp.mp.dps = 70
    av = mp.mpf(str(sp.N(a, 75)))
    bv = mp.mpf(str(sp.N(b, 75)))
    pv = mp.mpf(str(sp.N(phi, 75)))
    ff = lambda t: 1-pv*mp.exp(-av*t)+mp.exp(-bv*t)/pv
    tm = mp.log(bv/(pv*pv*av))/(bv-av)
    assert tm > 0
    assert ff(tm) < 0
    tau = mp.findroot(ff, (mp.mpf('0.08'),mp.mpf('0.14')))
    assert tau > tm and abs(ff(tau)) < mp.mpf('1e-60')
    assert mp.mpf('.10307871') < tau < mp.mpf('.10307872')
    Qm = mp.matrix([[mp.mpf(str(sp.N(Q[i,j],50))) for j in range(5)] for i in range(5)])
    projectors_m = [mp.matrix([[mp.mpf(str(sp.N(P[i,j],70))) for j in range(5)] for i in range(5)]) for P in projectors]
    count = 0
    for n in range(1, 221):
        t = mp.mpf(n)/1000
        E = mp.expm(t*Qm)
        F = projectors_m[0]+mp.exp(-av*t)*projectors_m[1]+mp.exp(-bv*t)*projectors_m[2]
        assert max(abs(E[i,j]-F[i,j]) for i in range(5) for j in range(5)) < mp.mpf('1e-44')
        assert abs(sum(E[0,j] for j in range(5))-1) < mp.mpf('1e-44')
        assert min(E[0,0],E[0,1],E[0,4]) > 0
        if t < tau:
            assert E[0,2] < 0 and E[0,3] < 0
        else:
            assert E[0,2] > 0 and E[0,3] > 0
        count += 25 + 5 + 1 + 2
    E = mp.expm(tau*Qm)
    assert max(abs(E[0,j]) for j in (2,3)) < mp.mpf('1e-44')
    assert all(E[0,j]>0 for j in (0,1,4))
    return tau, tm, count

if __name__ == '__main__':
    Q,a,b,phi,projectors=exact_checks()
    tau,tm,count=numerical_checks(Q,a,b,phi,projectors)
    print('PASS: exact 5-cycle stencil, projectors, algebraic derivative and Fourier coefficients')
    print(f'PASS: {count} high-precision independent matrix exponential/row-sum/sign comparisons')
    print('first minimum (dimensionless):',mp.nstr(tm,35))
    print('sharp restoration time (dimensionless):',mp.nstr(tau,55))
    print('strict negativity holds only at cyclic distance two before restoration')
