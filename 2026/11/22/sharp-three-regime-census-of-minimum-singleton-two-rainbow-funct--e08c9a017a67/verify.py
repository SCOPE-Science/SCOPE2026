#!/usr/bin/env python3
"""Independent finite-state enumeration of optimal singleton 2-rainbow labelings of wheel graphs."""
from collections import defaultdict
from itertools import product

def transfer(n,h):
    # cyclic rim words; keep first two symbols to close the cycle.
    out=defaultdict(int)
    for a,b in product(range(3),repeat=2):
        states={(a,b,int(a>0)+int(b>0), int(a==1)+int(b==1), int(a==2)+int(b==2)):1}
        for i in range(2,n):
            nxt=defaultdict(int)
            for (prev,curr,k,c1,c2),num in states.items():
                for v in range(3):
                    if curr==0 and not ({1,2} <= {h,prev,v}):
                        continue
                    nxt[(curr,v,k+int(v>0),c1+int(v==1),c2+int(v==2))]+=num
            states=nxt
        for (prev,curr,k,c1,c2),num in states.items():
            if curr==0 and not ({1,2} <= {h,prev,a}):continue
            if a==0 and not ({1,2} <= {h,curr,b}):continue
            if h==0 and not (c1 and c2):continue
            out[k+int(h>0)] +=num
    return min(out),out

def expected(n):
    if n<9:return {3:(2,12),4:(2,4),5:(3,20),6:(3,6),7:(4,56),8:(4,20)}[n]
    q,r=divmod(n,3)
    val={0:6,1:n*(q+4),2:2*n}[r]
    return (1+(n+2)//3,val)

for n in range(3,51):
    data=[transfer(n,h) for h in range(3)]
    m=min(x[0] for x in data)
    s=sum(x[1][m] for x in data)
    assert (m,s)==expected(n),(n,m,s,expected(n))
    if n in (3,4,5,6,7,8,9,10,11,12,13,14,15,19,20,21,50):
        print('n',n,'minimum',m,'count',s,'hub0',data[0][1].get(m,0),'hubcolor',data[1][1].get(m,0),flush=True)
print('FINITE_STATE_CHECK_3_TO_50_PASS')

def direct(n):
    counts=defaultdict(int)
    for vals in product(range(3),repeat=n+1):
        h=vals[0]; rim=vals[1:]
        if h==0 and (1 not in rim or 2 not in rim):continue
        if any(rim[i]==0 and not({1,2}<={h,rim[(i-1)%n],rim[(i+1)%n]}) for i in range(n)):continue
        counts[sum(v!=0 for v in vals)]+=1
    return min(counts),counts[min(counts)]
for n in range(3,11):
    assert direct(n)==expected(n),(n,direct(n),expected(n))
print('INDEPENDENT_DIRECT_LABELING_CENSUS_3_TO_10_PASS')
