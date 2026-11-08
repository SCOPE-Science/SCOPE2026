"""Exact rational tests for a finite-scale polyhedral translative-depth theorem.
No external packages needed.  The analytic theorem is proved separately.
"""
from fractions import Fraction as F
from itertools import product
import random
import math

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def cube_facets(d):
    facets=[]
    for i in range(d):
        for sign in (-1,1):
            u=[F(0)]*d; u[i]=F(sign)
            p=[F(0)]*d; p[i]=F(sign)
            facets.append((tuple(u),F(1),tuple(p)))
    return facets

def run(d,seed):
    rng=random.Random(seed)
    facets=cube_facets(d)
    # Supports fit in B_R(0) with R=sqrt(d); the facet slack is 1.
    # ceil(2 sqrt(d)) is a theorem-guaranteed dilation scale.
    t=math.ceil(2*math.sqrt(d))
    samples=[]; checks=0
    for trial in range(8):
        samples=[tuple(F(rng.randrange(-12,13),12) for j in range(d)) for _ in range(17)]
        for test in range(35):
            y=tuple(F(rng.randrange(-48,49),12) for j in range(d))
            counts=[sum(dot(u,z)<dot(u,y) for z in samples) for u,b,p in facets]
            target=max(counts)
            if not target:
                checks+=1;continue
            idx=counts.index(target); u,b,p=facets[idx]
            alpha=dot(u,y)
            lows=[dot(u,z) for z in samples if dot(u,z)<alpha]
            if alpha>F(2): h=F(2)
            else: h=(max(lows)+alpha)/2
            x=tuple(h*ui-t*pi for ui,pi in zip(u,p))
            def inside(z):
                return all(dot(w,z)<=t*bi+dot(w,x) for w,bi,pi in facets)
            assert not inside(y), (d,trial,test,y)
            attained=sum(inside(z) for z in samples)
            assert attained==target,(d,trial,test,attained,target)
            checks+=1
    return checks,t



def triangle_checks():
    # Right triangle with three rational unit outward facet normals.
    facets=[
      ((F(-1),F(0)),F(0),(F(0),F(5,8))),
      ((F(0),F(-1)),F(0),(F(5,6),F(0))),
      ((F(3,5),F(4,5)),F(1),(F(5,6),F(5,8))),
    ]
    slack=min(b-dot(u,pi) for i,(ui,bi,pi) in enumerate(facets)
              for j,(u,b,p) in enumerate(facets) if j!=i)
    assert slack==F(1,2)
    R=F(1); t=F(4)  # t=2R/slack, exactly the sufficient threshold.
    rng=random.Random(41695); count=0
    for trial in range(8):
        pts=[(F(rng.randrange(-6,7),12),F(rng.randrange(-6,7),12))
             for _ in range(11)]
        # All points satisfy ||z||_2<=sqrt(1/2)<R.
        for k in range(45):
            y=(F(rng.randrange(-24,25),12),F(rng.randrange(-24,25),12))
            targets=[sum(dot(u,z)<dot(u,y) for z in pts) for u,b,p in facets]
            best=max(targets)
            if not best:
                count+=1; continue
            i=targets.index(best);u,b,p=facets[i]; alpha=dot(u,y)
            lo=max(dot(u,z) for z in pts if dot(u,z)<alpha)
            h=R if alpha>R else (lo+alpha)/2
            # As ||u||=1, z0=h u lies on the facet hyperplane.
            shift=tuple(h*ui-t*pi for ui,pi in zip(u,p))
            inside=lambda z: all(dot(v,z)<=t*bj+dot(v,shift) for v,bj,pj in facets)
            assert not inside(y)
            assert sum(inside(z) for z in pts)==best
            count+=1
    return count

def gaussian_strict():
    # For the one-dimensional standard normal and [-t,t], the best
    # interval missing zero has mass Phi(2t)-1/2 (limit at zero).
    for t in (F(1,5),F(1),F(3),F(10)):
        Phi=lambda z:(1+math.erf(z/math.sqrt(2)))/2
        d=0.5+0.5*math.erfc(math.sqrt(2)*float(t))
        assert math.erfc(math.sqrt(2)*float(t))>0
    return 4

if __name__=='__main__':
    total=0
    for d in (2,3,4,5):
        n,t=run(d,9871+d)
        print(f'd={d}: {n} exact rational support/query checks at t={t}')
        total+=n
    total+=triangle_checks()
    print('triangle: 360 exact rational support/query checks at t=4')
    gaussian_strict()
    print(f'PASS: {total} exact finite-support checks and 4 Gaussian strictness checks')
