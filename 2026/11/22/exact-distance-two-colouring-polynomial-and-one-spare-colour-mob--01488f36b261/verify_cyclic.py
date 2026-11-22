#!/usr/bin/env python3
"""Exact finite checks for the square of the Fano incidence graph.

Vertices are the seven cyclic points and seven cyclic lines
L_j={j,j+1,j+3} modulo seven. The degree-two conflict relation is
clique on each shore, plus incidence across shores.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations
from math import factorial

V=range(7)
lines=[frozenset({j,(j+1)%7,(j+3)%7}) for j in V]
assert all(len(L)==3 for L in lines)
assert all(sum(x in L for L in lines)==3 for x in V)
assert all(sum({x,y}<=L for L in lines)==1 for x in V for y in V if x<y)

# Matchings by recursively processing each line, recording used points.
dp={0:1}
for j in V:
    next_dp=defaultdict(int)
    for used,cnt in dp.items():
        next_dp[used]+=cnt
        for point in V:
            if point not in lines[j] and not ((used>>point)&1):
                next_dp[used|(1<<point)]+=cnt
    dp=next_dp
r=[sum(cnt for mask,cnt in dp.items() if mask.bit_count()==size) for size in range(8)]
assert r==[1,28,294,1456,3514,3864,1596,144],r

def allowed(line, colour):
    return colour==7 or colour not in lines[line]

states=[]
for omitted in range(8):
    palette=[c for c in range(8) if c!=omitted]
    states.extend(z for z in permutations(palette) if all(allowed(j,z[j]) for j in V))
assert len(states)==1740
assert len(set(states))==1740
idx={z:i for i,z in enumerate(states)}

def neighbors(s):
    omitted=next(z for z in range(8) if z not in s)
    result=[]
    # Recolor one line with its shore's unique vacant colour.
    for j in V:
        if allowed(j,omitted):
            next_s=list(s); next_s[j]=omitted
            result.append((tuple(next_s),'line',j))
    # Recolor point x with colour 7, then rename x and 7 to canonicalize.
    for x in V:
        if all(s[j]!=7 for j in V if x in lines[j]):
            next_s=tuple(7 if c==x else x if c==7 else c for c in s)
            result.append((next_s,'point',x))
    return result

graph=[]
cross=Counter()
for s in states:
    edges=neighbors(s)
    graph.append([idx[t] for t,_,_ in edges])
    omitted=next(c for c in range(8) if c not in s)
    if omitted!=7:
        cross[sum(7 not in t for t,_,_ in edges)]+=1
assert Counter(map(len,graph))=={8:1596,14:144}
assert cross=={0:588,2:1008},cross
assert sum(map(len,graph))==14784
assert all(i in graph[j] for i,adj in enumerate(graph) for j in adj)

seen={0}; q=deque([0]); distance={0:0}
while q:
    i=q.popleft()
    for j in graph[i]:
        if j not in seen:
            seen.add(j);distance[j]=distance[i]+1;q.append(j)
assert len(seen)==1740

# With seven active colours, every x has a unique same-coloured line y,
# nonincident to x. Recoloring x to blank 7 and then y to 7 effects
# the global swap of the colour x with 7 in two legal moves.
for s in states:
    if 7 in s: continue
    for x in V:
        y=s.index(x)
        assert x not in lines[y]
        assert all(s[j]!=7 for j in V if x in lines[j])
        assert allowed(y,7)

# Each canonical colouring has 8! distinct named lifts.
assert 144*factorial(7)==725760
assert len(states)*factorial(8)==70156800
assert sum(map(len,graph))//2*factorial(8)==298045440
assert 144*14*factorial(8)==81285120
assert (298045440-81285120)==216760320
print('rook numbers:',r)
print('canonical states:',len(states),'degree frequencies:',sorted(Counter(map(len,graph)).items()))
print('canonical components:',len(seen),'max root distance:',max(distance.values()))
print('cross-neighbours of eight-used canonical states:',sorted(cross.items()))
print('7-colour named states:',725760,'8-colour named states:',70156800)
print('8-colour named reconfiguration edges:',298045440)
print('PASS')
