#!/usr/bin/env python3
"""Direct vertex-neighbor evolution, independent of the matrix checker.
Run: python3 check_states.py; relies on standard library only.
"""
from collections import Counter
from random import Random

def update(u,v,n):
    w = 0
    for i in range(n):
        for layer in range(2):
            ix=2*i+layer
            bit=(u >> (2*i+1-layer))&1
            if i: bit ^= (u >> (2*(i-1)+layer))&1
            if i<n-1: bit ^= (u >> (2*(i+1)+layer))&1
            bit ^= (v >> ix)&1
            w |= bit<<ix
    return w,u

def period(u,v,n,maximum):
    orig=(u,v)
    for t in range(1,maximum+1):
        u,v=update(u,v,n)
        if (u,v)==orig: return t
    raise AssertionError(('not periodic',n,orig))

def pred_count(n,p):
    if p==1: return 1
    if p%3: return 0
    j=(p//3).bit_length()-1
    if p!=3*2**j: return 0
    def fixed(k):
        s=2**k
        return 2**(2*(min(n+1,s)+min(n-1,s)))
    return fixed(j)-(fixed(j-1) if j>0 else 1)

def main():
    n=3; half=1<<(2*n)
    got=Counter()
    for u in range(half):
        for v in range(half):
            got[period(u,v,n,12)]+=1
    expected={p:pred_count(n,p) for p in (1,3,6,12)}
    assert dict(got)==expected,(got,expected)
    print('n=3 enumerated_states=',half*half,'least_period_state_counts=',dict(sorted(got.items())))
    for n,samples in [(7,1500),(15,600)]:
        rng=Random(730001+n)
        maximum=3*(n+1)
        seen=Counter()
        for i in range(samples):
            u=rng.getrandbits(2*n); v=rng.getrandbits(2*n)
            t=period(u,v,n,maximum)
            assert t==1 or (t%3==0 and (t//3)&((t//3)-1)==0)
            seen[t]+=1
        assert maximum in seen
        print(f'n={n} independent_sample={samples} observed_least_periods={dict(sorted(seen.items()))}')
    print('CHECK_STATES_PASS')
if __name__=='__main__':main()
