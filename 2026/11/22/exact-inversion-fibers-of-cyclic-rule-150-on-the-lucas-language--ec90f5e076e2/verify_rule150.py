#!/usr/bin/env python3
"""Independent exact finite checks of the cyclic hard-core Rule-150 claims.

Standard library only. The exhaustive check enumerates every indexed binary source
of each tested length; it is not a substitute for the all-length mathematical proof.
"""
from collections import Counter


def lucas(n):
    a,b=2,1
    for _ in range(n):
        a,b=b,a+b
    return a


def valid_tuple(x):
    n=len(x)
    return all(not(x[i] and x[(i+1)%n]) for i in range(n))


def step_tuple(x):
    n=len(x)
    return tuple(x[(i-1)%n]^x[i]^x[(i+1)%n] for i in range(n))


def bit_step(x,n):
    mask=(1<<n)-1
    left=((x<<1)&mask)|(x>>(n-1))
    right=(x>>1)|((x&1)<<(n-1))
    return (left^x^right)&mask


def valid_bits(x,n):
    return not (x & (((x<<1)&((1<<n)-1)) | (x>>(n-1))))


def spectrum(n,steps=1):
    counts=Counter()
    src=0
    for x in range(1<<n):
        if not valid_bits(x,n):
            continue
        src+=1
        y=x
        for _ in range(steps):
            y=bit_step(y,n)
        counts[y]+=1
    return Counter(counts.values()),src,counts


def check():
    tested=0
    for n in range(3,19):
        hist,src,pre=spectrum(n)
        assert src==lucas(n),(n,src,lucas(n))
        if n%3:
            expected={1:lucas(n)}
        else:
            m=n//3
            expected={1:lucas(n)-3*(2**m)+3,
                      2:3*(2**(m-1)-1),3:1}
        assert {k:v for k,v in hist.items() if v}=={k:v for k,v in expected.items() if v},(n,hist,expected)
        if n%3==0:
            assert pre[(1<<n)-1]==3
        else:
            assert max(hist)==1
        # Independent coordinate implementation on ALL admissible source configurations.
        for x in range(1<<n):
            if valid_bits(x,n):
                tup=tuple((x>>i)&1 for i in range(n))
                assert valid_tuple(tup)
                other=step_tuple(tup)
                out=tuple((bit_step(x,n)>>i)&1 for i in range(n))
                assert out==other,(n,x)
        tested+=1
    stable=0
    for n in range(3,18):
        if n%2 and n%3==0:
            first,_,_=spectrum(n,1)
            for t in (2,3,4,5,6):
                hist,_,_=spectrum(n,t)
                assert hist==first,(n,t,hist,first)
                stable+=1
        elif n%3:
            for t in (2,3,5):
                hist,_,_=spectrum(n,t)
                assert hist==Counter({1:lucas(n)}),(n,t)
                stable+=1
    for n in (6,12,18,24):
        x=int(''.join('101000' for _ in range(n//6))[::-1],2)
        # Check the pattern is cyclically admissible and is killed first at step 2.
        assert valid_bits(x,n)
        assert bit_step(x,n)!=0
        assert bit_step(bit_step(x,n),n)==0
    print(f'VERIFY_OK exact_lengths={tested} iterate_cases={stable} second_step_witnesses=4')


if __name__=='__main__':
    check()
