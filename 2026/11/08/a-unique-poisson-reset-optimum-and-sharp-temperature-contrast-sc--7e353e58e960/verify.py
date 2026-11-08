#!/usr/bin/env python3
"""Algebraic and numerical consistency checks for a Gaussian endpoint-divergence theorem.
Run with Python 3 and mpmath 1.3 or newer: python verify.py.
The symbolic argument in RESULT.md, not finite sampling, proves the global theorem.
"""
import mpmath as mp
mp.mp.dps = 48

def derivative_integral(q, k):
    d = 1-q
    def f(y):
        if y == 0: return mp.mpf('0')
        return y**k * (1-y)*(1+q-d*y)/(1-d*y)**2 * (1+k*mp.log(y))
    return d*d/(2*q)*mp.quad(f, [0, mp.mpf('0.25'), mp.mpf('0.75'), 1])

def rate(q, k):
    d=1-q
    def f(y):return y**k * (1-y)*(1+q-d*y)/(1-d*y)**2
    return d*d*k/(2*q)*mp.quad(f, [0, mp.mpf('0.25'), mp.mpf('0.75'), 1])

def h(q,k):
    d=1-q
    return mp.quad(lambda z:mp.exp(-z)/(1-d*mp.exp(-z/k)), [0, 1, 5, 20, 80, mp.inf])

def rate_alt(q,k):
    return 1/(2*q) - (1-q)/(2*q*(k+1)) - (k+1)/2 + k*q*h(q,k)/2

def bisect_root(q,lo,hi):
    assert derivative_integral(q,lo)>0 and derivative_integral(q,hi)<0
    for _ in range(42):
        mid=(lo+hi)/2
        if derivative_integral(q,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def main():
    qlist=['0.99','0.9','0.5','0.1','0.01','0.001']
    count=0
    for qs in qlist:
        q=mp.mpf(qs)
        root=bisect_root(q, mp.mpf('0.1'), mp.mpf('150'))
        v=rate(q,root)
        v2=rate_alt(q,root)
        assert abs(v-v2) < mp.mpf('1e-30') * max(1, abs(v))
        assert abs(derivative_integral(q,root)) < mp.mpf('1e-8')
        assert rate(q,root*.8)<v and rate(q,root*1.2)<v
        print('q=',qs,' dimensionless_optimum=',mp.nstr(root,15),' dimensionless_peak=',mp.nstr(v,15))
        count+=5
    for qs in ['0.999','0.9999']:
        q=mp.mpf(qs)
        root=bisect_root(q,1,2)
        assert abs(root-mp.sqrt(2))<mp.mpf('0.004')
        count+=1
    for qs,tol in [('0.0001','0.06'),('0.00001','0.025')]:
        q=mp.mpf(qs)
        root=bisect_root(q,mp.mpf('0.1'),2/mp.sqrt(q))
        assert abs(root*mp.sqrt(q)-1) < mp.mpf(tol)
        peak=rate(q,root)
        assert abs((1/(2*q)-peak)*mp.sqrt(q)-1) < mp.mpf(tol)
        count+=2
    print('PASS:',count,'exact-formula, derivative, maximum and asymptotic numerical comparisons')
if __name__ == '__main__':main()
