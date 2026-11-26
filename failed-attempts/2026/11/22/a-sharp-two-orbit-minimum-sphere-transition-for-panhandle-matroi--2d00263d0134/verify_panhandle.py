"""Exact arithmetic corroboration of the canonical panhandle outer-ball theorem.

Requires only Python 3 standard library. Run: python verify_panhandle.py
"""
from fractions import Fraction as F
from itertools import combinations


def all_vertices(r, p, t):
    n = p+t
    head = range(p)
    tail = range(p,n)
    bases = list(combinations(head,r))
    bases += [b+(j,) for b in combinations(head,r-1) for j in tail]
    return [tuple(F(int(i in b)) for i in range(n)) for b in bases]


def exact_ball(r,p,t):
    n=p+t
    if (r-1)*t <= p:
        return (F(r,n),)*n, F(r)-F(r*r,n), 'all'
    return (F(r-1,p),)*p+(F(1,t),)*t, F(r)-F((r-1)**2,p)-F(1,t), 'mixed'


def squared_distance(v,w):
    return sum((x-y)**2 for x,y in zip(v,w))


def test(r,p,t):
    n=p+t
    center,R2,mode=exact_ball(r,p,t)
    vertices=all_vertices(r,p,t)
    assert len(vertices)==__import__('math').comb(p,r)+t*__import__('math').comb(p,r-1)
    assert sum(center)==r
    assert R2>0
    assert all(sum(v)==r for v in vertices)
    for v in vertices:
        dist=squared_distance(v,center)
        assert dist<=R2, (r,p,t,dist,R2)
        ht=sum(v[p:])
        assert (dist==R2)==(mode=='all' or ht==1),(r,p,t)
    # Construct an explicit barycentric certificate on contact vertices.
    A=[v for v in vertices if sum(v[p:])==0]
    B=[v for v in vertices if sum(v[p:])==1]
    meanA=tuple(sum(v[i] for v in A)/len(A) for i in range(n))
    meanB=tuple(sum(v[i] for v in B)/len(B) for i in range(n))
    if mode=='all':
        lam=F(t*r,n)
        assert 0<=lam<=1
        witness=tuple((1-lam)*x+lam*y for x,y in zip(meanA,meanB))
    else:
        witness=meanB
    assert witness==center, (r,p,t,'barycenter failure')
    # Independent exact quadratic minimax witness: a center supported by equal-radius
    # contact points is globally optimal, uniquely, by the variance identity.
    for q in [-2,-1,0,1,2]:
        probe=tuple(center[i]+(F(q,5) if i==0 else -F(q,5) if i==1 else F(0)) for i in range(n))
        bound=R2+squared_distance(probe,center)
        avgA=sum(squared_distance(v,probe) for v in A)/len(A)
        avgB=sum(squared_distance(v,probe) for v in B)/len(B)
        certified=(1-F(t*r,n))*avgA+F(t*r,n)*avgB if mode=='all' else avgB
        assert certified==bound
        assert max(squared_distance(v,probe) for v in vertices)>=bound
    # Exact squared-radius improvement over the ambient hypersimplex sphere.
    improvement=F(r)-F(r*r,n)-R2
    expected=F(max(0,(r-1)*t-p)**2,p*t*n)
    assert improvement==expected
    if mode=='mixed':
        # Strict clearance of the omitted pure-head vertices.
        assert R2-squared_distance(A[0],center)==F(2*((r-1)*t-p),p*t)


if __name__=='__main__':
    count=0
    cases={'all':0,'mixed':0,'tie':0}
    for p in range(3,9):
        for r in range(2,p):
            for t in range(2,7):
                test(r,p,t)
                count+=1
                mode= 'tie' if (r-1)*t==p else ('all' if (r-1)*t<p else 'mixed')
                cases[mode]+=1
    assert all(v>0 for v in cases.values()),cases
    print('PANHANDLE_OUTER_BALL_EXACT_PASS',count,cases)
