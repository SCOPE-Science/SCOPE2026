#!/usr/bin/env python3
"""Exact weighted state enumeration for majority dynamics on pineapple graphs.
All initial clique masks of weight m and all leaf masks of weight ell have
identical class, with multiplicity binom(r,m)*binom(s,ell).
"""
from collections import Counter
from math import comb

def update(state, r, s):
    mask,hub,leaf_count=state
    m=mask.bit_count();nxtmask=0
    for j in range(r):
        bit=(mask>>j)&1
        ones=m-bit+hub
        if 2*ones>r or (2*ones==r and bit):nxtmask|=1<<j
    hubones=m+leaf_count
    hn=int(2*hubones>r+s or (2*hubones==r+s and hub))
    return nxtmask,hn,s if hub else 0

def census(r,s):
    ans=Counter()
    for m in range(r+1):
        mask=(1<<m)-1
        for h in (0,1):
            for ell in range(s+1):
                st=(mask,h,ell)
                seen={st:0};trace=[st]
                for _ in range(7):
                    y=update(trace[-1],r,s)
                    if y in seen:
                        ans[(seen[y],len(trace)-seen[y])]+=comb(r,m)*comb(s,ell)
                        break
                    seen[y]=len(trace);trace.append(y)
                else:raise AssertionError((r,s,m,h,ell,'not period<=2 by time 3'))
    return ans

def expected_general(r,s):
    C=comb(r,(r-1)//2) if r%2 else 0
    fixed=2+(2 if s>=r else 0)
    twocycles=C+(2 if s>r else 0)
    if s>r:
        a=sum(comb(s,i) for i in range((s-1)//2+1))
        tie=comb(r+s,(r+s)//2) if (r+s)%2==0 else 0
        b2=(1<<(r+s))-tie
        b1=(1<<(r+s))+tie
        t2=2*C*a
        return {(0,1):4,(0,2):4+2*C,(1,1):b1-4-t2,
                (1,2):b2-4-2*C,(2,1):t2}
    return {(0,1):fixed,(0,2):2*twocycles}

cases=0
weighted_total=0
for r in range(2,51):
    for s in sorted({1,2,max(1,r-1),r,r+1,r+2,r+5,2*r+1,3*r+2}):
        counts=census(r,s);exp=expected_general(r,s)
        assert all(counts[k]==v for k,v in exp.items()),(r,s,counts,exp)
        assert sum(counts.values())==1<<(r+s+1),(r,s,'sum')
        assert set(k[1] for k in counts)=={1,2} or not any(k[1]>2 for k in counts)
        maxt=max(k[0] for k in counts)
        assert maxt <= (2 if s>r else 3),(r,s,counts)
        if s>r:assert maxt==(2 if r%2 else 1),(r,s,counts)
        elif (r%2==0 or s>=2):assert maxt==3,(r,s,counts)
        else:assert maxt==2,(r,s,counts)
        cases+=1;weighted_total+=1<<(r+s+1)
print('PASS: exact weighted enumeration of',cases,'parameter pairs (2<=r<=50) on both sides of the leaf threshold.')
print('State weights total:',weighted_total)
for r,s in [(3,2),(3,3),(3,4),(4,4),(4,5),(5,5),(5,6)]:
 print(f' r={r},s={s}:',dict(sorted(census(r,s).items())))
