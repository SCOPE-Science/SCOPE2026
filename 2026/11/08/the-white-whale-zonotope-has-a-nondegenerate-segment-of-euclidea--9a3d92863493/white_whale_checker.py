"""Reproducible finite checks for minimum-width and incenter geometry of all-subset zonotopes.

Uses integer cofactors and deterministic high-precision integer root enclosures; the
all-dimensions theorem is proved in the accompanying mathematical argument.
"""
import itertools
from math import gcd, isqrt, comb
from functools import reduce


def det(A):
    n=len(A)
    if n==1:return A[0][0]
    if n==2:return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    total=0
    for j,z in enumerate(A[0]):
        if z:
            total+=(-1)**j*z*det([[row[k] for k in range(n) if k!=j] for row in A[1:]])
    return total


def primitive_normal(rows,d):
    entries=[(-1)**j*det([[row[k] for k in range(d) if k!=j] for row in rows]) for j in range(d)]
    g=reduce(gcd, entries)
    if g==0:return None
    a=tuple(x//g for x in entries)
    if sum(a)<0 or (sum(a)==0 and next((x for x in a if x),0)<0):a=tuple(-x for x in a)
    return a


def cube_rays(d):
    bits=[v for v in itertools.product((0,1),repeat=d) if any(v)]
    rays=set()
    for ids in itertools.combinations(range(len(bits)),d-1):
        v=primitive_normal([bits[j] for j in ids],d)
        if v is not None:rays.add(v)
    return bits,rays


def support_twice(a,bits):
    return sum(abs(sum(x*y for x,y in zip(a,v))) for v in bits)

Q=10**28

def sqrt_lower(n):
    return isqrt(n*Q*Q)

def certify_nonnegative_affine_sqrts(h2,a,d,t_case):
    # Prove h=(h2/2) >= r_d*|a| + t_d*|sum(a)|.
    # The RHS contains radicals; compare using integer lower/upper bounds.
    # Equality is handled by exact explicit radical patterns.
    normsq=sum(x*x for x in a)
    S=abs(sum(a))
    if S==0 and sorted(x for x in a if x)==[-1,1]:
        return h2==2**(d-1)  # sharp Szarek equality for opposite equal coefficients
    C=2**(d-3) if d>=3 else None
    if d==2:
        # radius = 1/sqrt(2), t=1-1/sqrt(2)
        # h-S >= (sqrt(2*normsq)-S)/sqrt(2)
        L=(h2-2*S)*Q
        root_upper=sqrt_lower(2*normsq)+1
        # 2h - 2S >= sqrt(2*normsq) - sqrt(2)*S
        R=root_upper-sqrt_lower(2)*S
        if L>=R:return True
        return a in ((1,0),(0,1)) and h2==2
    # radius C*sqrt(2); t = C*(3-sqrt(6))
    # 2h >= 2C*(sqrt(2*normsq)+3*S-sqrt(6)*S)
    L=h2*Q
    root_2norm_upper=sqrt_lower(2*normsq)+1
    root_6_lower=sqrt_lower(6)
    R=2*C*(root_2norm_upper+3*S*Q-root_6_lower*S)
    if L>=R:return True
    # Exact equality at 3-sparse signed unit patterns (a,b,c)=(1,1,-1).
    nz=sorted(x for x in a if x)
    return (nz==[-1,1,1] or nz==[-1,-1,1]) and h2==6*C


def strict_endpoint_slack(h2,a,d):
    """Prove the endpoint inequality is strict using outward radical bounds."""
    S=abs(sum(a))
    if not S:
        return False
    normsq=sum(x*x for x in a)
    if d==2:
        L=(h2-2*S)*Q
        R=(sqrt_lower(2*normsq)+1)-sqrt_lower(2)*S
    else:
        C=2**(d-3)
        L=h2*Q
        R=2*C*(sqrt_lower(2*normsq)+1+3*S*Q-sqrt_lower(6)*S)
    return L>R


def expected_extra_contact(a,d):
    nonzero=sorted(x for x in a if x)
    if d==2:
        return nonzero==[1]
    return nonzero==[-1,1,1]


def main():
    summary=[]
    for d in (2,3,4,5):
        bits,rays=cube_rays(d)
        extras=[]
        for a in rays:
            h2=support_twice(a,bits)
            assert certify_nonnegative_affine_sqrts(h2,a,d,d)
            if sum(a):
                if expected_extra_contact(a,d):
                    extras.append(a)
                    if d==2:
                        assert h2==2
                    else:
                        assert h2==6*2**(d-3)
                else:
                    assert strict_endpoint_slack(h2,a,d)
        assert len(extras)==(2 if d==2 else 3*comb(d,3))
        # Explicit candidate is an actual ray; its support achieves equality.
        candidate=(1,0) if d==2 else (1,1,-1)+(0,)*(d-3)
        assert candidate in rays or tuple(-x for x in candidate) in rays
        # Both signs for minimizing facet normal e_i-e_j give the radius.
        for i,j in itertools.combinations(range(d),2):
            a=tuple((1 if k==i else -1 if k==j else 0) for k in range(d))
            assert support_twice(a,bits)==2**(d-1)
        summary.append((d,len(bits),len(rays),len(extras)))
    print('WHITE_WHALE_FINITE_CHECKS_PASSED d,generators,rays,extra_endpoint_facets=',summary)

if __name__=='__main__':main()
