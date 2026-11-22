#!/usr/bin/env python3
"""Exhaustive separate ten-vertex Petersen quotient check, including its colouring number."""
from functools import lru_cache
from itertools import combinations
N=10
adj=[0]*N
for i in range(5):
 for a,b in [(i,(i+1)%5),(i,i+5),(5+i,5+(i+2)%5)]:
  adj[a] |= 1<<b; adj[b] |= 1<<a
assert all(m.bit_count()==3 for m in adj)
valid=[]
for mask in range(1,1<<N):
 if all((not(mask>>v&1) or not(mask&adj[v])) and ((mask>>v&1) or (mask&adj[v]).bit_count()!=2) for v in range(N)):
  valid.append(mask)
assert {size:sum(s.bit_count()==size for s in valid) for size in range(1,11)} == {1:10,2:0,3:10,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
triples=[s for s in valid if s.bit_count()==3]
assert sum(not a&b for a,b in combinations(triples,2)) == 15
assert not any(not(a&b or a&c or b&c) for a,b,c in combinations(triples,3))
# Four classes would need three triples and one singleton. Six can use two triples and four singletons.
by=[[s for s in valid if (s>>v)&1] for v in range(N)]
@lru_cache(None)
def covers(uncovered,k):
 if not uncovered:return int(k==0)
 if not k:return 0
 v=(uncovered&-uncovered).bit_length()-1
 return sum(covers(uncovered^s,k-1) for s in by[v] if (s&uncovered)==s)
assert [covers((1<<N)-1,k) for k in range(1,7)] == [0,0,0,0,0,15]
# Every 6-coloring uses exactly two triple classes and four singletons.
print('PETERSEN_ODD_INDEPENDENT_CLASS_HISTOGRAM=10t+10t^3')
print('PETERSEN_FOUR_COLOR_PARTITIONS=0; SIX_COLOR_PARTITIONS=15')
print('VERIFY_PETERSEN_OK')
