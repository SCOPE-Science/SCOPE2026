"""Exact-rational checks for parabolic polygon area/polar exchange identities.
Scientific calculations only; finite tests support the analytic argument.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random


def area_primal(knots):
    gaps = [a-b for a,b in zip(knots,knots[1:])]
    return Q(8,3)-Q(2,3)*sum((x*x*x for x in gaps), Q(0))


def area_polar_vertices(knots):
    pts = [(Q(1),Q(0))]
    for a,b in zip(knots,knots[1:]):
        pts.append(((a+b)/(1+a*b), Q(1)/(1+a*b)))
    pts.append((Q(0),Q(1)))
    return 2*sum((x*v-y*u for (x,y),(u,v) in zip(pts,pts[1:])),Q(0))


def clip(poly, a):
    # Clip a rational polygon by a*x+(1-a*a)*y<=1.
    def fun(p): return a*p[0]+(1-a*a)*p[1]-1
    result=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp, fq = fun(p),fun(q)
        if fp<=0: result.append(p)
        if (fp<0 and fq>0) or (fp>0 and fq<0):
            t=fp/(fp-fq)
            result.append((p[0]+t*(q[0]-p[0]), p[1]+t*(q[1]-p[1])))
    # eliminate consecutive duplicates to keep polygon compact
    return [p for j,p in enumerate(result) if j==0 or p!=result[j-1]]


def area_polar_clip(knots):
    P=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    for a in knots[1:-1]: P=clip(P,a)
    s=sum((x*v-y*u for (x,y),(u,v) in zip(P,P[1:]+P[:1])),Q(0))
    return 2*s


def add_test(knots,c):
    pair=next(i for i,(a,b) in enumerate(zip(knots,knots[1:])) if a>c>b)
    a,b=knots[pair:pair+2]
    new=knots[:pair+1]+[c]+knots[pair+1:]
    q=2*(a-b)*(a-c)*(c-b)
    D=(1+a*b)*(1+a*c)*(1+b*c)
    U,W=area_primal(knots),area_polar_vertices(knots)
    UU,WW=area_primal(new),area_polar_vertices(new)
    assert UU-U==q, (knots,c,'primal',UU-U,q)
    assert W-WW==q/D, (knots,c,'polar',W-WW,q/D)
    assert UU*WW-U*W==q*(W-UU/D), (knots,c,'product')
    assert UU*WW>U*W
    assert WW==area_polar_clip(new)
    return 5


def main():
    n=0
    rng=Random(20261118)
    grid=[Q(i,8) for i in range(1,8)]
    for mask in range(128):
        inside=[grid[i] for i in range(7) if mask>>i & 1]
        knots=[Q(1)]+list(reversed(inside))+[Q(0)]
        assert area_polar_vertices(knots)==area_polar_clip(knots)
        n+=1
        for c in grid:
            if c not in knots:
                n+=add_test(knots,c)
    for k in range(1000):
        options=rng.sample(range(1,200),rng.randint(0,15))
        knots=[Q(1)]+sorted([Q(i,200) for i in options],reverse=True)+[Q(0)]
        available=[i for i in range(1,200) if Q(i,200) not in knots]
        c=Q(rng.choice(available),200)
        n+=add_test(knots,c)
    assert area_primal([Q(1),Q(0)])==2
    assert area_polar_vertices([Q(1),Q(0)])==4
    for ratio in [Q(1,10),Q(1,2),Q(9,10),Q(99,100)]:
        # A truncated geometric string with final knot zero.
        knots=[Q(1)]
        for _ in range(100): knots.append(knots[-1]*ratio)
        knots.append(Q(0))
        assert area_primal(knots)>2 and area_primal(knots)<Q(8,3)
        assert area_polar_vertices(knots)<4
        n+=2
    print('PASS:',n,'exact-rational assertions, independent polar clipping, and exhaustive grid refinements; analytic proof needed for infinite sequences.')

if __name__=='__main__': main()
