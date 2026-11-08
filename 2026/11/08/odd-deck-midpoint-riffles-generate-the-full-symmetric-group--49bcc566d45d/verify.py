"""Finite exact checks for the odd-deck midpoint-interleaving group theorem.

This checker tests finite instances; the all-order proof is written separately.
Uses only the Python standard library.
"""
from fractions import Fraction
from math import factorial
from collections import deque


def merge(n,k):
    if k in (0,n):
        return tuple(range(n))
    left = [(Fraction(2*i+1,2*k),i) for i in range(k)]
    right = [(Fraction(2*j+1,2*(n-k)),k+j) for j in range(n-k)]
    keys = left + right
    assert len({x[0] for x in keys}) == n, 'unexpected odd-deck tie'
    return tuple(v for _,v in sorted(keys))


def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    b=[0]*len(a)
    for i,j in enumerate(a):b[j]=i
    return tuple(b)


def sign(a):
    return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1


def orbit_group(generators):
    n=len(generators[0]); eye=tuple(range(n)); seen={eye}; queue=deque([eye]);
    while queue:
        x=queue.popleft()
        for g in generators:
            y=compose(x,g)
            if y not in seen:
                seen.add(y);queue.append(y)
    return len(seen)


def power(g,e):
    x=tuple(range(len(g)))
    for _ in range(e): x=compose(x,g)
    return x


def check():
    checks=0
    for n in range(3,64,2):
        a=(n-1)//2
        A=merge(n,1);B=merge(n,n-1);C=merge(n,2)
        assert A==tuple(list(range(1,a+1))+[0]+list(range(a+1,n)))
        assert B==tuple(list(range(a))+[n-1]+list(range(a,n-1)))
        assert sign(C)==-1
        assert sign(A)==sign(B)==(-1)**a
        checks+=4
        # Check mixed 3-cycles furnished by the two overlapping cycles.
        p=a; S=set(range(a+1)); T=set(range(a,n))
        for i in range(1,a+1):
            U=power(A,i)
            for j in range(1,a+1):
                V=power(B,j)
                com=compose(compose(compose(inverse(U),inverse(V)),U),V)
                support={x for x in range(n) if com[x]!=x}
                assert len(support)==3 and p in support
                assert len(support&S)==2 and len(support&T)==2
                assert compose(compose(com,com),com)==tuple(range(n))
                checks+=3
        if n<=7:
            subgroup=orbit_group([A,B]); entire=orbit_group([A,B,C])
            assert subgroup==(factorial(n)//2 if n%4==1 else factorial(n))
            assert entire==factorial(n)
            checks+=2
    return checks


if __name__=='__main__':
    print('PASS finite exact midpoint/group checks:',check())
