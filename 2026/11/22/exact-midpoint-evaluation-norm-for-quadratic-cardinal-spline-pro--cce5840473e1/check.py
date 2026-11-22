#!/usr/bin/env python3
"""Recompute an exact root-series for the midpoint kernel of quadratic cardinal L2 projection.
Only Python's standard library is needed. The analytic tail bound is independent of rounding.
"""
from decimal import Decimal as D, localcontext

with localcontext() as ctx:
    ctx.prec = 85
    one=D(1); half=D('0.5'); quarter=D('0.25')
    sq105=D(105).sqrt()
    u=[-D(13)+sq105,-D(13)-sq105]
    r=[(v+(v*v-4).sqrt())/2 for v in u]
    q=-r[0]
    def g(j):
        j=abs(j)
        return D(60)/sq105 * (r[0]**j/(r[0]-1/r[0])-r[1]**j/(r[1]-1/r[1]))
    def a(j):
        j=abs(j)
        return (-1 if j%2 else 1)*(g(j-1)+6*g(j)+g(j+1))/8
    def intpoly(c0,c1,c2,x):
        return c0*x+c1*x*x/2+c2*x*x*x/3
    def cell(j):
        A,B,C,E=a(j-1),a(j),a(j+1),a(j+2)
        # The left half has one sign; the right half has one root in (1/2,1).
        l0=(6*B-A-C)/8
        l1=(A-C)/2
        l2=-B-(A+C)/2
        assert l0>0 and l0+l1*half+l2*half*half>0
        c0=9*B/8+C/4+E/8
        c1=-3*B/2-2*C-E/2
        c2=B/2+C+E/2
        disc=c1*c1-4*c2*c0
        root=(-c1-disc.sqrt())/(2*c2)
        assert half<root<1
        first=intpoly(l0,l1,l2,half)
        second=2*intpoly(c0,c1,c2,root)-intpoly(c0,c1,c2,half)-intpoly(c0,c1,c2,one)
        return first+second,root
    for j in range(18):
        v=(D(66)*g(j)+D(26)*(g(j-1)+g(j+1))+(g(j-2)+g(j+2)))/120
        assert abs(v-(one if j==0 else D(0)))<D('1e-68')
    assert D('0.31')<a(1)/a(0)<D('0.44')
    assert D('0.40')<a(2)/a(1)<D('0.44')
    assert D('0.43')<q<D('0.44')
    for j in range(70):
        assert a(j)>0 and D('0.31')<a(j+1)/a(j)<D('0.44')
    N=70
    s=sum((cell(j)[0] for j in range(N)), D(0))*2
    tail=2*a(N-1)/(1-q)
    assert D('1.75676378')<s and s+tail<D('1.75676379')
    print('midpoint_point_evaluation_lower_bound=',s)
    print('exact_analytic_tail_bound=',tail)
    print('certified_claim_interval=(1.75676378, 1.75676379) using root formula and tail; decimal arithmetic numerical')
    print('root_in_first_right_half=',cell(0)[1])
    print('checks_passed')
