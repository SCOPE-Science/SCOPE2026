#!/usr/bin/env python3
"""Independent geometry/maximum induced-tree verification on a binary symplectic quadrangle."""
from collections import Counter
from itertools import combinations

def omega(x,y):
    return ((x&1!=0)*(y&4!=0) + (x&4!=0)*(y&1!=0) + (x&2!=0)*(y&8!=0) + (x&8!=0)*(y&2!=0))%2
P=list(range(1,16))
L=sorted({tuple(sorted((x,y,x^y))) for x in P for y in P if x<y and omega(x,y)==0})
assert len(L)==15
adj=[0]*30
for j,line in enumerate(L):
    for x in line:
        a=x-1; b=15+j
        adj[a]|=1<<b; adj[b]|=1<<a
assert all(x.bit_count()==3 for x in adj)
full=(1<<30)-1

def connected_left(left):
    seen=0
    front=left&-left
    while front:
        seen|=front
        near=0
        active=front
        while active:
            bit=active&-active
            near|=adj[bit.bit_length()-1]
            active-=bit
        front=near&left&~seen
    return seen==left

def synchronous_rounds(seeds):
    cur=seeds; r=0
    while cur!=full:
        other=full^cur; new=0
        while other:
            bit=other&-other
            v=bit.bit_length()-1
            if (adj[v]&cur).bit_count()>=2: new|=bit
            other-=bit
        if not new:return None
        cur|=new;r+=1
    return r

counts=Counter(); times=Counter(); indep_count=0; optima=[]

def search(chosen, allowed, length):
    global indep_count
    if length==8:
        indep_count+=1
        if connected_left(full^chosen):
            optima.append(chosen)
            counts[(chosen & ((1<<15)-1)).bit_count()]+=1
            rr=synchronous_rounds(chosen)
            assert rr is not None
            times[rr]+=1
        return
    while allowed and allowed.bit_count()>=8-length:
        bit=allowed&-allowed
        allowed-=bit
        v=bit.bit_length()-1
        search(chosen|bit, allowed & ~adj[v], length+1)
search(0,full,0)
assert indep_count==111225,indep_count
assert [counts[i] for i in range(9)]==[225,720,1860,2280,2610,2280,1860,720,225],counts
assert dict(times)=={4:120,5:660,6:3360,7:4320,8:1440,9:2880},times
print('SYMPLECTIC_VERIFY_OK', 'independent_sets_8=',indep_count,'maximum_induced_trees=',sum(counts.values()), 'shore_profile=',dict(sorted(counts.items())),'completion_rounds=',dict(sorted(times.items())))

# Independent reconfiguration census in the symplectic model.
optset=set(optima)
assert len(optset)==12780
allseen=set(); comps=[]; degrees=Counter(); total_neighbors=0
def adj_opt(s):
    out=[]; x=s
    while x:
        a=x&-x; x-=a; z=full^s
        while z:
            b=z&-z; z-=b
            t=s^a^b
            if t in optset: out.append(t)
    return out
for s in optima:
    ns=adj_opt(s)
    degrees[len(ns)]+=1;total_neighbors+=len(ns)
for s in optima:
    if s in allseen:continue
    comp={s};allseen.add(s); stack=[s]
    while stack:
        z=stack.pop()
        for t in adj_opt(z):
            if t not in allseen:
                allseen.add(t);comp.add(t);stack.append(t)
    comps.append(comp)
assert degrees==Counter({8:12780}), degrees
assert total_neighbors==102240, total_neighbors
assert Counter(map(len,comps))==Counter({9:70,12150:1})
# A 9-vertex 8-regular simple component must be K_9.
shapes=Counter(tuple(Counter((x&32767).bit_count() for x in c)[j] for j in range(9)) for c in comps if len(c)==9)
assert shapes==Counter({(9,0,0,0,0,0,0,0,0):15,(0,0,0,0,0,0,0,0,9):15,(0,0,3,6,0,0,0,0,0):20,(0,0,0,0,0,6,3,0,0):20}),shapes
print('SYMPLECTIC_EXCHANGE_OK','vertices=',len(optima),'edges=',total_neighbors//2,'components=',Counter(map(len,comps)),'small_component_shore_profiles=',shapes)
