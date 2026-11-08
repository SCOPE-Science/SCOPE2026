"""Exact finite checks and numerical spot checks for the high-power Bergman defect law.
Standard library only; infinite assertions are established analytically in RESULT.md.
"""
from fractions import Fraction
from math import exp, log, isclose

COUNT = 0

def check(q, msg):
    global COUNT
    assert q, msg
    COUNT += 1

def exact_w(n, k, delta):
    result = Fraction(1)
    for j in range(1, k + 1):
        result *= Fraction(n + j, n + j + delta)
    return result

def wd(n, k, delta):
    result = 1.0
    for j in range(1, k + 1):
        result *= (n + j) / (n + j + delta)
    return result

def dval(n, k, delta):
    return wd(n, k, delta) - (wd(n - k, k, delta) if n >= k else 0.0)

def profile(t, delta):
    if t <= 0:
        return 0.0
    u = (t / (t + 1)) ** delta
    return u - (((t - 1) / t) ** delta if t > 1 else 0.0)

def peak(delta):
    if delta <= 1:
        return 1.0, 2.0 ** (-delta)
    def log_ratio(t):
        return delta * log(t*t/(t*t-1)) + log((t-1)/(t+1))
    lo, hi = 1 + 1.e-12, delta
    assert log_ratio(lo) > 0 and log_ratio(hi) < 0
    for _ in range(100):
        mid=(lo+hi)/2
        if log_ratio(mid)>0: lo=mid
        else: hi=mid
    t=(lo+hi)/2
    return t, profile(t,delta)

for delta in range(1, 6):
    for k in range(1, 11):
        s = Fraction(0)
        for n in range(0, 42):
            w = exact_w(n, k, delta)
            back = exact_w(n-k, k, delta) if n >= k else Fraction(0)
            x = w - back
            check(x >= 0, f"positivity {delta} {k} {n}")
            s += x
            expected = sum((exact_w(j,k,delta) for j in range(max(0,n-k+1),n+1)), Fraction(0))
            check(s == expected, f"trace telescoping {delta} {k} {n}")
for delta in (0.6, 1.0, 2.0, 4.0):
    tpeak, c = peak(delta)
    for k in (48, 128, 320):
        dlist = [dval(n,k,delta) for n in range(8*k+1)]
        index = max(range(len(dlist)),key=lambda n:dlist[n])
        check(abs(index/k - tpeak) < 0.09, f"peak site {delta} {k}")
        check(abs(dlist[index] - c) < 0.017, f"peak value {delta} {k}")
        check(all(x>=-1.e-12 for x in dlist), f"float positivity {delta} {k}")
for delta in (1,2,4):
    for k in (1,3,7):
        n=200000
        x=dval(n,k,delta)
        check(abs(n*n*x/(delta*k*k)-1)<0.002, f"tail {delta} {k}")
print('BERGMAN_HIGH_POWER_CHECK_OK',COUNT,'checks: rational telescoping, positivity, bulk maxima, fixed-power tails')
