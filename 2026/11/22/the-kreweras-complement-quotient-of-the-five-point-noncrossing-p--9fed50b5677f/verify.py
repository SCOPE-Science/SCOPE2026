#!/usr/bin/env python3
"""Exact cell-orbit and homotopy verification for a five-label Kreweras quotient.

Uses only the Python standard library. All cells, actions and relations are
reconstructed from the definition; no precomputed boundary matrices are read.
"""
import collections
import itertools
import json
from pathlib import Path

N = 5

def partitions(elements):
    if not elements:
        yield ()
        return
    a = min(elements)
    for p in partitions(elements - {a}):
        yield tuple(sorted(((a,),) + p))
        for i, block in enumerate(p):
            yield tuple(sorted(p[:i] + (tuple(sorted((a,) + block)),) + p[i+1:]))

def noncrossing(p):
    lookup = {x: i for i, block in enumerate(p) for x in block}
    for a,b,c,d in itertools.combinations(range(N),4):
        if lookup[a] == lookup[c] and lookup[b] == lookup[d] and lookup[a] != lookup[b]:
            return False
    return True

def refines(p,q):
    return all(any(set(b).issubset(c) for c in q) for b in p)

def complement(p):
    w = {a:b for block in p for a,b in zip(block, block[1:] + block[:1])}
    iw = {v:k for k,v in w.items()}
    # w^{-1}c with c(x)=x+1 modulo five.
    m = {a:iw[(a+1)%N] for a in range(N)}
    unseen=set(range(N)); blocks=[]
    while unseen:
        start=min(unseen); a=start; block=[]
        while a in unseen:
            unseen.remove(a); block.append(a); a=m[a]
        assert a == start
        blocks.append(tuple(sorted(block)))
    return tuple(sorted(blocks))

def inverse(word):
    return [-v for v in word[::-1]]

def reduce_word(word):
    out=[]
    for v in word:
        if out and out[-1]==-v: out.pop()
        else: out.append(v)
    return out

def data():
    pp=sorted((p for p in partitions(set(range(N))) if noncrossing(p) and 1<len(p)<N), key=str)
    assert len(pp)==40
    rank=[N-len(p) for p in pp]
    index={p:i for i,p in enumerate(pp)}
    kperm=tuple(index[complement(p)] for p in pp)
    assert set(kperm)==set(range(40))
    assert all(rank[kperm[i]] == 4-rank[i] for i in range(40))
    assert all(kperm[kperm[i]] == index[tuple(sorted(tuple(sorted((x-1)%N for x in b)) for b in pp[i]))] for i in range(40))
    assert all(next((j for j in range(1,11) if iterate(kperm,i,j)==i),None) in (5,10,2) for i in range(40))
    assert any(iterate(kperm,i,5)==i for i in range(40))
    # Original order complex, ranks 1,2,3.
    faces={1:{(i,) for i in range(40)},2:set(),3:set()}
    for i,j in itertools.combinations(range(40),2):
        f=tuple(sorted((i,j),key=lambda a:rank[a]))
        if rank[f[0]] != rank[f[1]] and refines(pp[f[0]],pp[f[1]]):
            faces[2].add(f)
    for f in itertools.combinations(range(40),3):
        f=tuple(sorted(f,key=lambda a:rank[a]))
        if tuple(rank[a] for a in f)!=(1,2,3): continue
        if refines(pp[f[0]],pp[f[1]]) and refines(pp[f[1]],pp[f[2]]):
            faces[3].add(f)
    assert tuple(map(lambda j: len(faces[j]),(1,2,3)))==(40,150,125)
    assert all(tuple(sorted((kperm[i] for i in f),key=lambda i:rank[i])) in faces[len(f)]
               for fs in faces.values() for f in fs)
    original=set().union(*faces.values())
    # The barycentric subdivision is the order complex of the nonempty-face poset.
    flags={1:{(f,) for f in original},2:set(),3:set()}
    for a in original:
        for b in original:
            if len(a)<len(b) and set(a).issubset(b):
                flags[2].add((a,b))
    for a,b in flags[2]:
        if len(a)!=1 or len(b)!=2: continue
        for c in faces[3]:
            if set(b).issubset(c): flags[3].add((a,b,c))
    assert (len(flags[1]),len(flags[2]),len(flags[3])) == (315,1050,750)
    def ka(f):return tuple(sorted((kperm[i] for i in f),key=lambda i:rank[i]))
    def kflag(t):return tuple(ka(f) for f in t)
    def orbit_rep(t):
        all_images=[];s=t
        for _ in range(10):
            all_images.append(s);s=kflag(s)
        assert s==t
        return min(all_images)
    orbit={dim:sorted({orbit_rep(t) for t in flags[dim]}) for dim in (1,2,3)}
    assert (len(orbit[1]),len(orbit[2]),len(orbit[3])) == (36,110,75)
    loc={dim:{t:i for i,t in enumerate(orbit[dim])} for dim in (1,2,3)}
    edges={i:tuple(loc[1][orbit_rep((face,))] for face in e)
           for i,e in enumerate(orbit[2])}
    triangles={i:tuple(loc[2][orbit_rep(tuple(t[j] for j in range(3) if j!=k))]
                 for k in range(3)) for i,t in enumerate(orbit[3])}
    for t,(e12,e02,e01) in triangles.items():
        a,b=edges[e01];c,d=edges[e12];e,f=edges[e02]
        assert b==c and a==e and d==f, (t,(e12,e02,e01))
    return pp, kperm, faces, flags, orbit, edges, triangles

def iterate(p, i, n):
    for _ in range(n):i=p[i]
    return i

def spanning_tree(edges, vertex_count):
    parent=list(range(vertex_count))
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    selected=[]
    for e,(a,b) in edges.items():
        a=find(a);b=find(b)
        if a!=b:
            parent[a]=b;selected.append(e)
    assert len(selected)==vertex_count-1
    return selected

def relations(triangles, tree):
    excluded=set(tree)
    return {i: reduce_word([v for v in (edge[2]+1,edge[0]+1,-edge[1]-1)
                            if abs(v)-1 not in excluded]) for i,edge in triangles.items()}

def cancel(relations_dict, live, ops):
    relators={k:v[:] for k,v in relations_dict.items()}; live=set(live)
    for ti,ei in ops:
        assert ti in relators and ei in live
        w=relators.pop(ti)
        where=[i for i,v in enumerate(w) if abs(v)==ei+1]
        assert len(where)==1, (ti,ei,w)
        i=where[0];rest=w[i+1:]+w[:i]
        replacement=inverse(rest) if w[i]>0 else rest
        live.remove(ei)
        for key,word in list(relators.items()):
            revised=[]
            for v in word:
                if v==ei+1: revised.extend(replacement)
                elif v==-ei-1: revised.extend(inverse(replacement))
                else:revised.append(v)
            relators[key]=reduce_word(revised)
    return relators,live

def discover(rel,live):
    result=[]
    while True:
        choices=[]
        for t,w in rel.items():
            cnt=collections.Counter(map(abs,w))
            for v in w:
                if cnt[abs(v)]==1:choices.append((len(w),t,abs(v)-1))
        if not choices:break
        _,t,e=min(choices)
        result.append((t,e))
        rel,live=cancel(rel,live,[(t,e)])
    return result,rel,live

def main():
    pp,kperm,faces,flags,orbit,edges,triangles=data()
    tree=spanning_tree(edges,len(orbit[1])); assert len(tree)==35
    initial=relations(triangles,tree)
    available=set(edges)-set(tree)
    ops,rem,live=discover(initial,available)
    assert len(ops)==74 and len(live)==len(rem)==1
    assert sorted(abs(v) for w in rem.values() for v in w)==[next(iter(live))+1]*5
    assert len(next(iter(rem.values())))==5
    assert len(set(next(iter(rem.values()))))==1
    check=Path(__file__).with_name('cancellation_certificate.json')
    cert={'tree_edges':tree, 'two_cell_generator_eliminations':[list(z) for z in ops],
          'final_generator_edge':next(iter(live)),
          'final_relator':next(iter(rem.values())),
          'orbit_cell_counts':[36,110,75]}
    if check.exists():
        recorded=json.loads(check.read_text(encoding='utf8'))
        assert recorded==cert, 'Certificate differs from canonical reconstruction'
        rr,ll=cancel(initial,available,recorded['two_cell_generator_eliminations'])
        assert rr==rem and ll==live
    else:
        print('CERTIFICATE_JSON='+json.dumps(cert,separators=(',',':')))
    print('KREWERAS_NC5_QUOTIENT_MOORE5_OK')
    print('vertices=36 edges=110 triangles=75; tree_edges=35; generator_eliminations=74')
    print('last generator=',next(iter(live))+1,'last relator=',next(iter(rem.values())))

if __name__=='__main__':main()
