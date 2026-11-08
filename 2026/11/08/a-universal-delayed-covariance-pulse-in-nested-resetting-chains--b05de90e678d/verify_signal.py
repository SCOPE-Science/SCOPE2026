#!/usr/bin/env python3
"""Independent reproducibility checks for stationary lagged covariance transmission.
Requires Python 3 standard library only. This is not a proof of asymptotics.
"""
from fractions import Fraction
import math

CHECKS=0

def check(cond, name):
    global CHECKS
    if not cond: raise AssertionError(name)
    CHECKS += 1

def stationary_cov(n, q=None):
    # Independent calculation from all quadratic infinitesimal-generator balances.
    # q_i is the arbitrary Levy finite-variance injection rate; resetting r=1.
    if q is None: q=[Fraction(0)]+[Fraction(2) for _ in range(n)]
    C=[[Fraction(0) for _ in range(n+1)] for _ in range(n+1)]
    for j in range(1,n+1):
        C[j][j]=C[j-1][j-1]+q[j]
        for i in range(1,j):
            # r=1 and i<j; reset i and reset j are distinct events
            C[i][j]=(C[i-1][j]+C[i][j-1])/2
            C[j][i]=C[i][j]
    return C

def closed(m,x):
    # C_{1,m+1}(x), x=r*t, V=2
    a=1.0; total=1.0
    for k in range(1,m+1):
        a*=2*x/k
        total+=a
    return 2.0*2.0**(-m)*math.exp(-x)*total

def backward(m,x):
    return 2.0*2.0**(-m)*math.exp(-x)

def rk4_forward(C, endtime, h=0.002):
    # evolve all C_{1,j}(t) using the differential moment equation;
    # deliberately do not use the closed-form exponential/Poisson propagator
    n=len(C)-1
    y=[0.0]+[float(C[1][j]) for j in range(1,n+1)]
    steps=max(1,round(endtime/h)); h=endtime/steps
    def rhs(z):
        return [0.0]+[-z[1]]+[z[j-1]-z[j] for j in range(2,n+1)]
    for _ in range(steps):
        k1=rhs(y)
        k2=rhs([z+h*v/2 for z,v in zip(y,k1)])
        k3=rhs([z+h*v/2 for z,v in zip(y,k2)])
        k4=rhs([z+h*v for z,v in zip(y,k3)])
        y=[z+h*(a+2*b+2*c+d)/6 for z,a,b,c,d in zip(y,k1,k2,k3,k4)]
    return y

def ratio(m,lambd):
    # Q_m(lambda)/(lambda**m/m!) + 1, stable for large m.
    term=1.0; total=0.0
    for l in range(1,m+1):
        term*= (m-l+1)/lambd
        total+=term
    return total

def optimum_lambda(m):
    lo=1e-12; hi=4.0*m
    check(ratio(m,lo)>1.0 and ratio(m,hi)<1.0, 'root bracket')
    for _ in range(90):
        mid=(lo+hi)/2
        if ratio(m,mid)>1: lo=mid
        else: hi=mid
    return (lo+hi)/2

def peak_amplitude(m, lam):
    return 4.0*math.exp(-lam/2 + m*math.log(lam/2) - math.lgamma(m+1))

def simpson(f, upper, steps=12000):
    assert steps%2==0
    h=upper/steps
    s=f(0.0)+f(upper)
    for k in range(1,steps):
        s+=(4 if k%2 else 2)*f(k*h)
    return h*s/3

def main():
    C=stationary_cov(12)
    for j in range(1,13):
        check(C[j][j]==2*j,'stationary variance')
        check(C[1][j]==Fraction(2,2**(j-1)), 'first-row covariance')
        for i in range(1,j):
            check(2*C[i][j]==C[i-1][j]+C[i][j-1],'quadratic generator balance')
    # The first-to-downstream cross correlation is blind to all downstream
    # Levy variance rates and to higher jump cumulants.
    for seed in range(1,17):
        q=[Fraction(0),Fraction(2)]+[Fraction(1+((seed*23+j*13)%29),7) for j in range(2,13)]
        H=stationary_cov(12,q)
        for j in range(1,13):
            check(H[1][j]==Fraction(2,2**(j-1)), 'downstream variance universality')
            check(H[j][j]==sum(q[1:j+1]), 'heterogeneous stationarity')
    for time in (0.05,0.25,1.0,2.75,5.0,9.0):
        y=rk4_forward(C,time)
        for j in range(1,13):
            check(abs(y[j]-closed(j-1,time))<3e-10,'independent RK4 evolution')
    # Explicit causality: forward covariance exceeds backward for any positive lag.
    for m in range(1,20):
        for x in (0.005,0.25,1.,2.,4.,10.):
            check(closed(m,x)>backward(m,x),'directed lag asymmetry')
    # Existence/uniqueness of maximum is proved by the polynomial's single sign change;
    # numerically check root and derivative sides for a broad finite range.
    for m in range(1,201):
        lam=optimum_lambda(m)
        check(ratio(m,lam*0.999)>1 and ratio(m,lam*1.001)<1,'unique maximum sign')
        x=lam/2
        check(abs(closed(m,x)-peak_amplitude(m,lam))<2e-10,'peak identity')
        check(closed(m,x)>closed(m,0.0),'peak vs simultaneous')
    check(abs(optimum_lambda(1)-1)<1e-12,'first exact root')
    check(abs(optimum_lambda(2)-(1+math.sqrt(3)))<1e-12,'second exact root')
    # Compare long-chain location and amplitude with rigorous leading asymptotics.
    for m in (100,200,500,1000,2000):
        lam=optimum_lambda(m)
        check(abs((lam-(2*m-2))*m-4)<6.0,'root asymptotic first correction')
        check(abs(peak_amplitude(m,lam)/(2*math.sqrt(2/(math.pi*m)))-1)<0.01,'peak asymptotic')
    # Integrated transfer: quadrature independent of exact gamma-integral evaluation.
    for m in range(0,10):
        integral=simpson(lambda x:closed(m,x),max(50.,5.*m+40.))
        target=2*(2-2.**(-m))   # V/r=2 at D=r=1
        check(abs(integral-target)<1e-7,'integrated forward transfer')
        reverse=simpson(lambda x:backward(m,x),50.)
        check(abs(reverse-2*2.**(-m))<1e-7,'integrated backward transfer')
    print('PASS: %d deterministic independent generator, RK4, root, and quadrature checks' % CHECKS)
    print('Example: m=10, lambda_peak=%.12f, peak=%.12f, zero_lag=%.12f' %
          (optimum_lambda(10),peak_amplitude(10,optimum_lambda(10)),closed(10,0.0)))

if __name__=='__main__': main()
