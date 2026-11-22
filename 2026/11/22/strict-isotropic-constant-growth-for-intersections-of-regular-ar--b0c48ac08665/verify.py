"""Reproduce analytic identities and independent numerical moment checks for regular disk intersections.

Requires Python 3 and SymPy; only standard-library code is used for quadrature.
"""
from math import pi, sin, cos, sqrt, atan2
from collections import Counter
import sympy as sp

checks = 0

def check(assertion, label):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError(label)

# Nonstandard identity powering the strict covariance comparison.
a,t = sp.symbols('a t', real=True)
d = sp.sqrt(1-a*a*(1-t*t))
r = d-a*t
check(sp.simplify(r*(d+a*t)-(1-a*a)) == 0, 'rationalized radius')
check(sp.simplify(sp.diff(r,t)/r+a/d) == 0, 'first logarithmic derivative')
check(sp.simplify(sp.diff(-a/d,a)+d**(-3)) == 0, 'mixed derivative')
check(sp.simplify(r*r+2*a*t*r+a*a-1) == 0, 'disk boundary relation')

# Midpoint polar quadrature independently computes area and polar second moment.
def polar(n,a,N=20000):
    sum2=sum4=0.
    h=2*pi/N
    for j in range(N):
        theta=(j+0.5)*h
        worst=min(cos(theta-2*pi*k/n) for k in range(n))
        u=-worst
        radius=sqrt(1-a*a+a*a*u*u)-a*u
        sum2+=radius*radius
        sum4+=radius**4
    return h*sum2/2, h*sum4/4

# Green boundary-flux identities computed from each contributing circle arc.
def arc(n,a):
    alpha=pi/n
    radius=sqrt(1-a*a*sin(alpha)**2)-a*cos(alpha)
    beta=atan2(radius*sin(alpha),a+radius*cos(alpha))
    area=n*(beta-a*sin(beta))
    moment=n/2*((1+2*a*a)*beta-(3*a+a**3)*sin(beta)+a*a*sin(beta)*cos(beta))
    return area,moment

def L4(A,J):
    return J**2/(4*A**4)

for n in (3,4,5,6,8,11,17):
    alpha=pi/n
    end=(1+__import__('math').tan(alpha)**2/3)**2/(16*n*n*__import__('math').tan(alpha)**2)
    vals=[]
    for radius in (0,0.1,0.3,0.6,0.85,0.97):
        ar,jr=polar(n,radius)
        ab,jb=arc(n,radius)
        check(abs(ar-ab)<=max(2e-8,2e-8*ab),f'area {n=} {radius=}: {ar} != {ab}')
        check(abs(jr-jb)<=max(2e-8,2e-8*jb),f'moment {n=} {radius=}: {jr} != {jb}')
        z=L4(ab,jb)
        check(1/(16*pi*pi)-1e-10 <= z < end+1e-10,f'endpoint range {n=} {radius=}')
        vals.append(z)
    check(all(y>x for x,y in zip(vals,vals[1:])),f'strict sampled ordering {n=}')
    check(abs(vals[0]-1/(16*pi*pi))<1e-10,f'disk limit {n=}')
    # Endpoint inferred from a rescaled body: compare near-degenerate geometry
    near=L4(*arc(n,0.999))
    check(abs(near/end)<1.015 and near<end,f'polygon endpoint {n=} {near=} {end=}')

print(f'PASS: {checks} independent symbolic and quadrature assertions')
