#!/usr/bin/env python3
"""Exact checks of norm-two coefficient lifting and the resulting progressions."""
from math import comb


def mul(a, b, d):
    return (a[0]*b[0] + d*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def pow_pair(a, n, d):
    z=(1,0)
    while n:
        if n&1: z=mul(z,a,d)
        a=mul(a,a,d)
        n//=2
    return z


def solution_at_odd_index(d, x, y, n):
    assert n>=1 and n%2 and x*x-d*y*y==2
    unit=(x*x-1,x*y)
    assert unit[0]*unit[0]-d*unit[1]*unit[1]==1
    out=mul((x,y),pow_pair(unit,(n-1)//2,d),d)
    assert out[0]*out[0]-d*out[1]*out[1]==2
    return out


def v_p(v,p):
    t=0
    while v%p==0 and v:
        v//=p
        t+=1
    return t


def direct_binomial(d,x,y,n):
    numerator_x=sum(comb(n,2*j)*x**(n-2*j)*y**(2*j)*d**j for j in range((n+1)//2))
    numerator_y=sum(comb(n,2*j+1)*x**(n-2*j-1)*y**(2*j+1)*d**j for j in range((n+1)//2))
    denominator=2**((n-1)//2)
    assert numerator_x%denominator==numerator_y%denominator==0
    return numerator_x//denominator,numerator_y//denominator


def check():
    examples=[(7,3,1),(23,5,1),(31,39,7)]
    count=0
    for d,x,y in examples:
        for n in (1,3,5,7,9,11,15,23,31,49):
            a,b=solution_at_odd_index(d,x,y,n)
            assert (a,b)==direct_binomial(d,x,y,n)
            for p in (7,23,31):
                if d%p==0:
                    assert v_p(b,p)==v_p(y,p)+v_p(n,p)
            count+=1
        for r in (1,2,3):
            n=d**r
            a,b=solution_at_odd_index(d,x,y,n)
            assert b%d**r==0
            z=b//d**r
            assert a*a-d**(2*r+1)*z*z==2
            assert a>2 and z>0
            s=((a-2)**2,(a-1)**2,d**(2*r+1)*z*z)
            assert s[0]+s[2]==2*s[1] and s[0]>0
            count+=1
    # The only positive m<23 with m≡7 mod8 are 7 and 15,
    # and m=15 fails x^2≡2 mod 3. The next m=23 has (5,1).
    assert [m for m in range(1,23) if m%8==7]==[7,15]
    assert {i*i%3 for i in range(3)}=={0,1}
    assert solution_at_odd_index(7,3,1,7)==(11427,4319)
    a,b=solution_at_odd_index(23,5,1,23)
    assert b%23==0
    print('VERIFY_OK exact_cases=%d m=[7,23,31] odd_power_levels=1,2,3 second_multiplier=23'%count)
    print('M7 r1 X=%d Z=%d'%(11427,4319//7))
    print('M23 r1 X=%d Z=%d'%(a,b//23))

if __name__=='__main__':check()
