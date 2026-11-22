#!/usr/bin/env python3
"""Independent finite checks of projected-pyramid brightness and the cap law.

Finite tests supplement, and do not establish, the quantified geometric proof.
"""
import math
import random


def dot(v,w):
    return sum(x*y for x,y in zip(v,w))

def cross(v,w):
    return (v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])

def norm(v):
    return math.sqrt(dot(v,v))

def unit(v):
    n=norm(v)
    return tuple(t/n for t in v)

def polygon_area(points):
    points=sorted(set(points))
    if len(points)<3: return 0
    def cr(o,p,q): return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
    lo=[]; hi=[]
    for p in points:
        while len(lo)>=2 and cr(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>=2 and cr(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    hull=lo[:-1]+hi[:-1]
    return abs(sum(x*y1-x1*y for (x,y),(x1,y1) in zip(hull,hull[1:]+hull[:1])))/2

def independent_shadow_area(a,b,h,u):
    u=unit(u)
    seed=(0.,0.,1.) if abs(u[2])<0.9 else (0.,1.,0.)
    e=unit(cross(u,seed)); f=cross(u,e)
    vertices=[(xx*a,yy*b,0.) for xx in (-1,1) for yy in (-1,1)]+[(0.,0.,h)]
    return polygon_area([(dot(v,e),dot(v,f)) for v in vertices])

def support_vectors(a,b,h):
    s=h/a; r=b/a
    v=[(0.,0.,z*4.) for z in (-1,1)]
    v += [(x*s,0.,z*3.) for x in (-1,1) for z in (-1,1)]
    v += [(0.,y*s/r,z*3.) for y in (-1,1) for z in (-1,1)]
    v += [(x*s,y*s/r,z*2.) for x in (-1,1) for y in (-1,1) for z in (-1,1)]
    return v

def brightness(a,b,h,u):
    u=unit(u)
    return a*b*(2*abs(u[2])+max(abs(u[2]),h/a*abs(u[0]))+max(abs(u[2]),h/b*abs(u[1])))

def cap_info(a,b,h):
    v=support_vectors(a,b,h)
    L=max(map(norm,v))
    win=[w for w in v if abs(norm(w)-L)<1e-11]
    low=[w for w in v if abs(norm(w)-L)>=1e-11]
    other=max([norm(w) for w in low], default=0.)
    contact=max([math.sqrt(max(0.,(L*L+dot(x,y))/2)) for i,x in enumerate(win) for y in win[i+1:]],default=0.)
    return a*b*L, a*b*max(other,contact), win

def exact_phase_count(r,s):
    c=math.sqrt(7/5)
    if abs(r-c)<1e-9 and abs(s-math.sqrt(7))<1e-9: return 14
    if r<c:
        threshold=math.sqrt(12*r*r/(r*r+1))
        if abs(s-threshold)<1e-9: return 10
        return 2 if s<threshold else 8
    if r>c:
        if abs(s-math.sqrt(7))<1e-9: return 6
        if abs(s-math.sqrt(5)*r)<1e-9: return 12
        return 2 if s<math.sqrt(7) else (4 if s<math.sqrt(5)*r else 8)
    return 2 if s<math.sqrt(7) else 8

def run():
    rng=random.Random(4407)
    test_shapes=[(1.,1.,.3),(1.,1.,math.sqrt(6)),(1.,1.,4.),(1.,1.1,2.),(1.,1.1,math.sqrt(12*1.21/2.21)),
      (1.,math.sqrt(7/5),math.sqrt(7)),(1.,2.,1.),(1.,2.,math.sqrt(7)),(1.,2.,3.),(1.,2.,2*math.sqrt(5)),(1.,2.,6.),(1.,4.,12.)]
    checked=0
    for a,b,h in test_shapes:
        M,q,winners=cap_info(a,b,h)
        assert q<M, (a,b,h,q,M)
        assert len(winners)==exact_phase_count(b/a,h/a), (a,b,h,len(winners))
        assert abs(M-max(4*a*b, a*b*math.sqrt(9+(h/a)**2),a*b*math.sqrt(4+(h/a)**2+(h/b)**2)))<1e-10
        for w in winners:
            assert abs(brightness(a,b,h,w)-M)<1e-10
            assert abs(independent_shadow_area(a,b,h,w)-M)<1e-9
        for j in range(1200):
            u=unit((rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1)))
            direct=independent_shadow_area(a,b,h,u)
            analytic=brightness(a,b,h,u)
            assert abs(direct-analytic)<1e-9*(1+analytic), (a,b,h,u,direct,analytic)
            assert analytic<=M+1e-9
            checked+=1
        # Check caps disjoint on their intended range via pairwise spherical-angle criterion.
        Lambda=M/(a*b)
        for i,x in enumerate(winners):
            for y in winners[i+1:]:
                touch=a*b*math.sqrt(max(0.,(Lambda*Lambda+dot(x,y))/2))
                assert touch<=q+1e-10
        # For nonwinners, no cap can occur above q.
        assert all(a*b*norm(x)<=q+1e-10 for x in support_vectors(a,b,h) if abs(norm(x)-Lambda)>1e-11)
    print('PASS', checked,'independent projected-hull area comparisons;',len(test_shapes),'exact phase counts, maximizing normals and cap-separation certificates')
    for a,b,h in test_shapes:
        M,q,W=cap_info(a,b,h)
        print('shape',a,b,round(h,8),'cap_multiplicity',len(W),'M',round(M,10),'q',round(q,10),'tail_slope',len(W)/2)

if __name__=='__main__':run()
