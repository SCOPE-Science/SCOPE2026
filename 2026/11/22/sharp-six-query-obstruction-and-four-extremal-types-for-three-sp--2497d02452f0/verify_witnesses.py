#!/usr/bin/env python3
"""Check all explicitly claimed three-sparse parity traces by direct XOR."""
from itertools import combinations
P={
  (3,6): [0,0,0,1,2,4],
  (4,7): [0,0,12,1,2,4,8],
  (5,8): [0,24,7,1,2,4,8,16],
  (6,9): [0,0,63,1,2,4,8,16,32],
  (6,10):[0,0,0,63,1,2,4,8,16,32],
}
for (m,n), a in P.items():
 assert len(a)==n and all(0<=v<2**m for v in a)
 traces={a[i]^a[j]^a[k] for i,j,k in combinations(range(n),3)}
 expected=(1<<m) - (m==6 and n==9)
 assert len(traces)==expected, (m,n,len(traces))
 if (m,n)==(6,9):assert traces==set(range(1,64))
 print(f'd={m} n={n} distinct_traces={len(traces)} full={len(traces)==1<<m}')
