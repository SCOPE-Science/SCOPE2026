#!/usr/bin/env python3
"""Exact rational regression checks for a symmetric single-notch polygon theorem."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext


def polygon_area(v):
    return abs(sum((x*y2 - x2*y for (x,y),(x2,y2) in zip(v,v[1:]+v[:1])),Q(0)))/2


def clip(poly, p, q):
    # Return the portion of a convex polygon on the left of oriented line p->q.
    def cross(z):
        return (q[0]-p[0])*(z[1]-p[1])-(q[1]-p[1])*(z[0]-p[0])
    if not poly:
        return []
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        u,v=cross(a),cross(b)
        if u>=0:out.append(a)
        if (u<0 and v>0) or (u>0 and v<0):
            out.append((a[0]+u*(b[0]-a[0])/(u-v),a[1]+u*(b[1]-a[1])/(u-v)))
        elif u<0 and v==0:
            out.append(b)
    return out


def independent_kernel_area(b,t):
    h=Q(1)
    poly=[(-Q(1),Q(0)),(Q(1),Q(0)),(b,h),(Q(0),1-t),(-b,h)]
    M=Q(100)
    sq=[(-M,-M),(M,-M),(M,M),(-M,M)]
    for a,c in zip(poly,poly[1:]+poly[:1]):
        sq=clip(sq,a,c)
    return polygon_area(sq)


def closed_kernel_area(b,t):
    if b<=t/(1-t):
        return b*(1-t)**2/t
    return (b*b*(1-t)**2+b*(1-t*t)-t)/(b*(1+t)-t)


def run():
    n=0
    ts=[Q(1,100),Q(1,20),Q(3,50),Q(1,4),Q(1,2),Q(3,4),Q(9,10)]
    factors=[Q(1,5),Q(1,2),Q(1),Q(2),Q(4),Q(9)]
    for t in ts:
        for factor in factors:
            b=factor*t/(1-t)
            k=independent_kernel_area(b,t)
            assert k==closed_kernel_area(b,t),(b,t,k,closed_kernel_area(b,t))
            polygon=[(-Q(1),Q(0)),(Q(1),Q(0)),(b,Q(1)),(Q(0),1-t),(-b,Q(1))]
            assert polygon_area(polygon)==1+b*(1-t)
            n+=1
    b,t=Q(3,20),Q(3,50)
    assert closed_kernel_area(b,t)/(1+b*(1-t))==Q(12149,12551)
    h=Q(1000)
    rational_lower=Q(12149,12551)*(1+(t*h-b)/(1+b+h+(1-b)**2/(2*h)))
    assert rational_lower==Q(10312074711061,10052350547239)
    assert rational_lower>Q(41,40)
    with localcontext() as ctx:
        ctx.prec=75
        s=Decimal(2).sqrt()
        def p(x): return x**3+3*(s-1)*x**2+(10*s-13)*x+7-5*s
        lo,hi=Decimal(0),Decimal(1)
        assert p(lo)<0<p(hi)
        for _ in range(320):
            mid=(lo+hi)/2
            if p(mid)<0: lo=mid
            else:hi=mid
        root=(lo+hi)/2
        a=(1-root*root)*(root+3-2*s)/(root+s-1)**2
        beta=root*(1+s)/(1-root)
        assert Decimal('0.05834590395624')<root<Decimal('0.05834590395625')
        assert Decimal('1.02607839496396')<a<Decimal('1.02607839496398')
        assert Decimal('0.14958727757027')<beta<Decimal('0.14958727757028')
    print('PASS: %s independent exact halfplane and polygon-area cases; exact witness; 320 high-precision root-bisection steps' % n)

if __name__=='__main__':run()
