"""Independent numerical checks of the finite-release diffusion-uptake formulas.

Uses Python standard library only. Numerical checks supplement the analytic proof.
"""
import math

P = 1.5

def mode(a, k):
    return 2*a/(P + math.sqrt(P*P + 4*a*k))

def lag(a, k, T):
    # Solve the logarithm of equality of the two diffusion impulse values.
    def f(d):
        return a/d - a/(T+d) - P*math.log1p(T/d) - k*T
    lo = 0.0
    hi = mode(a, k)
    for _ in range(250):
        mid = (lo + hi)/2
        if mid == 0.0: break
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def asymptotic(a,k,T):
    B = math.log(T/a) + math.log(P) + k*T/P
    return a/(P*(B+math.log(B)))

for a in [0.1,1.0,8.0]:
    for T in [0.1*a,a,10*a,100*a,1e4*a]:
        for k in [0.0,0.001/a,0.1/a,1.0/a]:
            d = lag(a,k,T)
            assert 0<d<mode(a,k)
            assert max(T,mode(a,k)) < T+d < T+mode(a,k)
            assert abs((a/d-a/(T+d)-P*math.log1p(T/d)-k*T))/(1+k*T)<3e-12
            bigger=lag(a,k,T*1.001)
            assert 0<bigger<d
            assert T+d<T*1.001+bigger
for k in [0.0,0.001,0.1,1.0,100.0]:
    a=1.0
    T=1e6
    delta=lag(a,k,T)
    approx=asymptotic(a,k,T)
    assert abs(delta/approx-1)<0.02
# The coefficient of the late-time delay changes from inverse-log to inverse-T.
a=1.; T=1e6
assert abs(lag(a,0,T)*P*math.log(T/a)/a-1)<0.25
assert abs(lag(a,1,T)*T/a-1)<0.001
print('PASS: exact peak equation, uniqueness brackets, duration monotonicity, and large-pulse crossover examples')
