"""Exact-rational examples for the planar Makai-volume flag inequality.

Finite arithmetic regression only. The universal proof is analytic.
"""
from fractions import Fraction as F


def area(poly):
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1]))) / 2


def clip(poly, a, b):
    out = []
    def f(p):
        return a*p[0]+b*p[1]-1
    for p,q in zip(poly, poly[1:]+poly[:1]):
        fp,fq=f(p),f(q)
        inside_p,inside_q = fp<=0,fq<=0
        if inside_p:
            out.append(p)
        if inside_p != inside_q:
            ratio=fp/(fp-fq)
            out.append((p[0]+ratio*(q[0]-p[0]),p[1]+ratio*(q[1]-p[1])))
    return out


def quad_product(s,t):
    """Polar normalized by the two diagonal difference inequalities."""
    poly=[(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))]
    differences=[(F(1),F(-1)),(F(s),F(1)),(F(s),F(-t)),(F(1),F(t))]
    for dx,dy in differences:
        for sign in (-1,1):
            poly=clip(poly,F(sign)*dx/(1+s),F(sign)*dy/(1+t))
    return area(poly)/2


triangle_dual=[(F(1),F(1)),(F(1),F(0)),(F(0),F(-1)),(F(-1),F(-1)),(F(-1),F(0)),(F(0),F(1))]
assert area(triangle_dual)==3
assert F(1,2)*area(triangle_dual)==F(3,2)
for s,t in [(F(1),F(1)),(F(2),F(1)),(F(3,2),F(3,2)),(F(1,2),F(2)),(F(1,3),F(2,5)),(F(2),F(2))]:
    score=quad_product(s,t)
    assert score<=2, (s,t,score)
    assert (score==2)==(s==t==1), (s,t,score)
    st=s*t
    checks=[
        (F(1)/(1+s)+F(1)/(1+t)<=1,st>=1),
        (s/(1+s)+F(1)/(1+t)<=1,s<=t),
        (s/(1+s)+t/(1+t)<=1,st<=1),
        (F(1)/(1+s)+t/(1+t)<=1,t<=s),
    ]
    assert all(a==b for a,b in checks), (s,t,checks)
assert F(22,7)**2 < 10
print('PLANAR_MAKAI_FLAG_RATIONAL_REGRESSIONS_OK')
