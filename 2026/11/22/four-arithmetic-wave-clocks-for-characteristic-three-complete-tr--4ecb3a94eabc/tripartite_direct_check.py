#!/usr/bin/env python3
"""Exhaustive coordinate-level ternary wave orbit enumerator for small tripartite graphs."""
from collections import Counter

def next_state(state, parts):
    N=sum(parts);s=0;shore=[]
    for n in parts:shore.append(sum(state[s:s+n])%3);s+=n
    out=[];s=0
    for h,n in enumerate(parts):
        t=(sum(shore)-shore[h])%3
        out.extend((t-state[N+j])%3 for j in range(s,s+n));s+=n
    return tuple(out+list(state[:N]))

def decode(i,d):
    a=[]
    for _ in range(d):a.append(i%3);i//=3
    return tuple(a)

def encode(a):
    z=0;p=1
    for x in a:z+=x*p;p*=3
    return z

def orbit_populations(parts):
    d=2*sum(parts);total=3**d;seen=bytearray(total);cnt=Counter()
    for v in range(total):
        if seen[v]:continue
        start=decode(v,d);x=start;orbit=[]
        while True:
            w=encode(x)
            assert not seen[w],('Premature revisit',parts,v)
            seen[w]=1;orbit.append(w)
            x=next_state(x,parts)
            if x==start:break
        cnt[len(orbit)]+=1
    assert all(seen)
    return dict(sorted(cnt.items()))

def main():
    # Independently computed from the explicit fixed-space formula in the theorem;
    # these numbers are asserted against direct state-iteration counts.
    expected={
        (1,1,1):{1:9,3:78,9:54},
        (1,1,2):{1:3,3:2,4:6,10:24,12:4,20:96,30:16,60:64},
        (1,2,2):{1:1,2:1,4:60,5:16,6:1,10:16,12:40,20:960,30:16,60:640},
        (2,2,2):{1:1,2:4,4:1638,6:39,12:14196,18:27,36:9828}
    }
    for part in [(1,1,1),(1,1,2),(1,2,2),(2,2,2)]:
        result=orbit_populations(part)
        assert sum(k*v for k,v in result.items())==3**(2*sum(part))
        print('parts',part,'orbits',result,'states',3**(2*sum(part)))
        if part in expected:assert result==expected[part]
if __name__=='__main__':main()
