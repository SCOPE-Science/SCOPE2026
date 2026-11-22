#!/usr/bin/env python3
"""Independent numerical diagnostics for symmetric spherical-slab shadow laws.

The mathematical argument is contained in RESULT.md; numerical checks do not
prove endpoint asymptotics or uniqueness assertions.
Requires Python 3.9+ and mpmath; no external data files.
"""
from math import acos, asin, cos, sin, sqrt, pi, gamma, log, hypot
from bisect import bisect_left
import mpmath as mp

mp.mp.dps = 48
checks = 0

def close(actual, expected, relative=0.01, absolute=1e-10):
    global checks
    checks += 1
    a, b = float(actual), float(expected)
    assert abs(a-b) <= max(absolute, relative*max(abs(b),1e-12)), (a,b)

def H(t, a):
    """Exact support of a unit ball clipped to |z|<=a, for t=|u_z|."""
    t=mp.mpf(t); a=mp.mpf(a)
    if t <= a: return mp.mpf(1)
    b=mp.sqrt(1-a*a)
    return a*t+b*mp.sqrt(1-t*t)

def loss(t, a):
    """Stable rationalized 1-H(t), avoiding cancellation near tangency."""
    if t <= a: return mp.mpf(0)
    b=mp.sqrt(1-a*a)
    q=mp.sqrt(1-t*t)
    h=a*t+b*q
    return (b*t-a*q)**2/(1+h)

def M(d,a,theta):
    """Normalized mean support of the hyperplane shadow, exact quadrature."""
    a=mp.mpf(a); theta=mp.mpf(theta)
    s=mp.sin(theta)
    if s<=a: return mp.mpf(1)
    c=mp.gamma(mp.mpf(d-1)/2)/(mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d-2)/2))
    limit=mp.acos(a/s)
    return 1-2*c*mp.quad(lambda p: loss(s*mp.cos(p),a)*mp.sin(p)**(d-3),[0,limit])

def critical_constant(d,a):
    a=mp.mpf(a); b=mp.sqrt(1-a*a); alpha=mp.mpf(d-2)/2
    return 2**alpha*mp.gamma(mp.mpf(d-1)/2)/(mp.sqrt(mp.pi)*mp.gamma(alpha+3))*(b/a)**alpha

def sphere_flat_probability(d,a):
    a=mp.mpf(a)
    return mp.betainc(mp.mpf(d-1)/2,mp.mpf('0.5'),0,a*a,regularized=True)

def orient_pdf(d,theta):
    return 2*mp.gamma(mp.mpf(d)/2)/(mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d-1)/2))*mp.sin(theta)**(d-2)

def L_end(d,a):
    assert d>=4
    a=mp.mpf(a); b=mp.sqrt(1-a*a)
    c=mp.gamma(mp.mpf(d-1)/2)/(mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d-2)/2))
    lim=mp.acos(a)
    # substitute z=cos(phi), making numerical integrand smooth for d>=4
    return 2*c*mp.quad(lambda p:(b*mp.cos(p)**2/mp.sin(p)-a*mp.cos(p))*mp.sin(p)**(d-3),[0,lim])

def hull_perimeter(coords):
    """Planar convex hull perimeter, with no geometry library."""
    points=sorted(set(coords))
    def cross(o,p,q): return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
    lower=[]
    for p in points:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    hull=lower[:-1]+upper[:-1]
    return sum(hypot(hull[i][0]-hull[i-1][0],hull[i][1]-hull[i-1][1]) for i in range(len(hull)))

def sampled_projection_perimeter(a,theta,nz=70,nphi=240):
    """Project actual boundary points of the spherical zone, then take hull."""
    pts=[]
    for i in range(nz+1):
        z=a*(2*i/nz-1)
        r=sqrt(1-z*z)
        for j in range(nphi):
            phi=2*pi*j/nphi
            x,y=r*cos(phi),r*sin(phi)
            pts.append((x*cos(theta)-z*sin(theta),y))
    return hull_perimeter(pts)

for d in (3,4,5,7):
    for a_text in ('0.25','0.5','0.8'):
        a=mp.mpf(a_text); b=mp.sqrt(1-a*a); th=mp.asin(a)
        k=critical_constant(d,a)
        close(M(d,a,th*mp.mpf('.95')),1,relative=1e-13)
        close(M(d,a,th),1,relative=1e-13)
        for eta in ('0.0008','0.0003'):
            eta=mp.mpf(eta)
            ratio=(1-M(d,a,th+eta))/(k*eta**(mp.mpf(d+2)/2))
            close(ratio,1,relative=0.045)
        sampled=[M(d,a,th+mp.mpf('.04')),M(d,a,(th+mp.pi/2)/2),M(d,a,mp.pi/2)]
        assert sampled[0]>sampled[1]>sampled[2], (d,a,sampled)
        checks+=2
        flat=sphere_flat_probability(d,a)
        # The beta CDF equals the independent angular integral of viewing normals.
        g=mp.quad(lambda theta: orient_pdf(d,theta),[0,th])
        close(flat,g,relative=1e-12)
        if d>=4:
            h=mp.mpf('.002')
            ratio=(M(d,a,mp.pi/2-h)-M(d,a,mp.pi/2))/(L_end(d,a)*h*h/2)
            close(ratio,1,relative=.03)
        else:
            close(M(d,a,mp.pi/2),2*(mp.asin(a)+b)/mp.pi,relative=1e-12)
            for h in ('0.008','0.002'):
                h=mp.mpf(h)
                ratio=(M(d,a,mp.pi/2-h)-M(d,a,mp.pi/2))/(b/mp.pi*h*h*mp.log(1/h))
                close(ratio,1,relative=.15)

for a in (0.25,0.5,0.8):
    th0=asin(a)
    for th in (0.4*th0,th0+0.08,(th0+pi/2)/2,pi/2):
        exact=float(2*mp.pi*M(3,mp.mpf(a),mp.mpf(th)))
        direct=sampled_projection_perimeter(a,th)
        close(direct,exact,relative=.0015)

# Strict support/mean-support variation on a deterministic angular grid.
for d in (3,4,5,7):
    for a in ('0.25','0.5','0.8'):
        alpha=mp.asin(mp.mpf(a))
        vals=[M(d,a,alpha+(mp.pi/2-alpha)*i/8) for i in range(1,9)]
        assert all(vals[i] > vals[i+1] for i in range(7))
        checks += 7

print('PASS:',checks,'deterministic checks')
print('d=3, a=0.5: plateau mass',float(sphere_flat_probability(3,mp.mpf('.5'))))
print('d=3, a=0.5: critical M coefficient',float(critical_constant(3,mp.mpf('.5'))))
print('d=3, a=0.5: minimum projected perimeter',float(2*mp.pi*M(3,mp.mpf('.5'),mp.pi/2)))
