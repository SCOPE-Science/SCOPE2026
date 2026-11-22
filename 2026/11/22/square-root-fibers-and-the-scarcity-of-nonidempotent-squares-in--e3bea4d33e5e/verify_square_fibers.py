#!/usr/bin/env python3
"""Direct finite enumeration of square roots of cyclic partial permutations.

Uses explicit partial-function tuples for the oracle, and the word/orbit
formula for the predicted fibers. No packages beyond Python's stdlib.
"""
from collections import Counter
from math import gcd


def fib(j):
    a, b = 0, 1
    for _ in range(j):
        a, b = b, a+b
    return a


def lucas(j):
    if j == 1: return 1
    if j == 2: return 3
    a,b = 1,3
    for _ in range(3,j+1): a,b=b,a+b
    return b


def word_fiber(bits):
    l = len(bits)
    if all(bits): return 1
    if not any(bits): return lucas(l)
    if any(bits[i] and not bits[(i+1)%l] and bits[(i+2)%l]
           for i in range(l)):
        return 0
    # Runs of missing edges, each preceded and followed by required edges.
    runs = []
    for i in range(l):
        if bits[i] and not bits[(i+1)%l]:
            j=(i+1)%l
            b=0
            while not bits[j]:
                b+=1
                j=(j+1)%l
            runs.append(b)
    answer = 1
    for b in runs:
        answer *= fib(b-1)
    return answer


def cyclic_word_count(l):
    return sum(not any(((m>>i)&1) and not ((m>>((i+1)%l))&1)
                      and ((m>>((i+2)%l))&1) for i in range(l))
               for m in range(1<<l))


def predicted_roots(output,n):
    # output is a tuple, -1 for undefined; includes the global empty map.
    if all(y<0 for y in output):
        return 1 + sum(lucas(n//gcd(n,k))**gcd(n,k)-1 for k in range(n))
    starts=[x for x,y in enumerate(output) if y>=0]
    j=(output[starts[0]]-starts[0])%n
    assert all((output[x]-x)%n==j for x in starts)
    count=0
    for k in range(n):
        if 2*k%n!=j: continue
        used=set()
        product=1
        for base in range(n):
            if base in used: continue
            orbit=[]
            v=base
            while v not in used:
                used.add(v)
                orbit.append(v)
                v=(v+k)%n
            product*=word_fiber([int(output[x]>=0) for x in orbit])
        count+=product
    return count


def direct_counts(n):
    sq=Counter()
    for k in range(n):
        for mask in range(1,1<<n):
            f=tuple((i+k)%n if ((mask>>i)&1) else -1 for i in range(n))
            ff=tuple(f[f[i]] if f[i]>=0 else -1 for i in range(n))
            sq[ff]+=1
    sq[(-1,)*n]+=1
    return sq


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def totient(d):
    return sum(gcd(k,d)==1 for k in range(d))


def predicted_image_odd(n):
    # counts cyclic binary words admitting an adjacent-AND precursor
    C={1:2,2:2,3:5}
    for l in range(4,n+1):
        C[l]=2*C[l-1]-C[l-2]+C[l-3]
    return sum(totient(d)*C[d]**(n//d) for d in divisors(n))-n+1


def run():
    tuples=0
    for n in range(1,11):
        actual=direct_counts(n)
        universe=n*(2**n-1)+1
        assert sum(actual.values())==universe
        for output,number in actual.items():
            assert predicted_roots(output,n)==number,(n,output,number)
            tuples+=1
        # Check that no excluded output has positive predicted root count.
        for j in range(n):
            for mask in range(1,1<<n):
                output=tuple((i+j)%n if ((mask>>i)&1) else -1 for i in range(n))
                assert predicted_roots(output,n)==actual.get(output,0)
                tuples+=1
        if n%2:
            assert len(actual)==predicted_image_odd(n),(n,len(actual))
    for l in range(1,17):
        # Independently count the entire local squaring map on binary words.
        fibers=Counter()
        for a in range(1<<l):
            b=tuple(int(bool((a>>i)&1 and (a>>((i+1)%l))&1)) for i in range(l))
            fibers[b]+=1
        assert len(fibers)==cyclic_word_count(l)
        for bits,count in fibers.items():
            assert word_fiber(bits)==count,(l,bits)
    print('CYCLIC_INVERSE_SQUARE_FIBERS_VERIFIED',tuples,'n<=10; local cycle lengths<=16')

if __name__=='__main__': run()
