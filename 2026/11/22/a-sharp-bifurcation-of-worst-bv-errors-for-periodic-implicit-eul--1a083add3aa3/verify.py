"""Reproduce independent numerical checks for the periodic backward-Euler residual theorem.
Standard-library Python 3.10+ only. Finite checks are not proofs.
"""
import math

PI = math.pi

def g(u):
    return u / math.tanh(u) if u > 1.0e-7 else 1 + u*u/3 - u**4/45

def bisection(fn, lo, hi, count=100):
    f_lo, f_hi = fn(lo), fn(hi)
    assert f_lo * f_hi <= 0, (lo, hi, f_lo, f_hi)
    for _ in range(count):
        m = (lo+hi)/2
        if fn(m)*f_lo > 0:
            lo, f_lo = m, fn(m)
        else:
            hi = m
    return (lo+hi)/2

A_CRIT = bisection(lambda a:g(a)-3, 2.5, 3.5)
T_CRIT = 1/(4*A_CRIT*A_CRIT)

def optimal(t):
    lam=math.sqrt(t)
    a=1/(2*lam)
    if g(a) <= 3:
        return 0.5, 0.0
    z=bisection(lambda z:g(z)-(g(a)-2), 0, a)
    return 0.5-lam*z,z

def exact(t,s):
    lam=math.sqrt(t)
    a=1/(2*lam)
    z=(.5-s)/lam
    # Valid and stable for parameter values in the executable tests.
    return lam/(8*math.sinh(a))*(a*math.sinh(a)-z*math.sinh(z)
          +(g(a)-1)*(math.cosh(z)-math.cosh(a)))

def fourier(t,s,N=150000):
    total=0.0
    for k in range(1,N+1):
        q=2*PI*k
        r=t*q*q/(1+t*q*q)
        total+=(1-math.cos(q*s))*r*r/(q*q)
    # The exact positive discarded tail is at most 1/(2*pi^2*N).
    return total, 1/(2*PI*PI*N)

assert 2.98<A_CRIT<2.99
assert .028<T_CRIT<.0281
for t in (.0001,.001,.007,.01,.02,.026,.0281,.04,.3):
    s,z=optimal(t)
    assert 0<s<=.5 and 0<=z<1/(2*math.sqrt(t))
    assert abs((g(z)+2-g(1/(2*math.sqrt(t)))) if z else 0) < 5e-12
    assert exact(t,s) >= exact(t,.5) - 3e-13
    for v in (min(.5,s/2), s, min(.5,(s+.5)/2), .5):
        f, tail=fourier(t,v,N=100000)
        assert abs(exact(t,v)-f)<tail+2e-10, (t,v,exact(t,v),f,tail)
    h=min(1e-6,s/50,(.5-s)/50) if s<.5 else 1e-6
    if s<.5:
        assert abs(exact(t,s+h)-exact(t,s-h)) < 4e-9
    else:
        assert exact(t,.5) > exact(t,.499)

assert abs(optimal(1e-4)[0]/.01 - 2)<2e-4
short=(1+math.exp(-2))/8
assert abs(exact(1e-4,optimal(1e-4)[0])/.01-short)<1e-7
root_coefficient=math.sqrt(1.5*(A_CRIT*A_CRIT-6))
for delta in (1e-4,1e-5):
    t=T_CRIT-delta
    s,_=optimal(t)
    assert abs((.5-s)/math.sqrt(delta) /root_coefficient-1) < 5e-4
print('PASS: 9 parameter values, 36 independent Fourier comparisons, stationary checks, critical and asymptotic laws')
print(f'a_crit={A_CRIT:.15f}; t_crit={T_CRIT:.15f}; short coefficient={short:.15f}; sqrt-critical coefficient={root_coefficient:.15f}')
