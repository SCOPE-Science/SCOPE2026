"""Standalone deterministic and random crosschecks of metric Voronoi rigidity.
Public research supplement; no third-party modules required.
"""
import math, random, itertools

def nearest_brute(x, p, radius=2):
    n=len(x); candidates=[]
    for bits in (0.,.5):
        for z in itertools.product(range(-radius, radius+1),repeat=n):
            site=tuple(t+bits for t in z)
            delta=[abs(a-b) for a,b in zip(x,site)]
            val=max(delta) if p==float('inf') else sum(t**p for t in delta)
            candidates.append((val, site))
    val=min(a for a,_ in candidates)
    return tuple(site for a,site in candidates if abs(a-val)<1e-10)

def round_cosets(x,p):
    # interior [0,.5]^n: best integer and half-shifted coset are 0 and (.5,...,.5)
    n=len(x)
    a=max(x) if p==float('inf') else sum(t**p for t in x)
    b=max(.5-t for t in x) if p==float('inf') else sum((.5-t)**p for t in x)
    return -1 if a<b-1e-12 else 1 if a>b+1e-12 else 0

checks=0
rng=random.Random(20261113)
for n in (1,2,3,4):
    for _ in range(250):
        x=tuple(rng.uniform(.001,.499) for j in range(n))
        for p in (1.,1.25,1.5,2.,3.,4.,10.,float('inf')):
            b=nearest_brute(x,p,radius=1)
            label=round_cosets(x,p)
            predicted=(.0,)*n if label==-1 else (.5,)*n if label==1 else None
            if predicted is not None:
                assert b==(predicted,), (n,x,p,b,predicted)
            if p in (1.,2.) or n<=2:
                assert label==round_cosets(x,2.), (n,x,p,label)
            checks+=1
for p in (1.25,1.5,1.9,2.1,3.,4.,10.,float('inf')):
    t=.023
    u=[.25+t,.25+t,.25-2*t]
    if p==float('inf'):
        # positive shift of last coordinate moves l1 into half-coset while l-infinity chooses integer
        u[2]+=.001
    else:
        gp=lambda z:(.25+z)**p-(.25-z)**p
        raw=2*gp(t)-gp(2*t)
        assert abs(raw)>1e-12
        # calculate delta fine enough to reverse l1 sign but preserve the lp classification
        sign=1 if raw<0 else -1
        u[2]+=sign*1e-7
    assert round_cosets(u,1.)!=round_cosets(u,p),(p,u)
    assert round_cosets(u,1.)!=0 and round_cosets(u,p)!=0
    checks+=1
# Strict rational three-dimensional witness: p=1 selects the half coset,
# while p=3 and p=infinity select the integer coset.
from fractions import Fraction
xx=[Fraction(3,10),Fraction(3,10),Fraction(151,1000)]
assert sum(xx)>Fraction(3,4)
assert sum(t**3 for t in xx)<sum((Fraction(1,2)-t)**3 for t in xx)
assert max(xx)<max(Fraction(1,2)-t for t in xx)
checks+=3
# Weighted l1 versus weighted l2^2: same minimizers in every dimension.
for n in (1,2,3,4):
    for _ in range(250):
        x=tuple(rng.uniform(.001,.499) for j in range(n))
        w=tuple(rng.uniform(.1,4.) for j in range(n))
        left=sum(a*b for a,b in zip(w,x))
        thresh=sum(w)/4
        s1=sum(a*b for a,b in zip(w,x))
        t1=sum(a*(.5-b) for a,b in zip(w,x))
        s2=sum(a*b*b for a,b in zip(w,x))
        t2=sum(a*(.5-b)**2 for a,b in zip(w,x))
        assert (s1<t1)==(s2<t2)==(left<thresh)
        checks+=1
print(f'PASS {checks} deterministic seeded geometric checks')
