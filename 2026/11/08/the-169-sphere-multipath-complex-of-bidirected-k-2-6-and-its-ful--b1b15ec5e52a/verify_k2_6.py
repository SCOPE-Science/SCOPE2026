#!/usr/bin/env python3
"""Exact independent checks for the multipath complex of bidirected K_{2,6}."""
from itertools import combinations
from collections import deque
from hashlib import sha256

M=6
ARCS=[(h,2+i) for h in (0,1) for i in range(M)] + [(2+i,h) for h in (0,1) for i in range(M)]

def is_multipath(face):
    sources=set();targets=set();successor={}
    for e in face:
        u,v=ARCS[e]
        if u in sources or v in targets:return False
        sources.add(u);targets.add(v);successor[u]=v
    for v in successor:
        seen=set();w=v
        while w in successor:
            if w in seen:return False
            seen.add(w);w=successor[w]
    return True

def build_faces():
    faces={()}
    for size in range(1,5):
        faces.update(s for s in combinations(range(24),size) if is_multipath(s))
    return faces

def build_matching(faces):
    active=set(faces);pairs=[]
    for e in range(24):
        for s in sorted(active,key=lambda x:(len(x),x)):
            if e in s:continue
            t=tuple(sorted(s+(e,)))
            if t in active:
                active.remove(s);active.remove(t);pairs.append((s,t))
    return pairs,active

def test_acyclic(faces,pairs):
    matched=set(pairs)
    adj={f:[] for f in faces}; indeg={f:0 for f in faces}
    covers=0
    for face in faces:
        for k in range(len(face)):
            sub=face[:k]+face[k+1:]
            if (sub,face) in matched:a,b=sub,face
            else:a,b=face,sub
            adj[a].append(b);indeg[b]+=1;covers+=1
    q=deque(f for f in faces if indeg[f]==0)
    seen=0
    while q:
        a=q.popleft();seen+=1
        for b in adj[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    assert seen==len(faces),f'directed gradient cycle exists; visited {seen}'
    return covers

def rank_p(columns,p):
    piv={}
    for col in columns:
        a={k:v%p for k,v in col.items() if v%p}
        while a:
            k=max(a)
            if k not in piv:
                piv[k]=a;break
            b=piv[k];factor=(a[k]*pow(b[k],-1,p))%p
            for j,val in b.items():
                a[j]=(a.get(j,0)-factor*val)%p
                if not a[j]:del a[j]
    return len(piv)

def crosscheck_homology(faces):
    bysize=[[f for f in sorted(faces) if len(f)==k] for k in range(5)]
    counts=tuple(len(fs) for fs in bysize)
    assert counts==(1,24,192,600,600),counts
    for prime in (2,3):
        ranks=[1]
        for k in range(2,5):
            lower={s:i for i,s in enumerate(bysize[k-1])}
            cols=[{lower[f[:j]+f[j+1:]]:(-1)**j for j in range(k)} for f in bysize[k]]
            ranks.append(rank_p(cols,prime))
        assert tuple(ranks)==(1,23,169,431),(prime,ranks)
        betti=[counts[k]-ranks[k-1]-(ranks[k] if k<4 else 0) for k in range(1,5)]
        assert betti==[0,0,0,169],(prime,betti)
    return counts

def main():
    faces=build_faces()
    counts=crosscheck_homology(faces)
    pairs,critical=build_matching(faces)
    assert len(pairs)==624,len(pairs)
    assert len(critical)==169 and all(len(s)==4 for s in critical)
    assert len(set(x for pair in pairs for x in pair))==2*len(pairs)
    assert all(len(t)==len(s)+1 and set(s).issubset(t) for s,t in pairs)
    covers=test_acyclic(faces,pairs)
    # Canonical certificate digest; all face and pair labels are sorted integer tuples.
    signature=sha256('\n'.join(str((s,t)) for s,t in pairs).encode('utf-8')).hexdigest()
    assert signature=='4b74f6d6352facf63b8331aea1dcf5cd2247daa557581d0c58e868280595c03a'
    print('digraph_vertices=8 arcs=24')
    print('augmented_face_counts='+str(counts))
    print('acyclic_matching_pairs=624 critical_3_cells=169 lower_critical_cells=0')
    print('oriented_hasse_cover_relations='+str(covers))
    print('pair_certificate_sha256='+signature)
    print('exact_boundary_ranks_mod_2_and_3=(1,23,169,431)')
    print('reduced_betti_mod_2_and_3=(0,0,0,169)')
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
