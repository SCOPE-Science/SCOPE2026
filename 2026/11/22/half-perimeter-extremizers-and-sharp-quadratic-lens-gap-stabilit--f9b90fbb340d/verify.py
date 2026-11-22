"""Exact lens-gap identities and independent disk-intersection quadrature.

Usage: python verify.py    (Python >=3.9 and SymPy)
The infinite-parameter proof is in RESULT.md; finite tests corroborate it.
"""
import math
import sympy as sp

q=sp.symbols('q', real=True)
for m in [3,4,5,7,10]:
    alpha=sp.pi/m
    A_m=q-m*sp.sin((sp.pi-q)/m)*sp.sin(q/m)/sp.sin(alpha)
    A2=q-sp.sin(q)
    K=m/(2*sp.sin(alpha))
    D=sp.sin(q)-K*(sp.cos((sp.pi-2*q)/m)-sp.cos(alpha))
    assert sp.simplify(sp.expand_trig((A_m-A2)-D))==0
    G=1-K*(1-sp.cos(alpha))
    assert sp.simplify(sp.trigsimp(D.subs(q,sp.pi/2)-G))==0
    assert abs(float(sp.N(G-(1-sp.Rational(m,2)*sp.tan(alpha/2)),25)))<1e-22
    assert sp.simplify(D.subs(q,0))==0
    assert sp.simplify(D.subs(q,sp.pi))==0


def area(m,p):
    q=p/2
    a=math.pi/m
    return q-m*math.sin((math.pi-q)/m)*math.sin(q/m)/math.sin(a)


def excess(m,p):
    return area(m,p)-(p/2-math.sin(p/2))


def radial_area(m,p,n=8192):
    a=math.pi/m
    t=math.sin((math.pi-p/2)/m)/math.sin(a)
    centers=[(t*math.cos(2*math.pi*j/m),t*math.sin(2*math.pi*j/m)) for j in range(m)]
    acc=0.
    for j in range(n):
        angle=2*math.pi*(j+.5)/n
        ux,uy=math.cos(angle),math.sin(angle)
        rho=min((z:=ux*cx+uy*cy)+math.sqrt(max(0,1-t*t+z*z)) for cx,cy in centers)
        acc+=rho*rho
    return math.pi*acc/n

for m in [3,4,6,10,20]:
    G=1-(m/2)*math.tan(math.pi/(2*m))
    assert G>0
    for p in [.1,.8,math.pi,4.2,6.0]:
        D=excess(m,p)
        assert abs(radial_area(m,p)-area(m,p))<7e-7,(m,p)
        assert D>0 and D<=G*(1-(p-math.pi)**2/math.pi**2)+2e-12,(m,p,D)
    assert abs(excess(m,math.pi)-G)<3e-14
    for j in range(1,1000):
        p=2*math.pi*j/1000
        D=excess(m,p)
        assert D>0
        assert D<=G*(1-(p-math.pi)**2/math.pi**2)+2e-12
    local=(1-2/(m*math.sin(math.pi/m)))/8
    global_coefficient=G/math.pi**2
    assert local>global_coefficient
print('LENS_GAP_FORMULAS_OPTIMA_STABILITY_AND_RADIAL_INTEGRALS_OK')
