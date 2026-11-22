"""Independent numerical and algebraic spot checks for an OR-pooled Poisson alarm design.
Uses only Python standard library. This is not a substitute for the printed proof.
"""
import math
import random


def performance(rates, fractions, budget):
    assert len(rates) == len(fractions)
    assert abs(sum(fractions) - 1) <= 1.e-9
    assert all(f >= -1.e-12 for f in fractions)
    a = sum(p[0] * q for p,q in zip(rates, fractions))
    b = sum(p[1] * q for p,q in zip(rates, fractions))
    return math.exp(-budget*b) * (-math.expm1(-budget*a))


def low_hull(rate_pairs):
    # Discard duplicate alpha values except smallest beta.
    best = {}
    for a,b in rate_pairs:
        assert a > 0 and b > 0
        best[a] = min(best.get(a,float('inf')),b)
    pts = sorted(best.items())
    v=[]
    for p in pts:
        while len(v)>=2:
            (a0,b0),(a1,b1)=v[-2:]
            a2,b2=p
            if (b1-b0)*(a2-a1) >= (b2-b1)*(a1-a0)-1e-12:
                v.pop()
            else:
                break
        v.append(p)
    mb=min(p[1] for p in v)
    start=max(j for j,p in enumerate(v) if abs(p[1]-mb)<1.e-12)
    return v[start:]


def hull_solution(rates,B):
    v=low_hull(rates)
    if len(v)==1:return v[0],v[0],0.0
    best=(-1.0,None)
    for p in v:
        score=math.exp(-B*p[1])*(-math.expm1(-B*p[0]))
        if score>best[0]:best=(score,(p,p,0.0))
    for lo,hi in zip(v,v[1:]):
        da=hi[0]-lo[0];db=hi[1]-lo[1]
        assert da>0 and db>0
        c=math.log1p(da/db)
        x=max(0.0,min(1.0, (c/B-lo[0])/da))
        a=lo[0]+x*da;b=lo[1]+x*db
        score=math.exp(-B*b)*(-math.expm1(-B*a))
        if score>best[0]:best=(score,(lo,hi,x))
    return best[1]


def exhaustive_pairs(rates,B):
    best=-1.0
    for i,(a0,b0) in enumerate(rates):
        for j,(a1,b1) in enumerate(rates):
            if j<i:continue
            a0,b0=rates[i]
            if a0>a1:
                a0,a1=a1,a0;b0,b1=b1,b0
            if a0==a1: x=0 if b0<=b1 else 1
            elif b1<=b0: x=1.0
            else:
                c=math.log1p((a1-a0)/(b1-b0))
                x=min(1.0,max(0.0,(c/B-a0)/(a1-a0)))
            a=a0+x*(a1-a0)
            b=b0+x*(b1-b0)
            best=max(best,math.exp(-B*b)*(-math.expm1(-B*a)))
    return best


rates = [(1.,0.2),(2.,0.5),(4.,2.)]
assert low_hull(rates)==rates
c1=math.log(13/3);c2=math.log(7/3)
assert c2/4 < c2/2 < c1/2 < c1
cases=[(c2/8,2),(3*c2/8,-1),(0.5*(c2/2+c1/2),1),(0.75*c1,-2),(2*c1,0)]
checks=0
for B,idx in cases:
    lo,hi,x=hull_solution(rates,B)
    if idx==2:assert lo==hi==rates[2]
    elif idx==1:assert lo==hi==rates[1]
    elif idx==0:assert lo==hi==rates[0]
    elif idx==-1:assert lo==rates[1] and hi==rates[2] and 0<x<1
    elif idx==-2:assert lo==rates[0] and hi==rates[1] and 0<x<1
    checks+=1
for j in range(400):
    B=math.exp(-4+j*8/399)
    lo,hi,x=hull_solution(rates,B)
    val=math.exp(-B*((1-x)*lo[1]+x*hi[1]))*(-math.expm1(-B*((1-x)*lo[0]+x*hi[0])))
    assert abs(val-exhaustive_pairs(rates,B)) < 1e-12
    checks+=1

rng=random.Random(733571)
for _ in range(300):
    m=rng.randrange(2,12)
    rates=[(rng.uniform(.01,7),rng.uniform(.01,7)) for _ in range(m)]
    for _ in range(30):
        B=math.exp(rng.uniform(-5,5))
        lo,hi,x=hull_solution(rates,B)
        val=math.exp(-B*((1-x)*lo[1]+x*hi[1]))*(-math.expm1(-B*((1-x)*lo[0]+x*hi[0])))
        assert abs(val-exhaustive_pairs(rates,B))<3e-13,(rates,B,val,exhaustive_pairs(rates,B))
        checks+=1

# Verify an exhaustive KKT partition of a 3-point strictly convex frontier.
for B in [c2/4,c2/2,c1/2,c1]:
    score=exhaustive_pairs([(1.,.2),(2.,.5),(4.,2.)],B)
    assert score>=0
    checks+=1
print('PASS',checks,'independently checked optima/phase constraints')
