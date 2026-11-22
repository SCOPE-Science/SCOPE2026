#!/usr/bin/env python3
"""Exact finite certificate checker for a Durer perfect-matching fault atlas.
Python 3 standard library only. Run beside CERTIFICATE.json.
"""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

# Vertices 0..5 are u_i; 6..11 are v_i; all indices modulo six.
EDGES = [tuple(sorted((i, (i+1)%6))) for i in range(6)]
EDGES += [tuple(sorted((i, 6+i))) for i in range(6)]
EDGES += [tuple(sorted((6+i, 6+(i+2)%6))) for i in range(6)]
assert len(EDGES) == 18 and len(set(EDGES)) == 18


def enumerate_matchings():
    adj = [[] for _ in range(12)]
    for e, (u,v) in enumerate(EDGES):
        adj[u].append((v,e)); adj[v].append((u,e))
    answer = []
    def walk(unmatched, chosen):
        if not unmatched:
            answer.append(tuple(sorted(chosen))); return
        u = min(unmatched)
        for v,e in adj[u]:
            if v in unmatched:walk(unmatched-{u,v},chosen+(e,))
    walk(set(range(12)),())
    return sorted(answer)


def independent_matchings():
    answer=[]
    for candidate in combinations(range(18), 6):
        incidence=[0]*12
        for edge in candidate:
            for v in EDGES[edge]:incidence[v]+=1
        if all(a==1 for a in incidence):answer.append(candidate)
    return sorted(answer)


def nerve_faces(matchings):
    # A face is a nonempty collection of matching facets with common edge.
    masks=[sum(1<<e for e in p) for p in matchings]
    answer=set()
    for m in range(1, 1<<len(masks)):
        common=(1<<18)-1
        for i,pm in enumerate(masks):
            if m>>i&1:common &= pm
            if not common:break
        if common:answer.add(m)
    return answer


def next_pair(faces):
    cofaces={}
    for upper in faces:
        for bit in range(upper.bit_length()):
            if upper>>bit&1:
                lower=upper^(1<<bit)
                if lower in faces:
                    cofaces.setdefault(lower,[]).append(upper)
    possible=[(upper.bit_count(),upper,lower)
              for lower, up in cofaces.items() if len(up)==1 for upper in up]
    if not possible:return None
    _,upper,lower=min(possible)
    return (lower,upper)


def make_certificate():
    P=enumerate_matchings(); answer=[]
    for length in range(4):
        for deleted in combinations(range(18),length):
            removed=set(deleted)
            remain=[p for p in P if removed.isdisjoint(p)]
            faces=nerve_faces(remain);pairs=[]
            while True:
                pair=next_pair(faces)
                if pair is None:break
                lo,hi=pair
                pairs.append([lo,hi]);faces.remove(lo);faces.remove(hi)
            answer.append({'deleted':list(deleted),'pairs':pairs,'residue':sorted(faces)})
    return {'format':'elementary-nerve-collapse-v1','edge_order':'outer-0:5,spoke-6:11,inner-12:17',
            'cases':answer}


def graph_data(faces):
    if not faces:return ('void',None,None)
    assert all(mask.bit_count()<=2 for mask in faces)
    verts={x for x in faces if x.bit_count()==1}
    edges={x for x in faces if x.bit_count()==2}
    assert len(verts)>0
    assert all((x&-x) in verts and (x^(x&-x)) in verts for x in edges)
    parent={x:x for x in verts}
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    for e in edges:
        first=e&-e;second=e^first
        parent[root(first)]=root(second)
    comp=len({root(v) for v in verts})
    loops=len(edges)-len(verts)+comp
    return ('graph',comp,loops)


def original_euler(matchings):
    # Independent evaluation from graph-edge subsets, NOT from the nerve.
    faces=set()
    for p in matchings:
        for k in range(1,len(p)+1):
            for s in combinations(p,k):
                faces.add(sum(1<<v for v in s))
    return sum((-1)**(mask.bit_count()-1) for mask in faces)-1


def verify(data):
    assert data['format']=='elementary-nerve-collapse-v1'
    P=enumerate_matchings()
    assert P==independent_matchings() and len(P)==10
    assert len(data['cases'])==988
    hist=Counter(); preserved=Counter(); total_pairs=0; size_counts=Counter()
    case_iter=iter(data['cases'])
    for length in range(4):
        for deleted in combinations(range(18),length):
            case=next(case_iter)
            assert case['deleted']==list(deleted)
            remaining=[p for p in P if set(deleted).isdisjoint(p)]
            faces=nerve_faces(remaining)
            size_counts[length]+=1
            for low,high in case['pairs']:
                assert low in faces and high in faces
                assert low.bit_count()+1==high.bit_count()
                assert low & high == low
                # Strict elementary collapse: exactly one total proper coface.
                assert [f for f in faces if f!=low and (low&f)==low] == [high]
                faces.remove(low);faces.remove(high)
                total_pairs+=1
            assert sorted(faces)==case['residue']
            # The certificate must finish at dimension at most one.
            sig,components,loops=graph_data(faces)
            if sig=='void':
                assert len(remaining)==0
                hist[length,'void']+=1
            else:
                assert components==1
                # Independent direct-Euler check of the ORIGINAL complex.
                assert original_euler(remaining)==-loops
                hist[length,loops]+=1
                if length == 1:
                    e = deleted[0]
                    assert loops == (1 if e < 6 else 2 if e < 12 else 0)
                if loops==3:preserved['three_loops']+=1
                if length==3 and loops==3:
                    assert deleted in ((0,2,4),(1,3,5))
                if length==3 and sig=='void':raise AssertionError
            # Full face-family closure is checked for every generated nerve.
            assert all((face^(1<<j)) in nerve_faces(remaining)
                       for face in nerve_faces(remaining)
                       for j in range(face.bit_length())
                       if face.bit_count()>=2 and face>>j&1)
    assert next(case_iter,None) is None
    expected={
        (0,0):1,
        (1,0):6,(1,1):6,(1,2):6,
        (2,0):78,(2,1):63,(2,2):12,
        (3,'void'):20,(3,0):662,(3,1):132,(3,3):2}
    assert dict(hist)==expected, (hist,expected)
    assert size_counts=={0:1,1:18,2:153,3:816}
    print('Perfect matchings: 10; exhaustive independent enumeration: PASS')
    print('Nerve/face closure and elementary collapses: PASS')
    print('All original-complex Euler cross-checks: PASS')
    print('Cases: 988; elementary collapses:',total_pairs)
    for length in range(4):
        print('fault count',length,':',sorted(((str(k[1]),v) for k,v in hist.items() if k[0]==length)))


if __name__=='__main__':
    path=Path(__file__).with_name('CERTIFICATE.json')
    verify(json.loads(path.read_text(encoding='utf-8')))
