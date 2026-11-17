"""Standalone supplementary tests for scalar sampled-flow intensity asymptotics.
No external packages and no claims of infinite-case verification.
"""
import math


def golden_max(fun, a, b, iterations=125):
    r=(math.sqrt(5)-1)/2
    x=b-r*(b-a); y=a+r*(b-a)
    fx=fun(x); fy=fun(y)
    for _ in range(iterations):
        if fx<fy:
            a=x; x=y; fx=fy; y=a+r*(b-a); fy=fun(y)
        else:
            b=y; y=x; fy=fx; x=b-r*(b-a); fx=fun(x)
    z=(a+b)/2
    return z, fun(z)

# Logistic: exact maximum and uniform asymptotic coefficient.
for h in [1, 3, 6, 12, 20]:
    root=math.exp(h/2)
    x=1/(1+root)
    y=root/(1+root)
    d=y-x
    exact=math.tanh(h/4)
    assert abs(d-exact)<1e-14
    assert abs((1-d)*math.exp(h/2)-2)<2*math.exp(-h/2)+1e-9

# Cubic: exact formula already in the motivating work.
for h in [1, 3, 6, 12, 20]:
    u=math.exp(-2*h/3)
    d=(1-u)/math.sqrt(1+u+u*u)
    x=u/math.sqrt(1+u+u*u)
    y=1/math.sqrt(1+u+u*u)
    assert abs(y-x-d)<1e-14
    assert abs((1-d)*math.exp(2*h/3)-1.5)<4*u+1e-9

# Nonlinear-transit test with fixed endpoint slopes and changed constant.
alpha=-2.0

def simpson(fun, a, b, n=1000):
    z=fun(a)+fun(b)
    step=(b-a)/n
    for k in range(1,n):
        z+=(4 if k%2 else 2)*fun(a+step*k)
    return z*step/3


def g(x): return -alpha/(1+alpha*x*(1-x))
def T(x): return math.log(x/(1-x))+simpson(g,.5,x,200)
eta=simpson(g,0.0,1.0,2000)
constant=2*math.exp(eta/2)

def phi(h,x):
    tx=T(x)
    lo=x; hi=1-1e-13
    for _ in range(60):
        mid=(lo+hi)/2
        if T(mid)-tx<h:lo=mid
        else:hi=mid
    return (lo+hi)/2

for h,tol in [(8,.30),(12,.15),(16,.06),(20,.03)]:
    _, d=golden_max(lambda x: phi(h,x)-x, 1e-9,.4)
    ratio=(1-d)*math.exp(h/2)
    assert abs(ratio/constant-1)<tol,(h,ratio,constant)
print('CHECK PASSED: logistic/cubic exact identities and four deformed-flow samples')
