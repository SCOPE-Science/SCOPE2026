#!/usr/bin/env python3
"""Exact finite homotopy certificate for the level-one forest complex of K2 x K3 x K4.

Standard library only; all simplicial faces are represented by 24-bit masks.
The acyclic-matching certificate is reconstructed and checked in its entirety.
"""
import collections
import functools
import hashlib
import json
import random

VERTICES = tuple((a,b,c) for a in range(2) for b in range(3) for c in range(4))
N = len(VERTICES)
ADJ = tuple(sum(1 << j for j,w in enumerate(VERTICES)
                if j != i and all(x != y for x,y in zip(v,w)))
            for i,v in enumerate(VERTICES))


def direct_faces():
    result = [0]
    def rec(s,start):
        for i in range(start,N):
            t = s | (1 << i)
            if (t & ADJ[i]).bit_count() > 1:
                continue
            if any((t & ADJ[j]).bit_count()>1 for j in range(N) if (s>>j)&1):
                continue
            result.append(t)
            rec(t,i+1)
    rec(0,0)
    return set(result)


def obstruction_faces():
    # An induced graph has maximum degree <= 1 iff it contains no centered P3.
    # A forbidden triple is constructed directly from unordered neighbor pairs.
    triples=set()
    for center in range(N):
        neighbors=[i for i in range(N) if ADJ[center] >> i & 1]
        for ix,u in enumerate(neighbors):
            for w in neighbors[ix+1:]:
                triples.add((1<<center)|(1<<u)|(1<<w))
    assert len(triples)==360
    blockers=[]
    for v in range(N):
        blockers.append(tuple(t^(1<<v) for t in triples if t & (1<<v)))
    faces={0}
    for v in range(N):
        bit=1<<v
        additions={s|bit for s in faces
                   if all((s & p)!=p for p in blockers[v])}
        faces.update(additions)
    return faces, len(triples)


def facets_of(s):
    c=s
    while c:
        bit=c&-c;c-=bit
        yield s^bit


def matching(faces,order):
    unpaired=set(faces)-{0}
    mate_low={}
    for v in order:
        bit=1<<v
        for s in tuple(unpaired):
            if not s&bit and (s|bit) in unpaired:
                unpaired.remove(s);unpaired.remove(s|bit)
                mate_low[s]=s|bit
    return mate_low,unpaired


def matching_acyclic(faces,mate_low):
    # Directed Hasse orientation: upper -> lower for unmatched incidences,
    # lower -> upper for matched incidences.  Kahn's algorithm checks all nodes.
    indeg={s:0 for s in faces if s}
    outgoing=collections.defaultdict(list)
    incidence=0
    for s in indeg:
        for t in facets_of(s):
            if not t: continue
            incidence+=1
            if mate_low.get(t)==s:
                u,v=t,s
            else:
                u,v=s,t
            outgoing[u].append(v)
            indeg[v]+=1
    q=collections.deque(s for s,d in indeg.items() if d==0)
    seen=0
    while q:
        u=q.popleft()
        seen+=1
        for v in outgoing.get(u,()):
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert seen==len(faces)-1, ('cycle found',seen,len(faces)-1)
    return incidence, seen


def morse_boundary_rank_mod2(mate_low,critical,dimension):
    src=sorted(s for s in critical if s.bit_count()==dimension+1)
    dst=sorted(s for s in critical if s.bit_count()==dimension)
    idx={s:i for i,s in enumerate(dst)}
    uppers=set(mate_low.values())
    @functools.lru_cache(None)
    def projection(s):
        if s in idx:return 1<<idx[s]
        if s in uppers:return 0
        assert s in mate_low, ('unexpected noncritical face',s,dimension)
        up=mate_low[s]
        total=0
        for f in facets_of(up):
            if f!=s:total^=projection(f)
        return total
    basis={}
    for s in src:
        boundary=0
        for t in facets_of(s):
            boundary ^= projection(t)
        w=boundary
        while w:
            pivot=w.bit_length()-1
            if pivot in basis:w^=basis[pivot]
            else:
                basis[pivot]=w
                break
    return len(basis),len(dst),len(src)


def shuffled_order():
    order=list(range(N))
    random.Random(1).shuffle(order)
    return order

def verify():
    faces=direct_faces()
    other,obstructions=obstruction_faces()
    assert faces==other
    fvector=dict(sorted(collections.Counter(s.bit_count()-1 for s in faces).items()))
    assert len(faces)==34910
    facet_hist=dict(sorted(collections.Counter(s.bit_count()-1 for s in faces if s and all((s|(1<<j)) not in faces for j in range(N) if not (s>>j)&1)).items()))
    assert facet_hist=={5:52,6:504,7:435,11:2}
    assert [ADJ[i].bit_count() for i in range(N)]==[6]*24
    assert sum(map(int.bit_count,ADJ))//2==72
    assert sum((-1)**(k)*v for k,v in fvector.items())==78*(-1)**5
    outcomes={}
    for tag,order in (
        ('forward',tuple(range(N))),
        ('reverse',tuple(reversed(range(N)))),
        ('mixed',tuple(shuffled_order())),
    ):
        mate,crit=matching(faces,order)
        incidence,processed=matching_acyclic(faces,mate)
        histogram=dict(sorted(collections.Counter(s.bit_count()-1 for s in crit).items()))
        info={'matched_pairs':len(mate),'critical_cells':histogram,
              'hasse_incidences':incidence,'acyclic_vertices_checked':processed,
              'matching_edge_digest':hashlib.sha256('\n'.join(f'{s}:{mate[s]}' for s in sorted(mate)).encode()).hexdigest()}
        if tag in ('forward','reverse'):
            assert histogram=={0:1,5:78}
        else:
            assert histogram=={0:1,4:9,5:95,6:8}
            ranks={}
            for d in (4,5,6):
                rank,tgt,src=morse_boundary_rank_mod2(mate,crit,d)
                ranks[str(d)]={'rank':rank,'target_critical_cells':tgt,'source_critical_cells':src}
            assert ranks['4']['rank']==0
            assert ranks['5']['rank']==9
            assert ranks['6']['rank']==8
            info['mod2_morse_boundary_ranks']=ranks
        outcomes[tag]=info
    return {'graph':'K2 x K3 x K4 (categorical product)',
            'vertex_count':N,'edge_count':72,'forbidden_centered_triples':obstructions,
            'face_count_including_empty':len(faces),
            'independent_face_enumerations_agree':True,
            'face_vector':{str(k):v for k,v in fvector.items()},
            'facets_by_dimension':{str(k):v for k,v in facet_hist.items()},
            'matching_checks':outcomes,
            'theorem':'F1(K2 x K3 x K4) homotopy equivalent to wedge of 78 five-spheres',
            'status':'PASS'}

if __name__=='__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
