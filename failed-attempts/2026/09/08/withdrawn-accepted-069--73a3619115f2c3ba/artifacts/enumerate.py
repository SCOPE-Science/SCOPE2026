"""Enumerate 8-subsets of PG(2,3) up to PGL(3,3); ordinary-line minimum.
Self-contained, stdlib only. Writes results.json."""
import itertools, json

MOD=3
def norm(v):
    for c in v:
        if c!=0:
            inv=1 if c==1 else 2
            return tuple((inv*c)%3 for c in v)
    raise ValueError
PTS=[]
seen=set()
for x in range(3):
    for y in range(3):
        for z in range(3):
            if x==y==z==0: continue
            n=norm((x,y,z))
            if n not in seen:
                seen.add(n); PTS.append(n)
assert len(PTS)==13
PID={p:i for i,p in enumerate(PTS)}
# lines of PG(2,3): 13 lines, each 4 pts
LINES=[]
seenL=set()
for a in range(3):
    for b in range(3):
        for c in range(3):
            if a==b==c==0: continue
            n=norm((a,b,c))
            if n in seenL: continue
            seenL.add(n)
            s=frozenset(i for i,p in enumerate(PTS) if (n[0]*p[0]+n[1]*p[1]+n[2]*p[2])%3==0)
            assert len(s)==4
            LINES.append(s)
assert len(LINES)==13
# PGL(3,3): all invertible 3x3 over GF3, act on points; dedupe to 5616 maps
import math
mats=[]
perms={}
for M in itertools.product(range(3),repeat=9):
    det=(M[0]*(M[4]*M[8]-M[5]*M[7])-M[1]*(M[3]*M[8]-M[5]*M[6])+M[2]*(M[3]*M[7]-M[4]*M[6]))%3
    if det==0: continue
    def apply(p,M=M):
        v=((M[0]*p[0]+M[1]*p[1]+M[2]*p[2])%3,(M[3]*p[0]+M[4]*p[1]+M[5]*p[2])%3,(M[6]*p[0]+M[7]*p[1]+M[8]*p[2])%3)
        return PID[norm(v)]
    perm=tuple(apply(p) for p in PTS)
    if perm not in perms:
        perms[perm]=M
print("PGL size",len(perms))
G=list(perms.keys())
def canon(S):
    return min(tuple(sorted(g[i] for i in S)) for g in G)
orbits={}
for S in itertools.combinations(range(13),8):
    # spanning + rank check: not all on one line (max 4 on line so auto), rank 3 = not contained in a line; 8 pts never on 4-pt line
    c=canon(S)
    orbits.setdefault(c,[]).append(S)
print("orbits:",len(orbits))
def lines_of(S):
    S=set(S)
    res=[]
    for L in LINES:
        inter=S&set(L)
        if len(inter)>=2:
            res.append(sorted(inter))
    # rank-2 flats of restriction = maximal intersections; in rank 3, each pair lies in unique flat
    # dedupe: intersections of size>=2 of PG-lines with S are already flats (line meets S in >=2 => closure)
    # but also closures of pairs contained in no PG line?? In a restriction every pair's closure = L cap S for unique L. So:
    uniq=sorted(set(tuple(x) for x in res))
    return uniq
results=[]
for c,members in orbits.items():
    S=members[0]
    flats=lines_of(S)
    ords=[f for f in flats if len(f)==2]
    results.append({"canon":list(c),"count_members":len(members),
        "nlines":len(flats),"nordinary":len(ords),
        "flats":[list(f) for f in flats],
        "example":[list(PTS[i]) for i in S]})
results.sort(key=lambda r:(r["nordinary"],r["canon"]))
E=min(r["nordinary"] for r in results)
from collections import Counter
print("E_3 =",E)
print(Counter(r["nordinary"] for r in results))
mins=[r for r in results if r["nordinary"]==E]
print("nminimizers:",len(mins))
for r in mins:
    print(r["canon"],"nlines",r["nlines"],"coords",r["example"])
json.dump({"E":E,"orbits":results,"n_orbits":len(results)},open("output/artifacts/results.json","w"),indent=1)
