#!/usr/bin/env python3
"""Numerical and algebraic consistency checks for positive acyclic passage.
Run with Python 3 standard library: python checker.py
These finite tests do not establish uniform-in-epsilon statements.
"""
import math


def gaussian_pair(eps, t, b=10.0):
    ax = t*t/2-3*t
    ay = t*t-4*t
    x = math.exp(ax/eps)
    trunc = math.erf((t-1)/math.sqrt(2*eps))+math.erf(1/math.sqrt(2*eps))
    y = math.exp((ay+.5)/eps)*math.sqrt(math.pi/(2*eps))*trunc + math.exp((ay-b)/eps)
    return x, y


def return_time(eps):
    lo,hi=2.0,4.2
    assert sum(gaussian_pair(eps,lo)) < 1 < sum(gaussian_pair(eps,hi))
    for _ in range(95):
        mid=(lo+hi)/2
        if sum(gaussian_pair(eps,mid)) < 1:lo=mid
        else:hi=mid
    return (lo+hi)/2


def stable_two(eps,t,l1,l2,rate,a2,r):
    x=math.exp(l1*t/eps)
    if l1==l2:
        transfer=rate*(eps**(r-1))*t*x
    else:
        # exact variation of constants, no discretization
        transfer=rate*(eps**r)*(x-math.exp(l2*t/eps))/(l1-l2)
    y=math.exp((a2+l2*t)/eps)+transfer
    return x,y


def main():
    n=0
    largest_scaled_error=0.
    for eps in (.2,.1,.05,.025):
      for t in (.5,1.,1.5):
       for l1 in (-2.,-.5,.5):
        for l2 in (-1.5,-.5,.75):
         for rate in (.3,1.,2.):
          for a2 in (-3.,-1.,0.):
           for r in (0,1):
            x,y=stable_two(eps,t,l1,l2,rate,a2,r)
            assert x>0 and y>0
            p1=l1*t
            p2=max(a2+l2*t,t*max(l1,l2))
            err=max(abs(eps*math.log(x)-p1),abs(eps*math.log(y)-p2))
            scaled=err/(eps*(1+abs(math.log(eps))))
            largest_scaled_error=max(largest_scaled_error,scaled)
            assert scaled < 12, (eps,t,l1,l2,rate,a2,r,scaled)
            n+=1
    tstar=2+math.sqrt(3.5)
    slope=2*math.sqrt(3.5)
    checks=[]
    for eps in (.1,.05,.02,.01,.005):
        t=return_time(eps)
        x,y=gaussian_pair(eps,t)
        assert abs(x+y-1)<2e-12
        correction=(eps/(2*slope))*math.log(eps/(2*math.pi))
        resid=(t-tstar-correction)/eps
        lower=0.5*math.erfc(1/math.sqrt(2*eps))
        upper=0.5*math.erfc((t-1)/math.sqrt(2*eps))
        tv=lower+upper
        checks.append((eps,t,resid,x,tv))
        assert t>2 and t<tstar
        assert abs(resid)<1.0  # smaller epsilon asymptotic in the theorem
    assert abs(checks[-1][2])<abs(checks[0][2])
    print('TWO_NODE_EXACT_CASES',n)
    print('MAX_LOG_ERROR_SCALED',round(largest_scaled_error,6))
    print('CROSSING_ROOT=%.12f SLOPE=%.12f'%(tstar,slope))
    print('EPS;RETURN;SECOND_ORDER_RESIDUAL/EPS;X_AT_RETURN;GAUSSIAN_TV')
    for eps,t,resid,x,tv in checks:
        print('%.3g;%.12f;%.6g;%.4g;%.4g'%(eps,t,resid,x,tv))
    print('CHECK_OK')

if __name__=='__main__': main()
