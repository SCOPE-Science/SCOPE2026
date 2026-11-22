"""Numerical and algebraic checks of mode-dependent first-passage crossing for intermittent diffusion and blind ballistic relocations."""
from math import sqrt, exp, log, pi
import random
import numpy as np
from scipy.integrate import quad
from fractions import Fraction


def parameters(D,v,alpha,beta,s):
    L=s+beta
    B=(s+alpha)/D + L*L/(v*v)
    C=s*L*(s+alpha+beta)/(D*v*v)
    disc=B*B-4*C
    assert disc>0
    tm=2*C/(B+sqrt(disc))
    tp=(B+sqrt(disc))/2
    lm,lp=sqrt(tm),sqrt(tp)
    R=s*L/v**2
    phi_m=L**2/(v*v*lm)-lm
    phi_p=L**2/(v*v*lp)-lp
    den=phi_m-phi_p
    assert 0<tm<L**2/v**2<tp and den>0
    A=(tm-R)/lm
    Bcoef=(R-tp)/lp
    assert Bcoef<0 and A+Bcoef<0
    return lm,lp,R,A,Bcoef,den


def fvals(D,v,alpha,beta,s,x):
    lm,lp,R,A,B,den=parameters(D,v,alpha,beta,s)
    L=s+beta
    fm=L*L/(v*v*lm)-lm
    fp=L*L/(v*v*lp)-lp
    K=beta*L/(v*v*lm*lp)
    fd=(fm*exp(-lm*x)-fp*exp(-lp*x))/den
    fv=K*(lp*exp(-lm*x)-lm*exp(-lp*x))/den
    return fd,fv,(A*exp(-lm*x)+B*exp(-lp*x))/den


def direct(D,v,alpha,beta,s,x):
    L=s+beta
    def green(k):
        w=L*L+(v*k)**2
        return 1/(s+alpha+D*k*k-alpha*beta*L/w)
    i=quad(green,0,np.inf,weight='cos',wvar=x,epsabs=2e-11,epsrel=1e-11,limlst=120)[0]/pi
    j=quad(lambda k:green(k)*beta*L/(L*L+(v*k)**2),0,np.inf,weight='cos',wvar=x,epsabs=2e-11,epsrel=1e-11,limlst=120)[0]/pi
    i0=quad(lambda k:green(k),0,np.inf,epsabs=2e-10,epsrel=1e-10)[0]/pi
    return i/i0,j/i0

rng=random.Random(411)
count=0
for q in range(240):
    D=10**rng.uniform(-1,1)
    alpha=10**rng.uniform(-1,1)
    beta=10**rng.uniform(-1,1)
    s=10**rng.uniform(-1,1)
    speed2=D*(s+beta)*10**rng.uniform(-1,1)
    v=sqrt(speed2)
    lm,lp,R,A,B,den=parameters(D,v,alpha,beta,s)
    assert (A>0)==(speed2>D*(s+beta))
    fd0,fv0,diff0=fvals(D,v,alpha,beta,s,0)
    assert abs(fd0-1)<1e-10 and 0<fv0<1 and diff0<0
    if speed2>D*(s+beta):
        xstar=log(-B/A)/(lp-lm)
        assert xstar>0
        for x,mult,sign in [(xstar,0,0),(xstar*.7,0,-1),(xstar*1.5,0,1)]:
            fd,fv,diff=fvals(D,v,alpha,beta,s,x)
            assert abs((fv-fd)-diff)<1e-8
            if sign==0: assert abs(diff)<1e-9
            else: assert diff*sign>0
            count+=1
    else:
        for x in [0,.1,1.,3.]:
            fd,fv,diff=fvals(D,v,alpha,beta,s,x)
            assert diff<0 and fv<fd
            assert abs((fv-fd)-diff)<1e-8
            count+=1

# Independently use the Fourier Green function and spatial-source identity.
for D,v,alpha,beta,s,x in [(1,sqrt(5),1,1,1,2.5),(1,1,1,1,1,.4),(.7,2.2,.5,1.3,.8,.9),(.8,.9,2,.7,1.1,1.1)]:
    fd,fv,_=fvals(D,v,alpha,beta,s,x)
    fd2,fv2=direct(D,v,alpha,beta,s,x)
    assert abs(fd-fd2)<3e-8 and abs(fv-fv2)<3e-8,((fd,fv),(fd2,fv2))
    count+=2

# Exact algebraic root-polynomial comparison at R with rational examples.
for D,v2,alpha,beta,s in [(Fraction(1),Fraction(5),Fraction(1),Fraction(1),Fraction(1)),(Fraction(2),Fraction(3),Fraction(4),Fraction(5),Fraction(6))]:
    L=s+beta; R=s*L/v2
    p=D*v2*R*R-((s+alpha)*v2+D*L*L)*R+s*L*(s+alpha+beta)
    assert p==s*L*beta*(1-D*L/v2)
    count+=1

print('PASS',count,'crossing, denominator, analytic/Fourier, root, boundary assertions')
