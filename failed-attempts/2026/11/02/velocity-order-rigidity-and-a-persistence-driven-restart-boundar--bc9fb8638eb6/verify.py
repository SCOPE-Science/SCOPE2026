#!/usr/bin/env python3
"""Reproduce finite checks for a reflected active-velocity first-passage calculation.

Uses the standard library only. None of the finite checks substitutes for the
coupling, renewal, perturbation, or asymptotic arguments in the accompanying proof.
"""
import math
import random

CHECKS = 0

def check(condition, context):
    global CHECKS
    if not condition:
        raise AssertionError(context)
    CHECKS += 1

def close(a, b, rel=1e-7, abs_tol=1e-9):
    return abs(a-b) <= abs_tol + rel*max(abs(a), abs(b))

def f0(s, x, D=1., L=1.):
    k = math.sqrt(s/D)
    return math.cosh(k*(L-x))/math.cosh(k*L)

def g(s, x, tau, D=1., L=1.):
    k = math.sqrt(s/D)
    q = math.sqrt((s+1/tau)/D)
    B = tau*k*math.tanh(k*L)
    A = - (tau*k*k/math.cosh(k*L)/q+B*math.sinh(q*L))/math.cosh(q*L)
    return -tau*k*math.sinh(k*(L-x))/math.cosh(k*L)+A*math.sinh(q*x)+B*math.cosh(q*x)

def solve_mixed(rhs, D, tau, L, n=1000):
    # solve (-D d_x^2 + 1/tau) u = rhs; u(0)=0, u'(L)=0.
    h=L/n
    xs=[i*h for i in range(n+1)]
    diag=[0.0]*n
    lower=[0.0]*n
    upper=[0.0]*n
    f=[0.0]*n
    b0=D/h**2
    for j in range(n):
        i=j+1
        diag[j]=2*b0+1/tau
        lower[j]=-b0
        upper[j]=-b0
        f[j]=rhs(xs[i])
    lower[n-1]=-2*b0
    upper[n-1]=0
    for j in range(1,n):
        t=lower[j]/diag[j-1]
        diag[j]-=t*upper[j-1]
        f[j]-=t*f[j-1]
    u=[0.0]*(n+1)
    u[n]=f[n-1]/diag[n-1]
    for j in range(n-2,-1,-1):
        u[j+1]=(f[j]-upper[j]*u[j+2])/diag[j]
    return xs,u

def interp(xs,ys,x):
    p=x/(xs[-1]/(len(xs)-1))
    i=min(len(xs)-2,int(p))
    return ys[i]*(1-(p-i))+ys[i+1]*(p-i)

def moments(D,L,tau,n=1000):
    m1=lambda x: (L*x-x*x/2)/D
    m1p=lambda x:(L-x)/D
    m2=lambda x: (2*L**3*x/3-L*x**3/3+x**4/12)/D**2
    m2p=lambda x:(2*L**3/3-L*x*x+x**3/3)/D**2
    xs,a=solve_mixed(m1p,D,tau,L,n)
    def rhsb(x):return 2*interp(xs,a,x)+m2p(x)
    xs,b=solve_mixed(rhsb,D,tau,L,n)
    xc=L*(1-1/math.sqrt(5))
    at=interp(xs,a,xc)
    bt=interp(xs,b,xc)
    gphase=2*m1(xc)*at-bt/2
    slope=(math.sqrt(5)*L**3)/(15*D**2)
    return -gphase/slope, xs,a,b

def f_drift(s,x,c,D=1.,L=1.):
    q=math.sqrt(c*c+4*D*s)/(2*D)
    def C(y):return math.cosh(q*y)-c*math.sinh(q*y)/(2*D*q)
    return math.exp(-c*x/(2*D))*C(L-x)/C(L)

def reflected_upper_path(noise, v0, tau, eps, dt, L, x0):
    # Exact discrete OU relaxation without OU noise, with identical position noise.
    x=x0
    v=v0
    for step in noise:
        dy=eps*v*tau*(1-math.exp(-dt/tau))+step
        x=min(L,x+dy)
        if x<=0:
            return False
        v*=math.exp(-dt/tau)
    return True

def run():
    # Mixed-boundary scalar ODE and sign against independent finite differences.
    for D,L,tau,s in [(1.,1.,.1,.5),(.7,1.2,.6,2.),(2.,.8,2.,.3),(1.,2.,.3,4.)]:
        dx=0.0005
        for j in range(1,60):
            x=0.03+j*(L-.06)/61
            val=g(s,x,tau,D,L)
            resid=D*(g(s,x+dx,tau,D,L)-2*val+g(s,x-dx,tau,D,L))/dx**2-(s+1/tau)*val
            k=math.sqrt(s/D)
            fp=-k*math.sinh(k*(L-x))/math.cosh(k*L)
            check(close(resid,-fp,rel=1.5e-4,abs_tol=2e-4),('ODE',D,L,tau,s,x,resid,-fp))
            check(val<0,('strict-sign',x,tau,s))
        check(abs(g(s,0,tau,D,L))<1e-9,'Dirichlet')
        h=1e-5
        check(abs((g(s,L,tau,D,L)-g(s,L-h,tau,D,L))/h)<3e-4,'Neumann')
    # The exact linear response to fixed drift is the tau-infinity limit.
    for s in [.1,.5,2.,10.]:
        for x in [.15,.35,.7]:
            h=1e-5
            response=(f_drift(s,x,h)-f_drift(s,x,-h))/(2*h)
            # For constant v the correction solves Dg''-sg=-f0'.
            k=math.sqrt(s)
            fprime=-k*math.sinh(k*(1-x))/math.cosh(k)
            # Exact drift derivative computed from independent closed propagator.
            approx=g(s,x,1e7)
            check(close(response,approx,rel=6e-6,abs_tol=1e-6),('drift-limit',s,x,response,approx))
            check(fprime<0,'passive-derivative')
    # Quadratic infinitesimal-restart phase boundary, independent asymptotic limits.
    xstar=1-1/math.sqrt(5)
    def M1(x):return x-x*x/2
    def M2(x):return 2*x/3-x**3/3+x**4/12
    for i in range(1,100):
        x=i/100
        h0=M1(x)**2-M2(x)/2
        poly=x*(x-2)*(4-10*x+5*x*x)/24
        check(close(h0,poly,abs_tol=1e-13),('phase-poly',x))
        check((h0<0)==(x<xstar),'phase-sign')
    small,_,_,_=moments(1.,1.,0.0005,1600)
    large,_,_,_=moments(1.,1.,1e6,1600)
    check(close(small/0.0005,-1,rel=.035),'short-persistence-slope')
    check(close(large,4/125,rel=.005),'long-persistence-slope')
    check(small<0 and large>0,'opposite-phase-shift-signs')
    # A finite observation of an intervening zero, not a proof of uniqueness.
    mids=[moments(1.,1.,t,900)[0] for t in [.1,.5,1.,2.,5.,10.]]
    check(mids[0]<0 and mids[-1]>0,'crossover-bracket')
    # Renewal formulas, slopes, and pathwise ordering for a collection of forced paths.
    for r in [.1,.5,2.,5.,20.]:
        for s in [.1,1.,3.]:
            x=.4; tau=.6
            f=f0(s+r,x)
            gg=g(s+r,x,tau)
            dF=s*(s+r)*gg/(s+r*f)**2
            check(dF<0,'renewal-Laplace-negative-susceptibility')
        ff=f0(r,.4);gg=g(r,.4,.6)
        dm=-gg/(r*ff*ff)
        check(dm>0,'MFPT-positive-response')
    rng=random.Random(260921124)
    for _ in range(500):
        noise=[rng.gauss(0,.06) for j in range(200)]
        slower=reflected_upper_path(noise,-1,.6,.7,.02,1.,.4)
        faster=reflected_upper_path(noise,1,.6,.7,.02,1.,.4)
        check(not (slower and not faster),'path-order')
    print('PASS:',CHECKS,'finite checks; small-tau shift',small,'large-tau shift',large)

if __name__=='__main__':
    run()
