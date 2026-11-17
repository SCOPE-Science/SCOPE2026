#!/usr/bin/env python3
"""Finite-state proof and independent checks for upper domination in ladder graphs."""
from collections import deque
from itertools import product
V=tuple(((k&1),((k>>1)&1)) for k in range(4))+((0,0),)
SENTINEL=4
NSTATE=5**4

def admissible(a,b,c,d,e):
    # The two selected vertices in the real central column must be irredundant,
    # and every unselected vertex there must be dominated.
    if c==SENTINEL: return True
    for r in (0,1):
        selected=V[c][r]
        own=V[c][r]+V[c][1-r]+V[b][r]+V[d][r]
        if not selected:
            if own==0:return False
            continue
        priv=(own==1 or
              V[c][1-r]+V[c][r]+V[b][1-r]+V[d][1-r]==1 or
              (b!=SENTINEL and V[a][r]+V[b][r]+V[b][1-r]+V[c][r]==1) or
              (d!=SENTINEL and V[c][r]+V[d][r]+V[d][1-r]+V[e][r]==1))
        if not priv:return False
    return True

def encode(q):
    s=0
    for a in q:s=5*s+a
    return s

def unpack(s):
    return (s//125,(s//25)%5,(s//5)%5,s%5)

TRANS=[]
for s in range(NSTATE):
    a,b,c,d=unpack(s)
    TRANS.append(tuple((s*5+k)%NSTATE if admissible(a,b,c,d,k) else -1 for k in range(5)))

def score_step(D):
    E={}
    for s,v in D.items():
        for k in range(4):
            t=TRANS[s][k]
            if t<0:continue
            w=v+sum(V[k])-1
            if t not in E or w>E[t]: E[t]=w
    return E

def initial():
    return {encode((4,4,a,b)):sum(V[a])+sum(V[b])-2 for a in range(4) for b in range(4)}

scores={2:initial()}
for n in range(3,11):scores[n]=score_step(scores[n-1])
assert scores[7]==scores[9] and scores[8]==scores[10], 'No two-period max-plus identity'
print('TROPICAL_PERIOD_2_CERTIFICATE_OK states',len(scores[7]),len(scores[8]))

def tail_valid(s):
    s=TRANS[s][4]
    return s>=0 and TRANS[s][4]>=0

patterns=((1,),(2,),(1,2),(2,1),(0,3,3,0),(3,0,0,3))
def char(p,j):return p[(j-1)%len(p)]
def mask_prefix(w):
    return sum(1<<q for q,p in enumerate(patterns) if all(char(p,j)==k for j,k in enumerate(w,1)))
def mask_extend(mask,k,pos):
    return sum((1<<j) for j,p in enumerate(patterns) if mask & (1<<j) and char(p,pos)==k)

def terminal_good(s,nmod4,m):
    if not tail_valid(s):return True
    delta=scores[7 if nmod4%2 else 8][s]
    assert delta<=0, ('false upper domination',s,nmod4,delta)
    if delta<0:return True
    return bool(m & (15 if nmod4%2 else 63))

initial_nodes=set()
for w in product(range(4),repeat=7):
    s=encode((4,4,w[0],w[1]));v=sum(sum(V[k])-1 for k in w[:2]);good=True
    for k in w[2:]:
        s=TRANS[s][k]
        if s<0:good=False;break
        v+=sum(V[k])-1
    if good and v==scores[7][s]:
        initial_nodes.add((s,7%4,mask_prefix(w)))
print('OPTIMAL_LENGTH_7_PREFIX_NODES_OK',len(initial_nodes))
queue=deque(initial_nodes); visited=set(initial_nodes);edges=0
while queue:
    s,res,m=queue.popleft()
    assert terminal_good(s,res,m),('COUNTEREXAMPLE_STATE',s,res,m)
    nxt=(res+1)%4
    a=scores[7 if res%2 else 8][s]
    for k in range(4):
        t=TRANS[s][k]
        if t<0:continue
        f=scores[7 if nxt%2 else 8].get(t)
        if f is None or a+sum(V[k])-1!=f:continue
        node=(t,nxt,mask_extend(m,k,res+1))
        edges+=1
        if node not in visited:visited.add(node);queue.append(node)
print('INFINITE_OPTIMAL_LANGUAGE_INCLUSION_OK',len(visited),'states',edges,'edges')

def direct(n):
    # Independent of transfer automaton: calculate every closed neighborhood.
    cl=[]
    for i in range(n):
        for r in range(2):
            u=2*i+r; neigh={u,u^1}
            if i:neigh.add(u-2)
            if i+1<n:neigh.add(u+2)
            cl.append(sum(1<<j for j in neigh))
    good=[]
    for d in range(1<<(2*n)):
        if d.bit_count()!=n:continue
        if any(d & c==0 for c in cl):continue
        if any(not any((d & cl[v]) == (1<<u) for v in range(2*n)) for u in range(2*n) if (d>>u)&1):continue
        good.append(tuple((d>>(2*i))&3 for i in range(n)))
    template={tuple(char(p,j) for j in range(1,n+1)) for idx,p in enumerate(patterns) if idx<4 or n%2==0}
    assert set(good)==template,(n,good,template)
    print('DIRECT_ALL_SIZE_N_OK',n,len(good))
for n in range(2,11):direct(n)
# Proof that each listed periodic pattern is valid at every length:
# all interior five-column windows are periodic (period <=4), while boundary
# windows depend only on the first/last four symbols. Exhaust a complete
# residue period for the open endpoints and all five-column windows.
for j,p in enumerate(patterns):
    for n in range(2,25):
        if j>=4 and n%2:continue
        w=[4,4]+[char(p,i) for i in range(1,n+1)]+[4,4]
        assert all(admissible(*w[i:i+5]) for i in range(n)),(j,n)
print('TEMPLATE_LOCAL_PERIOD_BOUNDARIES_OK')
print('VERIFY_OK')
