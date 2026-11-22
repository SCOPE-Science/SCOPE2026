"""Exact checks of arclength two-point distance fingerprints on metric stars.
Requires Python 3.9+ standard library only; no network access.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from random import Random

def positive(x): return x if x > 0 else F(0)

def tail(arms,t):
    arms=[F(x) for x in arms]
    t=F(t)
    L=sum(arms)
    same=sum((positive(x-t)**2 for x in arms), F(0))
    cross=sum((2*x*y-(t*t-positive(t-x)**2-positive(t-y)**2+positive(t-x-y)**2)
               for x,y in combinations(arms,2)),F(0))
    return (same+cross)/(L*L)

def jumps(arms):
    m=len(arms)
    J=Counter()
    for a in arms: J[a]+=m-2
    for a,b in combinations(arms,2): J[a+b]-=1
    return {k:v for k,v in J.items() if v}

def invert(J,m):
    assert m>=3
    found=[]
    seen=set()
    for _ in range(5*m*m+50):
        if len(found)==m: return sorted(found)
        events=set(J)
        events.update(a+b for a,b in combinations(found,2))
        events.difference_update(seen)
        assert events, ('not enough evidence', found)
        t=min(events)
        c=sum(a+b==t for a,b in combinations(found,2))
        x=F(J.get(t,0)+c,m-2)
        assert x.denominator==1 and x>=0 and len(found)+int(x)<=m, (t,x,found,J)
        found.extend([t]*int(x))
        seen.add(t)
    raise AssertionError('failed to terminate')

def brute_grid(arms,n=500):
    from math import isclose
    arms=list(map(float,arms)); L=sum(arms)
    coords=[(i,(k+.5)*l/n,l/n) for i,l in enumerate(arms) for k in range(n)]
    out=[]
    for t in [0.12*L,0.41*L,0.67*L]:
        count=sum((wx*wy for i,x,wx in coords for j,y,wy in coords
                 if (abs(x-y) if i==j else x+y)>t))
        out.append((t, count/L**2, float(tail(arms,t))))
    return out

def run():
    sets=[[1,1,2],[1,1,1,2,2],[1,2,3],[2,3,5,8],[1,1,1,1],
          [F(1,3), F(1,2),F(5,6),F(4,3)],[1,1,2,2,3,3],[1,3,4,4,7,10]]
    rng=Random(314159)
    for m in range(3,11):
        for _ in range(100):
            sets.append([F(rng.randint(1,22),rng.randint(1,12)) for _ in range(m)])
    for arms in sets:
        a=list(map(F,arms)); m=len(a); L=sum(a)
        J=jumps(a)
        assert invert(J,m)==sorted(a), (a,J)
        knots=sorted(set(a)|{x+y for x,y in combinations(a,2)})
        for t in [F(0)]+knots+[L*2]:
            assert F(0)<=tail(a,t)<=F(1)
        z=min(a)/3
        assert tail(a,z)==1-2*z/L+F(m*(3-m),2)*(z/L)**2
    # Direct finite-grid integration of the distance predicate, independent
    # of the closed formula and of distributional differentiation.
    for a in [[1,1,2],[1,2,3,4],[F(1,2),F(5,4),F(7,3)]]:
        for t,grid,exact in brute_grid(a):
            assert abs(grid-exact)<0.00075,(a,t,grid,exact)
    # The two-arm metric star is merely a length-L interval, with
    # its split point invisible to the two-point distance law.
    for a in [[1,3],[2,2],[F(1,3),F(11,3)]]:
        for t in [F(0),F(1,2),F(1),F(7,2),F(4)]:
            assert tail(a,t)==positive(F(4)-t)**2/F(16)
    print('STAR_GEODESIC_DISTANCE_INVERSE_EXACT_OK',len(sets))
if __name__=='__main__': run()
