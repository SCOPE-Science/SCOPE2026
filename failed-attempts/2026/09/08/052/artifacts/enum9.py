"""Exhaustive enumeration of 9-caps containing {0,1} in AG(3,4) with completeness test."""
import sys; sys.path.insert(0,'output/artifacts')
from caps3034 import PTS,LINES,PAIR2LINE,PT2LINES,coords,pt,is_cap,uncovered
import time
FIX=(0,1)
# candidate points: exclude third points on line(0,1)
L01=set(LINES[PAIR2LINE[(0,1)]])
CAND=[p for p in PTS if p not in L01 and p>1]
THIRD={}  # (a,b) sorted pair -> set of other 2 pts on line
for i,L in enumerate(LINES):
    L=list(L)
    for x in range(4):
        for y in range(x+1,4):
            a,b=L[x],L[y]
            key=(a,b) if a<b else (b,a)
            THIRD[key]=set(L)-{a,b}
from functools import lru_cache
count=[0]; complete_ex=[]
t0=time.time(); nodes=[0]
def backtrack(S,forb,start):
    if len(S)==9:
        count[0]+=1
        if not uncovered(S):
            complete_ex.append(tuple(sorted(S)))
        return True  # keep going (no time cap in pilot? use cap)
    # prune: need 9-len from available
    return False
# pilot with node budget: iterative DFS
import collections
budget=2000000
stack=[(set(FIX),set(L01)-set(FIX),2)]
n9=0; ncomp=0; first=None; exhausted=False
while stack:
    S,forb,idx=stack.pop()
    nodes[0]+=1
    if nodes[0]>budget: break
    if len(S)==9:
        n9+=1
        if not uncovered(S):
            ncomp+=1
            if first is None: first=tuple(sorted(S))
        continue
    # find next candidate >= idx not forbidden
    for i in range(idx,len(CAND)):
        p=CAND[i]
        if p in forb or p in S: continue
        # add p
        newforb=set(forb)
        ok=True
        for q in S:
            key=(p,q) if p<q else (q,p)
            newforb|=THIRD[key]
        newforb.discard(p)
        if len(S)+1+(len(CAND)-i-1)>=9:  # crude
            stack.append((S|{p},newforb,i+1))
else:
    exhausted=True
print(f"nodes={nodes[0]} n9={n9} ncomp={ncomp} first={first} exhausted={exhausted} time={time.time()-t0:.1f}s")
