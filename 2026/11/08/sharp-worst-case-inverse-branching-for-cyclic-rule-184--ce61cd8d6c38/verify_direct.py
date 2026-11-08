#!/usr/bin/env python3
"""Exhaustive independent ring-map verification of an exact predecessor maximum."""
from collections import Counter


def lucas(k):
    a,b=2,1
    for _ in range(k):a,b=b,a+b
    return a


def fibonacci(k):
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a


def successor(source,n):
    # Implement the local traffic rule directly with scalar bits, no inverse formula.
    bits=[(source>>i)&1 for i in range(n)]
    result=0
    for i in range(n):
        a,b,c=bits[(i-1)%n],bits[i],bits[(i+1)%n]
        bit=int((a==1 and b==0) or (b==1 and c==1))
        result |= bit<<i
    return result


def expected_max(n):
    return lucas(n//2) if n%2==0 else fibonacci((n+1)//2)


def target_is_alternating(n,y):
    return all(((y>>i)&1)!=((y>>((i+1)%n))&1) for i in range(n))


def target_is_single_defect(n,y):
    return sum(((y>>i)&1)==((y>>((i+1)%n))&1) for i in range(n))==1


for n in range(1,19):
    counts=[0]*(1<<n)
    for x in range(1<<n):
        counts[successor(x,n)]+=1
    max_count=max(counts)
    assert max_count==expected_max(n), (n,max_count,expected_max(n))
    max_set={i for i,c in enumerate(counts) if c==max_count}
    if n<=3:
        assert max_set==set(range(1<<n)),n
    elif n%2==0:
        assert max_set=={y for y in range(1<<n) if target_is_alternating(n,y)},n
        assert len(max_set)==2
    else:
        assert max_set=={y for y in range(1<<n) if target_is_single_defect(n,y)},n
        assert len(max_set)==2*n
    assert sum(counts)==1<<n
    print(f'n={n:02d} maximum={max_count:3d} maximizers={len(max_set):2d} absent={counts.count(0):6d}')
print('DIRECT_VERIFY_OK')
