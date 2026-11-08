#!/usr/bin/env python3
"""Independent occupied-state calculation of final RSA distributions.

States here are occupied independent sets, rather than masks of remaining
candidate vertices. This implementation deliberately does not use the
factorial/available-set recurrence.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

N = 20
FULL = (1 << N) - 1

def adjacency(k):
    adj = [set() for _ in range(N)]
    for i in range(10):
        for a,b in ((i,(i+1)%10),(i,i+10),(i+10,10+((i+k)%10))):
            adj[a].add(b)
            adj[b].add(a)
    return adj

def compute(k):
    adj = adjacency(k)
    @lru_cache(None)
    def rec(chosen):
        blocked = chosen
        for i in range(N):
            if chosen & (1<<i):
                for v in adj[i]: blocked |= (1<<v)
        viable = [i for i in range(N) if not blocked & (1<<i)]
        if not viable: return {chosen.bit_count(): Fraction(1)}
        result={}
        for v in viable:
            child = rec(chosen | (1<<v))
            for size,prob in child.items():
                result[size] = result.get(size,Fraction(0)) + prob/len(viable)
        return result
    d=rec(0)
    return d,rec.cache_info()

def brute_sample(k,subset):
    a=adjacency(k); val=0
    for order in permutations(subset):
        chosen=set()
        for v in order:
            if all(u not in chosen for u in a[v]):chosen.add(v)
        val+=len(chosen)
    return Fraction(val,len(list(permutations(subset))))

def main():
    expect={
       2:{6:Fraction(1,90),7:Fraction(302009,336960),8:Fraction(31207,336960)},
       3:{6:Fraction(1055,6912),7:Fraction(2152,7371),8:Fraction(81557,207360),10:Fraction(37763,232960)}
    }
    for k in (2,3):
        result, info=compute(k)
        assert result==expect[k],(k,result)
        print('GP(10,%d) occupied-state recursion PASS; states=%s'%(k,info.currsize))
    # Independent brute force 5! orders on physically meaningful five-site motifs.
    expected_cases = {
        (0,1,2,3,4): Fraction(37,15),
        (0,1,2,10,11): Fraction(41,15),
        (0,2,4,6,8): Fraction(5),
    }
    for k in (2,3):
        for subset,want in expected_cases.items():
            value=brute_sample(k,subset)
            assert value == want, (k,subset,value,want)
            print('brute-force permutation test',k,subset,value)
    print('PASS independent occupied-state check and direct permutation sampling')

if __name__=='__main__': main()
