"""Independent verifier (stdlib only): rebuilds AG(3,4), checks all witnesses."""
import json,itertools,hashlib
add=lambda a,b:a^b
M=[[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
def mul(a,b): return M[a][b]
def coords(p): return ((p>>4)&3,(p>>2)&3,p&3)
def pt(c): return (c[0]<<4)|(c[1]<<2)|c[2]
PTS=list(range(64))
dirs=[(a,b,c) for a in range(4) for b in range(4) for c in range(4)
      if (a,b,c)!=(0,0,0) and (a if a!=0 else (b if b!=0 else c))==1]
assert len(dirs)==21,"ndirs"
L=set()
for d in dirs:
    seen=set()
    for p in PTS:
        if p in seen: continue
        c=coords(p)
        Li=tuple(sorted(pt((add(c[0],mul(t,d[0])),add(c[1],mul(t,d[1])),add(c[2],mul(t,d[2])))) for t in range(4)))
        assert len(Li)==4
        L.add(Li); seen.update(Li)
LINES=sorted(L)
assert len(LINES)==336,"nlines"
pc={}
for Li in LINES:
    for a,b in itertools.combinations(sorted(Li),2):
        pc[(a,b)]=pc.get((a,b),0)+1
assert len(pc)==2016 and all(v==1 for v in pc.values()),"pair uniqueness"
def is_cap(S):
    s=set(S)
    return all(len(s.intersection(Li))<3 for Li in LINES)
def uncovered(S):
    s=set(S); cov=set()
    for Li in LINES:
        if sum(1 for q in Li if q in s)==2:
            cov.update(q for q in Li if q not in s)
    return sorted(p for p in PTS if p not in s and p not in cov)
W=json.load(open('output/artifacts/witnesses.json'))
ok=True
for name,S in W.items():
    cap=is_cap(S); u=uncovered(S)
    line=f"{name}: n={len(S)} distinct={len(set(S))==len(S)} inrange={all(0<=x<64 for x in S)} cap={cap} uncovered={len(u)}"
    print(line)
    if not (cap and not u): ok=False
# cube cover replay
C=json.load(open('output/artifacts/cube_secant_cover.json'))
cube=set(W["cube8"])
assert len(C)==56
for ks,inter in C.items():
    k=int(ks)
    assert k not in cube and len(inter)==2 and all(q in cube for q in inter)
    # k collinear with the pair
    found=any(set(Li)>={k,inter[0],inter[1]} for Li in LINES)
    assert found,f"cover line missing for {k}"
print("cube secant cover: 56/56 outside points on a cube secant: OK")
# puncture check on C12
C12=W["C12"]
import itertools as it
for k in (11,10,9):
    nc=0; ncomp=0
    for sub in it.combinations(C12,k):
        s=set(sub)
        if all(len(s.intersection(Li))<3 for Li in LINES):
            nc+=1
            if not uncovered(sub): ncomp+=1
    print(f"C12 puncture k={k}: cap-subsets={nc} complete={ncomp}")
    assert ncomp==0
print("ALL CHECKS PASS" if ok else "FAILURE")
