#!/usr/bin/env python3
"""Finite independent checks for one-point-extension rank on colored finite chains."""
from functools import lru_cache
from itertools import product, permutations
import random

@lru_cache(None)
def interval_rank(word, q):
    if not word or any(c not in word for c in range(q)):
        return 0
    return 1 + min(max(min(interval_rank(word[:i], q), interval_rank(word[i+1:], q)) for i,v in enumerate(word) if v==c) for c in range(q))

# Independent realization-game recursion: states are subsets of selected host indices,
# and universally quantified extension types are each marked gap and new point color.
def rank_by_game(word, q):
    n=len(word)
    @lru_cache(None)
    def r(mask):
        sel=[i for i in range(n) if mask>>i&1]
        boundaries=[-1]+sel+[n]
        best=10**9
        for a,b in zip(boundaries,boundaries[1:]):
            for c in range(q):
                choices=[i for i in range(a+1,b) if word[i]==c]
                if not choices:return 0
                best=min(best, max(r(mask | (1<<i)) for i in choices))
        return 1+best
    # Verify every marked-state rank against gap ranks, not only the root.
    for mask in range(1<<n):
        sel=[i for i in range(n) if mask>>i&1]
        bounds=[-1]+sel+[n]
        gaps=[tuple(word[a+1:b]) for a,b in zip(bounds,bounds[1:])]
        predicted=min(interval_rank(g,q) for g in gaps)
        actual=r(mask)
        assert actual==predicted, (word,q,mask,actual,predicted)
    return r(0)

def canonical_words(q,t):
    ans={()}
    for _ in range(t):
        ans={u+per+v for u in ans for v in ans for per in permutations(range(q))}
    return ans

def is_subsequence(pattern, word):
    it=iter(word)
    return all(any(z==y for z in it) for y in pattern)

def test_embedding():
    trials=0
    for q,t,max_n in [(2,1,8),(2,2,10),(2,3,14),(3,1,7),(3,2,9)]:
        patterns=canonical_words(q,t)
        for n in range(max_n+1):
            for w in product(range(q),repeat=n):
                have=any(is_subsequence(p,w) for p in patterns)
                assert (interval_rank(w,q)>=t)==have,(q,t,w)
                trials+=1
    rng=random.Random(1203)
    patterns=canonical_words(2,3)
    for n in (15,18,23):
        for _ in range(300):
            w=tuple(rng.randrange(2) for _ in range(n))
            have=any(is_subsequence(p,w) for p in patterns)
            assert (interval_rank(w,2)>=3)==have
            trials+=1
    print('EMBEDDING_CRITERION',trials)

def main():
    checked=0
    for q,max_n in [(1,10),(2,9),(3,6)]:
        for n in range(max_n+1):
            for w in product(range(q), repeat=n):
                a=interval_rank(w,q)
                b=rank_by_game(w,q)
                assert a==b,(q,w,a,b)
                checked+=1
    print('RECURSION_GAME',checked)
    for q,t in [(1,1),(1,4),(2,1),(2,2),(2,3),(3,1),(3,2)]:
        length=q*((1<<t)-1)
        correct=canonical_words(q,t)
        assert len(correct)==(mathfactorial(q))**((1<<t)-1)
        assert all(interval_rank(w,q)>=t for w in correct)
        if length<=14 and q<=3:
            fromiter=set(w for w in product(range(q),repeat=length) if interval_rank(w,q)>=t)
            assert fromiter==correct,(q,t,len(fromiter),len(correct),list(fromiter.symmetric_difference(correct))[:2])
        print('EXTREMA',q,t,length,len(correct))
    rng=random.Random(390477)
    for q,t in [(2,4),(3,3),(4,3)]:
        for j in range(60):
            def build(z):
                if z==0:return ()
                p=list(range(q));rng.shuffle(p)
                return build(z-1)+tuple(p)+build(z-1)
            w=build(t)
            assert len(w)==q*((1<<t)-1)
            assert interval_rank(w,q)==t,(q,t,w)
        print('RANDOM_EXTREMA',q,t,60)
    test_embedding()
    print('ALL_CHECKS_OK')

def mathfactorial(n):
    out=1
    for i in range(2,n+1):out*=i
    return out

if __name__=='__main__': main()
