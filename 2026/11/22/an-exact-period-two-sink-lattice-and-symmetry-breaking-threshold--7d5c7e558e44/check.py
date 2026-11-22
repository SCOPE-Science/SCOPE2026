"""Reproducibility checks for an exact sinusoidal planar period-two theorem.

Only the standard Python library is required. Numeric checks are diagnostics;
the accompanying written proof supplies the exhaustive analytic arguments.
"""
import math

pi=math.pi

def f(a,x,y):
    return x+math.sin(x+y),a*x

def central_theta(a):
    c=(a-1)/2
    assert c>1
    lo,hi=0.0,pi
    for _ in range(100):
        theta=(lo+hi)/2
        if theta/math.sin(theta)<c: lo=theta
        else: hi=theta
    return (lo+hi)/2

def central(a,m=0):
    theta=central_theta(a)
    d=math.sin(theta)
    s=4*pi*m/(a+1)
    return ((s-d)/2,a*(s+d)/2),((s+d)/2,a*(s-d)/2),theta

def side(a,m=0,sgn=1):
    assert 1+pi<a<1+2*pi and sgn in (-1,1)
    d=pi/(a-1)
    phi=math.acos(d)
    s=2*(2*pi*m+sgn*phi)/(a+1)
    return ((s-d)/2,a*(s+d)/2),((s+d)/2,a*(s-d)/2),phi

def transition(a,P,Q):
    assert abs(f(a,*P)[0]-Q[0])<1e-10
    assert abs(f(a,*P)[1]-Q[1])<1e-10
    assert abs(f(a,*Q)[0]-P[0])<1e-10
    assert abs(f(a,*Q)[1]-P[1])<1e-10

def multiply(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def jac(a,P):
    t=math.cos(P[0]+P[1]); return ((1+t,t),(a,0.0))

def floquet(a,P,Q):
    M=multiply(jac(a,Q),jac(a,P))
    tr=M[0][0]+M[1][1]
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return tr,det

def one_step_modulus(a,t):
    tr=1+t; det=-a*t
    disc=tr*tr-4*det
    if disc<0: return math.sqrt(det)
    return max(abs((tr+math.sqrt(disc))/2),abs((tr-math.sqrt(disc))/2))

def critical_a():
    lo,hi=pi/2,pi-1e-10
    for _ in range(100):
        th=(lo+hi)/2
        a=1+2*th/math.sin(th)
        if -a*math.cos(th)<1: lo=th
        else: hi=th
    th=(lo+hi)/2
    return 1+2*th/math.sin(th)

assert abs(critical_a()-4.659463703928983)<1e-12
for a in (3.2,4.0,1+pi,4.15,4.3,4.6,critical_a(),4.7,6.9):
    for m in (-3,0,5):
        P,Q,th=central(a,m)
        transition(a,P,Q)
        tr,det=floquet(a,P,Q)
        t=math.cos(th)
        assert abs(det-(a*t)**2)<1e-8
        assert abs(tr-((1+t)**2+2*a*t))<1e-8
        expected=(1+pi<a<critical_a())
        assert (one_step_modulus(a,t)<1-1e-7)==expected if min(abs(a-(1+pi)),abs(a-critical_a()))>1e-6 else True
        if a>1+pi:
            for sign in (-1,1):
                B,C,phi=side(a,m,sign)
                transition(a,B,C)
                tr,det=floquet(a,B,C)
                v2=1-(pi/(a-1))**2
                assert abs(tr-(1-v2))<1e-8
                assert abs(det+a*a*v2)<1e-8
                assert 1-tr+det <0
# Exact polynomial identity for side branches: p(1)=-(a*a-1)*v*v.
for a in (1+pi+.001,4.3,4.7):
    d=pi/(a-1)
    phi=math.acos(d)
    assert abs(phi/math.sqrt(a-1-pi)-math.sqrt(2/pi))<.05 if a<4.2 else True
print('VERIFY_OK', 'critical_a=',repr(critical_a()))
