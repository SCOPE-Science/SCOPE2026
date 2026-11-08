#!/usr/bin/env python3
"""Exact conditional area-moment and independent geometric Monte Carlo checks."""
from fractions import Fraction as F
from math import sqrt
import random


def expand_mul(p, q):
    o={}
    for a,x in p.items():
        for b,y in q.items():
            c=tuple(a[i]+b[i] for i in range(3))
            o[c]=o.get(c,F(0))+x*y
    return {i:x for i,x in o.items() if x}

def polynomial_cube_moment(poly, k):
    r={(0,0,0):F(1)}
    for _ in range(k):r=expand_mul(r,poly)
    return sum((c/F((i+1)*(j+1)*(h+1)) for (i,j,h),c in r.items()),F(0))

# The expression uv+w(1-u-v) for three different sides.
tri={(1,1,0):F(1),(0,0,1):F(1),(1,0,1):F(-1),(0,1,1):F(-1)}
def a(k):return polynomial_cube_moment(tri,k)
def b(k):return F(2,(k+1)**2*(k+2))
def es(p):return p[0]*p[1]+p[0]*p[2]+p[1]*p[2]
def et(p):return p[0]*p[1]*p[2]
def conditional_moment(k,p):
    e2,e3=es(p),et(p)
    return 3*b(k)*e2+(6*a(k)-9*b(k))*e3

def independent_geom_sim(p, N=400000,seed=754):
    rng=random.Random(seed)
    # Build a Euclidean triangle from ratios p1,p2,p3, with p1=|BC|, p2=|CA|, p3=|AB|.
    vA=(0.,0.);vB=(float(p[2]),0.)
    xx=float((p[1]**2+p[2]**2-p[0]**2)/(2*p[2]))
    vC=(xx,sqrt(float(p[1]**2)-xx*xx))
    base_area=(vB[0]*vC[1])/2
    ends=[(vB,vC),(vC,vA),(vA,vB)]
    sums=[0.,0.,0.]; zero=0
    for i in range(N):
        pts=[]; lab=[]
        for j in range(3):
            r=rng.random(); s=0; idx=2
            for ii in range(2):
                s+=float(p[ii])
                if r<s:idx=ii;break
            lab.append(idx)
            a0,b0=ends[idx];t=rng.random()
            pts.append((a0[0]*(1-t)+b0[0]*t,a0[1]*(1-t)+b0[1]*t))
        if lab[0]==lab[1]==lab[2]:zero+=1
        z=abs((pts[1][0]-pts[0][0])*(pts[2][1]-pts[0][1])-(pts[1][1]-pts[0][1])*(pts[2][0]-pts[0][0]))/(2*base_area)
        for k in range(1,4):sums[k-1]+=z**k
    return [q/N for q in sums],zero/N


def main():
    assert [a(k) for k in (1,2,3)]==[F(1,4),F(1,12),F(5,144)]
    assert [b(k) for k in (1,2,3)]==[F(1,6),F(1,18),F(1,40)]
    p=(F(4,15),F(4,15),F(7,15)); q=(F(2,5),F(2,5),F(1,5))
    assert sum(p)==sum(q)==1 and max(p)<F(1,2) and max(q)<F(1,2)
    assert es(p)==es(q)==F(8,25) and et(p)-et(q)==F(4,3375)
    assert conditional_moment(1,p)==conditional_moment(1,q)==F(4,25)
    assert conditional_moment(2,p)==conditional_moment(2,q)==F(4,75)
    assert conditional_moment(3,q)-conditional_moment(3,p)==F(1,50625)
    for k in range(1,7):
        # Compute (not merely display a range of) exact rational moments through order six.
        moment=a(k)
        assert F(0)<moment<=F(1)
    for pp in [p,q,(F(1,3),F(1,3),F(1,3)),(F(2,5),F(7,20),F(1,4))]:
        assert sum(pp)==1
        for k in range(1,7):
            m=conditional_moment(k,pp)
            assert F(0)<m<F(1)
        assert conditional_moment(2,pp)==conditional_moment(1,pp)/3
        assert F(1)-3*es(pp)+3*et(pp)==sum(x**3 for x in pp)
        est,atom=independent_geom_sim(pp)
        for k in (1,2,3):
            target=float(conditional_moment(k,pp))
            assert abs(est[k-1]-target)<0.0020, (pp,k,est,target)
        assert abs(atom-float(sum(x**3 for x in pp)))<0.0020
    print('VERIFY_OK exact_moment_orders=1..6 configurations=4 simulation_trials=1600000')
    print('First three conditional universal moments:', [str(a(k)) for k in (1,2,3)])
    print('Inverse minimality witness:',list(map(str,p)),list(map(str,q)))
    print('Moments p:',[str(conditional_moment(k,p)) for k in (1,2,3)])
    print('Moments q:',[str(conditional_moment(k,q)) for k in (1,2,3)])

if __name__=='__main__':main()
