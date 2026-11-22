"""Independent numerical diagnostics for near-extremal affine sections of solid ball caps.
Uses quadrature of the exact disk section and direct normal/offset integrations.
"""
import math
import numpy as np
from scipy.integrate import quad

pi=math.pi

def M3(h):
    r=math.sqrt(1-h*h)
    J=lambda a:(a*math.sqrt(max(0,1-a*a))+math.asin(a))/2
    if h>=0:return 2*pi*(r*(pi/4+J(h))+1-h-h*(1-h*h)/2)
    a=-h
    return 2*pi*(1+a+a*(1-a*a)/2+r*(pi/4-J(a)))

def sect(h,theta,s):
    r=np.sqrt(np.maximum(0,1-s*s));st=np.sin(theta)
    v=(h-s*np.cos(theta))/(np.maximum(st*r,1.e-200))
    vc=np.clip(v,-1,1)
    return np.where(v<=-1,pi*r*r,np.where(v>=1,0,r*r*(np.arccos(vc)-vc*np.sqrt(np.maximum(0,1-vc*vc)))))

def nearprob(h,eps,N=1000):
    if h<-.02:
        # s~=sqrt(eps), theta is in the full polar cone
        sm=1.2*math.sqrt(eps/pi)
        tm=math.asin(-h)+0.3
    elif h>.02:
        c=2*pi*h
        sm=max(.02,4*eps/c)+h
        tm=max(.02,4*eps/(c*math.sqrt(1-h*h)))
    else:
        sm=5*math.sqrt(eps)+abs(h)
        tm=5*math.sqrt(eps)+abs(h)
    ss=np.linspace(-sm,sm,N) if h<.02 else np.linspace(max(-1,h-.002),min(1,sm),N)
    th=np.linspace(0,min(pi/2,tm),N)
    target=pi*(1-max(h,0)**2)-eps
    numerator=0
    for start in range(0,N,64):
        A=sect(h,th[None,:],ss[start:start+64,None])
        numerator+=np.sum((A>=target)*np.sin(th)[None,:])
    numerator*=2*pi*(ss[1]-ss[0])*(th[1]-th[0])
    return numerator/M3(h)

def theory(h,eps):
    m=M3(h)
    if h<0:
        om=2*pi*(1-math.sqrt(1-h*h))
        return 2*om/m/math.sqrt(pi)*math.sqrt(eps)
    if h==0:return pi/(3*m*pi**1.5)*eps**1.5
    rho=math.sqrt(1-h*h);c=2*pi*h
    return pi/(3*m*rho*rho*c**3)*eps**3

def cross(lam,eps):
    a=1/math.sqrt(pi)
    T=math.sqrt(max(lam,0)**2+a*a);L=max(lam,-a)
    return (pi/(3*M3(0)))*((T-lam)**3-(L-lam)**3)*eps**1.5

def run():
    tests=0
    for h in (-.4,-.15,0,.2,.4):
        for eps in (2.e-3,5.e-4):
            actual=nearprob(h,eps)
            predicted=theory(h,eps)
            rel=actual/predicted
            print('fixed h,epsilon,ratio',h,eps,rel)
            assert .74<rel<1.28,(h,eps,rel)
            tests+=1
    for lam in (-2,-.5,0,.5,2):
        for eps in (2.e-3,5.e-4):
            actual=nearprob(lam*math.sqrt(eps),eps)
            predicted=cross(lam,eps)
            rel=actual/predicted
            print('critical lambda,epsilon,ratio',lam,eps,rel)
            assert .72<rel<1.34,(lam,eps,rel)
            tests+=1
    for h in (-.7,-.1,0,.2,.6):
        num=quad(lambda th: (2 if h<0 and math.cos(th)<=-h else (2*math.sqrt(1-h*h)*math.sin(th) if h>=0 and math.cos(th)<h else 1-h*math.cos(th)+math.sqrt(1-h*h)*math.sin(th) if h>=0 else 1+(-h)*math.cos(th)+math.sqrt(1-h*h)*math.sin(th)))*math.sin(th)*2*pi,0,pi/2,points=[math.acos(abs(h))],epsabs=2e-10)[0]
        assert abs(num-M3(h))<1e-8,(h,num,M3(h))
        tests+=1
    print(f'PASS {tests} independent numerical checks; numerical tests are not infinite proofs.')
if __name__=='__main__':run()
