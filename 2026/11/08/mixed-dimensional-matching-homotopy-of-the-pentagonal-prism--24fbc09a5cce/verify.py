#!/usr/bin/env python3
"""Finite integral discrete-Morse certificate for the ordinary matching complex of the pentagonal prism."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import itertools

N=5
V=[(i,j) for i in range(N) for j in range(2)]
E=[]
for i in range(N):
    for j in range(2): E.append(((i,j),((i+1)%N,j)))
for i in range(N): E.append(((i,0),(i,1)))
assert len(E)==15 and len({frozenset(e) for e in E})==15
ORDER=(7,12,3,9,1,4,8,2,11,6,5,13,10,14,0)

# Enumerate matching faces, including the empty simplex.
faces={0}
for m in range(1,1<<15):
    L=[E[i] for i in range(15) if (m>>i)&1]
    endpoints=[v for e in L for v in e]
    if len(endpoints)==len(set(endpoints)): faces.add(m)
assert len(faces)==342
fvec=Counter(m.bit_count()-1 for m in faces if m)
assert [fvec[i] for i in range(5)]==[15,75,145,95,11]

# Sequential elementary matching by edge coordinate. The empty face is excluded.
remaining=faces-{0}
pairs=[]
for i in ORDER:
    bit=1<<i
    lower=sorted(s for s in remaining if not s&bit and (s|bit) in remaining)
    for a in lower:
        b=a|bit
        assert a in remaining and b in remaining
        remaining.remove(a);remaining.remove(b)
        pairs.append((a,b))
assert len(pairs)==168 and len(remaining)==5
critical=sorted(remaining)
assert Counter(m.bit_count()-1 for m in critical)=={0:1,2:2,3:2}

# Check complete directed Hasse diagram acyclic: ordinary arrows downward,
# matched arrows reversed. This is a finite certificate, not a heuristic.
matched={(a,b) for a,b in pairs}
succ=defaultdict(list)
indeg={c:0 for c in faces if c}
incidences=0
for b in faces:
    if not b: continue
    for i in range(15):
        if not(b>>i)&1: continue
        a=b^(1<<i)
        if not a:continue
        incidences+=1
        u,v=(a,b) if (a,b) in matched else (b,a)
        succ[u].append(v)
        indeg[v]+=1
q=deque(x for x,k in indeg.items() if k==0)
visited=0
while q:
    x=q.popleft();visited+=1
    for y in succ[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert visited==len(faces)-1

# Integral incidence numbers in standard ascending edge-index orientation.
def bdry(s):
    ids=[i for i in range(15) if (s>>i)&1]
    return [(s^(1<<i),(-1)**p) for p,i in enumerate(ids)]

lower_to_upper={a:b for a,b in pairs}
upper_set={b for a,b in pairs}
critical_set=set(critical)

@lru_cache(None)
def project(s):
    if s in critical_set:return {s:1}
    if s in upper_set:return {}
    assert s in lower_to_upper
    b=lower_to_upper[s]
    terms=bdry(b)
    unit=dict(terms)[s]
    assert unit in (-1,1)
    result={}
    for face,coef in terms:
        if face==s:continue
        for t,v in project(face).items():
            result[t]=result.get(t,0)-unit*coef*v
            if not result[t]:del result[t]
    return result

morse={}
for cell in critical:
    d=cell.bit_count()-1
    if d==0:continue
    out={}
    for lower,coef in bdry(cell):
        for target,v in project(lower).items():
            out[target]=out.get(target,0)+coef*v
            if not out[target]:del out[target]
    morse[cell]=out
assert all(not v for v in morse.values()),morse

# Independent simplicial boundary ranks over prime fields.
def rankmod(p,d):
    lower=sorted(s for s in faces if s and s.bit_count()==d)
    upper=sorted(s for s in faces if s and s.bit_count()==d+1)
    index={s:i for i,s in enumerate(lower)}
    pivots={}
    for s in upper:
        v={index[t]:c%p for t,c in bdry(s)}
        while v:
            i=min(v)
            if i not in pivots:
                inv=pow(v[i],-1,p)
                pivots[i]={j:(x*inv)%p for j,x in v.items() if (x*inv)%p}
                break
            factor=v[i]
            for j,x in pivots[i].items():
                value=(v.get(j,0)-factor*x)%p
                if value:v[j]=value
                elif j in v:del v[j]
    return len(pivots)

betti_by_prime={}
for p in (2,3,5):
    ranks={d:rankmod(p,d) for d in range(1,6)}
    betti={d:fvec[d]-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d in range(5)}
    betti_by_prime[p]=betti
    assert betti=={0:0,1:0,2:2,3:2,4:0},(p,betti,ranks)

print('GRAPH_EDGES=15')
print('NONEMPTY_FACES=341')
print('FVECTOR='+','.join(map(str,[fvec[i] for i in range(5)])))
print('HASSE_INCIDENCES='+str(incidences))
print('MATCHED_PAIRS='+str(len(pairs)))
print('CRITICAL='+str(dict(sorted(Counter(c.bit_count()-1 for c in critical).items()))))
print('MORSE_3_TO_2='+str([[morse[c].get(t,0) for t in critical if t.bit_count()==3] for c in critical if c.bit_count()==4]))
for p in (2,3,5): print('BETTI_MOD_'+str(p)+'='+','.join(map(str,[betti_by_prime[p][d] for d in range(5)])))
print('ALL_VERIFY_OK')
