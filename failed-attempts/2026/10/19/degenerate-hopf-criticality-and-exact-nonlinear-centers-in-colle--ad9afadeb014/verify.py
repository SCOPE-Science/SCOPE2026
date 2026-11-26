#!/usr/bin/env python3
"""Reproducible symbolic and numerical checks for a binomial collective-risk game.

Requires Python 3, sympy, scipy. Execute: python verify.py
Exact SymPy checks cover six rational-parameter examples; the proof for all
admissible group sizes is in RESULT.md. Numerical trajectories are ancillary.
"""
from math import comb, pi, sqrt
import sympy as S
from scipy.integrate import solve_ivp

x, r = S.symbols('x r', real=True)

def fields(N, M, feedback):
    assert 1 < M < N
    n, m, k = N-1, M-1, N-M
    p = S.Rational(m, n)
    c, b, eps = S.Rational(1, 10), S.Integer(1), S.Rational(1, 10)
    P = b*S.binomial(n, m)*x**m*(1-x)**k
    r0 = S.factor(c/P.subs(x, p))
    assert 0 < r0 < 1
    if feedback == 'linear':
        D = S.Rational(m, k)*(1-x)-x
    elif feedback == 'sigmoid':
        D = -S.tanh(S.Rational(3, 2)*(x-p))
    else:
        raise ValueError(feedback)
    F = S.Matrix([x*(1-x)*(P*r-c)/eps, r*(1-r)*D])
    return F, p, r0, c, b, eps

def complex_lyapunov_check(N, M, feedback):
    F, p, r0, c, bvalue, eps = fields(N, M, feedback)
    vars_ = [x, r]
    J = S.simplify(F.jacobian(vars_).subs({x:p, r:r0}))
    a, b = J[0, 1], -J[1, 0]
    assert S.simplify(J[0,0]) == 0 and J[1,1] == 0
    assert a.is_positive and b.is_positive
    omega = S.sqrt(a*b)
    q = S.Matrix([1, S.I*omega/a])
    dual = S.Matrix([S.Rational(1,2), S.I*omega/(2*b)])
    assert S.simplify(J*q-S.I*omega*q) == S.zeros(2,1)
    assert S.simplify((S.conjugate(dual).T*q)[0]-1) == 0
    subs = {x:p, r:r0}
    second = [[[S.diff(F[i], vars_[j], vars_[k]).subs(subs)
             for k in range(2)] for j in range(2)] for i in range(2)]
    third = [[[[S.diff(F[i],vars_[j],vars_[k],vars_[h]).subs(subs)
             for h in range(2)] for k in range(2)] for j in range(2)] for i in range(2)]
    def B(v,w):
        return S.Matrix([sum(second[i][j][k]*v[j]*w[k]
            for j in range(2) for k in range(2)) for i in range(2)])
    def C(v,w,z):
        return S.Matrix([sum(third[i][j][k][h]*v[j]*w[k]*z[h]
            for j in range(2) for k in range(2) for h in range(2)) for i in range(2)])
    qc=S.conjugate(q)
    numerator=C(q,q,qc)-2*B(q,J.inv()*B(q,qc))+B(qc,(2*S.I*omega*S.eye(2)-J).inv()*B(q,q))
    G21=S.simplify((S.conjugate(dual).T*numerator)[0])
    first=S.simplify(S.re(S.expand_complex(G21))/(2*omega))
    assert first == 0, (N,M,feedback,first)
    print(f'normal form: N={N}, M={M}, feedback={feedback}, l1=0 (exact), omega^2={S.factor(omega**2)}')
    if N == 5 and M == 3:
        R = {x:1-x}
        assert S.simplify((F[0].subs(R)-F[0]).expand()) == 0
        assert S.simplify((F[1].subs(R)+F[1]).expand()) == 0
        omega_f=float(omega)
        p_f,r0_f=float(p),float(r0)
        system=S.lambdify((x,r),F,'numpy')
        def fun(t,y):
            z=system(*y)
            return float(z[0,0]),float(z[1,0])
        def section(t,y):
            return y[0]-p_f
        section.terminal=False
        section.direction=0
        for delta in [0.02,0.04]:
            y0=(p_f,r0_f+delta)
            sol=solve_ivp(fun,(0,7*pi/omega_f),y0,events=section,
                rtol=1e-12,atol=1e-13,max_step=0.04)
            nonzero=[(tt,yy) for tt,yy in zip(sol.t_events[0],sol.y_events[0]) if tt>1e-7]
            assert len(nonzero)>=2,(feedback,delta,nonzero)
            t_return,y_return=nonzero[1]
            assert abs(y_return[0]-p_f)<2e-11
            assert abs(y_return[1]-(r0_f+delta))<2e-9,(feedback,delta,t_return,y_return)
            print(f'  reversible periodic check: delta={delta}, period={t_return:.9f}, error={abs(y_return[1]-(r0_f+delta)):.3g}')

if __name__=='__main__':
    for N,M in ((5,3),(6,3),(8,5)):
        for feedback in ('linear','sigmoid'):
            complex_lyapunov_check(N,M,feedback)
    print('PASS: six exact normal-form checks and four periodic trajectory returns')
