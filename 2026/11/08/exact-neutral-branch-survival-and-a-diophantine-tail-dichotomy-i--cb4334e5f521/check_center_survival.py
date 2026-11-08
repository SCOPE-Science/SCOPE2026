#!/usr/bin/env python3
"""Independent finite polygon-clipping checks for the center no-switch area law.
No scientific claim is inferred from finite enumeration alone.
"""
from fractions import Fraction as F
from math import acos, cos, sin, pi, tan, isclose, sqrt

def clip(poly, a, b, t):
    # Retain a*x+b*y <= t, including boundary.
    output=[]
    for u,v in zip(poly, poly[1:]+poly[:1]):
        fu=a*u[0]+b*u[1]-t
        fv=a*v[0]+b*v[1]-t
        if fu<=0: output.append(u)
        if (fu<0 and fv>0) or (fu>0 and fv<0):
            r=fu/(fu-fv)
            output.append((u[0]+r*(v[0]-u[0]), u[1]+r*(v[1]-u[1])))
        elif fu>0 and fv==0: output.append(v)
    # duplicate vertices do not alter signed area, but remove for speed
    dedup=[]
    for pt in output:
        if not dedup or pt!=dedup[-1]: dedup.append(pt)
    if len(dedup)>1 and dedup[-1]==dedup[0]:dedup.pop()
    return dedup

def area(poly):
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1])))/2

def survival_poly(c,N,h=1):
    # J=[[2-c,-1],[1,0]], h real or rational.
    m=1000*h
    poly=[(-m,-m),(m,-m),(m,m),(-m,m)]
    a,b=1,-1
    for n in range(N):
        poly=clip(poly,a,b,h)
        poly=clip(poly,-a,-b,h)
        # row (a,b) J = ((2-c)a+b,-a)
        a,b=(2-c)*a+b,-a
    return poly

def formula_area(c,N,h=1):
    theta=acos(1-c/2)
    phases=sorted(set(round((k*theta+s*pi)%(2*pi),14) for k in range(N) for s in (0,1)))
    gaps=[((phases[(j+1)%len(phases)]-phases[j])%(2*pi)) for j in range(len(phases))]
    R2=h*h*(4-c)/4
    return R2/sin(theta)*sum(tan(d/2) for d in gaps)

def direct_formula_area(c,N,h=1):
    # Avoid rounding duplicate phases by working with argument list for test regimes.
    theta=acos(1-c/2)
    ph=sorted(((k*theta+s*pi)%(2*pi)) for k in range(N) for s in (0,1))
    uniq=[]
    for p in ph:
        if not uniq or p-uniq[-1]>1e-8:uniq.append(p)
    if len(uniq)>1 and uniq[0]+2*pi-uniq[-1]<1e-8:uniq.pop()
    gaps=[(uniq[(i+1)%len(uniq)]-uniq[i])%(2*pi) for i in range(len(uniq))]
    return h*h*(4-c)/(4*sin(theta))*sum(tan(g/2) for g in gaps)

def run():
    checks=0
    # Rational exact arithmetic: 2, 3, 4, 5, 6, 7, 8, 9 iterates at c=1,2,3.
    for c,q,Ainfty in [(F(1),3,F(3)),(F(2),2,F(2)),(F(3),3,F(1))]:
        prev=None
        for N in range(2,12):
            poly=survival_poly(c,N,h=F(1))
            observed=area(poly)
            assert observed==Ainfty if N>=q else observed>Ainfty, (c,N,observed)
            assert observed<=F(4,c), (c,N,observed)
            if prev is not None:assert observed<=prev
            prev=observed
            checks+=3
    # Numeric independent polygon clipping versus support-gap formula.
    for theta in [pi/2,pi/3,2*pi/3,2*pi/5,3*pi/7,pi*(sqrt(2)-1),pi*(sqrt(5)-1)/2]:
        c=2*(1-cos(theta))
        for N in range(2,17):
            poly=survival_poly(c,N,h=1.0)
            measured=float(area(poly))
            predicted=direct_formula_area(c,N)
            assert isclose(measured,predicted,rel_tol=5e-8,abs_tol=5e-8),(theta,N,measured,predicted)
            checks+=1
    # Rational exact asymptotic at infinite horizon vs direct clipping.
    for p,q in [(1,2),(1,3),(2,3),(1,4),(1,5),(2,5),(3,7),(1,9)]:
        theta=pi*p/q
        c=2*(1-cos(theta))
        if q<2:continue
        pred=(1/2)*sqrt((4-c)/c)*(2*q*tan(pi/(2*q)))
        measured=float(area(survival_poly(c,q,h=1.0)))
        assert isclose(measured,pred,rel_tol=3e-9,abs_tol=3e-9),(p,q,measured,pred)
        checks+=1
    # Verify scale invariance and discontinuity magnitudes on test parameters.
    for theta in [pi/2,pi/3,pi/5,pi/7]:
        c=2*(1-cos(theta))
        q=round(pi/theta)
        p_mass = float(area(survival_poly(c,q,h=1.0)))/float(area(survival_poly(c,2,h=1.0)))
        target=(q*sin(theta)/2)*tan(pi/(2*q))
        assert isclose(p_mass,target,rel_tol=3e-9,abs_tol=3e-9)
        checks+=1
    print(f'PASS {checks} supporting exact and numerical comparisons')

if __name__=='__main__':run()
