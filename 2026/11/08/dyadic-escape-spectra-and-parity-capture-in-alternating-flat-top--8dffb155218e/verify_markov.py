#!/usr/bin/env python3
"""Exact rational Markov-graph checks for dyadic alternating flat-top tent maps.
Checks finite representative indices; the general algebraic proof handles every index.
"""
from fractions import Fraction as Q
from math import log

def T(x): return 1-2*abs(x)
def H(x): return T(T(x))

def build(m):
    assert isinstance(m,int) and m>=1
    r=Q(1,2**(m+1))
    pts={Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1),-r,r}
    if m%2==0:
        k=m//2
        pts.update(-1+Q(2,4**j) for j in range(2,k+1))
    else:
        k=(m-1)//2
        pts.update(-1+Q(1,4**j) for j in range(1,k+1))
    pts=sorted(pts)
    assert all(H(t) in pts for t in pts), (m,pts)
    ind=[i for i in range(len(pts)-1) if not (-r<(pts[i]+pts[i+1])/2<r)]
    assert len(ind)==(m//2+3 if m%2==0 else (m-1)//2+4)
    a=[]
    for i in ind:
        l,h=H(pts[i]),H(pts[i+1]); l,h=min(l,h),max(l,h)
        row=[int(l<=pts[j] and pts[j+1]<=h) for j in ind]
        # Markov containment: any target interval lies fully inside image or is disjoint
        assert all((l<=pts[j] and pts[j+1]<=h) or
                   (pts[j+1]<=l or h<=pts[j]) for j in ind)
        # Each starting interval has affine signed slope four
        mid=(pts[i]+pts[i+1])/2
        assert H(mid)==(H(pts[i])+H(pts[i+1]))/2
        assert abs(H(pts[i+1])-H(pts[i]))==4*(pts[i+1]-pts[i])
        a.append(row)
    return pts,ind,a

def mmul(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def characteristic_coeffs(A):
    # Newton identities, integer exact, monic det(t I-A)
    n=len(A); B=[[int(i==j) for j in range(n)] for i in range(n)]
    pows=[]
    for k in range(1,n+1):
        B=mmul(B,A)
        pows.append(sum(B[i][i] for i in range(n)))
    cs=[1]
    for k in range(1,n+1):
        num=-sum(cs[k-j]*pows[j-1] for j in range(1,k+1))
        assert num%k==0
        cs.append(num//k)
    return cs

def mat_vec(A,v): return [sum(a*b for a,b in zip(row,v)) for row in A]

def test(m):
    pts,ind,A=build(m)
    n=len(A)
    coeff=characteristic_coeffs(A)
    if m%2:
        k=(m-1)//2
        # det(tI-A)=t^3(t^(k+1)-4t^k+1), degree k+4
        target=[0]*(n+1);target[0]=1;target[1]=-4;target[k+1]=1 if k+1!=1 else target[k+1]+1
        # coefficient position of constant term +1 in factor t^(k+1)-4t^k+1 is k+1
        if k==0: target[1]=-3
    else:
        k=m//2
        target=[0]*(n+1);target[0]=1;target[1]=-4;target[k+1]=2
    assert coeff==target,(m,coeff,target)
    # Exact two-step successor on plateau and subsequent finite orbit
    u=Q(1)-Q(1,2**m)
    def ctrl(x):return T(u) if -Q(1,2**(m+1))<x<Q(1,2**(m+1)) else H(x)
    y=ctrl(Q(0))
    if m%2:
        k=(m-1)//2
        for z in range(k):y=ctrl(y)
        assert y==0,(m,y)
    else:
        k=m//2
        for z in range(k+1):y=ctrl(y)
        assert y==-1,(m,y)
    assert ctrl(-1)==-1
    # Exact survivor-length calculation by Markov paths vs direct preimage splitting.
    lengths=[pts[j+1]-pts[j] for j in ind]
    assert sum(lengths)==Q(2)-Q(1,2**m)
    v=lengths
    for j in range(1,7):
        survival=sum(v, Q(0))/4**(j-1)
        assert Q(0)<survival<=2
        v=mat_vec(A,v)
    return n

if __name__=='__main__':
    N=0
    for m in range(1,23):
        N+=test(m)
    # Independent fixed-grid cylinder enumeration, not using the Markov transfer matrix.
    comparisons=0
    for m in range(1,7):
        pts, inds, A = build(m)
        r=Q(1,2**(m+1))
        lengths=[pts[i+1]-pts[i] for i in inds]
        v=lengths
        for n in range(1,5):
            if n>1: v=mat_vec(A,v)
            predicted=sum(v,Q(0))/4**(n-1)
            denom=2**(m+1)*4**n
            numerator=0
            for j in range(-denom,denom):
                x=Q(2*j+1,2*denom)
                for _ in range(n):
                    if -r<x<r:break
                    x=H(x)
                else:numerator+=1
            assert predicted==Q(numerator,denom),(m,n,predicted,numerator,denom)
            comparisons+=1
    print('DYADIC_ALTERNATING_TENT_EXACT_MARKOV_AND_CHARPOLY_OK', 'parameters=22', 'cells_checked=',N)
    print('DIRECT_GRID_CYLINDER_LENGTHS_OK','independent_comparisons=',comparisons)
