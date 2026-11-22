#!/usr/bin/env python3
"""Independent finite-field and footprint checks for the anticanonical F_1 torus code.
Run with Python 3 (standard library only)."""
from itertools import combinations
from collections import defaultdict

A = tuple((i,j) for i in range(4) for j in range(4-i) if i+j >= 1)
assert len(A) == 9
TARGET_MAX = [(3,0), (2,1), (2,0), (1,2), (1,1), (1,0), (0,3), (0,2), (0,1)]

def footprint_coefficients(B):
    # For t>=4 the uncovered monomials in [0,t-1]^2 comprise a
    # 3x3 corner and at most six strips of length t-3.
    corner = sum(all(i<a or j<b for a,b in B)
                 for i in range(3) for j in range(3))
    horizontal = sum(all(j<b for a,b in B) for j in range(3))
    vertical = sum(all(i<a for a,b in B) for i in range(3))
    return horizontal+vertical, corner - 3*(horizontal+vertical)

def footprint_at(B,t):
    return sum(all(i<a or j<b for a,b in B)
               for i in range(t) for j in range(t))

def verify_footprint():
    for r in range(1,10):
        r4 = []; slopes=[]
        for B in combinations(A,r):
            slope,intercept=footprint_coefficients(B)
            assert footprint_at(B,4) == 4*slope+intercept
            assert footprint_at(B,5) == 5*slope+intercept
            r4.append(4*slope+intercept)
            slopes.append(slope)
        a,b=TARGET_MAX[r-1]
        assert max(r4)==4*a+b,(r,max(r4),4*a+b)
        assert max(slopes)==a,(r,max(slopes),a)
        # For all t>=4 every profile stays under a*t+b.
        assert all(x<=4*a+b for x in r4)
        assert all(x<=a for x in slopes)
        print('rank=%d, subsets=%d, footprint_at_t4=%d, max_slope=%d, bound=%dt%+d' %
              (r,len(r4),max(r4),max(slopes),a,b))

def gf_rank(columns, p):
    basis=[]
    for col in columns:
        w=list(col)
        for pv,row in basis:
            if w[pv]:
                c=w[pv];w=[(x-c*y)%p for x,y in zip(w,row)]
        if any(w):
            pv=next(i for i,x in enumerate(w) if x)
            inv=pow(w[pv],-1,p)
            basis.append((pv,tuple((x*inv)%p for x in w)))
    return len(basis)

def finite_q5_check():
    p=5;t=p-1
    pts=[(x,y) for x in range(1,p) for y in range(1,p)]
    cols=[tuple(pow(x,i,p)*pow(y,j,p)%p for i,j in A) for x,y in pts]
    # For each point subset, compute evaluation rank exactly. 2^16=65,536 subsets.
    # A breadth-first pivot-basis recursion avoids approximate rank estimates.
    n=len(pts)
    max_points_for_rank=[-1]*10
    nsub=0
    for k in range(n+1):
        for idx in combinations(range(n), k):
            rr=gf_rank([cols[j] for j in idx],p)
            if k>max_points_for_rank[rr]:max_points_for_rank[rr]=k
            nsub+=1
    for rr in range(1,10):
        max_zero=max(max_points_for_rank[:10-rr])
        a,b=TARGET_MAX[rr-1]
        expect=a*t+b if rr<=6 else (2 if rr==7 else 1 if rr==8 else 0)
        assert max_zero==expect,(rr,max_zero,expect)
    assert nsub==1<<16
    print('F5_EXHAUSTIVE: 65536 subsets, max common zeros by rank',
          [max(max_points_for_rank[:10-r]) for r in range(1,10)])

def construction_check(p):
    # Find three distinct nonzero slopes and off-line points.
    t=p-1
    slopes=[1,2,3]
    def line(x,y,c):return (x-c*y)%p
    def zero_set(fn):return {(x,y) for x in range(1,p) for y in range(1,p) if fn(x,y)%p==0}
    # For r=1, three distinct lines through the blown-up torus fixed point.
    f=lambda x,y:line(x,y,1)*line(x,y,2)*line(x,y,3)
    assert len(zero_set(f))==3*t
    # For r=2, product of two slope lines times a pencil through a third torus point.
    P=(3,1) if p>3 else None
    s0=lambda x,y:line(x,y,1)*line(x,y,2)
    W=[lambda x,y:s0(x,y)*(x-P[0]),lambda x,y:s0(x,y)*(y-P[1])]
    assert len(set.intersection(*(zero_set(f) for f in W)))==2*t+1
    # Full residual affine-linear system yields exactly two slope fibers.
    W3=[s0,lambda x,y:s0(x,y)*x,lambda x,y:s0(x,y)*y]
    assert len(set.intersection(*(zero_set(f) for f in W3)))==2*t
    # A line through origin times all quadratics vanishing at 2,1,0 torus points.
    # Use explicit coefficient-nullspaces over Fp.
    pts=[(1,2),(1,3)]
    Q=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
    def constrained_quad(z):
        # Basis of kernel of first z evaluation rows using pivot elimination
        rows=[tuple(pow(x,i,p)*pow(y,j,p)%p for i,j in Q) for x,y in pts[:z]]
        if z==0:return [tuple(1 if i==j else 0 for i in range(6)) for j in range(6)]
        pivotcols=[];rr=[list(v) for v in rows]
        rank=0
        for c in range(6):
            k=next((k for k in range(rank,z) if rr[k][c]),None)
            if k is None:continue
            rr[rank],rr[k]=rr[k],rr[rank]
            inv=pow(rr[rank][c],-1,p)
            rr[rank]=[u*inv%p for u in rr[rank]]
            for j in range(z):
                if j!=rank and rr[j][c]:
                    a=rr[j][c];rr[j]=[(u-a*v)%p for u,v in zip(rr[j],rr[rank])]
            pivotcols.append(c);rank+=1
            if rank==z:break
        basis=[]
        for fc in range(6):
            if fc in pivotcols:continue
            v=[0]*6;v[fc]=1
            for j,pc in enumerate(pivotcols):v[pc]=-rr[j][fc]%p
            basis.append(tuple(v))
        return basis
    for z,r in [(2,4),(1,5),(0,6)]:
        B=constrained_quad(z)
        assert len(B)==r
        def make(b):
            return lambda x,y:(x-y)*sum(co*pow(x,i,p)*pow(y,j,p) for co,(i,j) in zip(b,Q))
        common=set.intersection(*(zero_set(make(b)) for b in B))
        assert len(common)==t+z,(z,len(common))
    print(f'F{p}_CONSTRUCTION: maxima attained for ranks 1..6')

if __name__=='__main__':
    verify_footprint()
    finite_q5_check()
    for p in [5,7,11]:construction_check(p)
    print('ANTICANONICAL_F1_HIERARCHY_VERIFIED')
