#!/usr/bin/env python3
"""Supplementary exact-formula and finite numerical tests for cumulative Neumann heat error."""
from math import pi,sqrt,erfc,exp,expm1,sin,cos,isfinite


def A(z):
    return (1+2*z*z)*erfc(z)-2*z*exp(-z*z)/sqrt(pi)

def h(z):
    return 2*erfc(z)-erfc(z/sqrt(2))

def Q(z):
    return 2*A(z)-A(z/sqrt(2))

def simpson(f,left,right,n=3000):
    assert n%2==0
    delta=(right-left)/n
    acc=f(left)+f(right)
    for j in range(1,n):
        acc+=(4 if j%2 else 2)*f(left+delta*j)
    return delta*acc/3

def bisect(f,lo,hi,n=90):
    assert f(lo)*f(hi)<0
    for _ in range(n):
        mid=(lo+hi)/2
        if f(mid)*f(lo)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

root=bisect(Q,.6,1.0)
G=lambda z:simpson(Q,0,z,n=1800)
assert abs(root-.77239728443447)<2e-11
assert abs(G(root)-.25718813959451015)<2e-10
assert abs(2*(2-sqrt(2))/(3*sqrt(pi))-.22032973752843146)<1e-12
checks=3

for i in range(1,101):
    z=.012*i
    eps=1e-4
    assert abs((A(z+eps)-A(z-eps))/(2*eps)-(4*z*erfc(z)-4*exp(-z*z)/sqrt(pi)))<2e-6
    assert abs((A(z+eps)-2*A(z)+A(z-eps))/eps**2-4*erfc(z))<3e-5
    assert abs((G(z+eps)-G(z-eps))/(2*eps)-Q(z))<2e-6
    checks+=3

for z in (.1,.25,.5,.75,1.,1.2,1.5,2.):
    quad=simpson(lambda u:erfc(z/sqrt(u)) if u>0 else 0.,0,1,n=3000)
    assert abs(quad-A(z))<2e-7,(z,quad,A(z))
    checks+=1

for i in range(1,100):
    z=.025*i
    assert (Q(z)>0)==(z<root)
    checks+=1

# Stable spectral time-integral formula; b_n is a positive loss correction.
def b_n(T,n):
    v=pi*pi*n*n*T
    return (1.5-2*exp(-v)+.5*exp(-2*v))/(pi*pi*n*n)

def J(T,s,N=6000):
    return T*s*(1-s)-sum((2/(pi*pi*n*n))*b_n(T,n)*sin(pi*n*s)**2 for n in range(1,N+1))

def Jsum(T,s,N=300):
    return sum(2*sin(pi*n*s)**2/(pi*pi*n*n)*(T-b_n(T,n)) for n in range(1,N+1))

def Jsecond(T,s,N=2000):
    return -2*T-4*sum(b_n(T,n)*cos(2*pi*n*s) for n in range(1,N+1))

def F(T,s,N=1000):
    return sum((2/(pi*pi*n*n))*(-expm1(-pi*pi*n*n*T))**2*sin(pi*n*s)**2 for n in range(1,N+1))

for T in (.003,.01,.1,.5,1.,2.):
    for s in (.13,.25,.31,.4,.5,.67,.85):
        assert abs(J(T,s,1800)-J(T,1-s,1800))<5e-13
        assert J(T,s,1800)>0
        # Integrate Fourier sums numerically on a coarser set of time grid nodes.
        raw=simpson(lambda t:F(t,s,260),0,T,n=300)
        clipped=Jsum(T,s,260)
        assert abs(raw-clipped)<5e-5,(T,s,raw,clipped)
        checks+=3

for T in (.5,1.,2.,5.):
    for i in range(1,100):
        s=i/100
        assert Jsecond(T,s,1000)<0,(T,s,Jsecond(T,s,1000))
        assert J(T,.5,1000)>J(T,s,1000) if abs(s-.5)>1e-12 else True
        checks+=2

for T in (.002,.005,.01):
    proposed=root*sqrt(T)
    step=.005*sqrt(T)
    # Peak is inside near-wall region and beats the bulk plateau.
    assert J(T,proposed,3500)>J(T,.5,3500)
    assert J(T,proposed,3500)>J(T,proposed-5*step,3500)
    assert J(T,proposed,3500)>J(T,proposed+5*step,3500)
    assert abs(J(T,proposed,3500)/(T**1.5)-G(root))<.002
    checks+=4

print('PASS',checks,'finite checks; root',format(root,'.15g'),'coefficient',format(G(root),'.15g'))
