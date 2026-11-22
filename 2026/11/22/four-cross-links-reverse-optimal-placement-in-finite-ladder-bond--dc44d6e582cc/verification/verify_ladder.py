#!/usr/bin/env python3
"""Independent exact checks for four-crosslink bond percolation on two rails."""
from fractions import Fraction
from itertools import combinations


def conditional_formula(L, locations, p, q):
    p, q = Fraction(p), Fraction(q)
    total = Fraction(0)
    for mask in range(1, 1 << len(locations)):
        active = [locations[i] for i in range(len(locations)) if mask & (1 << i)]
        weight = q ** len(active) * (1-q) ** (len(locations)-len(active))
        factor = p ** L
        for a, b in zip(active, active[1:]):
            factor *= 2-p**(b-a)
        total += weight*factor
    return total


def independent_edge_census(L, locations, p, q):
    # The exact count sums full edge configurations, without conditioning on rungs.
    p, q = Fraction(p), Fraction(q)
    assert len(locations) == 4
    rail_edges = [(j, j+1) for j in range(L)] + [(L+1+j,L+2+j) for j in range(L)]
    rungs = [(j, L+1+j) for j in locations]
    E = len(rail_edges)+len(rungs)
    den = p.denominator**(2*L)*q.denominator**4
    powp=[p.numerator**k*(p.denominator-p.numerator)**(2*L-k) for k in range(2*L+1)]
    powq=[q.numerator**k*(q.denominator-q.numerator)**(4-k) for k in range(5)]
    number=0
    for mask in range(1<<E):
        rm=mask&((1<<(2*L))-1)
        bm=mask>>(2*L)
        w=powp[rm.bit_count()]*powq[bm.bit_count()]
        if not w: continue
        parent=list(range(2*(L+1)))
        def root(x):
            while x!=parent[x]: x=parent[x]
            return x
        for i,(a,b) in enumerate(rail_edges):
            if rm>>i&1:
                x,y=root(a),root(b)
                if x!=y:parent[x]=y
        for i,(a,b) in enumerate(rungs):
            if bm>>i&1:
                x,y=root(a),root(b)
                if x!=y:parent[x]=y
        if root(0)==root(2*L+1):number+=w
    return Fraction(number,den)


def limit_coefficient(L, loc, lam):
    assert loc[0]==0 and loc[-1]==L
    a,b,c=[loc[i+1]-loc[i] for i in range(3)]
    return a*a+b*b+c*c+lam*(a+c)


def main():
    checks=0
    for L in range(3,6):
        for loc in combinations(range(L+1),4):
            for p,q in [(Fraction(1,2),Fraction(2,3)),(Fraction(3,4),Fraction(1,2))]:
                exact=independent_edge_census(L,loc,p,q)
                formula=conditional_formula(L,loc,p,q)
                assert exact==formula,(L,loc,p,q,exact,formula)
                checks+=1
    print('Full-edge independent census equals conditional formula:',checks,'exact rational cases')
    for L in range(5,12):
        for lam in [0,1,3,5,2*L-7]:
            locs=[(0,)+x+(L,) for x in combinations(range(1,L),2)]
            mincost=min(limit_coefficient(L,loc,lam) for loc in locs)
            best=[loc for loc in locs if limit_coefficient(L,loc,lam)==mincost]
            for eps in [Fraction(1,5000),Fraction(1,10000)]:
                p=1-eps
                q=1-lam*eps
                vals=[conditional_formula(L,loc,p,q) for loc in locs]
                top=max(vals)
                assert all(loc in best for loc,val in zip(locs,vals) if val==top),(L,lam,eps)
    print('Small-failure optimizer agrees with quadratic coefficient: 70 rational comparisons')
    for L in range(5,13):
        for lam in range(2*L-7,2*L+1):
            locs=[(0,)+x+(L,) for x in combinations(range(1,L),2)]
            top=min(limit_coefficient(L,x,lam) for x in locs)
            assert limit_coefficient(L,(0,1,L-1,L),lam)==top
            if lam>2*L-8:
                assert sum(limit_coefficient(L,x,lam)==top for x in locs)==1
    print('Cluster uniqueness beyond lambda > 2L-8: 64 integer cases')
    for L in range(5,13):
        # Under perfect rungs, three gaps as balanced as possible maximize reliability.
        locs=[(0,)+x+(L,) for x in combinations(range(1,L),2)]
        p=Fraction(3,5)
        vals=[conditional_formula(L,loc,p,1) for loc in locs]
        best=max(vals)
        assert all(max(loc[i+1]-loc[i] for i in range(3))-min(loc[i+1]-loc[i] for i in range(3))<=1 for loc,v in zip(locs,vals) if v==best)
        # Fixed imperfect crosslinks favor endpoint clustering for near-perfect rails.
        p=Fraction(999999,1000000)
        q=Fraction(2,3)
        vals=[conditional_formula(L,loc,p,q) for loc in locs]
        assert [loc for loc,v in zip(locs,vals) if v==max(vals)]==[(0,1,L-1,L)]
        # With three rungs, balanced central position is always optimal.
        locs3=[(0,j,L) for j in range(1,L)]
        vals3=[conditional_formula(L,loc,p,q) for loc in locs3]
        assert all(abs(2*loc[1]-L)<=1 for loc,v in zip(locs3,vals3) if v==max(vals3))
    print('Perfect/imperfect layout reversal and three-rung bound: 24 rational checks')
    print('PASS')

if __name__=='__main__': main()
