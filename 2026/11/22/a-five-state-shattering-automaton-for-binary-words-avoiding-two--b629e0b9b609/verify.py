"""Independent finite-state and direct checks of coordinate shattering for binary strings avoiding 000 and 101."""
from collections import deque
from itertools import product
from math import floor

FORBIDDEN = {(0,0,0),(1,0,1)}
def extension(state, bit):
    trial=state+(bit,)
    if len(trial)>=3 and trial[-3:] in FORBIDDEN: return None
    return trial[-2:]

def advance_family(family,mask):
    new=set()
    for subset in family:
        for choices in ((0,1),) if mask==0 else ((0,),(1,)):
            image=frozenset(next_state for st in subset for bit in choices
                            if (next_state:=extension(st,bit)) is not None)
            if not image: return None
            new.add(image)
    return frozenset(new)

start=frozenset((frozenset(((),)),))
seen={start:0}
queue=deque([start])
trans=[]
while queue:
    cur=queue.popleft()
    row=[]
    for mask in (0,1):
        nxt=advance_family(cur,mask)
        if nxt is not None and nxt not in seen:
            seen[nxt]=len(seen)
            queue.append(nxt)
        row.append(None if nxt is None else seen[nxt])
    trans.append(tuple(row))
assert len(seen)==16, len(seen)
# partition refinement from the two output symbols and a rejecting dead state
classes=[0]*len(seen)
for _ in range(len(seen)+1):
    key_to_class={}; updated=[]
    for i,row in enumerate(trans):
        sig=(classes[i], tuple(-1 if j is None else classes[j] for j in row))
        if sig not in key_to_class: key_to_class[sig]=len(key_to_class)
        updated.append(key_to_class[sig])
    if updated==classes: break
    classes=updated
assert len(set(classes))==5
mintrans=[]
for c in range(5):
    i=classes.index(c)
    mintrans.append(tuple(None if j is None else classes[j] for j in trans[i]))
assert mintrans==[(0,1),(2,3),(0,3),(4,None),(2,None)],mintrans
# A potential h obeying h[next] <= h[current] + (2-5*mask), gives 5k <=2n+6.
h=(0,-3,-2,-6,-4)
for i,row in enumerate(mintrans):
    for mask,j in enumerate(row):
        if j is not None: assert h[j]<=h[i]+2-5*mask
assert min(h)==-6

def accepts(indicator):
    s=0
    for bit in indicator:
        s=mintrans[s][bit]
        if s is None:return False
    return True

def admissible(words):
    return all(tuple(words[i:i+3]) not in FORBIDDEN for i in range(len(words)-2))

def count_poly(n):
    dp={(0,0):1}
    for _ in range(n):
        nxt={}
        for (state,k),count in dp.items():
            for b in (0,1):
                state2=mintrans[state][b]
                if state2 is not None:
                    nxt[(state2,k+b)]=nxt.get((state2,k+b),0)+count
        dp=nxt
    poly=[0]*(n+1)
    for (state,k),count in dp.items():poly[k]+=count
    return poly

for n in range(0,12):
    hypotheses=[w for w in product((0,1),repeat=n) if admissible(w)]
    poly=[0]*(n+1)
    for support in product((0,1),repeat=n):
        positions=[i for i,x in enumerate(support) if x]
        traces={tuple(w[i] for i in positions) for w in hypotheses}
        reality=len(traces)==2**len(positions)
        assert accepts(support)==reality,(n,support,accepts(support),traces)
        poly[len(positions)]+=reality
    assert poly==count_poly(n),(n,poly,count_poly(n))
    if n>=1: assert max(k for k,c in enumerate(poly) if c)==(2*n+6)//5,(n,poly)
    print('n=',n,'polynomial=',poly,'VC=',max(k for k,c in enumerate(poly) if c),'hypotheses=',len(hypotheses))
# Construct sharp witnesses for every k>=2, and check all lengths n<=100.
for k in range(2,45):
    r=k//2
    witness=('11'+'00011'*(r-1)) if k%2==0 else ('10011'+'00011'*(r-1))
    assert len(witness)==(5*k-6+1)//2,(k,len(witness))
    assert witness.count('1')==k and accepts(tuple(int(c) for c in witness)),(k,witness)
print('FINITE_STATE_CERTIFICATE_PASS 16 reachable states, 5 minimized states, exhaustive n=0..11, potential bound, constructions k=2..44')
