"""Exact-rational consistency checks for positive-feedback planar map escape-clock identities."""
from fractions import Fraction as Q
from random import Random

r=Q(5,4)

def F(a,b,c,x,y):
    return x*(a+b*abs(y)), c*x-r*y

rng=Random(137)
checks=0
for _ in range(400):
    a=Q(rng.randint(1,15),rng.randint(1,10))+1
    b=Q(rng.randint(1,9),rng.randint(1,10))
    c=Q(rng.choice([-1,1])*rng.randint(1,9),rng.randint(1,10))
    x=Q(rng.choice([-1,1])*rng.randint(1,10),rng.randint(1,10))
    y=Q(rng.choice([-1,1])*rng.randint(0,20),rng.randint(1,10))
    x1,y1=F(a,b,c,x,y)
    x2,y2=F(a,b,c,x1,y1)
    assert abs(x2)>=a*a*abs(x)+(a*b*abs(c)/r)*abs(x)**2
    checks+=1

for kind in ('bottom','top','interior'):
    a=r;b=Q(1,3);c=Q(2,5)
    x=Q(3,2)
    y={'bottom':Q(0),'top':c*x/r,'interior':c*x/(2*r)}[kind]
    seq=[(x,y)]
    for n in range(19):
        x,y=F(a,b,c,x,y)
        assert x>0 and 0<=y<=c*x/r
        seq.append((x,y))
    for n in range(len(seq)-2):
        xx,yy=seq[n]
        xxx,yyy=seq[n+2]
        assert yyy==(r*r+b*c*xx)*yy
        checks+=1
    if kind=='interior':
        assert all(0<yy<c*xx/r for xx,yy in seq)
    else:
        shift=0 if kind=='bottom' else 1
        for n in range(shift,len(seq)-2,2):
            xx,yy=seq[n]; xxx,yyy=seq[n+2]
            assert yy==yyy==0
            assert xxx==r*r*xx+r*b*c*xx*xx
            checks+=1
print('PASS: {} exact-rational checks'.format(checks))
