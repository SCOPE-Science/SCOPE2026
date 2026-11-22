#!/usr/bin/env python3
"""Numerical checks for the Airy variational solution of a quadratic flow.

Requires mpmath>=1.3. This is a reproducibility check, not a substitute
for the analytic proof or a test of nonlinear perturbed trajectories.
"""
import mpmath as mp

mp.mp.dps = 65


def ingredients(a, b, c, z0):
    a, b, c, z0 = map(mp.mpf, (a, b, c, z0))
    h = (a+c)/2
    q = mp.root(a*b, 3)
    star = (a*(c+z0)-h*h)/(a*b)
    return a, b, c, z0, h, q, star


def solution(data, t, kind):
    a, b, c, z0, h, q, star = data
    t = mp.mpf(t)
    s = q*(t-star)
    if kind == "Ai":
        v = mp.airyai(s); dv = mp.airyai(s, 1)
    else:
        v = mp.airybi(s); dv = mp.airybi(s, 1)
    x = mp.exp(-h*t)*v
    y = mp.exp(-h*t)*((1-h/a)*v+(q/a)*dv)
    return x, y


def log_norm(data, t, kind):
    x, y = solution(data, t, kind)
    return mp.log(mp.sqrt(x*x+y*y))


def close(v, w, tol):
    assert abs(v-w) <= tol*(1+abs(v)+abs(w)), (v, w)


# Direct substitution in the source variational ODE and Wronskian.
for params in [(12,100,10,0),(2,3,4,1),('0.5','0.7','1.5',7)]:
    data = ingredients(*params)
    a,b,c,z0,h,q,star = data
    for t in [mp.mpf(0), mp.mpf(1), mp.mpf(3)]:
        for kind in ["Ai", "Bi"]:
            x, y = solution(data, t, kind)
            xp = mp.diff(lambda t1: solution(data, t1, kind)[0], t)
            yp = mp.diff(lambda t1: solution(data, t1, kind)[1], t)
            close(xp, a*(y-x), mp.mpf('1e-35'))
            close(yp, -(z0-b*t)*x-c*y, mp.mpf('1e-35'))
        s = q*(t-star)
        close(mp.airyai(s)*mp.airybi(s,1)-mp.airyai(s,1)*mp.airybi(s),
              1/mp.pi, mp.mpf('1e-38'))

# Sharp universal growth and decay coefficients, and their opposite slopes.
data=ingredients(2,3,4,1)
a,b,c,z0,h,q,star=data
for kind, sign in [('Ai', -1), ('Bi', 1)]:
    for t in (300, 1200):
        x,y=solution(data, t, kind)
        rate=log_norm(data,t,kind)/(mp.mpf(t)**mp.mpf('1.5'))
        target=sign*(mp.mpf(2)/3)*mp.sqrt(a*b)
        assert abs(rate-target) < mp.mpf('0.2')
        slope=y/(x*mp.sqrt(t))
        assert abs(slope-sign*mp.sqrt(b/a)) < mp.mpf('0.15')

# The three displayed first-passage terms: errors decrease toward zero.
# A fixed Bi solution is one nonstable variational direction.
errors=[]
for L in (1000,10000):
    L=mp.mpf(L)
    leading=(3*L/(2*mp.sqrt(a*b)))**(mp.mpf(2)/3)
    approx=leading+h/mp.sqrt(a*b)*mp.sqrt(leading)+star+3*h*h/(4*a*b)
    exact=mp.findroot(lambda t: log_norm(data,t,'Bi')-L,(approx-1,approx+1))
    errors.append(abs(exact-approx))
assert errors[1]<errors[0] and errors[1]<mp.mpf('0.05'),errors
print('Airy variational identities, Wronskian, growth and first-passage diagnostics: OK')
