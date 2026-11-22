#!/usr/bin/env python3
"""Standalone numerical/algebraic checks for the Gaussian-perception resource theorem.
All steps use the Python standard library. Numerical tests complement, not replace, the proof.
"""
from math import erf, exp, log, sqrt
from fractions import Fraction as F


def omega(c, sigma, n):
    k = sigma * sqrt(2)
    return (erf(n/k) + erf((c-n)/k))/(erf(n/k)+erf((1-n)/k))


def root(c, sigma):
    lo, hi = 0., 1.
    for _ in range(90):
        mid=(lo+hi)/2
        if omega(c,sigma,mid)>c:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def logit(x):
    return log(x/(1-x))


def logistic(v):
    return 1/(1+exp(-v))


def rk4(y0, derivative, step, total):
    y=y0
    for i in range(round(total/step)):
        t=i*step
        a=derivative(t,y)
        b=derivative(t+step/2,y+step*a/2)
        c=derivative(t+step/2,y+step*b/2)
        d=derivative(t+step,y+step*c)
        y+=step*(a+2*b+2*c+d)/6
    return y


def check_replicator():
    # The payoff slice R=S=0,T=P=1 produces exact phenotype fitness:
    # LL=w, LH=0, HL=1, HH=1-w.
    for z in [(0.1,0.2,0.3,0.4),(0.25,)*4,(0.37,0.1,0.28,0.25)]:
        zll,zlh,zhl,zhh=z
        x=zll+zlh; y=zll+zhl; D=zll-x*y
        for w in [.03,.2,.6,.94]:
            f=(w,0.,1.,1-w)
            avg=sum(zi*fi for zi,fi in zip(z,f))
            zd=[zi*(fi-avg) for zi,fi in zip(z,f)]
            xd=zd[0]+zd[1]; yd=zd[0]+zd[2]
            Dd=zd[0]-xd*y-x*yd
            xp=-(1-w)*x*(1-x)+w*D
            yp=w*y*(1-y)-(1-w)*D
            Dp=-((1-w)*(1-2*x)-w*(1-2*y))*D
            assert max(abs(xd-xp),abs(yd-yp),abs(Dd-Dp))<3e-15
    print('PASS exact phenotype-payoff/aggregate-equations reconstruction')


def check_high_noise():
    for c in [.2,.5,.8]:
        A=(1+c)/3
        vals=[]
        for s in [1.,3.,10.,30.]:
            nstar=root(c,s)
            assert 0<nstar<1
            assert abs(omega(c,s,nstar)-c)<4e-12
            vals.append(nstar)
            if s>=10:
                assert abs(nstar-A)<.2/s**2
                for n in [.05,.25,.5,.8,.97]:
                    predicted=c*(1-c)*(A-n)/2
                    actual=s*s*(omega(c,s,n)-c)
                    assert abs(predicted-actual)<.04/s**2
        print(f'c={c:.1f}: equilibria sigma=[1,3,10,30] {vals}; limit {A:.12f}')
    # independent rational-moment identity for Gaussian expansion
    for c in [F(1,5),F(1,2),F(4,5)]:
        A=(1+c)/3
        for n in [F(0),F(1,3),F(3,4),F(1)]:
            num_m2=c**3/3-n*c*c+n*n*c
            den_m2=F(1,3)-n+n*n
            assert (c*den_m2-num_m2)/2 == c*(1-c)*(A-n)/2
    print('PASS exact rational asymptotic moments and high-noise root checks')


def check_infinite_noise():
    for c in [.2,.5,.8]:
        for x0,y0 in [(.5,.5),(.3,.75),(.65,.4)]:
            eps=1.4; n0=.8
            p=1-c
            # k=-1, D=0: x'=-(1-c)x(1-x), y'=c*y(1-y)
            def x(t): return logistic(logit(x0)-p*t)
            def y(t): return logistic(logit(y0)+c*t)
            def deriv(t,L):return eps/c*(p*x(t)+c*y(t)-c)
            Lend=rk4(logit(n0),deriv,.015,120.)
            target=logit(n0)+(eps/c)*log(y0/(1-x0))
            assert abs(Lend-target)<2e-7,(Lend,target)
            if x0==y0==.5:assert abs(logistic(Lend)-n0)<2e-7
    print('PASS infinite-noise logistic-odds memory formula')


def check_slow_time():
    c=.2; eps=1; center=(1+c)/3
    # Coarse check of limiting cubic on tau in [delta,T] from the fast-system complete ODE.
    def cubic(t, n):return eps*(1-c)*n*(1-n)*(center-n)/2
    for tau in [1.,4.,10.]:
        slow=rk4(.8,cubic,.001,tau)
        print(f'cubic slow-time tau={tau:g}: resource={slow:.10f}')
    # Directly integrate the finite-noise full ecological ODE on the same slow clock.
    # This is a non-proof consistency check of the stated crossover theorem.
    dt=.4
    for sigma in [10.,20.]:
        x=y=.5; n=.8
        targets={int(round(sigma*sigma/dt)):1.,int(round(4*sigma*sigma/dt)):4.}
        for i in range(1,max(targets)+1):
            def rates(a,b,h):
                w=omega(c,sigma,h);p=1-w
                return (-p*a*(1-a),w*b*(1-b),eps/c*(p*a+w*b-c)*h*(1-h))
            u=rates(x,y,n)
            v=rates(x+dt*u[0]/2,y+dt*u[1]/2,n+dt*u[2]/2)
            w=rates(x+dt*v[0]/2,y+dt*v[1]/2,n+dt*v[2]/2)
            q=rates(x+dt*w[0],y+dt*w[1],n+dt*w[2])
            x+=dt*(u[0]+2*v[0]+2*w[0]+q[0])/6
            y+=dt*(u[1]+2*v[1]+2*w[1]+q[1])/6
            n+=dt*(u[2]+2*v[2]+2*w[2]+q[2])/6
            if i in targets:
                tau=targets[i]
                slow=rk4(.8,cubic,.002,tau)
                assert abs(n-slow)<.003,(sigma,tau,n,slow)
                print(f'finite sigma {sigma:g}, tau={tau:g}: actual resource {n:.9f}; cubic {slow:.9f}')
    print('PASS finite-noise slow-time comparison and limiting cubic integration')


if __name__=='__main__':
    check_replicator()
    check_high_noise()
    check_infinite_noise()
    check_slow_time()
    print('ALL CHECKS PASSED')
