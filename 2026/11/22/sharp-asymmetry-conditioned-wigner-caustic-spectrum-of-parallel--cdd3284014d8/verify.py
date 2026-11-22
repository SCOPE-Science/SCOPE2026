"""Exact rational checks of the sharp difference-body profile for six-sided CPPOS.

Uses only the Python standard library. Run: python verify.py
These finite checks supplement, not replace, the analytic argument.
"""
from fractions import Fraction as F
from itertools import product

def hull(points):
    points=sorted(set(points))
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in points:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def area(points):
    return abs(sum(x*v-y*u for (x,y),(u,v) in zip(points,points[1:]+points[:1])))/2

def poly(a,b,c,t):
    return [(F(0),F(0)), (a,F(0)), (a,b), (a-c,b+c),(-c-t,b+c),(-c-t,c+t)]

def ratio_from_vertices(vertices):
    d=[(x-u,y-v) for x,y in vertices for u,v in vertices]
    return area(hull(d))/area(hull(vertices))

def param_ratio(a,b,c,t):
    s=a+b+c
    v=s+t
    return max(s/v,v/s)

def profile_limits(s):
    low=2*(s+1)**2/(4*s-s*s-1)
    high=2*(5-s)/(3-s)
    return low,high

count=0
for aa,bb,cc,tt in product(range(1,7),range(1,7),range(1,7),range(-3,4)):
    a,b,c,t=map(F,(aa,bb,cc,tt))
    if a+t<=0 or b-t<=0 or c+t<=0: continue
    P=poly(a,b,c,t)
    Ap=area(hull(P)); Ad=area(hull([(x-u,y-v) for x,y in P for u,v in P]))
    assert Ap>0
    assert Ad==4*Ap+t*t
    # Wigner caustic is the midpoint triangle of opposite vertices.
    Ms=[((P[j][0]+P[j+3][0])/2,(P[j][1]+P[j+3][1])/2) for j in range(3)]
    Aw=area(Ms)
    assert Aw==t*t/8
    assert (Ad/Ap-4)/8==Aw/Ap
    s=param_ratio(a,b,c,t)
    R=Ad/Ap
    if s==1:
        assert t==0 and R==4
    else:
        lo,hi=profile_limits(s)
        assert lo<=R<hi, (a,b,c,t,R,lo,hi)
        # Exact normalized variance identity in terms of the three positive excesses.
        if t>0:
            x,y,z=a/t,(b-t)/t,c/t
        else:
            # Cyclic relabeling followed by positive normalization gives a positive t.
            # The triple (a+t,b,c+t) is positive for t<0.
            x,y,z=(a+t)/(-t),b/(-t),(c+t)/(-t)
        W=x+y+z
        Amax=F(1,2)+W+W*W/3
        assert F(1,lo-4)==Amax
        assert F(1,R-4)==Ap/(t*t)
        assert Amax-Ap/(t*t)==sum((v-W/3)**2 for v in (x,y,z))/2
    count+=1

# Fixed asymmetry: balanced triple is the unique minimum, and degenerating
# triples asymptotically approach the strict maximum.
for W in [F(1,5), F(1), F(3), F(12)]:
    t=F(1);s=(W+2)/(W+1);lo,hi=profile_limits(s)
    a=c=W/3;b=1+W/3
    assert ratio_from_vertices(poly(a,b,c,t))==lo
    for den in (10,100,1000):
        eps=W/F(den)
        a=W-2*eps;b=1+eps;c=eps
        R=ratio_from_vertices(poly(a,b,c,t))
        assert lo<=R<hi
    count+=4
print('VERIFY_OK',count,'exact-rational polygon hull/profile cases')
