#!/usr/bin/env python3
"""Direct-stage checks for two covariance integrators on a rotating rank-one source."""
import cmath
import math


def source(t, omega):
    c=math.cos(omega*t); s=math.sin(omega*t)
    return (c*c, c*s, s*s)


def apply(method, n, h, omega):
    # The integrating-factor update W'=R(-omega*t)e1e1^T R(-omega*t)^T.
    w=(0.,0.,0.)
    for j in range(n):
        t=j*h
        if method==2:
            # SSPRK(2,2), computed in the paper's three-stage Shu-Osher form.
            s0=source(-t,omega)
            w1=tuple(w[i]+h*s0[i] for i in range(3))
            s1=source(-(t+h),omega)
            w2=tuple(w1[i]+h*s1[i] for i in range(3))
            w=tuple((w[i]+w2[i])/2 for i in range(3))
        else:
            # SSPRK(3,3), computed in the paper's five-stage Shu-Osher form.
            s0=source(-t,omega)
            w1=tuple(w[i]+h*s0[i] for i in range(3))
            s1=source(-(t+h),omega)
            w2=tuple(w1[i]+h*s1[i] for i in range(3))
            wm=tuple(3*w[i]/4+w2[i]/4 for i in range(3))
            sm=source(-(t+h/2),omega)
            w3=tuple(wm[i]+h*sm[i] for i in range(3))
            w=tuple(w[i]/3+2*w3[i]/3 for i in range(3))
    return w


def eigs(w):
    a,b,d=w
    D=math.hypot(a-d,2*b)
    return ((a+d-D)/2,(a+d+D)/2)


def predicted(method,n,h,phi):
    if abs(math.sin(phi))<1e-10:  # This branch is used only for exact integer-pi input.
        k=round(phi/math.pi)
        rho=1.0 if method==2 else (1.0 if k%2==0 else 1/3)
    else:
        factor=abs(math.sin(n*phi)/(n*math.sin(phi)))
        rho=factor*(abs(math.cos(phi)) if method==2 else (2+math.cos(phi))/3)
    return n*h*(1-rho)/2,n*h*(1+rho)/2


def close(a,b):
    return abs(a-b)<=3e-10*max(1,abs(a),abs(b))


def run():
    tests=0
    # Direct stage recurrences are algebraically separate from Fourier closed forms.
    for n in range(1,21):
        for phi in [0.12,0.25,0.6,1.0,1.2,1.7,2.0,2.4,2.8,3.6,4.0,4.8,5.5,6.1,
                    1.0e-2,math.pi/2, 2*math.pi/3,math.pi/3,
                    math.pi/5, math.pi*(1+1.e-4), 2*math.pi*(1+2.e-4)]:
            h=0.7
            for method in (2,3):
                z=apply(method,n,h,phi/h)
                actual=eigs(z); formula=predicted(method,n,h,phi)
                for a,b in zip(actual,formula):
                    assert close(a,b),(n,phi,method,actual,formula)
                    tests+=1
                assert actual[0]>=-2e-11
                tests+=1
    # Exact resonances, using positive-sum sampling identities (no floating-point proof).
    # omega*h = pi: trapezoid has weights entirely on e1; Simpson has 1/3 e1, 2/3 e2.
    for n in range(1,51):
        T=n*0.7
        for method,low,hi in ((2,0,T),(3,T/3,2*T/3)):
            r=eigs(apply(method,n,0.7,math.pi/0.7))
            assert close(r[0],low) and close(r[1],hi),(method,n,r)
            tests+=2
        for method in (2,3):
            r=eigs(apply(method,n,0.7,2*math.pi/0.7))
            assert close(r[0],0) and close(r[1],T),(method,n,r)
            tests+=2
    # The transition in the smallest covariance eigenvalue occurs at cos(phi)=-1/2.
    for n in (1,2,3,5,10):
        for phi in (1.0,2.5, 2*math.pi/3, math.pi):
            v2=predicted(2,n,0.7,phi)[0]
            v3=predicted(3,n,0.7,phi)[0]
            c=math.cos(phi)
            if c<-.500001: assert v3>=v2-1e-10
            if c>-.499999 and c<.99999: assert v3<=v2+1e-10
            if abs(c+.5)<1e-10: assert close(v2,v3)
            tests+=1
    print('CHECK_OK',tests,'direct-stage/eigenvalue/phase comparison checks')

if __name__=='__main__':
    run()
