#!/usr/bin/env python3
"""Exact finite chain-level and discrete-Morse checks for an octagonal bipyramid.
Run: python3 verify.py certificate.json
Only Python 3 standard library is needed. No external source files are needed.
"""
import json,sys
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations

N=8
ORDER=[18,11,4,6,5,10,0,3,9,2,20,21,12,22,15,7,16,17,8,1,13,19,14,23]

def edge_list():
    ed=[(i,(i+1)%N) for i in range(N)]
    ed += [(i,N) for i in range(N)]
    ed += [(i,N+1) for i in range(N)]
    return [sorted(p) for p in ed]

def simplices(ed):
    by_size=defaultdict(list)
    def visit(start,occupied,face,k):
        by_size[k].append(face)
        for j in range(start,len(ed)):
            a,b=ed[j]
            if not (occupied & (1<<a | 1<<b)):
                visit(j+1,occupied | (1<<a) | (1<<b),face | (1<<j),k+1)
    visit(0,0,0,0)
    return by_size

def boundary_rank_mod2(by_size):
    out={}
    for k in sorted(by_size):
        if k==0:continue
        lower={face:i for i,face in enumerate(by_size[k-1])}
        basis={}
        for face in by_size[k]:
            col=0
            x=face
            while x:
                bit=x&-x;x^=bit
                col ^= 1 << lower[face^bit]
            while col:
                pivot=col.bit_length()-1
                if pivot in basis:col ^= basis[pivot]
                else:
                    basis[pivot]=col
                    break
        out[k]=len(basis)
    return out

def sign(top,fac):
    assert top.bit_count()==fac.bit_count()+1 and (top&fac)==fac
    missing=top^fac
    return -1 if (top & (missing-1)).bit_count()%2 else 1

def build():
    ed=edge_list()
    by_size=simplices(ed)
    available=set(f for layer in by_size.values() for f in layer)
    initial=available.copy()
    pairs=[]
    for v in ORDER:
        bit=1<<v
        lower=[f for f in sorted(available) if not f&bit and f|bit in available]
        for f in lower:
            assert f in available and f|bit in available
            available.remove(f)
            available.remove(f|bit)
            pairs.append([f,f|bit])
    critical=sorted(available)
    assert len(initial)==951 and len(pairs)==468 and len(critical)==15
    assert Counter(f.bit_count()-1 for f in critical)=={2:4,3:11}
    # An independent check of all the Hasse incidences and the reversed graph.
    lower={a:b for a,b in pairs}
    upper={b:a for a,b in pairs}
    assert len(set(lower)|set(upper))==2*len(pairs)
    graph={face:[] for face in initial}
    indeg={face:0 for face in initial}
    for face in initial:
        z=face
        while z:
            bit=z&-z;z^=bit
            facet=face^bit
            assert facet in initial
            if lower.get(facet)==face:
                start,end=facet,face
            else:
                start,end=face,facet
            graph[start].append(end)
            indeg[end]+=1
    queue=[f for f in initial if indeg[f]==0]
    done=0
    for f in queue:
        done+=1
        for g in graph[f]:
            indeg[g]-=1
            if indeg[g]==0:queue.append(g)
    assert done==len(initial), 'directed Hasse cycle detected'
    crit=set(critical)
    @lru_cache(None)
    def project(f):
        if f in crit:return {f:1}
        if f in upper:return {}
        top=lower[f]
        coeff=sign(top,f)
        acc={}
        z=top
        while z:
            bit=z&-z;z^=bit
            facet=top^bit
            if facet==f:continue
            for c,m in project(facet).items():
                acc[c]=acc.get(c,0)-coeff*sign(top,facet)*m
        return {c:m for c,m in acc.items() if m}
    low=sorted(f for f in critical if f.bit_count()==3)
    high=sorted(f for f in critical if f.bit_count()==4)
    morse=[]
    for l in low:
        row=[]
        for h in high:
            acc=0
            z=h
            while z:
                bit=z&-z;z^=bit
                facet=h^bit
                acc+=sign(h,facet)*project(facet).get(l,0)
            row.append(acc)
        morse.append(row)
    assert len(morse)==4 and all(len(r)==11 for r in morse)
    # Explicit integer rank-2 certificate: row1=row2,
    # row0+row1+row3=0, and a unit 2x2 minor.
    assert morse[1]==morse[2]
    assert all(morse[0][i]+morse[1][i]+morse[3][i]==0 for i in range(11))
    determinant=morse[0][1]*morse[3][5]-morse[0][5]*morse[3][1]
    assert abs(determinant)==1
    # Independent simplicial mod-two Betti calculation.
    ranks=boundary_rank_mod2(by_size)
    betti={k-1:len(by_size[k])-ranks.get(k,0)-ranks.get(k+1,0)
           for k in by_size if k>0}
    assert betti=={0:0,1:0,2:2,3:9,4:0}
    return {
        'n':N,'edge_list':ed,'face_vector':[len(by_size[k]) for k in range(1,6)],
        'all_face_count':len(initial), 'order':ORDER, 'pairs':pairs,
        'critical':critical,'critical_dims':{'2':4,'3':11},
        'acyclic_hasse_vertices':done,
        'lower_boundaries':morse,
        'mod2_ranks':{str(k):v for k,v in ranks.items()},
    },determinant,betti

def main():
    if len(sys.argv)!=2:
        raise SystemExit('usage: python3 verify.py certificate.json')
    with open(sys.argv[1],encoding='utf-8') as f:expected=json.load(f)
    observed,det,betti=build()
    assert sorted(map(tuple,observed.pop('pairs'))) == sorted(map(tuple,expected.pop('pairs'))), 'matching pairs differ'
    assert observed==expected, 'reconstructed certificate disagrees with stored certificate'
    observed['pairs_count']=468
    print('OCTAGONAL_BIPYRAMID_MATCHING_MORSE_OK')
    print('simplicial face vector (dimensions 0..4):',observed['face_vector'])
    print('all faces including empty:',observed['all_face_count'])
    print('acyclic directed Hasse vertices:',observed['acyclic_hasse_vertices'])
    print('matched facet pairs:',observed['pairs_count'])
    print('critical face dimensions:',observed['critical_dims'])
    print('integral Morse boundary (4 rows x 11 columns):',observed['lower_boundaries'])
    print('rank = 2; primitive 2x2 minor determinant:',det)
    print('reduced mod-2 Betti numbers:',betti)
    print('integral homotopy model: wedge of 2 S^2 and 9 S^3')

if __name__=='__main__':main()
