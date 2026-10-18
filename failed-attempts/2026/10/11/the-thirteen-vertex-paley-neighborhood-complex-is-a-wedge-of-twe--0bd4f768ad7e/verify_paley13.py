#!/usr/bin/env python3
"""Exact finite discrete-Morse certificate for the open-neighborhood complex of Paley(13)."""
from itertools import combinations
from collections import Counter, deque

P=13
Q=frozenset({pow(t,2,P) for t in range(1,P)})
ORDER=(4,2,6,5,10,12,3,11,0,7,8,1,9)
assert Q==frozenset({1,3,4,9,10,12})


def faces():
    out=set()
    for center in range(P):
        near=[x for x in range(P) if (x-center)%P in Q]
        assert len(near)==6
        for d in range(1,7):
            for combo in combinations(near,d):
                out.add(sum(1<<v for v in combo))
    return out


def matching(face_set):
    remaining=set(face_set)
    pairs=[]
    for v in ORDER:
        bit=1<<v
        for mask in sorted(tuple(remaining)):
            if mask in remaining and not(mask&bit) and (mask|bit) in remaining:
                remaining.remove(mask)
                remaining.remove(mask|bit)
                pairs.append((mask,mask|bit))
    return pairs,remaining


def verify_acyclic(face_set,pairs):
    from_lower={a:b for a,b in pairs}
    assert len(from_lower)==len(pairs)
    indegree={x:0 for x in face_set}
    directed={x:[] for x in face_set}
    incidence_count=0
    for s in face_set:
        if s.bit_count()<=1:continue
        for v in range(P):
            if not (s>>v&1): continue
            t=s^(1<<v)
            if not t:continue
            assert t in face_set
            incidence_count+=1
            if from_lower.get(t)==s:
                tail,head=t,s
            else:
                tail,head=s,t
            directed[tail].append(head)
            indegree[head]+=1
    queue=deque(v for v,k in indegree.items() if k==0)
    visited=0
    while queue:
        v=queue.popleft();visited+=1
        for w in directed[v]:
            indegree[w]-=1
            if indegree[w]==0:queue.append(w)
    assert visited==len(face_set),(visited,len(face_set))
    return incidence_count


def main():
    fs=faces()
    assert len(fs)==598
    assert Counter(s.bit_count()-1 for s in fs)=={0:13,1:78,2:221,3:195,4:78,5:13}
    pairs,critical=matching(fs)
    assert len(pairs)==286 and len(critical)==26
    assert Counter(s.bit_count()-1 for s in critical)=={0:1,2:25}
    edges=verify_acyclic(fs,pairs)
    assert edges==sum((s.bit_count() for s in fs if s.bit_count()>=2))
    critical_vertices=sorted(m.bit_length()-1 for m in critical if m.bit_count()==1)
    critical_triangles=sorted(tuple(v for v in range(P) if m>>v&1) for m in critical if m.bit_count()==3)
    print('CERTIFICATE_OK','faces',len(fs),'pairs',len(pairs),'incidences',edges,'critical_vertex',critical_vertices,'critical_triangles',critical_triangles)

if __name__=='__main__':main()
