"""Exhaustive bitmask certificate for minimum locating-total versus identifying codes of mu(C5).
Python 3, no nonstandard dependencies. Run: python verification_a.py
"""
from itertools import combinations
from collections import Counter, deque

N = 11
edges = set()
for i in range(5):
    edges.add(tuple(sorted((i, (i+1)%5))))
    edges.add(tuple(sorted((i, 5+(i-1)%5))))
    edges.add(tuple(sorted((i, 5+(i+1)%5))))
    edges.add((5+i,10))
assert len(edges)==20
A=[0]*N
for x,y in edges:
    A[x]|=1<<y
    A[y]|=1<<x
assert sorted(x.bit_count() for x in A)==[3]*5+[4]*5+[5]
ALL=(1<<N)-1

def identifying(S):
    seen=set()
    for v in range(N):
        signature=(A[v]|1<<v)&S
        if not signature or signature in seen:return False
        seen.add(signature)
    return True

def locating_total(S):
    sigs=set()
    for v in range(N):
        x=A[v]&S
        if not x:return False
        if not (S>>v)&1:
            if x in sigs:return False
            sigs.add(x)
    return True

def codes(predicate):
    for k in range(12):
        x={sum(1<<v for v in s) for s in combinations(range(N),k) if predicate(sum(1<<v for v in s))}
        if x:return k,x
    raise AssertionError('nonexistent code')

kT,T=codes(locating_total)
kI,I=codes(identifying)
assert (kT,len(T),kI,len(I))==(5,110,5,191)
assert T<=I and len(I-T)==81

def build(sets,slide):
    nb={s:set() for s in sets}
    for S in sets:
        for x in range(N):
            if not (S>>x)&1:continue
            for y in range(N):
                if (S>>y)&1 or (slide and not (A[x]>>y)&1):continue
                D=S^(1<<x)^(1<<y)
                if D in nb:nb[S].add(D)
    for s,ss in nb.items():
        assert all(s in nb[t] for t in ss)
    return nb

def distances(gr,s):
    dist={s:0}
    queue=deque([s])
    while queue:
        v=queue.popleft()
        for w in gr[v]:
            if w not in dist:
                dist[w]=dist[v]+1
                queue.append(w)
    assert len(dist)==len(gr), ('not connected',len(dist),len(gr))
    return dist

for mode in ('jump','slide'):
    Gt=build(T,mode=='slide')
    Gi=build(I,mode=='slide')
    E_T=sum(map(len,Gt.values()))//2
    E_I=sum(map(len,Gi.values()))//2
    dT={s:distances(Gt,s) for s in T}
    dI={s:distances(Gi,s) for s in T}
    dif=Counter(dT[s][t]-dI[s][t] for s,t in combinations(sorted(T),2))
    assert min(dif)>=0
    assert sum(dif.values())==110*109//2
    radiusT=min(max(r.values()) for r in dT.values());diamT=max(max(r.values()) for r in dT.values())
    diamI=max(max(distances(Gi,s).values()) for s in I)
    radiusI=min(max(distances(Gi,s).values()) for s in I)
    expected={'jump':(520,1405,4,5,4,5,{0:5725,1:270}),
              'slide':(190,555,6,8,5,6,{0:4135,1:1440,2:360,3:60})}[mode]
    got=(E_T,E_I,radiusT,diamT,radiusI,diamI,dict(sorted(dif.items())))
    assert got==expected,(mode,got,expected)
    print(mode, 'LT_edges',E_T,'IC_edges',E_I,'LT_radius_diam',radiusT,diamT,
          'IC_radius_diam',radiusI,diamI,'unordered_distance_saving',dict(sorted(dif.items())))
print('PASS exhaustive certificate: 5 selected vertices, 110 LT codes subset 191 identifying codes')
