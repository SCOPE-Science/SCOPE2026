#!/usr/bin/env python3
"""Exact arithmetic checks for a height law and rescaled gaps in four-runner speeds.

No numerical approximation is used in the logical comparisons. This script
checks finite examples and the polygon identities; the asymptotic sieve proof
is mathematical and is not replaced by this finite verification.
"""
from fractions import Fraction as F
from math import gcd

EXPECTED_AREAS = {
    (0,1):F(1), (0,3):F(1,3), (1,0):F(2,3),
    (1,3):F(13,15), (2,1):F(7,15), (2,3):F(1,3),
    (3,0):F(4,3), (3,1):F(1,3),
}

def classes():
    return [(a,b) for a in range(4) for b in range(4)
            if (a%2 or b%2) and (b-a)%4 and (b-2*a)%4]

def forms(a,b):
    r=(b-a)%4
    s=(b-2*a)%4
    first={1:(F(1,2),F(1,2)), 2:(F(1,4),F(3,4)),
           3:(F(1,2),F(3,2))}[r]
    third={1:(F(1),F(1,2)), 2:(F(1,2),F(3,4)),
           3:(F(1),F(3,2))}[s]
    return first,third

def clip(poly,a,b,c):
    result=[]
    for P,Q in zip(poly, poly[1:]+poly[:1]):
        u=a*P[0]+b*P[1]-c
        v=a*Q[0]+b*Q[1]-c
        if u<=0:result.append(P)
        if (u<0<v) or (v<0<u):
            t=u/(u-v)
            result.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
        elif u>0==v:result.append(Q)
    return result

def polygon(a,b):
    poly=[(F(0),F(0)),(F(20),F(0)),(F(20),F(20)),(F(0),F(20))]
    for A,B in forms(a,b): poly=clip(poly,A,B,F(1))
    return poly

def polygon_area(poly):
    cross=sum(P[0]*Q[1]-P[1]*Q[0]
              for P,Q in zip(poly,poly[1:]+poly[:1]))
    return abs(cross)/2

def m_value(x,y):
    r=(y-x)%4
    s=(y-2*x)%4
    u={1:(x+y-1)//2, 2:(x+3*y-2)//4,3:(x+3*y-1)//2}[r]
    v={1:(2*x+y-1)//2,2:(2*x+3*y-2)//4,3:(2*x+3*y-1)//2}[s]
    return max(u,v)

def dist(n,t):
    w=n*t
    r=w.numerator % w.denominator
    return min(F(r,w.denominator),F(1)-F(r,w.denominator))

def exact_loneliness(speeds):
    """Max of min of sawtooth functions via all affine cells and crossings."""
    xs={F(0),F(1)}
    for v in speeds:
        xs.update(F(j,2*v) for j in range(2*v+1))
    pts=sorted(xs)
    best=F(0)
    for L,R in zip(pts,pts[1:]):
        LV=[dist(v,L) for v in speeds]
        RV=[dist(v,R) for v in speeds]
        best=max(best,min(LV),min(RV))
        for i in range(4):
            for j in range(i+1,4):
                p=LV[i]-LV[j]
                q=RV[i]-RV[j]
                if p==q:continue
                t= L + (R-L)*p/(p-q)
                if L<t<R:
                    best=max(best, min(dist(v,t) for v in speeds))
    return best

def count(X,thresholds=(F(1,2),F(1),F(2))):
    # Map x,y injectively to their four-element speed sets.
    vals={}
    for y in range(1,X//2+1):
        for x in range(1,X-2*y+1):
            if gcd(x,y)>1 or (y-x)%4==0 or (y-2*x)%4==0:continue
            v=tuple(sorted((x,y,x+y,x+2*y)))
            assert v not in vals
            m=m_value(x,y)
            vals[v]=F(1,8*m+4)
    # Source's separate one-parameter family and isolated exception.
    for k in range(1,X//4+1):
        v=(1,2,3,4*k)
        d=F(1,4)-F(k,4*k+1)
        if v in vals:assert k==1
        vals[v]=d
    if X>=14:
        vals[(1,3,4,14)]=F(1,4)-F(4,17)
    upper=[sum(1 for d in vals.values() if X*d>z) for z in thresholds]
    return len(vals),upper

def main():
    keys=classes()
    assert keys==list(EXPECTED_AREAS)
    s=F(0)
    max_height=F(0)
    for key in keys:
        p=polygon(*key)
        A=polygon_area(p)
        assert A==EXPECTED_AREAS[key],(key,A,EXPECTED_AREAS[key])
        s+=A
        max_height=max(max_height,max(u+2*v for u,v in p))
    assert s==F(16,3) and max_height==4
    assert s/F(128)==F(1,24)
    crosschecked=0
    for y in range(1,9):
        for x in range(1,9):
            if gcd(x,y)!=1 or (y-x)%4==0 or (y-2*x)%4==0:continue
            v=(x,y,x+y,x+2*y)
            m=m_value(x,y)
            assert exact_loneliness(v)==F(m,4*m+2),(x,y,v,m)
            crosschecked+=1
    expected={200:4125,400:16343,800:65133}
    for X,desired in expected.items():
        total,tail=count(X)
        assert total==desired,(X,total)
        print('CENSUS X=%d count=%d tails_z_1over2_1_2=%s' % (X,total,tail))
    print('VERIFY_OK residue_classes=%d polygon_area_sum=%s max_polygon_height=%s tail_constant=%s exact_loneliness_pairs=%d census_cases=%d exact_rational=yes' %
          (len(keys),s,max_height,s/128,crosschecked,len(expected)))

if __name__=='__main__':main()
