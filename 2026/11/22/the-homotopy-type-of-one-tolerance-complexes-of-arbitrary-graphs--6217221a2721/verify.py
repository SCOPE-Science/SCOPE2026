#!/usr/bin/env python3
"""Finite validation of the tolerance-one graph homotopy classification.
Run: python verify.py
Only finite checks; the arbitrary-order theorem follows from the proof.
"""
from itertools import combinations
from collections import deque


def components_and_order(n, edges):
    neighbors=[set() for _ in range(n)]
    for a,b in edges: neighbors[a].add(b);neighbors[b].add(a)
    roots=[]; parent={}; seen=set(); components=[]
    for start in range(n):
        if start in seen: continue
        seen.add(start); roots.append(start)
        comp=[start]; queue=deque([start])
        while queue:
            v=queue.popleft()
            for w in sorted(neighbors[v]):
                if w not in seen:
                    seen.add(w);parent[w]=v;comp.append(w);queue.append(w)
        components.append(comp)
    # Roots first, then non-roots in breadth-first parent-before-child order.
    order=roots + [v for comp in components for v in comp[1:]]
    return roots,parent,order,neighbors


def case(n, edges, do_acyclic=False):
    edges={tuple(sorted(e)) for e in edges}
    roots,parent,order,neighbors=components_and_order(n,edges)
    idx={v:i for i,v in enumerate(order)}
    c=len(roots); root0=roots[0]
    verts={(v,) for v in range(n)}
    e_all={tuple(sorted(e)) for e in combinations(range(n),2)}
    t_all={t for t in combinations(range(n),3)
           if any(e in edges for e in combinations(t,2))}
    faces=verts|e_all|t_all
    pairs=[]
    # Vertex-to-edge pairs, including contraction of the root graph to a star.
    for v in order:
        if v==root0: continue
        a=parent[v] if v in parent else root0
        pairs.append(((v,),tuple(sorted((a,v)))))
    # Edge-to-triangle pairs. The maximal endpoint always decreases along a V-path.
    for u,v in e_all:
        small,large=sorted((u,v),key=lambda z:idx[z])
        if large in parent and parent[large]!=small:
            tri=tuple(sorted((small,large,parent[large])))
            pairs.append(((u,v),tri))
    paired=[a for pr in pairs for a in pr]
    assert len(paired)==len(set(paired)), (n,edges,'duplicate matched cell')
    assert all(set(lo)<set(hi) and len(hi)==len(lo)+1 and hi in faces
               for lo,hi in pairs)
    critical=faces-set(paired)
    critbydim=[sum(len(face)==d+1 for face in critical) for d in (0,1,2)]
    expected1=(c-1)*(c-2)//2
    expected2=len(t_all)-(n*(n-1)//2 - (n-c) - c*(c-1)//2)
    assert critbydim==[1,expected1,expected2], (n,edges,critbydim)
    # Full directed Hasse graph: unmatched covers down; matched covers up.
    if do_acyclic:
        pairset=set(pairs); dig={f:[] for f in faces}; indeg={f:0 for f in faces}
        for upper in e_all|t_all:
            for lower in combinations(upper,len(upper)-1):
                lo,hi=tuple(lower),upper
                src,dst=(lo,hi) if (lo,hi) in pairset else (hi,lo)
                dig[src].append(dst);indeg[dst]+=1
        q=deque([f for f in faces if indeg[f]==0]); processed=0
        while q:
            f=q.popleft();processed+=1
            for g in dig[f]:
                indeg[g]-=1
                if indeg[g]==0:q.append(g)
        assert processed==len(faces), (n,edges,'gradient cycle')
    return len(faces),len(pairs),tuple(critbydim),len(t_all)


def rank_f2(columns):
    piv={}
    for x in columns:
        while x:
            b=x.bit_length()-1
            if b not in piv:
                piv[b]=x;break
            x^=piv[b]
    return len(piv)


def homology_check(n,edges):
    edges=set(edges)
    pairs=list(combinations(range(n),2)); ids={e:i for i,e in enumerate(pairs)}
    triangles=[t for t in combinations(range(n),3)
               if any(e in edges for e in combinations(t,2))]
    boundary=[sum(1<<ids[e] for e in combinations(t,2)) for t in triangles]
    r=rank_f2(boundary)
    roots,_,_,_=components_and_order(n,edges); c=len(roots)
    exp1=(c-1)*(c-2)//2
    exp2=len(triangles)-len(pairs)+(n-c)+c*(c-1)//2
    assert (len(pairs)-n+1-r,len(triangles)-r)==(exp1,exp2), (n,edges)


def main():
    total=0;faces=0;pairs=0
    for n in range(2,7):
        full=list(combinations(range(n),2))
        for mask in range(1<<len(full)):
            E={e for j,e in enumerate(full) if (mask>>j)&1}
            f,p,cr,t=case(n,E,do_acyclic=(n<=5))
            homology_check(n,E)
            total+=1;faces+=f;pairs+=p
        print('All simple labelled graphs on',n,'vertices:',1<<len(full),'passed Morse counts and mod-two ranks')
    samples=[]
    for n in range(7,13):
        samples.append(('cycle'+str(n),n,{tuple(sorted((i,(i+1)%n))) for i in range(n)}))
        samples.append(('path'+str(n),n,{(i,i+1) for i in range(n-1)}))
        samples.append(('star'+str(n),n,{(0,i) for i in range(1,n)}))
    for name,n,E in samples:
        _,_,cr,_=case(n,E,do_acyclic=True)
        homology_check(n,E)
        if n in (7,9,11): print(name, 'critical_0_1_2',cr)
    print('PASS: exact face matching, full Hasse acyclicity for all n<=5 and sample n<=12')
    print('PASS: mod-two Betti ranks for all',total,'graphs n<=6, and all cycle/path/star samples')
    print('Scientific scope: finite tests do not prove arbitrary n or the attaching-map statement')

if __name__=='__main__':main()
