#!/usr/bin/env python3
"""Independent column-mask DP cross-check using direct constraints, without potentials or characteristic polynomials."""
from itertools import product
COL=[(a,b) for a in range(3) for b in range(3)]
valid_col=lambda c: not(c[0]==c[1]!=0)
valid_adj=lambda a,b: all(a[r]!=b[r] or a[r]==0 for r in (0,1))

def valid_mid(a,b,c):
    if not valid_col(b) or not valid_adj(a,b) or not valid_adj(b,c): return False
    return all(b[r]!=0 or (1 in (a[r],b[1-r],c[r]) and 2 in (a[r],b[1-r],c[r])) for r in (0,1))

# Direct enumeration over valid column pairs and path completions, not the 35-state matrix.
for n in range(3,12):
    counts={}
    for first in COL:
        if not valid_col(first):continue
        for second in COL:
            if not valid_col(second) or not valid_adj(first,second):continue
            cur={(first,second,int(first[0]!=0)+int(first[1]!=0)+int(second[0]!=0)+int(second[1]!=0)):1}
            for pos in range(2,n):
                nxt={}
                for (prev,last,w),v in cur.items():
                    for c in COL:
                        if not valid_col(c) or not valid_mid(prev,last,c):continue
                        key=(last,c,w+int(c[0]!=0)+int(c[1]!=0))
                        nxt[key]=nxt.get(key,0)+v
                cur=nxt
            for (prev,last,w),v in cur.items():
                if not valid_mid(prev,last,first) or not valid_mid(last,first,second):continue
                counts[w]=counts.get(w,0)+v
    best=min(counts)
    val=counts[best]
    print('n=',n,'minimum=',best,'optimal=',val,'total=',sum(counts.values()))
    expected=[0,0,0,18,24,40,76,112,232,504,1084,2112]
    assert (best,val)==((4 if n==3 else n),expected[n])
print('COLUMN_RECURSION_VERIFIED_N_3_TO_11')
