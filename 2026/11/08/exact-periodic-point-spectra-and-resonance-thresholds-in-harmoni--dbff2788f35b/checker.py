"""Numerical cross-checks for the outer-billiard trace and resonance laws.

Run: python3 checker.py
Uses only Python's standard library. Does not constitute an infinite proof.
"""
import math


def gamma(t, n, e):
    return complex(math.cos(t)+e*math.cos(n*t), math.sin(t)+e*math.sin(n*t))


def tangent(t, n, e):
    return complex(-math.sin(t)-n*e*math.sin(n*t), math.cos(t)+n*e*math.cos(n*t))


def acceleration(t, n, e):
    return complex(-math.cos(t)-n*n*e*math.cos(n*t), -math.sin(t)-n*n*e*math.sin(n*t))


def cross(a,b):
    return (a.conjugate()*b).imag


def outer_step(point, n, e, t_start):
    # For a known tangent branch near t_start solve cross(point-gamma(t),gamma'(t))=0.
    t=t_start
    for _ in range(16):
        p=gamma(t,n,e)
        v=tangent(t,n,e)
        f=cross(point-p,v)
        der=cross(point-p,acceleration(t,n,e))
        delta=f/der
        t-=delta
        if abs(delta)<2e-14:
            break
    assert abs(cross(point-gamma(t,n,e),tangent(t,n,e)))<1e-9
    assert ((point-gamma(t,n,e)).conjugate()*tangent(t,n,e)).real < 0
    return 2*gamma(t,n,e)-point


def expected_trace(n,e,s):
    theta=2*math.pi/(n-1)
    v=1+s*n*e
    w=1+s*n*n*e
    R=1+s*e
    return 2+4*math.cos(theta)**2*(v*v/(R*w)-1)


def numerical_trace(n,e,s):
    theta=2*math.pi/(n-1)
    t0=(0 if s>0 else math.pi/(n-1))+2*theta
    point=(1+s*e)/math.cos(theta)*complex(math.cos(t0-theta),math.sin(t0-theta))
    step=outer_step(point,n,e,t0)
    expected=point*complex(math.cos(2*theta),math.sin(2*theta))
    assert abs(step-expected)<1e-9,(n,s,e,step,expected)
    h=1e-6
    dx=(outer_step(point+h,n,e,t0)-outer_step(point-h,n,e,t0))/(2*h)
    dy=(outer_step(point+1j*h,n,e,t0)-outer_step(point-1j*h,n,e,t0))/(2*h)
    # trace of R(-2theta) times real Jacobian
    rotation=complex(math.cos(-2*theta),math.sin(-2*theta))
    return (rotation*dx).real+(rotation*dy).imag, (dx.real*dy.imag-dx.imag*dy.real)


def eigenphase_max(n):
    c=math.cos(2*math.pi/(n-1))
    return math.acos(1-c*c*(n-1)**2/(n*n+1))


def resonance(n,j):
    N=n-1
    k=N//math.gcd(N,2)
    c=math.cos(2*math.pi/N)
    A=1-math.cos(j*math.pi/k)
    B=2*c*c*N*N-(1+n*n)*A
    disc=B*B-4*n*n*A*A
    assert disc>0
    return 2*A/(B+math.sqrt(disc))


def run():
    count=0
    for n in range(6,19):
        for frac in (0.04,0.16,0.42,0.8):
            e=frac/(n*n)
            for s in (-1,1):
                t,det=numerical_trace(n,e,s)
                predicted=expected_trace(n,e,s)
                assert abs(t-predicted)<2e-6, (n,e,s,t,predicted)
                assert abs(det-1)<2e-6,(n,e,s,det)
                assert (t>2 if s<0 else -2<t<2)
                count+=1
    resonances=0
    for n in range(6,110):
        k=(n-1)//math.gcd(n-1,2)
        lim=k*eigenphase_max(n)/math.pi
        allj=[j for j in range(1,k) if j<lim]
        for j in allj:
            e=resonance(n,j)
            assert 0<e<1/(n*n)
            t=expected_trace(n,e,1)
            angle=math.acos(t/2)
            assert abs(k*angle-j*math.pi)<2e-9,(n,j,k*angle,j*math.pi)
            resonances+=1
        if allj:
            assert all(resonance(n,j)<resonance(n,j+1) for j in allj[:-1])
    print('PASS',count,'finite-difference Jacobian comparisons; ',resonances,'resonance equations checked')

if __name__=='__main__':
    run()
