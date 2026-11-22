"""Independent checks of sharp Steiner inertia loss for rectangles.
Run: python steiner_rectangle_check.py  (requires sympy and scipy)
"""
from math import atan, sin, cos, pi
from fractions import Fraction
import sympy as sp
from scipy.integrate import quad

T, A, B = sp.symbols('T A B', positive=True)
c = 1/sp.sqrt(1 + T*T)
s = T/sp.sqrt(1 + T*T)
U = A*c
V = B*s
x = sp.symbols('x', real=True)
# Case A*cos(theta) >= B*sin(theta). Derive conditional fiber centers.
L1=2*V/(c*s)
m1=-s*x/c
L2=(U+V-x)/(c*s)
m2=((c*c-s*s)*x-(U-V))/(2*c*s)
delta_integral=2*(sp.integrate(L1*m1**2,(x,0,U-V)) + sp.integrate(L2*m2**2,(x,U-V,U+V)))
delta_formula=2*B*T*(2*A**3*T - 2*A*B**2*T**3 - 4*A*B**2*T + B**3*(T*T+1)**2)/(3*(T*T+1))
assert sp.cancel(delta_integral-delta_formula)==0
assert sp.factor(delta_formula.subs({A:1,B:1})) == 2*T*(T-1)**2/3
assert sp.simplify(sp.diff(2*T*(T-1)**2/3,T)-2*(T-1)*(3*T-1)/3)==0
assert sp.simplify((2*T*(T-1)**2/3).subs(T,sp.Rational(1,3))) == sp.Rational(8,81)
assert sp.Rational(8,3)-sp.Rational(8,81)==sp.Rational(208,81)

def fiber(a,b,theta,z):
    c,s=cos(theta),sin(theta)
    # Vertices in moving orthonormal coordinates (z,w).
    P=[(-a*c-b*s, a*s-b*c), (a*c-b*s,-a*s-b*c),
       (a*c+b*s,-a*s+b*c),(-a*c+b*s,a*s+b*c)]
    heights=[]
    for (u0,v0),(u1,v1) in zip(P,P[1:]+P[:1]):
        if u0==u1:
            if abs(z-u0)<1e-12: heights.extend((v0,v1))
        elif min(u0,u1)<=z<=max(u0,u1):
            heights.append(v0+(z-u0)*(v1-v0)/(u1-u0))
    if len(heights)<2:return 0,0
    lo,hi=min(heights),max(heights)
    return hi-lo,(hi+lo)/2

def numeric_delta(a,b,theta):
    # Independent polygon-line integration, with no use of symbolic fiber formulas.
    c,s=cos(theta),sin(theta)
    breaks=sorted({-a*c-b*s,-a*c+b*s,a*c-b*s,a*c+b*s})
    return sum(quad(lambda z: fiber(a,b,theta,z)[0]*fiber(a,b,theta,z)[1]**2,
                    p,q,epsabs=1e-11,epsrel=1e-11)[0] for p,q in zip(breaks[:-1],breaks[1:]))

def analytic_delta(a,b,theta):
    t=abs(__import__('math').tan(theta))
    if t==0:return 0.
    if t<=a/b:
        return float(delta_formula.subs({A:a,B:b,T:t}))
    return float(delta_formula.subs({A:b,B:a,T:1/t}))

count=5
for a,b in [(1.,1.),(2.,1.),(1.,3.),(.7,1.3), (3.,2.)]:
    for theta in [0.01,.12,atan(1/3),.41,pi/4,1.04,1.31,1.56]:
        v=analytic_delta(a,b,theta)
        w=numeric_delta(a,b,theta)
        assert abs(v-w)<1e-8*(1+max(v,w)),(a,b,theta,v,w)
        assert v>=-1e-9
        count+=2
for theta in [atan(1/3),atan(3),pi-atan(1/3),pi-atan(3)]:
    assert abs(numeric_delta(1.,1.,theta)-8/81)<1e-10
    count+=1
print(f"PASS: {count} exact identities and independently integrated numerical assertions")
