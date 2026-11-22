#!/usr/bin/env python3
"""Exhaustive finite verification for four consecutive cubic-coset words.
Only Python's standard library is required. No external data, networking or packages.
"""
import math

LIMIT = 19000  # Weil proves all patterns above this (even for prime powers under suitable conditions).

def primes_under(n):
    sieve = bytearray(b'\x01') * n
    sieve[:2] = b'\x00\x00'
    for r in range(2,math.isqrt(n-1)+1):
        if sieve[r]:
            sieve[r*r::r] = b'\x00' * ((n-1-r*r)//r+1)
    return [p for p in range(7,n) if sieve[p] and p%3==1]

def distinct_prime_factors(n):
    ans=[];d=2
    while d*d<=n:
        if n%d==0:
            ans.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:ans.append(n)
    return ans

def smallest_primitive_root(p):
    q=distinct_prime_factors(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//r,p)!=1 for r in q):return g
    raise AssertionError('no root')

def labeling_by_generator(p):
    g=smallest_primitive_root(p)
    colors=[-1]*p
    z=1
    for j in range(p-1):
        assert colors[z]==-1
        colors[z]=j%3
        z=z*g%p
    assert z==1 and colors[0]==-1
    return colors,g

def word_mask(colors,p):
    # No wrap into a 0: admissible n are 1,...,p-4.
    mask=0
    for x in range(1,p-3):
        w=colors[x]*27+colors[x+1]*9+colors[x+2]*3+colors[x+3]
        assert 0<=w<81
        mask|=1<<w
    return mask

def independent_labeling(p,g):
    # Cubic character defined directly by Euler exponent; never uses a discrete log.
    z=pow(g,(p-1)//3,p)
    idx={1:0,z:1,z*z%p:2}
    assert len(idx)==3
    return [-1]+[idx[pow(x,(p-1)//3,p)] for x in range(1,p)]

def decode(w):
    return ((w//27)%3,(w//9)%3,(w//3)%3,w%3)

def main():
    primes=primes_under(LIMIT)
    exceptional=[];full=0;randomish=0;pure_missing=[]
    for p in primes:
        colors,g=labeling_by_generator(p)
        mask=word_mask(colors,p)
        k=mask.bit_count()
        if not (mask & 1):pure_missing.append(p)
        if k<81:exceptional.append((p,81-k))
        else:full+=1
        # Independent character-algorithm comparison on EVERY tested prime.
        direct=independent_labeling(p,g)
        assert colors==direct, ('character labeling discrepancy',p)
        mask2=word_mask(direct,p)
        assert mask==mask2, ('word spectrum disagreement',p)
        randomish+=1
    exps=[p for p,_ in exceptional]
    print('cubic_coset_primes_under_19000',len(primes))
    print('complete',full,'incomplete',len(exceptional))
    print('exceptional_primes',exps)
    print('missing_word_counts',exceptional)
    assert exceptional and exps[-1]==547
    expected=[7,13,19,31,37,43,61,67,73,79,97,103,109,127,139,151,157,163,181,193,199,211,223,229,271,277,283,307,313,331,337,367,373,379,397,457,487,499,547]
    assert exps==expected, ('incorrect complete exceptional list',exps)
    assert pure_missing and pure_missing[-1]==379
    print('last_all_cubic_failure',pure_missing[-1])
    assert len(exceptional)==39
    assert all(p<571 for p in exps)
    for p in (547,571,283,307,379,487,499):
        # A third check constructs the three cubic cosets as explicit sets.
        cc,g=labeling_by_generator(p)
        cubes={pow(t,3,p) for t in range(1,p)}
        cosets=(cubes,{(g*t)%p for t in cubes},{(g*g*t)%p for t in cubes})
        assert all(sum(x in cos for cos in cosets)==1 for x in range(1,p))
        for x in range(1,p):
            assert x in cosets[cc[x]], ('cube-set mismatch',p,x)
        colors,g=labeling_by_generator(p)
        missing=[decode(w) for w in range(81) if not (word_mask(colors,p)>>w)&1]
        print('boundary',p,'generator',g,'missing',missing)
    assert [decode(w) for w in range(81) if not (word_mask(labeling_by_generator(547)[0],547)>>w)&1]==[(0,2,2,0)]
    # The analytic proof's lower bound is positive for every p >= 19000.
    assert 19000-136*math.sqrt(19000)-108>0
    print('analytic_bound_at_19000',19000-136*math.sqrt(19000)-108)
    print('All finite checks PASS')

if __name__=='__main__':main()
