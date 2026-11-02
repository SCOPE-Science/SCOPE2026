#!/usr/bin/env python3
"""Numerical cross-checks for regular-polygon central chord formulas.

All tests are finite diagnostics; the accompanying proof establishes the theorems.
Requires Python 3 standard library only.
"""
import math


def sec(t):
    return 1.0 / math.cos(t)


def analytic_quantile(n, p, radius):
    b = math.pi / n
    r = radius * math.cos(b)
    if n % 2 == 0:
        return 2.0 * r * sec(b*p)
    return r * (sec(b * (1.0+p)/2.0) + sec(b*(1.0-p)/2.0))


def ray_polygon(n, theta, radius):
    pts = [(radius*math.cos(2*math.pi*j/n),
            radius*math.sin(2*math.pi*j/n)) for j in range(n)]
    dx,dy=math.cos(theta),math.sin(theta)
    ts=[]
    for j in range(n):
        x,y=pts[j]
        xx,yy=pts[(j+1)%n]
        ex,ey=xx-x,yy-y
        det=dx*ey-dy*ex
        if abs(det)<1e-13:
            continue
        t=(x*ey-y*ex)/det
        s=(x*dy-y*dx)/det
        if -1e-10<=s<=1+1e-10:
            ts.append(t)
    assert len(ts)>=2,(n,theta,ts)
    return max(ts)-min(ts)


def exact_moments(n, radius):
    b=math.pi/n
    r=radius*math.cos(b)
    m=2*r*math.log(sec(b)+math.tan(b))/b
    if n%2==0:
        m2=4*r*r*math.tan(b)/b
    else:
        m2=2*r*r*(math.tan(b)-2*math.log(math.cos(b))/math.sin(b))/b
    return m,m2


def simpson(f, segments=4096):
    assert segments%2==0
    h=1/segments
    val=f(0)+f(1)
    for j in range(1,segments):
        val+=(4 if j%2 else 2)*f(j*h)
    return h*val/3


def check():
    tests=0
    for n in [3,4,5,6,7,8,9,11,12,15,16,23,24,37]:
        rad=1.3
        for j in range(97):
            theta=math.pi*((j+0.381234705)/97)
            direct=ray_polygon(n,theta,rad)
            # Find nearest positive ray wall normal, then opposite.
            norms=[2*math.pi*(k+0.5)/n for k in range(n)]
            def length_ray(angle):
                gap=min(abs(math.remainder(angle-a,2*math.pi)) for a in norms)
                return rad*math.cos(math.pi/n)*sec(gap)
            via_wall=length_ray(theta)+length_ray(theta+math.pi)
            assert abs(direct-via_wall)<2e-10,(n,theta,direct,via_wall)
            tests+=1
        em1,em2=exact_moments(n,rad)
        sm1=simpson(lambda u:analytic_quantile(n,u,rad))
        sm2=simpson(lambda u:analytic_quantile(n,u,rad)**2)
        assert abs(em1-sm1)<2e-9,(n,em1,sm1)
        assert abs(em2-sm2)<3e-9,(n,em2,sm2)
        tests+=2
        if n%2:
            b=math.pi/n
            for j in range(71):
                u=(j+0.27)/71
                z=analytic_quantile(2*n,u,rad)
                t=math.cos(b)*z/(1-(math.tan(b/2)**2)*z*z/(4*rad*rad))
                direct=analytic_quantile(n,u,rad)
                assert abs(t-direct)<1e-11,(n,u,t,direct)
                tests+=1
    for n in [800,801,1200,1201]:
        b=math.pi/n
        got=simpson(lambda u:(2-analytic_quantile(n,u,1))/(b*b),8192)
        expect=2/3 if n%2==0 else 2/3
        assert abs(got-expect)<2e-5,(n,got,expect)
        tests+=1
    print('VERIFY_OK')
    print('independent_ray_edge_and_moment_transport_checks',tests)
    print('finite tests do not replace analytic proof')

if __name__=='__main__':
    check()
