#!/usr/bin/env python3
"""Independent polygon-clipping and torus-sampling checks for cut-locus clearance formulas.
Public scientific implementation; deterministic seed; NumPy only.
"""
import math
import numpy as np


def parameters(a, b, p):
    if a <= 0 or b < a or not (0 <= p <= a / 2):
        raise ValueError('Gauss-reduced parameters required')
    q = math.sqrt(b*b-p*p)
    c = math.hypot(a-p, q)
    return q, c


def survival(a, b, p, r):
    q, c = parameters(a,b,p)
    if r <= 0:
        return 1.0
    if r >= a / 2:
        return 0.0
    threshold = a*p / (a+b-c)
    alpha = a/2-r
    B = b*(b/2-r)
    C = c*(c/2-r)
    if r < threshold:
        area = 2/q*((B+C)*alpha - a*alpha*alpha/2 - (C-B)**2/(2*a))
    else:
        area = 4*alpha*B/q
    return area/(a*q)


def intersect_poly(poly, normal, support):
    out=[]
    for x, y in zip(poly, poly[1:]+poly[:1]):
        dx = float(normal@x - support)
        dy = float(normal@y - support)
        if dx <= 1e-12:
            out.append(x)
        if (dx < -1e-12 and dy > 1e-12) or (dy < -1e-12 and dx > 1e-12):
            t = dx/(dx-dy)
            out.append(x+t*(y-x))
    return out


def clipped_area(a,b,p,r):
    q,c = parameters(a,b,p)
    if r>=a/2: return 0.
    u=np.array([a,0.]); v=np.array([p,q]);
    poly=[np.array([x,y],dtype=float) for x,y in [(-20,-20),(20,-20),(20,20),(-20,20)]]
    for vec in (u,v,v-u):
        for sign in [-1,1]:
            normal=sign*vec/np.linalg.norm(vec)
            poly=intersect_poly(poly,normal,np.linalg.norm(vec)/2-r)
    if not poly: return 0.
    return abs(sum(float(np.linalg.det(np.stack([x,y]))) for x,y in zip(poly,poly[1:]+poly[:1]))/2)


def monte_carlo(a,b,p,n=160000,seed=45161):
    q,c=parameters(a,b,p)
    rng=np.random.default_rng(seed)
    t=rng.uniform(-.5,.5,(n,2))
    u=np.array([a,0.]);v=np.array([p,q]);
    x=t[:,0,None]*u+t[:,1,None]*v
    dmin=np.full(n,np.inf)
    best=np.empty_like(x)
    for i in range(-3,4):
        for j in range(-3,4):
            y=x-i*u-j*v
            ds=np.einsum('ij,ij->i',y,y)
            take=ds<dmin
            dmin[take]=ds[take]
            best[take]=y[take]
    clear=np.full(n,np.inf)
    for v0 in [u,v,v-u]:
        clear=np.minimum(clear,np.linalg.norm(v0)/2-np.abs(best@(v0/np.linalg.norm(v0))))
    for r in [.04*a,.13*a,.27*a,.38*a,.47*a]:
        emp=np.mean(clear>=r);ana=survival(a,b,p,r)
        se=math.sqrt(max(1e-9,ana*(1-ana))/n)
        assert abs(emp-ana)<6*se+.002, (a,b,p,r,emp,ana,se)
    return True


def run():
    rng=np.random.default_rng(64103)
    cases=[(1.,1.,.5),(1.,1.,0.),(1.,1.,.2),
           (1.,1.3,.336464758),(1.,2.,.499),(1.,2.,0.),
           (1.,2.,.5),(1.,5.,.1)]
    for k in range(150):
        a=float(rng.uniform(.5,2.5))
        b=a*float(rng.uniform(1,3))
        p=a*float(rng.uniform(0,.5))
        cases.append((a,b,p))
    errs=[]; max_rat=0.
    for a,b,p in cases:
        q,_=parameters(a,b,p)
        for r in np.linspace(0,a/2,29):
            formula=survival(a,b,p,float(r))
            area=clipped_area(a,b,p,float(r))/(a*q)
            diff=abs(formula-area)
            errs.append(diff)
            assert diff<3e-9,(a,b,p,r,formula,area,diff)
            area_H=a*q
            # Regular hex Voronoi inradius for the same covolume.
            regular=max(0,1-r*math.sqrt(2*math.sqrt(3)/area_H))**2
            max_rat=max(max_rat,formula-regular)
            assert formula<=regular+3e-11,(a,b,p,r,formula,regular)
    for a,b,p in cases[:6]:
        monte_carlo(a,b,p)
    print('PLANAR_TORUS_CUT_CLEARANCE_OK',len(cases),29,len(cases[:6]),
          'max_clip_error',f'{max(errs):.3e}', 'max_dominance_defect',f'{max_rat:.3e}')

if __name__=='__main__':run()
