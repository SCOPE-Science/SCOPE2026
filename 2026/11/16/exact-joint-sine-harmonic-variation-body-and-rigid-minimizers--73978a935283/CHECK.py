#!/usr/bin/env python3
"""Exact rational consistency checks for two linked sine-harmonic BV coefficients."""
from fractions import Fraction as F

def moment(distribution, degree):
    return sum(weight * (u if degree == 1 else 2*u*u-1)
               for weight,u in distribution)

def coords(pos,neg):
    return ((moment(pos,1)-moment(neg,1))/2,
            (moment(pos,2)-moment(neg,2))/2)

def upper(x):
    x=F(x)
    assert abs(x)<=1
    if abs(x)<=F(1,2):
        pos=[((1+2*x)/2,F(1)),((1-2*x)/2,F(-1))]
        neg=[(F(1),F(0))]
    else:
        s=1 if x>0 else -1
        pos=[(F(1),F(s))]
        neg=[(F(1),F(s)-2*x)]
    return pos,neg

def ceiling(x):
    return 1-max(F(0),2*abs(x)-1)**2

def gauge(x,y):
    a,b=abs(x),abs(y)
    if b>=2*a: return b
    return 4*a*a/(4*a-b)

checks=0
xs=[F(i,48) for i in range(-48,49)]
for x in xs:
    pos,neg=upper(x)
    assert sum(w for w,u in pos)==sum(w for w,u in neg)==1
    assert all(w>=0 and abs(u)<=1 for w,u in pos+neg)
    assert coords(pos,neg)==(x,ceiling(x))
    # First-minus second-signed-moment and reverse/reflection symmetries.
    revpos=[(w,-u) for w,u in neg]
    revneg=[(w,-u) for w,u in pos]
    assert coords(revpos,revneg)==(x,-ceiling(x))
    assert gauge(x,ceiling(x))==1
    checks+=4
    # Signed convex combinations of top/bottom realizations, all budget <=1.
    for j in range(9):
        a=F(j,8)
        signed=[(a*w,u) for w,u in pos]+[(-(a*w),u) for w,u in neg]
        signed += [((1-a)*w,u) for w,u in revpos]+[(-((1-a)*w),u) for w,u in revneg]
        X=sum(w*u for w,u in signed)/2
        Y=sum(w*(2*u*u-1) for w,u in signed)/2
        assert X==x
        assert Y==(2*a-1)*ceiling(x)
        assert gauge(X,Y)<=1
        checks+=3
for x in [F(i,12) for i in range(-12,13)]:
    for y in [F(i,12) for i in range(-12,13)]:
        v=gauge(x,y)
        assert v>=abs(x) and v>=abs(y)
        if v:
            assert abs(x/v)<=1 and abs(y/v)<=ceiling(x/v)
        checks+=1
assert gauge(F(0),F(0))==0
assert gauge(F(3,4),F(0))==F(3,4)
assert gauge(F(3,4),F(3,4))==1
assert gauge(F(1,4),F(3,4))==F(3,4)
print('PASS:',checks+4,'exact rational assertions')
