"""Independent finite checks for polygon boundary-hull vertex laws.
Only finite diagnostics; the all-sample-size theorem is proved analytically.
"""
from math import factorial
from itertools import product
import numpy as np
from scipy.spatial import ConvexHull

rng=np.random.default_rng(20261102)

def expected(p,n):
    p=np.array(p,dtype=float)
    return float(np.sum(2-2*(1-p)**n-n*p*(1-p)**(n-1)))

def exact_pmf(p,n):
    m=len(p)
    out={}
    for c in product(range(n+1),repeat=m):
        if sum(c)!=n:
            continue
        weight=factorial(n)
        for x, k in zip(p,c):
            weight*=x**k/factorial(k)
        v=sum(min(k,2) for k in c)
        out[v]=out.get(v,0)+weight
    return out

def points_on_boundary(vertices,p,n,rep):
    m=len(vertices)
    ids=rng.choice(m,size=(rep,n),p=p)
    t=rng.random((rep,n,1))
    pts=vertices[ids]+t*(vertices[(ids+1)%m]-vertices[ids])
    counts=np.stack([(ids==i).sum(axis=1) for i in range(m)],axis=1)
    return pts, np.minimum(counts,2).sum(axis=1)

polygons=[
    np.array([[0.,0.],[2.,0.],[.7,1.5]]),
    np.array([[0.,0.],[2.,0.],[3.,1.7320508075688772],[1.,1.7320508075688772]]),
    np.array([[0.,0.],[2.,0.],[2.,1.],[0.,1.]]),
    np.array([[0.,0.],[3.,0.],[3.5,.8],[2.,2.],[.1,1.7]]),
]
checked=0
for P in polygons:
    lens=np.linalg.norm(np.roll(P,-1,axis=0)-P,axis=1)
    p=lens/lens.sum()
    for n in (3,4,6,9):
        pmf=exact_pmf(p,n)
        assert abs(sum(pmf.values())-1)<1e-9
        assert abs(sum(k*v for k,v in pmf.items())-expected(p,n))<1e-9
        checked+=1
    pts,pred=points_on_boundary(P,p,12,2500)
    geom=np.array([len(ConvexHull(x).vertices) for x in pts])
    assert np.array_equal(geom,pred)

# Equal-length rhombi with different angles have indistinguishable laws.
rhombi=[np.array([[0.,0.],[2.,0.],[3.,1.7320508075688772],[1.,1.7320508075688772]]),np.array([[0.,0.],[2.,0.],[2.,2.],[0.,2.]])]
for n in (3,4,7,11):
    ps=[np.linalg.norm(np.roll(R,-1,axis=0)-R,axis=1) for R in rhombi]
    ps=[v/v.sum() for v in ps]
    assert np.allclose(ps[0],ps[1])
    assert all(abs(exact_pmf(ps[0],n).get(k,0)-exact_pmf(ps[1],n).get(k,0))<1e-12 for k in set(exact_pmf(ps[0],n))|set(exact_pmf(ps[1],n)))

# Algebraic root-and-multiplicity extraction from the entire mean sequence.
p=[.11,.11,.17,.28,.33]
assert abs(sum(p)-1)<1e-12
q=1-min(p)
for n in (60,120,200):
    a=lambda k: sum(2*(1-x)**k+k*x*(1-x)**(k-1) for x in p)
    approx=a(n+1)/a(n)
    assert abs(approx-q)<.03
print('VERIFY_OK polygons=4 exact_occupancy_mean_cases=',checked,
      'geometric_hull_trials=',10000,'inverse_rate_cases=3','equal_side_rhombi=1')
