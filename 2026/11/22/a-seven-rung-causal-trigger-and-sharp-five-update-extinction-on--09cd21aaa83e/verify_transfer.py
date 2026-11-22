"""Independent regular-language and conflict certificate for late excitations."""
from itertools import product
from collections import deque

TOP = [(1,4,7), (3,), (0,2), (3,4,5), (0,2), (3,), (1,4,7)]
def swap(v): return 3*(v%3)+v//3
BOT = [tuple(swap(x) for x in q) for q in TOP]
PATTERNS = [tuple(x) for sets in (TOP,BOT) for x in product(*sets)]
assert len(PATTERNS) == len(set(PATTERNS)) == 216

# Two distinct time-three neighbors of any vertex cannot both be excited.
def overlay(row1,center1,row2,center2):
    z1,z2=(TOP,BOT)[row1],(TOP,BOT)[row2]
    for c in range(max(center1-3,center2-3),min(center1+3,center2+3)+1):
        if not(set(z1[c-center1+3]) & set(z2[c-center2+3])):
            return False
    return True
for row in (0,1):
    assert not overlay(row,-1,row,1)
    assert not overlay(row,-1,1-row,0)
    assert not overlay(row,1,1-row,0)
print('local conflicting-pair test: PASS (six cases)')

# Aho-Corasick DFA counts the strings avoiding either seven-rung motif.
children = [{}]; forbidden = [False]
for pat in PATTERNS:
    s=0
    for a in pat:
        if a not in children[s]:
            children[s][a]=len(children)
            children.append({})
            forbidden.append(False)
        s=children[s][a]
    forbidden[s]=True
fail=[0]*len(children)
queue=deque()
for a in range(9):
    if a in children[0]:
        v=children[0][a];fail[v]=0;queue.append(v)
    else:children[0][a]=0
while queue:
    s=queue.popleft()
    forbidden[s]=forbidden[s] or forbidden[fail[s]]
    for a in range(9):
        if a in children[s]:
            fail[children[s][a]]=children[fail[s]][a]
            queue.append(children[s][a])
        else:children[s][a]=children[fail[s]][a]
assert len(children)==420 and sum(not b for b in forbidden)==204

counts = [0]*len(children);counts[0]=1
known={7:216,8:3888,9:52488,10:629856,11:7085880,12:76524912}
for n in range(1,13):
    nxt=[0]*len(children)
    for s,w in enumerate(counts):
        if w:
            for a,t in children[s].items():
                if not forbidden[t]:nxt[t]+=w
    counts=nxt
    late=9**n-sum(counts)
    if n<7: assert late==0
    if n in known:assert late==known[n]
    print(f'n={n} seven-rung-event-population={late}')
print('dfa states=204, terminal or prefix states=420; TRANSFER_OK')
