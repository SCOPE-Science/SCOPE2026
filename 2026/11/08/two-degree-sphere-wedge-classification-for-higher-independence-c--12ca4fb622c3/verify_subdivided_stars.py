#!/usr/bin/env python3
"""Direct finite checks for higher independence complexes of subdivided double stars."""
from itertools import combinations
from math import comb

def graph(a,b):
    # 0=left hub, 1=middle, 2=right hub; leaves 3..3+a+b-1.
    N=3+a+b; nbr=[0]*N
    def edge(x,y):nbr[x]|=1<<y; nbr[y]|=1<<x
    edge(0,1);edge(1,2)
    for x in range(3,3+a):edge(0,x)
    for x in range(3+a,N):edge(2,x)
    return tuple(nbr)

def is_face(S,nbr,r):
    unvisited=S
    while unvisited:
        v=(unvisited&-unvisited).bit_length()-1
        stack=1<<v; component=0
        while stack:
            q=stack&-stack;stack-=q; component|=q
            k=q.bit_length()-1
            stack|=(nbr[k]&S&~component&~stack)
        if component.bit_count()>r:return False
        unvisited &= ~component
    return True

def mod2_betti(nbr,r):
    N=len(nbr);masks_by_card=[[] for _ in range(N+1)]
    for S in range(1,1<<N):
        if is_face(S,nbr,r):masks_by_card[S.bit_count()].append(S)
    ranks={};prev=0;betti={}
    # boundary from cardinality c faces to cardinality c-1, first c=1 is augmented differential to the empty simplex.
    for c in range(1,N+1):
        cols=masks_by_card[c]
        if c==1:
            rank=1 if cols else 0
        else:
            row_index={S:i for i,S in enumerate(masks_by_card[c-1])}
            pivots={};rank=0
            for s in cols:
                col=0;parts=s
                while parts:
                    v=parts&-parts;parts-=v
                    col ^= 1<<row_index[s^v]
                while col:
                    i=col.bit_length()-1
                    if i in pivots: col^=pivots[i]
                    else: pivots[i]=col;rank+=1;break
        ranks[c]=rank
    for c in range(1,N+1):
        bet=len(masks_by_card[c])-ranks[c]-ranks.get(c+1,0)
        if bet:betti[c-1]=bet
    return betti,tuple(len(x) for x in masks_by_card[1:])

def expected(a,b,r):
    t=a+b
    if r==1:return {1:1}
    if r>=t+3:return {}
    out={}
    low=comb(t-1,r-3) if 3<=r<=t+2 else 0
    high=(comb(a-1,r-1)*comb(b-1,r-1)) if r<=min(a,b) else 0
    if low:out[r-1]=low
    if high:out[2*r-1]=high
    return out

def check():
    total=0;face_count=0;expanded=[]
    for a in range(1,5):
     for b in range(1,5):
      if a+b>7:continue
      nbr=graph(a,b)
      for r in range(1,a+b+4):
       got,nums=mod2_betti(nbr,r);want=expected(a,b,r)
       if got!=want:raise AssertionError((a,b,r,got,want,nums))
       total+=1;face_count+=sum(nums)
       expanded.append((a,b,r,got))
    print(f'ALL_VERIFY_OK cases={total} total_face_instances={face_count}')
    return expanded
if __name__=='__main__':check()
