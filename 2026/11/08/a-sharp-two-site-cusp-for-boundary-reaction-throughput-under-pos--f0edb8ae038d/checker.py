#!/usr/bin/env python3
"""Standalone numerical diagnostics for the boundary-contact throughput theorem.

Uses Python's standard library only. This checks finite instances and identities;
all infinite and all-parameter assertions require the mathematical proof.
"""
import math

N = 0

def check(cond, message):
    global N
    N += 1
    if not cond:
        raise AssertionError(message)

def close(a, b, tol=1e-10):
    return abs(a-b) <= tol*(1+abs(a)+abs(b))

def H(beta,y):
    return math.exp(-(beta-1)*y)*(beta*y-1)/(1-y)

def F(beta,p,y):
    return y*(p*math.exp(-y)+(1-p)*math.exp(-beta*y))

def Fp(beta,p,y):
    return p*math.exp(-y)*(1-y)+(1-p)*math.exp(-beta*y)*(1-beta*y)

def bisect(fun,a,b,steps=100):
    fa,fb=fun(a),fun(b)
    if not fa*fb<0:
        raise ArithmeticError((a,b,fa,fb))
    for _ in range(steps):
        c=(a+b)/2
        if (fun(c)>0)==(fa>0):
            a=c
            fa=fun(a)
        else:
            b=c
    return (a+b)/2

def spinodals(beta):
    disc=beta*beta-6*beta+1
    if disc<=0:
        raise ValueError('No two spinodals')
    d=math.sqrt(disc)
    return ((beta+1-d)/(2*beta),(beta+1+d)/(2*beta))

def stationary_roots(beta,p):
    ym,yp=spinodals(beta)
    q=p/(1-p)
    return [bisect(lambda y:H(beta,y)-q,1/beta+1e-13,ym),
            bisect(lambda y:H(beta,y)-q,ym,yp),
            bisect(lambda y:H(beta,y)-q,yp,1-1e-13)]

def coexist(beta):
    ym,yp=spinodals(beta)
    hmin,hmax=H(beta,yp),H(beta,ym)
    lo=hmin/(1+hmin)+1e-11
    hi=hmax/(1+hmax)-1e-11
    def gap(p):
        u,v,w=stationary_roots(beta,p)
        return F(beta,p,w)-F(beta,p,u)
    p=bisect(gap,lo,hi)
    return p,stationary_roots(beta,p),lo,hi

def laplace_inverse(s,D,r,a,b,p,ell):
    k=math.sqrt((s+r)/D)
    A=p*math.exp(-k*a)+(1-p)*math.exp(-k*b)
    phi=s*k/(s+r*A)
    return math.exp(-ell*phi)

def laplace_from_reset(s,D,r,a,b,p,ell):
    k=math.sqrt((s+r)/D)
    A=p*math.exp(-k*a)+(1-p)*math.exp(-k*b)
    return (s+r)*A/(s+r*A)*laplace_inverse(s,D,r,a,b,p,ell)

def mean_from_reset(D,r,a,b,p,ell):
    k=math.sqrt(r/D)
    A=p*math.exp(-k*a)+(1-p)*math.exp(-k*b)
    return (1-A)/(r*A)+ell/(math.sqrt(D*r)*A)

def main():
    beta_c=3+2*math.sqrt(2)
    check(close((beta_c-1)**2,4*beta_c), 'exact cusp identity')
    for beta in (1.1,2.,5.,beta_c,6.,10.,20.,100.):
        for y in (0.05,0.09,0.15,0.4,0.65,0.8,0.95,1.2):
            for p in (0.03,0.15,0.33,0.55,0.87):
                diff=Fp(beta,p,y)
                h=2e-6
                approx=(F(beta,p,y+h)-F(beta,p,y-h))/(2*h)
                check(close(diff,approx,2e-8), 'derivative identity')
        for p in (.07,.31,.81):
            check(Fp(beta,p,1/beta)>0, 'left derivative')
            check(Fp(beta,p,1)<0, 'right derivative')
    for beta in (6.,8.,10.,20.):
        ym,yp=spinodals(beta)
        check(1/beta<ym<yp<1, 'critical point order')
        check(H(beta,ym)>H(beta,yp)>0, 'critical height order')
        check(close((beta-1),1/(ym-1/beta)+1/(1-ym)), 'lower critical equation')
        check(close((beta-1),1/(yp-1/beta)+1/(1-yp)), 'upper critical equation')
        p,roots,lo,hi=coexist(beta)
        check(lo<p<hi, 'interior coexistence')
        check(roots[0]<roots[1]<roots[2], 'stationary order')
        check(close(F(beta,p,roots[0]),F(beta,p,roots[2])), 'peak height equality')
        check(F(beta,p,roots[1])<F(beta,p,roots[0]),'middle is smaller')
        for u in roots:
            check(abs(Fp(beta,p,u))<1e-10,'stationary derivative')
        for pi in (lo+(p-lo)*0.5,p, p+(hi-p)*.5):
            rr=stationary_roots(beta,pi)
            check(rr[0]<rr[1]<rr[2],'three roots')
        below=lo+(p-lo)*.5
        above=p+(hi-p)*.5
        low=stationary_roots(beta,below)
        high=stationary_roots(beta,above)
        check(F(beta,below,low[0])>F(beta,below,low[2]),'low optimum before transition')
        check(F(beta,above,high[0])<F(beta,above,high[2]),'high optimum after transition')
    p,roots,_,_=coexist(10.)
    check(abs(p-0.1228819699964)<1e-8,'benchmark probability')
    check(abs(roots[0]**2-0.020660588845)<1e-8,'benchmark lower rate')
    check(abs(roots[2]**2-0.983120201416)<1e-8,'benchmark higher rate')
    for D in (0.2,1.,3.):
        for r in (0.15,1.0,4.0):
            for ell in (.1,1.,3.):
                for a,b,p in ((0.,0.,1.),(.5,.5,1.),(.5,3.,.23)):
                    expected=mean_from_reset(D,r,a,b,p,ell)
                    s=1e-8
                    approx=(1-laplace_from_reset(s,D,r,a,b,p,ell))/s
                    check(close(expected,approx,4e-6),'mean transform derivative')
                    check(0<laplace_inverse(.5,D,r,a,b,p,ell)<=1,'inverse transform bounds')
                    check(0<laplace_from_reset(.5,D,r,a,b,p,ell)<=1,'start distribution transform bounds')
                    if a==b==0:
                        phi=.5/math.sqrt(D*(r+.5))
                        check(close(laplace_inverse(.5,D,r,0.,0.,1.,ell),math.exp(-ell*phi)),
                              'reset-to-boundary known formula')
    print('PASS',N,'deterministic checks')

if __name__=='__main__':
    main()
