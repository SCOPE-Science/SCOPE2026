#!/usr/bin/env python3
"""Exact finite-field checks for the Hesse cyclic cubic surface.

The universal assertion is proved geometrically in the accompanying manuscript;
these finite checks test independent counts and the splitting criterion.
"""
from collections import Counter


def point_count_prime(p, t):
    cubes=[pow(x,3,p) for x in range(p)]
    count=0
    # w = 1 (affine chart)
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (cubes[x]+cubes[y]+cubes[z]+1+t*x*y*z)%p==0:
                    count+=1
    # w=0, z=1
    for x in range(p):
        for y in range(p):
            if (cubes[x]+cubes[y]+1+t*x*y)%p==0:
                count+=1
    # w=z=0, y=1
    for x in range(p):
        if (cubes[x]+1)%p==0:
            count+=1
    # point [1:0:0:0] not on the surface
    return count


def nonsquare(p):
    squares={x*x%p for x in range(p)}
    return next(x for x in range(2,p) if x not in squares)


def point_count_quadratic(p,t):
    d=nonsquare(p)
    elems=[(a,b) for a in range(p) for b in range(p)]
    one=(1,0)
    zero=(0,0)
    def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def mul(a,b):return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def neg(a):return ((-a[0])%p,(-a[1])%p)
    cubed={a:mul(mul(a,a),a) for a in elems}
    root_count=Counter(cubed.values())
    T=(t,0)
    result=0
    # projective P^2 charts x=1, then x=0 y=1, then x=y=0 z=1
    for y in elems:
        for z in elems:
            f=add(add(add(one,cubed[y]),cubed[z]),mul(T,mul(y,z)))
            result+=root_count[neg(f)]
    for z in elems:
        f=add(one,cubed[z]) # x=0,y=1
        result+=root_count[neg(f)]
    result+=root_count[neg(one)] # x=y=0,z=1
    return result


def validate():
    samples={}
    for p in (5,7,11,13,19,31):
        cubes={pow(x,3,p) for x in range(1,p)}
        counts=Counter()
        for t in range(p):
            if (t**3+27)%p==0:continue
            if p%3==1:
                c=(-1-t**3*pow(27,-1,p))%p
                split=c in cubes
                predicted=p*p+(7 if split else -2)*p+1
                lines=27 if split else 0
            else:
                predicted=p*p+p+1
                lines=3
            actual=point_count_prime(p,t)
            assert actual==predicted, (p,t,actual,predicted)
            counts[(lines, actual)]+=1
            if p in (5,7):
                aq=point_count_quadratic(p,t)
                q=p*p
                # For q=p^2, if p=5 all 27 split. If p=7, cubic nonresidue persists.
                if p%3==2 or (p%3==1 and split):
                    expected=q*q+7*q+1
                else:
                    expected=q*q-2*q+1
                assert aq==expected,(p,t,aq,expected)
        samples[str(p)]={f'{ln} lines, {pts} points':cnt for (ln,pts),cnt in sorted(counts.items())}
    # Nine geometric flex tangent restrictions over characteristic 7 & 13,
    # symbolic identity is given in proof; check every base flex using finite roots of unity.
    for p in (7,13,19,31):
        roots=[r for r in range(1,p) if r**3%p==1]
        assert len(roots)==3
        for t in range(p):
            if (t**3+27)%p==0:continue
            c=(1+t**3*pow(27,-1,p))%p
            for r in roots:
                v=(t*r*pow(3,-1,p))%p
                # set y=v*x-r*r*z and compare f on tangent with c*x^3
                for x,z in ((1,0),(0,1),(1,1),(2,3)):
                    y=(v*x-r*r*z)%p
                    assert (x**3+y**3+z**3+t*x*y*z-c*x**3)%p==0
    return samples

if __name__=='__main__':
    import json
    print(json.dumps(validate(),sort_keys=True,indent=2))
    print('HESSE_CUBIC_SURFACE_FROBENIUS_VERIFIED')
