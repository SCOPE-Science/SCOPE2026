#!/usr/bin/env python3
"""Standalone reproducibility checks for the polygonal outer-parallel centroid theorem.

All assertions are regressions against independent planar polygon decompositions;
the general claims follow from the analytic proof in RESULT.md, not these tests.
"""
import math
from fractions import Fraction

PI = math.pi

def center_data(a, b, h):
    assert 0 < a < b and h > 0
    d, s = b - a, a + b
    ell = math.hypot(d, h)
    A, L = h * s, 2 * (s + ell)
    G = h * (a + 2 * b) / (3 * s)
    H = h * (2 * b + ell) / (2 * (s + ell))
    S = h * (.5 + math.atan(d / h) / PI)
    return A, L, G, H, S

def derivative_y(a, b, h, t):
    A, L, G, H, S = center_data(a, b, h)
    q = A + L*t + PI*t*t
    return (A*(L+2*PI*t)*(H-G)+PI*t*(2*A+L*t)*(S-H))/(q*q)

def crossing_radius(a, b, h):
    A, L, G, H, S = center_data(a, b, h)
    if not (H > max(G, S)):
        return None
    r = (H-G)/(H-S)
    aa = PI*L
    bb = 2*PI*A*(1-r)
    discr = math.sqrt(bb*bb + 4*aa*r*A*L)
    if bb > 0:
        return 2*r*A*L/(bb+discr)
    return (-bb+discr)/(2*aa)

def poly_geom(vertices):
    n = len(vertices)
    area2 = mx = my = 0.0
    for i,(x,y) in enumerate(vertices):
        xx,yy = vertices[(i+1)%n]
        cr = x*yy-xx*y
        area2 += cr
        mx += (x+xx)*cr
        my += (y+yy)*cr
    assert area2 > 0
    area=area2/2
    centroid=(mx/(3*area2),my/(3*area2))
    edges=[]
    for i,(x,y) in enumerate(vertices):
        xx,yy = vertices[(i+1)%n]
        dx,dy=xx-x,yy-y
        leng=math.hypot(dx,dy)
        edges.append((leng,((x+xx)/2,(y+yy)/2),(dy/leng,-dx/leng)))
    L=sum(v[0] for v in edges)
    H=(sum(e[0]*e[1][0] for e in edges)/L,sum(e[0]*e[1][1] for e in edges)/L)
    sectors=[]
    for i,(x,y) in enumerate(vertices):
        n1=edges[i-1][2]
        n2=edges[i][2]
        ang1=math.atan2(n1[1],n1[0]);ang2=math.atan2(n2[1],n2[0]);delta=(ang2-ang1)%(2*PI)
        assert 0 < delta < PI
        integr=(n2[1]-n1[1],n1[0]-n2[0])
        sectors.append((delta,(x,y),integr))
    assert abs(sum(v[0] for v in sectors)-2*PI)<1e-12
    S=(sum(d*v[0] for d,v,_ in sectors)/(2*PI),sum(d*v[1] for d,v,_ in sectors)/(2*PI))
    return area,L,centroid,H,S,edges,sectors

def direct_offset_centers(vertices, t):
    A,L,G,H,S,edges,sectors=poly_geom(vertices)
    area=A
    mx,my=A*G[0],A*G[1]
    boundary_len=0
    bmx=bmy=0
    for ell,mid,norm in edges:
        area+=t*ell
        mx+=t*ell*(mid[0]+t*norm[0]/2)
        my+=t*ell*(mid[1]+t*norm[1]/2)
        boundary_len+=ell
        bmx+=ell*(mid[0]+t*norm[0])
        bmy+=ell*(mid[1]+t*norm[1])
    for angle,vertex,unit_int in sectors:
        area+=angle*t*t/2
        mx+=angle*t*t*vertex[0]/2+t**3*unit_int[0]/3
        my+=angle*t*t*vertex[1]/2+t**3*unit_int[1]/3
        boundary_len+=t*angle
        bmx+=t*angle*vertex[0]+t*t*unit_int[0]
        bmy+=t*angle*vertex[1]+t*t*unit_int[1]
    return area, (mx/area,my/area), (bmx/boundary_len,bmy/boundary_len)

def check():
    checks=0
    # Fully rational strict inequalities (Archimedes pi bounds, alternating atan series).
    lowpi=Fraction(223,71); highpi=Fraction(22,7)
    lowtheta=Fraction(26,81); hightheta=Fraction(391,1215)
    assert lowpi < PI < highpi
    assert lowtheta < math.atan(Fraction(1,3)) < hightheta
    lowS=Fraction(9,2)+9*lowtheta/highpi
    highS=Fraction(9,2)+9*hightheta/lowpi
    lowH=Fraction(315,58)
    assert lowS > Fraction(27,5)
    assert highS < lowH
    assert 3*math.sqrt(10) < Fraction(19,2)
    checks+=5
    A,L,G,H,S=center_data(1,4,9)
    assert G < S < H
    t=crossing_radius(1,4,9)
    assert 10.8282 < t < 10.8284
    assert abs(derivative_y(1,4,9,t))<1e-13
    assert derivative_y(1,4,9,0)>0 and derivative_y(1,4,9,1e3)<0
    checks+=4
    for a,b in ((1,2),(1,4),(2,3),(1,10),(3,11),(15,16)):
        d=b-a;s=a+b
        h0=math.sqrt(4*s*s-d*d)
        z=d/(2*s)
        phi=PI*z-3*math.asin(z)
        assert phi>0
        coef=z*math.sqrt(1-z*z)/phi
        for eps in (0.002,0.0005,0.0001):
            h=h0-eps
            A,L,G,H,S=center_data(a,b,h)
            assert H>G and H>S
            t=crossing_radius(a,b,h)
            assert t is not None and t>0
            assert abs(derivative_y(a,b,h,t))<2e-13
            assert abs(t/eps/coef-1) < .05
            checks+=5
        A,L,G,H,S=center_data(a,b,h0)
        assert abs(H-G)<3e-12 and H>S
        checks+=2
    # Independently decompose the rounded polygon into disjoint edge strips
    # and vertex sectors, and compare area/boundary first moments.
    for a,b,h in ((1,4,9),(1,2,4),(2,5,7),(3,4,10),(2,11,7)):
        v=[(-a,0),(a,0),(b,h),(-b,h)]
        a0,l0,g0,h0,s0,_,_=poly_geom(v)
        A,L,G,H,S=center_data(a,b,h)
        for u,w in ((a0,A),(l0,L),(g0[1],G),(h0[1],H),(s0[1],S)):
            assert abs(u-w)<2e-12
            checks+=1
        for t in (.001,.1,1,3,7,19):
            A2,g2,bb=direct_offset_centers(v,t)
            q=A+L*t+PI*t*t
            g=(A*G+L*t*H+PI*t*t*S)/q
            bh=(L*H+2*PI*t*S)/(L+2*PI*t)
            assert abs(A2-q)<2e-10
            assert abs(g2[0])<1e-12 and abs(bb[0])<1e-12
            assert abs(g2[1]-g)<5e-12 and abs(bb[1]-bh)<5e-12
            checks+=4
    print('PASS:',checks,'deterministic checks')
    _,_,wg,wh,ws=center_data(1,4,9)
    print('Trapezoid a=1,b=4,h=9: G =',wg,'H =',wh,'S =',ws)
    print('Certified witness crossing radius',round(crossing_radius(1,4,9),12))
    print('Verification is finite; universal proof is in RESULT.md')

if __name__=='__main__':
    check()
