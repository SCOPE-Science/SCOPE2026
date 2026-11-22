"""Exact rational checks of the cubic-spacing Gabor frame inequality.

Run: python3 checker.py. This verifies selected finite grids; the theorem
for arbitrary real shifts follows from the analytic argument.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from collections import Counter


def circ_diff(x, y):
    """Signed shortest torus displacement; square is unambiguous."""
    return (x-y+Q(1,2)) % 1-Q(1,2)


def frame_bounds(shifts):
    r=len(shifts)
    m=Counter(x%1 for x in shifts)
    pts=sorted(m)
    assert pts
    def pot(x):
        return 4*sum(n*circ_diff(x,y+Q(1,2))**2 for y,n in m.items())
    vals=[]
    for i,y in enumerate(pts):
        z=pts[(i+1)%len(pts)]+(i+1==len(pts))
        mid=(y+z)/2
        deriv8=sum(n*circ_diff(mid,p+Q(1,2)) for p,n in m.items())
        vert=mid-deriv8/r
        candidate=max(y,min(z,vert))
        vals.append(pot(candidate))
    return min(vals),Q(r),pts


def test():
    trials=0; eq=0; cross=0
    for r in range(1,7):
        for den in [4,6,8]:
            for v in combinations_with_replacement(range(den),r):
                xs=[Q(t,den) for t in v]
                A,B,distinct=frame_bounds(xs)
                k=len(distinct)
                gaps=[(distinct[(i+1)%k]-distinct[i])%1 for i in range(k)]
                if k==1: gaps=[Q(1)]
                C=Q(r,3)*(1-sum(g**3 for g in gaps))
                def F(x):
                    return 4*sum(circ_diff(x,t+Q(1,2))**2 for t in xs)
                midpoint_excess=sum(g*(F((distinct[i]+distinct[(i+1)%k]+(i+1==k))/2)-A) for i,g in enumerate(gaps))
                assert C-A==midpoint_excess, (r,den,xs,C-A,midpoint_excess)
                gap_excess=Q(r,3)*sum((g-Q(1,k))**2*(g+Q(2,k)) for g in gaps)
                assert Q(r,3)*(1-Q(1,k*k))-A==gap_excess+midpoint_excess
                assert A<=C, (r,den,xs,A,C)
                expected= k>1
                assert (A>0)==expected
                assert B==r
                # Equality cases must be equally spaced sites with equal multiplicities.
                balanced=(r%k==0 and all(g==Q(1,k) for g in gaps) and all(v==r//k for v in Counter(xs).values()))
                assert (A==C)==balanced,(r,den,xs,A,C,balanced)
                assert C<=Q(r,3)*(1-Q(1,k*k))
                trials+=1;eq+=int(A==C)
                if k==r:
                    D=Q(r,3)*sum((g-Q(1,r))**2*(g+Q(2,r)) for g in gaps)
                    assert Q(r*r-1,3*r)-A>=D
                    cross+=1
        # Explicit multiple-cluster equality constructions, for all divisors
        for k in range(1,r+1):
            if r%k: continue
            xs=[Q(i,k) for i in range(k) for z in range(r//k)]
            A,B,pts=frame_bounds(xs)
            assert A==Q(r,3)*(1-Q(1,k*k))
    print('PASS:',trials,'exact rational designs,',eq,'equality designs,',cross,'gap-deficit checks; all 6 values of r.')

if __name__=='__main__':
    test()
