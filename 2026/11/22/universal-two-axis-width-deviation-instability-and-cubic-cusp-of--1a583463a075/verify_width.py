#!/usr/bin/env python3
"""Independent numerical checks of orthodiagonal quadrilateral width expansions.

Uses direct support extrema of all four vertices and Simpson integration.
The non-asymptotic theorem is proved analytically in RESULT.md; finite tests do
not establish an all-parameter statement.
"""
import math

PI = math.pi


def integrate(f, n=16000):
    assert n > 0 and n % 2 == 0
    dtheta = (PI/2)/n
    z = f(0.0)+f(PI/2)
    z += 4.0*sum(f(j*dtheta) for j in range(1,n,2))
    z += 2.0*sum(f(j*dtheta) for j in range(2,n-1,2))
    return z*dtheta/3.0


def vertices(t,s,h):
    assert t>0 and abs(s)<1 and abs(h)<t
    return ((s-1.,0.),(s+1.,0.),(0.,h-t),(0.,h+t))


def direct_width(verts,theta):
    c,z=math.cos(theta),math.sin(theta)
    values=[x*c+y*z for (x,y) in verts]
    return max(values)-min(values)


def direct_delta_squared(t,s,h,n=16000):
    verts=vertices(t,s,h)
    f=lambda theta: direct_width(verts,theta)
    mean=(integrate(f,n)+integrate(lambda theta:f(-theta),n))/PI
    second=(integrate(lambda theta:f(theta)**2,n)
            +integrate(lambda theta:f(-theta)**2,n))/PI
    return second/(mean*mean)-1.0


def I0(t):
    return PI+2*(t*t-1)*math.atan(t)+2*t


def H(t):
    return I0(t)-4*t


def exact_base(t):
    return PI*I0(t)/(8*(1+t*t))-1.0


def asymptotic(t,s,h):
    q=t*t*s*s+h*h
    r6=(1+t*t)**3
    quadratic=-PI*H(t)*q/(8*r6)
    cubic=PI*(abs(t*s+h)**3+abs(t*s-h)**3)/(12*r6)
    return exact_base(t)+quadratic+cubic


def exact_kite_delta_squared(t,h):
    u,v=t-abs(h),t+abs(h)
    assert u>0
    J=PI+0.5*((u*u+2*u*v-1)*math.atan(u)
                 +(v*v-3)*math.atan(v)+u+3*v)
    perimeter=2*(math.hypot(1,u)+math.hypot(1,v))
    # mean = perimeter/pi and second = 2J/pi
    return 2*PI*J/(perimeter*perimeter)-1


def check():
    checked=0
    # Independent projection quadrature versus analytic base formula
    for t in (0.17,0.37,0.73,1.,1.6,3.8,11.):
        val=direct_delta_squared(t,0.,0.)
        assert abs(val-exact_base(t))<2e-9,(t,val,exact_base(t))
        checked+=1
    # Analytic kite formula versus independent direct vertex projection
    for t in (.3,.6,1.,1.8,3.):
        for ratio in (.09,.31,.61,.86):
            h=t*ratio
            val=direct_delta_squared(t,0.,h)
            exp=exact_kite_delta_squared(t,h)
            assert abs(val-exp)<3e-8,(t,h,val,exp)
            checked+=1
    # Perturbations in both diagonals (generically not kites).
    cases=[(.04,.03),(.03,-.04),(.03,.03),(.05,0.),(0.,.05),
           (.02,.02),(.04,-.02),(.045,.015)]
    for t in (.35,.7,1.,1.8,3.8):
        for s,hr in cases:
            h=hr*t
            exact=direct_delta_squared(t,s,h)
            approx=asymptotic(t,s,h)
            scale=max(abs(s),abs(h))
            assert abs(exact-approx)<0.6*scale**4+4e-8,(t,s,h,exact,approx)
            checked+=1
    # The strict local decrease is tested with two-parameter nonkite skews.
    for t in (.1,.27,.5,1.,2.,4.,9.):
        for u,v in ((.01,.01),(.02,.015),(-.015,.02),(.01,0.),(0.,.01)):
            exact=direct_delta_squared(t,u,t*v)
            assert exact < exact_base(t),(t,u,v,exact,exact_base(t))
            checked+=1
    # Asymptotic sign H(t)>0 is proved for every positive t in RESULT.md.
    for k in range(1,101):
        t=math.exp((k-50)*.12)
        assert H(t)>0,t
        checked+=1
    assert abs(exact_base(1.)-(PI*(PI+2)/16-1))<1e-13
    checked+=1
    print(f"ALL_CHECKS_PASSED: {checked} numerical regressions")


if __name__=='__main__':
    check()
