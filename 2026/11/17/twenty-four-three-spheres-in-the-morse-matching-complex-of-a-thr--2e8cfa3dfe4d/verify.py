#!/usr/bin/env python3
"""Reconstruct and verify the discrete Morse certificate for the three-triangle disk.
Run: python verify.py certificate.json
Only the Python standard library is used.
"""
import sys, json, itertools, collections, heapq, hashlib

TRIANGLES=((0,1,2),(0,1,3),(0,2,3))
base=sorted({tuple(c) for t in TRIANGLES for k in (1,2,3)
             for c in itertools.combinations(t,k)}, key=lambda a:(len(a),a))
bid={f:i for i,f in enumerate(base)}
primitive=tuple((i,j) for i,a in enumerate(base) for j,b in enumerate(base)
                if len(b)==len(a)+1 and set(a).issubset(b))
assert len(base)==13 and len(primitive)==21

# Independent cycle test: Hasse diagram, with matched incidences upward,
# all unmatched incidences downward.
def is_acyclic(choice):
    used=set()
    for i in choice:
        a,b=primitive[i]
        if a in used or b in used:return False
        used.add(a);used.add(b)
    chosen=set(choice)
    out=[[] for _ in base]
    indeg=[0]*len(base)
    for i,(a,b) in enumerate(primitive):
        src,dst=(a,b) if i in chosen else (b,a)
        out[src].append(dst);indeg[dst]+=1
    q=collections.deque(i for i,d in enumerate(indeg) if d==0)
    visited=0
    while q:
        i=q.popleft();visited+=1
        for j in out[i]:
            indeg[j]-=1
            if indeg[j]==0:q.append(j)
    return visited==len(base)

# Enumerate every nonempty gradient field as a bit mask of primitive edges.
# This recursion prunes only endpoint collisions and directed cycles.
allfaces={0}
def enumerate_faces(i,mask,used):
    if i==len(primitive):
        allfaces.add(mask);return
    enumerate_faces(i+1,mask,used)
    a,b=primitive[i]
    if a in used or b in used:return
    chosen=[j for j in range(i+1) if mask>>j&1]
    chosen.append(i)
    if is_acyclic(chosen):enumerate_faces(i+1,mask|(1<<i),used|{a,b})
enumerate_faces(0,0,set())
assert len(allfaces)==2122
counts=collections.Counter(mask.bit_count()-1 for mask in allfaces if mask)
assert [counts[k] for k in range(6)]==[21,162,560,846,468,64]
assert sum((-1)**k*counts[k] for k in range(6))==-23

with open(sys.argv[1],encoding='utf-8') as f:cert=json.load(f)
assert cert['base_triangles']==[list(t) for t in TRIANGLES]
assert cert['primitive_pairs']==[list(p) for p in primitive]
assert cert['expected_face_vector']==[21,162,560,846,468,64]
pairs=[tuple(p) for p in cert['matching_pairs']]
critical=cert['critical_faces']
assert len(pairs)==1048 and len(critical)==25
usedfaces=set()
matched=set()
for lo,hi in pairs:
    assert isinstance(lo,int) and isinstance(hi,int)
    assert lo in allfaces and hi in allfaces and lo!=0
    assert hi.bit_count()==lo.bit_count()+1
    assert lo&hi==lo and (hi^lo).bit_count()==1
    assert lo not in usedfaces and hi not in usedfaces
    usedfaces.update((lo,hi));matched.add((lo,hi))
for s in critical:
    assert s in allfaces and s!=0 and s not in usedfaces
    usedfaces.add(s)
assert usedfaces==allfaces-{0}
assert collections.Counter(s.bit_count()-1 for s in critical)=={0:1,3:24}

# Complete directed face-poset Hasse graph with exactly the certificate
# incidences reversed. Directed cycles are ruled out by Kahn's algorithm.
nonempty=sorted(allfaces-{0})
out={s:[] for s in nonempty}
indegree={s:0 for s in nonempty}
for hi in nonempty:
    for bit in range(len(primitive)):
        if not (hi>>bit&1):continue
        lo=hi^(1<<bit)
        if not lo:continue
        src,dst=(lo,hi) if (lo,hi) in matched else (hi,lo)
        out[src].append(dst);indegree[dst]+=1
queue=collections.deque(s for s in nonempty if indegree[s]==0)
visited=0
while queue:
    s=queue.popleft();visited+=1
    for t in out[s]:
        indegree[t]-=1
        if indegree[t]==0:queue.append(t)
assert visited==len(nonempty), 'gradient cycle in proposed matching'

# Independently calculate mod-two simplicial boundary ranks.
def mod2rank(columns):
    pivots={}
    for x in columns:
        while x:
            q=x.bit_length()-1
            if q in pivots:x^=pivots[q]
            else:pivots[q]=x;break
    return len(pivots)
bydim={k:sorted(s for s in nonempty if s.bit_count()==k+1) for k in range(6)}
ranks={0:0,6:0}
for k in range(1,6):
    lower={s:i for i,s in enumerate(bydim[k-1])}
    cols=[]
    for s in bydim[k]:
        col=0
        for b in range(21):
            if s>>b&1:col^=(1<<lower[s^(1<<b)])
        cols.append(col)
    ranks[k]=mod2rank(cols)
betti={k:len(bydim[k])-ranks[k]-ranks[k+1]-(k==0) for k in range(6)}
assert betti=={0:0,1:0,2:0,3:24,4:0,5:0},betti
print('MORSE_TRIANGLE_FAN_PASS')
print('base faces=13, primitive Hasse incidences=21')
print('Morse complex f-vector=',[counts[k] for k in range(6)])
print('all nonempty simplices=',len(nonempty))
print('acyclic face-poset matching pairs=',len(pairs))
print('critical cells=',{0:1,3:24})
print('mod-2 reduced Betti numbers=',betti)
print('unrestricted conclusion: wedge of 24 three-spheres by discrete Morse theorem')
