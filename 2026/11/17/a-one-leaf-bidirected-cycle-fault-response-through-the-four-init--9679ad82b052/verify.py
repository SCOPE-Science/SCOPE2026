#!/usr/bin/env python3
"""Exact finite checks for bidirected leaf-punctured cyclic multipath complexes."""
from collections import defaultdict
from functools import lru_cache
import json
from pathlib import Path


def arcs(n,leaf=True):
    e=[]
    for i in range(n):
        j=(i+1)%n
        e.extend([(i,j),(j,i)])
    if leaf:e.extend([(n,0),(0,n)])
    return e

def face_mask(mask, edges, count):
    indeg=[0]*count;outdeg=[0]*count; successor=[-1]*count
    for k,(u,v) in enumerate(edges):
        if mask>>k&1:
            indeg[v]+=1;outdeg[u]+=1
            if indeg[v]>1 or outdeg[u]>1:return False
            successor[u]=v
    # union of disjoint directed paths iff no directed cycles
    for v in range(count):
        seen=set();x=v
        while x>=0:
            if x in seen:return False
            seen.add(x);x=successor[x]
    return True

def faces_masks(n,leaf=True):
    E=arcs(n,leaf);count=n+int(leaf)
    return {x for x in range(1,1<<len(E)) if face_mask(x,E,count)}

def independently_valid(mask, edges, count):
    """Second construction: directed paths from their indegree-zero sources."""
    predecessor={};successor={}
    selected=[edges[j] for j in range(len(edges)) if mask & (1<<j)]
    for a,b in selected:
        if a in successor or b in predecessor:return False
        successor[a]=b;predecessor[b]=a
    traced=set()
    for start in range(count):
        if start in predecessor:continue
        at=start
        while at in successor:
            if at in traced:return False
            traced.add(at)
            at=successor[at]
    return len(traced)==len(selected)

def faces_recursive(n,leaf=True):
    E=arcs(n,leaf);count=n+int(leaf)
    faces={0};front=[0]
    while front:
        nextfront=[]
        for f in front:
            for k in range(len(E)):
                if not (f>>k&1):
                    g=f|(1<<k)
                    if g not in faces and independently_valid(g,E,count):
                        faces.add(g);nextfront.append(g)
        front=nextfront
    faces.discard(0);return faces

def lex_match(F,order):
    remaining=set(F);pairs=[]
    for p in order:
        bit=1<<p
        for a in sorted(remaining):
            if a&bit:continue
            b=a|bit
            if b in remaining:
                remaining.remove(a);remaining.remove(b);pairs.append((a,b))
    return pairs,remaining

def acyclic(F,pairs):
    paired=set(pairs);indeg=dict.fromkeys(F,0);adj={a:[] for a in F}
    for b in F:
        for k in range(b.bit_length()):
            if b>>k&1:
                a=b^(1<<k)
                if a==0:continue
                if (a,b) in paired:u,v=a,b
                else:u,v=b,a
                adj[u].append(v);indeg[v]+=1
    q=[a for a,z in indeg.items() if z==0];processed=0
    while q:
        u=q.pop();processed+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return processed==len(F)

def critical_count(remaining):
    C=defaultdict(int)
    for f in remaining:C[f.bit_count()-1]+=1
    return dict(sorted(C.items()))

def boundary(F,pairs,critical):
    # Integral algebraic discrete Morse differential: matched lower cell reduced
    # through its upper mate, with incidence ±1.
    lower_to_upper={a:b for a,b in pairs}
    upper_to_lower={b:a for a,b in pairs}
    def incidence(b,a):
        assert a in F and (a & b)==a and b.bit_count()==a.bit_count()+1
        extra=b^a
        return -1 if ((b & (extra-1)).bit_count()%2) else 1
    @lru_cache(None)
    def reduce(a):
        if a in critical:return {a:1}
        if a in upper_to_lower:return {}
        b=lower_to_upper[a]
        c=incidence(b,a)
        out=defaultdict(int)
        for i in range(b.bit_length()):
            if b>>i&1:
                x=b^(1<<i)
                if not x or x==a:continue
                coeff=-(incidence(b,x)//c)
                for y,w in reduce(x).items():out[y]+=coeff*w
        return {k:v for k,v in out.items() if v}
    diffs={}
    for b in critical:
        if b.bit_count()==1:continue
        total=defaultdict(int)
        for i in range(b.bit_length()):
            if b>>i&1:
                a=b^(1<<i)
                if a==0:continue
                for y,w in reduce(a).items():total[y]+=incidence(b,a)*w
        diffs[b]={a:coeff for a,coeff in total.items() if coeff}
    return diffs

EXPECTED={3:{0:1,1:3},4:{0:1,1:1,2:2},5:{0:1,2:3,3:2},6:{0:1,3:1,4:2}}

def verify():
    cert=json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text(encoding='utf8'))
    findings=[]
    for entry in cert['cases']:
        n=entry['cycle_vertices']
        assert n in EXPECTED
        F=faces_masks(n)
        assert F==faces_recursive(n),('independent enumeration disagreed',n)
        order=entry['pivot_arc_index_order']
        assert sorted(order)==list(range(len(arcs(n))))
        pairs,critical=lex_match(F,order)
        assert critical_count(critical)==EXPECTED[n]
        assert 2*len(pairs)+len(critical)==len(F)
        assert all(a in F and b in F and (a&b)==a and b.bit_count()==a.bit_count()+1 for a,b in pairs)
        assert acyclic(F,pairs),('gradient cycle',n)
        d=boundary(F,pairs,critical)
        assert all(not val for val in d.values()),('nonzero integer Morse attaching degrees',n,d)
        profile=[sum(1 for v in F if v.bit_count()==k) for k in range(1,len(arcs(n))+1)]
        while profile and profile[-1]==0:profile.pop()
        summary={'cycle_vertices':n,'graph_vertices':n+1,'arcs':len(arcs(n)),'face_vector':profile,'nonempty_faces':len(F),'matching_pairs':len(pairs),'critical_by_dimension':{str(k):v for k,v in EXPECTED[n].items()},'integer_morse_differentials_all_zero':True}
        assert summary == {k:v for k,v in entry.items() if k!='pivot_arc_index_order'},('certificate mismatch',n)
        findings.append(summary)
    assert len(findings)==4 and sorted(x['cycle_vertices'] for x in findings)==[3,4,5,6]
    return findings
if __name__=='__main__':
    print(json.dumps({'status':'PASS','findings':verify()},sort_keys=True,indent=2))
