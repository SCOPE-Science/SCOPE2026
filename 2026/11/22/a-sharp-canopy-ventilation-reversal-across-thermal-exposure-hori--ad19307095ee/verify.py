"""Reproducible numeric regression checks for a scalar canopy heat-balance model.

The mathematical proof is analytical; these finite checks test formula implementation
and boundary cases without claiming infinite-domain certification.
No nonstandard dependencies are required.
"""
from math import exp, expm1, log, comb, isfinite

checks = 0

def assert_close(a, b, tol=3e-7):
    global checks
    checks += 1
    assert abs(a - b) <= tol * (1.0 + abs(a) + abs(b)), (a,b)

def assert_true(condition, info=''):
    global checks
    checks += 1
    assert condition, info

def integrate(f, steps=4096):
    h = 1.0 / steps
    s = f(0.0) + f(1.0)
    for j in range(1,steps):
        s += (4 if j % 2 else 2) * f(j*h)
    return s * h / 3

def phi(k, y):
    assert k >= 0 and isinstance(k, int) and y > 0
    if k == 0:
        return -expm1(-y)/y
    if k == 1 and y >= 0.02:
        return (y+expm1(-y))/(y*y)
    return integrate(lambda v: (1-v)**k * exp(-y*v))

def elasticity(k, y):
    p = phi(k,y)
    numerator = integrate(lambda v: v*(1-v)**k*exp(-y*v))
    return y*numerator / p

def bisect(f, lo, hi, n=75):
    assert f(lo)<0 <f(hi)
    for _ in range(n):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else:lo=mid
    return (lo+hi)/2

def risk(k, T, x, alpha, beta, initial_rate=1., initial_load=1.):
    y = initial_rate*exp(-beta*x)*T
    return initial_load*exp(-alpha*x)*T**(k+1)*phi(k,y)

def derivative_sign(k,T,x,alpha,beta,initial_rate=1.):
    return -alpha+beta*elasticity(k,initial_rate*exp(-beta*x)*T)

# Reference parameters: endpoint source ratio 1/2 and ventilation ratio 1/4.
a,b = log(2),log(4)
reference = [(0,1.256431208626169,2.43751145374402), (1,2.14912579990698,4.24857018426470)]
for k, predicted_peak, predicted_switch in reference:
    ystar=bisect(lambda y:elasticity(k,y)-a/b,0.001,30)
    tstar=bisect(lambda T:risk(k,T,1,a,b)/risk(k,T,0,a,b)-1,0.001,50)
    assert_close(ystar,predicted_peak,3e-6)
    assert_close(tstar,predicted_switch,2e-8)
    assert_true(ystar<tstar<4*ystar)
    for T in [ystar*.5, ystar, ystar*1.1, tstar, ystar*3.,4*ystar,4.5*ystar]:
        values=[risk(k,T,j/120,a,b) for j in range(121)]
        # Strict interior points cannot improve either extreme for minimization.
        for j in range(1,120):
            assert_true(values[j]>min(values[0],values[-1])-1e-12)
        if T<ystar-1e-7:
            assert_true(all(values[j]>values[j+1] for j in range(120)))
        if T>4*ystar+1e-7:
            assert_true(all(values[j]<values[j+1] for j in range(120)))
        if ystar<T<4*ystar:
            xmax=log(T/ystar)/b
            assert_true(0<xmax<1)
            assert_close(derivative_sign(k,T,xmax,a,b),0,5e-7)
            assert_true(risk(k,T,xmax,a,b)>=max(values)-1e-8)
    print('k=',k,'ycrit=',format(ystar,'.12f'),'Tswitch=',format(tstar,'.12f'))

# General finite-difference tests of log-concavity and strictly increasing endpoint ratio.
for k in range(6):
    for alpha,beta in [(0.3,0.8),(0.7,1.9),(1.3,0.5)]:
        for T in (0.2,0.7,1.5,3.0,10.0):
            val=lambda x:risk(k,T,x,alpha,beta)
            for j in range(1,20):
                x=j/20
                assert_true(val(x)**2 > val(x-0.025)*val(x+0.025)*(1.-1e-9), (k,alpha,beta,T,x))
            vals=[val(j/100) for j in range(101)]
            assert_true(min(vals)>=min(vals[0],vals[-1])-1e-9)
            if alpha>=beta:
                assert_true(all(vals[j]>vals[j+1] for j in range(100)))
        ratios=[risk(k,T,1,alpha,beta)/risk(k,T,0,alpha,beta) for T in [0.1,0.3,0.7,1.2,2,4,8,16,32,64]]
        assert_true(all(ratios[i]<ratios[i+1] for i in range(len(ratios)-1)))

# Compare k=0,1 integral representation with closed forms and direct quadrature.
for k in (0,1):
    for T in (.07,.2,1,3,15):
        for x in (0,.2,.5,.9,1):
            lam=1.7*exp(-1.2*x)
            H=2.3*exp(-.4*x)
            exact=H*T**(k+1)*phi(k,lam*T)
            integ=H*T**(k+1)*integrate(lambda v:(1-v)**k*exp(-lam*T*v))
            assert_close(exact,integ,1e-9)
            if k==0:
                assert_close(exact,H*(-expm1(-lam*T))/lam,1e-10)
            else:
                assert_close(exact,H*(lam*T+expm1(-lam*T))/lam**2,1e-9)
print('PASS',checks,'numeric assertions; finite regressions only')
