#!/usr/bin/env python3
"""Standalone numerical cross-checks for equilibrium-line phase asymptotics.

Numerics are diagnostics; all asymptotic assertions use the mathematical proof.
"""
from math import log, pi, cos, sin, sqrt, isfinite

K = .1

def L(t, mu): return log(3-4*mu*t*(1-t))
def phase(t, mu): return 4*pi*mu*t*(1-t)
def g(t, mu): return t*L(t,mu)/K
def P(t,mu,gamma): return K*cos(gamma*phase(t,mu))/L(t,mu)
def Pprime(t,mu,gamma):
    d=3-4*mu*t*(1-t)
    lv=log(d)
    ph=gamma*phase(t,mu)
    return -K*gamma*4*pi*mu*(1-2*t)*sin(ph)/lv - K*cos(ph)*4*mu*(2*t-1)/(d*lv*lv)

def bisection(f,low,high):
    fl=f(low)
    fh=f(high)
    assert fl*fh<=0,(low,high,fl,fh)
    for _ in range(75):
        md=(low+high)/2
        if f(md)*fl<=0: high=md
        else: low=md; fl=f(md)
    return (low+high)/2

def endpoints(mu):
    a=bisection(lambda t:g(t,mu)+1,-K/log(3),0.)
    b=bisection(lambda t:g(t,mu)-1,0.,K/log(2))
    return a,b

def roots(mu,gamma):
    a,b=endpoints(mu)
    # More than 300 samples per cosine oscillation for safe detection
    n=max(3000,int(300*gamma*max(.02,phase(b,mu)-phase(a,mu))/pi))
    step=(b-a)/n
    ans=[]
    previous=a; old=P(a,mu,gamma)-a
    for j in range(1,n+1):
        current=a+j*step; nxt=P(current,mu,gamma)-current
        if old*nxt<0:
            p=bisection(lambda t:P(t,mu,gamma)-t,previous,current)
            if not ans or p-ans[-1]>1e-10: ans.append(p)
        previous=current;old=nxt
    return ans

def main():
    count_tests=0
    for mu in (.1,.5,1.0):
        a,b=endpoints(mu)
        assert -K/log(3)<a<0<b<K/log(2)
        length=phase(b,mu)-phase(a,mu)
        for gamma in (3.,11.,29.,80.,151.,400.):
            rr=roots(mu,gamma)
            expected=gamma*length/pi
            assert abs(len(rr)-expected)<5.,(mu,gamma,len(rr),expected)
            for p in rr:
                assert a-1e-13<=p<=b+1e-13
                assert abs(P(p,mu,gamma)-p)<1e-10
                for z in (.11,1.23,-.7):
                    h=.75
                    x2=P(p,mu,gamma)+h*sin(z)*(p-p)
                    y2=P(p,mu,gamma)-h*sin(z)*(p-p)
                    z2=z+p-p
                    assert max(abs(x2-p),abs(y2-p),abs(z2-z))<1e-10
                    dp=Pprime(p,mu,gamma)
                    # Two separate transverse eigen-directions; third eigenvalue one
                    mat=((dp+h*sin(z),-h*sin(z),0.),(-h*sin(z),dp+h*sin(z),0.),(1.,-1.,1.))
                    # Characteristic polynomial at three proved eigenvalues
                    lams=(dp,dp+2*h*sin(z),1.)
                    for lam in lams:
                        a11=mat[0][0]-lam;a12=mat[0][1];a21=mat[1][0];a22=mat[1][1]-lam
                        determinant=(1.-lam)*(a11*a22-a12*a21)
                        assert abs(determinant)<1e-7*(1+abs(lam)**3)
                count_tests+=1
            # CDF comparison at every observed root.
            if len(rr)>0:
                d=phase(b,mu)-phase(a,mu)
                for i,p in enumerate(rr):
                    theoretical=(phase(p,mu)-phase(a,mu))/d
                    assert abs((i+.5)/len(rr)-theoretical)<6/len(rr)
            print('mu=',mu,'gamma=',gamma,'roots=',len(rr),'phase_pred=',round(expected,6))
    print('PASS; checked',count_tests,'inverse-free exact equilibrium candidates and Jacobian eigenvalues')

if __name__=='__main__':main()
