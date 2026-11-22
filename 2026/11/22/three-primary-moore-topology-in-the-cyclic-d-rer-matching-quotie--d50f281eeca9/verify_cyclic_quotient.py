"""Standalone exact verification of the cyclic graph-matching quotient's homology and pi1.

Run: python3 verify_durer_quotient.py certificate.json
Uses Python standard library only. Rebuilds all quotient cells and boundary operators.
"""
import collections
import itertools
import json
import math
import sys


def run(path):
    cert = json.load(open(path, encoding='utf-8'))
    n = 6
    edges = set()
    for i in range(n):
        for a, b in [(('u', i), ('u', (i+1)%n)),
                     (('u', i), ('v', i)),
                     (('v', i), ('v', (i+2)%n))]:
            edges.add(tuple(sorted((a,b))))
    edges = tuple(sorted(edges))
    edge_to_id = {e:i for i,e in enumerate(edges)}
    assert len(edges)==18
    # The six index rotations form the specified cyclic subgroup of D6.
    permutations = []
    for s in (1,):
        for r in range(n):
            p=[]
            for a,b in edges:
                aa=(a[0],(s*a[1]+r)%n)
                bb=(b[0],(s*b[1]+r)%n)
                p.append(edge_to_id[tuple(sorted((aa,bb)))])
            assert sorted(p)==list(range(18))
            permutations.append(p)
    assert len({tuple(p) for p in permutations})==6
    def is_matching(mask):
        taken=set()
        for j,(a,b) in enumerate(edges):
            if mask>>j&1:
                if a in taken or b in taken: return False
                taken.update((a,b))
        return True
    faces=[m for m in range(1,1<<18) if is_matching(m)]
    face_set=set(faces)
    assert collections.Counter(m.bit_count()-1 for m in faces)=={0:18,1:117,2:334,3:402,4:156,5:10}
    transforms=[]
    for p in permutations:
        transforms.append({m:sum(1<<p[j] for j in range(18) if m>>j&1) for m in faces})
    canonical={}
    def canon(chain):
        if chain not in canonical:
            canonical[chain]=min(tuple(t[m] for m in chain) for t in transforms)
        return canonical[chain]
    def chains_ending(m):
        yield (m,)
        sub=(m-1)&m
        while sub:
            if sub in face_set:
                for chain in chains_ending(sub):
                    yield chain+(m,)
            sub=(sub-1)&m
    # Geometric simplices of barycentric subdivision are chains of nonempty
    # faces. Strictly increasing ranks prevent inversions under the action.
    index={};cells=[];degree=[]
    total=0
    for mask in faces:
        for chain in chains_ending(mask):
            total+=1
            c=canon(chain)
            if c not in index:
                index[c]=len(cells)
                cells.append(c)
                degree.append(len(c)-1)
    assert total==166087
    assert len(cells)==27703
    assert collections.Counter(degree)=={0:180,1:2205,2:7550,3:10448,4:6120,5:1200}
    bd=[]
    co=[[] for _ in cells]
    for g,chain in enumerate(cells):
        terms=[]
        if len(chain)>1:
            for j in range(len(chain)):
                f=index[canon(chain[:j]+chain[j+1:])]
                terms.append((f,(-1)**j))
                co[f].append(g)
            assert len({f for f,a in terms})==len(terms)
        bd.append(terms)
    active=set(range(len(cells)))
    # A free face has exactly one active codimension-one coface. Every pair
    # is explicitly checked against the regenerated geometric incidences.
    for f,g in cert['simplicial_collapse_pairs']:
        assert f in active and g in active
        assert degree[g]==degree[f]+1
        assert [h for h in co[f] if h in active]==[g]
        assert sum(1 for h,a in bd[g] if h==f)==1
        active.remove(f);active.remove(g)
    assert len(cert['simplicial_collapse_pairs'])==12488
    assert collections.Counter(degree[i] for i in active)=={0:94,1:673,2:1268,3:692}
    reduced={i:collections.defaultdict(int) for i in active}
    for g in active:
        for f,a in bd[g]:
            if f in active:reduced[g][f]+=a
        reduced[g]={f:a for f,a in reduced[g].items() if a}
    def chain_zero():
        for g in active:
            out=collections.defaultdict(int)
            for f,a in reduced[g].items():
                for k,b in reduced[f].items():out[k]+=a*b
            assert not any(out.values())
    chain_zero()
    # Integral unit-pivot chain contractions, retaining exact coefficients.
    for f,g,a in cert['integral_unit_pivots']:
        assert f in active and g in active
        d=degree[g]
        assert degree[f]==d-1 and reduced[g].get(f)==a and abs(a)==1
        for h in list(active):
            if h==g or degree[h]!=d:continue
            coefficient=reduced[h].pop(f,0)
            if coefficient:
                for k,v in reduced[g].items():
                    if k==f:continue
                    value=reduced[h].get(k,0)-coefficient*v*a
                    if value:reduced[h][k]=value
                    else:reduced[h].pop(k,None)
        for h in active:
            if degree[h]==d+1:reduced[h].pop(g,None)
        active.remove(f);active.remove(g)
    assert len(cert['integral_unit_pivots'])==1360
    assert collections.Counter(degree[i] for i in active)=={0:1,2:1,3:5}
    bottom=[i for i in active if degree[i]==2]
    top=[i for i in active if degree[i]==3]
    assert len(bottom)==1
    assert sorted(reduced[i].get(bottom[0],0) for i in top)==[0,0,0,0,3]
    assert all(not reduced[i] for i in active if degree[i]!=3)
    # The cell-cancellation certificate above proves integral cellular
    # homology. Independently prove pi_1=1 using the two-skeleton of the
    # already geometrically collapsed quotient (NOT algebraic cancellations).
    remaining=set(range(len(cells)))
    for f,g in cert['simplicial_collapse_pairs']:
        remaining.discard(f);remaining.discard(g)
    verts={i for i in remaining if degree[i]==0}
    segs={i for i in remaining if degree[i]==1}
    tris={i for i in remaining if degree[i]==2}
    def ends(e):
        assert len(bd[e])==2
        return (next(f for f,a in bd[e] if a==-1),
                next(f for f,a in bd[e] if a==1))
    tree=set(cert['presentation_tree_edges'])
    assert tree <= segs and len(tree)==len(verts)-1
    parent={v:v for v in verts}
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for e in tree:
        a,b=ends(e)
        ra,rb=find(a),find(b)
        assert ra!=rb
        parent[ra]=rb
    assert len({find(v) for v in verts})==1
    gens=segs-tree
    def reduce_word(w):
        stack=[]
        for x in w:
            if stack and stack[-1]==-x:stack.pop()
            else:stack.append(x)
        while len(stack)>1 and stack[0]==-stack[-1]:
            stack.pop();stack.pop(0)
        return tuple(stack)
    relators=[]
    for t in sorted(tris):
        assert [a for e,a in bd[t]]==[1,-1,1]
        # Ordered boundary circuit: edge(0,1), edge(1,2), edge(0,2)^-1.
        e0,e1,e2=[e for e,a in bd[t]]
        r=[e2,e0,-e1]
        relators.append(reduce_word(x for x in r if abs(x) in gens))
    seen=set()
    for g,sol0 in cert['presentation_eliminations']:
        sol=tuple(sol0)
        assert g in gens and g not in seen
        match=None
        for j,r in enumerate(relators):
            for k,x in enumerate(r):
                if abs(x)!=g or sum(abs(z)==g for z in r)!=1:continue
                rem=r[k+1:]+r[:k]
                expression=tuple(-z for z in reversed(rem))
                if x<0:expression=tuple(-z for z in reversed(expression))
                if expression==sol:
                    match=j;break
            if match is not None:break
        assert match is not None,(g,sol)
        seen.add(g)
        new=[]
        for j,r in enumerate(relators):
            if j==match:continue
            word=[]
            for x in r:
                if x==g:word.extend(sol)
                elif x==-g:word.extend(-z for z in reversed(sol))
                else:word.append(x)
            new.append(reduce_word(word))
        relators=new
    assert len(seen)==len(gens)==580
    assert all(not r for r in relators)
    print('DURER_CYCLIC_MATCHING_QUOTIENT_MOORE_THREE_TORSION_OK')
    print('cells=27703 flags=166087 elementary_collapses=12488 integer_pivots=1360 pi1_eliminations=580')

if __name__=='__main__':
    assert len(sys.argv)==2,'Usage: python verify_durer_quotient.py certificate.json'
    run(sys.argv[1])
