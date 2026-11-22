#!/usr/bin/env python3
"""Reproducible independent finite-difference and optimization checks for two reactive ends."""
import math,random

def phi(z,k,K,a):
    b=K-a;S=math.sinh(k);C=math.cosh(k)
    return (a*math.cosh(k*(1-z))+b*math.cosh(k*z)
            +a*b*(math.sinh(k*(1-z))+math.sinh(k*z)))/(S+K*C+a*b*S)

def threshold(k,z):
    if abs(z-0.5)<1e-14:return 0.
    z=min(z,1-z);t=k*z;u=k*(1-z);S=math.sinh(k)
    delta=math.cosh(u)-math.cosh(t)
    B1=math.cosh(k+t)-math.cosh(t)
    B2=S*math.cosh(t)-math.sinh(t)-math.sinh(u)
    return 2*delta*S/(B1+math.sqrt(B1*B1+4*B2*delta*S))

def derivative(z,k,K,a):
    t=k*z;u=k*(1-z);S=math.sinh(k);C=math.cosh(k)
    delta=math.cosh(u)-math.cosh(t)
    H=math.sinh(u)+math.sinh(t)
    d0=S+K*C;Z=H*d0-S*K*math.cosh(t)
    return (delta*S*a*a-2*Z*a+K*Z+delta*d0)/(d0+S*a*(K-a))**2

def optimum(z,k,K):
    if z>0.5:return K-optimum(1-z,k,K)
    if z==0.5:return K/2
    if K <=threshold(k,z):return K
    low,high=0.,K
    for _ in range(100):
        mid=(low+high)/2
        if derivative(z,k,K,mid)>0:low=mid
        else:high=mid
    return (low+high)/2

def finite_difference_phi(z,k,K,a,n=1400):
    """Independent centered difference BVP with Robin ghost-point boundaries."""
    b=k*(K-a);a=k*a;h=1/n; h2=1/(h*h)
    diag=[2*h2+k*k]*(n+1)
    low=[-h2]*n;high=[-h2]*n; rhs=[0.]*(n+1)
    diag[0]=2*h2+2*a/h+k*k;high[0]=-2*h2;rhs[0]=2*a/h
    diag[n]=2*h2+2*b/h+k*k;low[n-1]=-2*h2;rhs[n]=2*b/h
    for j in range(1,n+1):
        g=low[j-1]/diag[j-1]
        diag[j]-=g*high[j-1]
        rhs[j]-=g*rhs[j-1]
    y=[0.]*(n+1);y[n]=rhs[n]/diag[n]
    for j in range(n-1,-1,-1): y[j]=(rhs[j]-high[j]*y[j+1])/diag[j]
    idx=int(z/h);t=z/h-idx
    return (1-t)*y[idx]+t*y[min(idx+1,n)]

def golden(z,k,K):
    a,b=0.,K;g=(math.sqrt(5)-1)/2
    c=b-g*(b-a);d=a+g*(b-a);fc=phi(z,k,K,c);fd=phi(z,k,K,d)
    for _ in range(120):
        if fc>fd:
            b,d,fd=d,c,fc;c=b-g*(b-a);fc=phi(z,k,K,c)
        else:
            a,c,fc=c,d,fd;d=a+g*(b-a);fd=phi(z,k,K,d)
    best=(a+b)/2
    return max([0.,K,best],key=lambda aa:phi(z,k,K,aa))

if __name__=='__main__':
    rng=random.Random(830472)
    max_bvp=0.;max_optim=0.
    for j in range(100):
        z=rng.uniform(0,1);k=rng.uniform(.12,4);K=rng.uniform(.02,5);a=rng.uniform(0,K)
        err=abs(phi(z,k,K,a)-finite_difference_phi(z,k,K,a))
        max_bvp=max(max_bvp,err)
        assert err<1.3e-5,(j,err,z,k,K,a)
        best=optimum(z,k,K);g=golden(z,k,K)
        err2=phi(z,k,K,g)-phi(z,k,K,best)
        max_optim=max(max_optim,abs(err2))
        assert abs(err2)<1e-10,(j,err2,z,k,K,best,g)
    for z in [0,.05,.2,.4,.49]:
        for k in [.2,1.,3.]:
            Kc=threshold(k,z)
            for mult in [.4,1.6]:
                K=Kc*mult
                a=optimum(z,k,K)
                assert (abs(a-K)<1e-10) == (mult<1)
                for j in range(101):
                    assert phi(z,k,K,a)+1e-11>=phi(z,k,K,K*j/100)
    for k in [.2,1.,3.]:
        assert abs(threshold(k,0)-math.sinh(k))<2e-13
    print('PASS 100 independent Robin BVP comparisons; max absolute error',max_bvp)
    print('PASS 100 independent scalar optimizations; max objective discrepancy',max_optim)
    print('PASS 30 threshold regime tests, 3030 allocation scans, 3 boundary identities')
    for z,k,K in [(0,1,.5),(0,1,3),(.2,1,.3),(.2,1,3),(.5,1,3)]:
        a=optimum(z,k,K)
        print('example z,k,K',z,k,K,'Kcrit',threshold(k,z),'aopt',a,'capture probability',phi(z,k,K,a),'all near',phi(z,k,K,K))
