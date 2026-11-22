#!/usr/bin/env python3
"""Independent direct-neighbor simulation of face-feedback cube dynamics.
Run: python verify_direct.py
"""
from collections import Counter

def update(state, d, q):
    """Each entry is a q=2^s field element; all coefficients 0/1, so XOR suffices."""
    N = 1 << d
    out = [0]*N
    for v in range(N):
        z = state[v] if (v&1)==0 else 0
        for i in range(d):
            z ^= state[v^(1<<i)]
        out[v] = z
    return tuple(out)

def census(d, q):
    N=1<<d
    num=q**N
    counts=Counter()
    for encoded in range(num):
        a=encoded; state=[]
        for _ in range(N):
            state.append(a%q); a//=q
        s=tuple(state)
        seq=[s]
        for i in range(6):seq.append(update(seq[-1],d,q))
        assert seq[6]==s, (d,q,encoded)
        period=next(t for t in (1,2,3,6) if seq[t]==s)
        counts[period]+=1
    expected={1:1,3:q**(2**(d-1))-1,6:q**(2**d)-q**(2**(d-1))} if d>=2 else {1:1,3:q*q-1}
    assert dict(counts)==expected,(d,q,counts,expected)
    print(f'd={d} q={q} states={num} fixed={counts[1]} p3={counts[3]} p6={counts[6]}: OK')

if __name__=='__main__':
    for d,q in [(1,2),(2,2),(3,2),(4,2),(1,4),(2,4),(3,4)]:census(d,q)
    print('DIRECT_FACET_CENSUS_OK')
