#!/usr/bin/env python3
"""Standalone standard-library checks for a three-step accelerated power filter.

Finite tests supplement, but do not replace, the scalar calculus proof.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

def check(pred):
    global checks
    assert pred
    checks += 1

def polynomials(t, b):
    p_minus, p_now = F(1), F(1)
    out = [p_now]
    for _ in range(3):
        nex = t*((1+b)*p_now-b*p_minus)
        p_minus, p_now = p_now, nex
        out.append(nex)
    return out

def poly3(t,b):
    return t*t*(t-(b*(b+2))*(1-t))

# Exact rational proof-step reconstruction and sharp scalar extrema.
for a in range(1, 24):
    q = F(a, 24)
    for k in range(0, 25, 2):
        b = q*F(k, 24)
        c = b*(2+b)
        for j in range(25):
            t = q*F(j, 24)
            p = polynomials(t,b)
            check(p[0] == 1)
            check(p[1] == t)
            check(p[2] == t*(t-b*(1-t)))
            check(p[3] == poly3(t,b))
            check(poly3(F(1),b) == 1)
        # Check that the only derivative critical point is exact when within range.
        tcrit = 2*c/(3*(1+c)) if c else F(0)
        def candidate_value(x): return abs(poly3(x,b))
        theoretical=max(candidate_value(F(0)), candidate_value(q),
                        candidate_value(tcrit) if tcrit <= q else F(0))
        for j in range(121):
            t=q*F(j,120)
            check(candidate_value(t) <= theoretical)


def n(c): return 4*c*c*c/(27*(1+c)*(1+c))
def p(q,c): return q*q*(q-(1-q)*c)
def equi(q):
    low, high = 0.0, q/(1-q)
    for _ in range(90):
        mid=(low+high)/2
        if p(q,mid)>n(mid): low=mid
        else: high=mid
    return (low+high)/2

def f(q): return q*q+q-1-4*(q+2)**3/(27*(1+q)**4)
low,high = .618,1.
for _ in range(100):
    mid=(low+high)/2
    if f(mid)>0: high=mid
    else: low=mid
qstar=(low+high)/2
check(abs(qstar-.755526784205864)<3e-14)
check(f(.618)<0<f(1))

for i in range(1, 500):
    q=i/500
    ce=equi(q)
    cm=q*(q+2)
    cc=min(ce,cm)
    beta=sqrt(1+cc)-1
    check(abs(beta-q)<1e-11 if q>qstar else beta<q+1e-11)
    check((cc==cm) == (q>qstar))
    if cc==ce:
        check(abs(p(q,cc)-n(cc))<1e-10)
    exact = max(abs(poly3(q,beta)), abs(poly3(2*cc/(3*(1+cc)),beta)))
    expected = n(ce) if q<qstar else q**3*(q*q+q-1)
    check(abs(exact-expected)<3e-10)
    check(0<exact<q**3)
    # Check uniqueness qualitatively against 50 other admissible parameters.
    for j in range(51):
        b=q*j/50
        c=b*(b+2)
        tcritical=2*c/(3*(1+c)) if c>0 else 0
        actual=max(abs(poly3(q,b)),
                   abs(poly3(tcritical,b)) if tcritical <= q else 0)
        check(actual+1e-9>=expected)

phi=(sqrt(5)-1)/2
for i in range(1,401):
    q=i/500
    b=1/sqrt(1-q)-1
    check((b <= q+1e-12) == (q <= phi+1e-12))
    check(abs(poly3(q,b))<5e-13)
    maxnotch=4*q**3/(27*(1-q))
    check(abs(poly3(2*q/3,b))<=maxnotch+1e-12)
    for k in range(1,21):
        t=q*k/20
        check(abs(poly3(t,b))<=maxnotch+1e-12)

# Separate finite matrix recurrence (not just direct scalar substitution).
for aa in range(1,11):
    vals = [F(1), F(aa, 12), F(aa,24)]
    b = F(aa, 20)
    v0 = [F(1), F(2), F(-3)]
    vm, vn = list(v0), list(v0)
    for step in range(1,4):
        vnew = [vals[j]*((1+b)*vn[j]-b*vm[j]) for j in range(3)]
        vm, vn = vn, vnew
    for j in range(3):
        check(vn[j] == poly3(vals[j],b)*v0[j])

# At exact golden-ratio endpoint, the unique notch parameter equals the cap.
check(abs((1/sqrt(1-phi)-1)-phi)<3e-15)
# Explicit numerical independent benchmarks.
q=.5
b=sqrt(1+equi(q))-1
check(abs(b-.3448025780920969)<1e-11)
check(abs(n(equi(q))-.0239382532446062)<1e-11)
q=.8
check(abs(q**3*(q*q+q-1)-.22528)<1e-14)
print(f"VERIFY_OK {checks} exact-rational and numerical assertions")
