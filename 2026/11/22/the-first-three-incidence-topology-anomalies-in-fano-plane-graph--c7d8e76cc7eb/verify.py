"""Exact exhaustive binary homology check for flags deleted from the Fano incidence graph.
All arithmetic is integer; no external packages. Run with Python 3.
"""
from collections import Counter, deque
from itertools import combinations

def incidence():
    lines=[{j,(j+1)%7,(j+3)%7} for j in range(7)]
    edges=tuple((i,7+j) for j in range(7) for i in range(7) if i in lines[j])
    assert len(edges)==21 and len(set(edges))==21
    assert len({tuple(sorted(line)) for line in lines})==7
    assert all(sum(p in line and q in line for line in lines)==1 for p in range(7) for q in range(p+1,7))
    return lines,edges

def components(adj):
    seen=set();components=[]
    for v in range(14):
        if v in seen:continue
        found={v}; seen.add(v); stack=[v]
        while stack:
            for u in adj[stack.pop()]:
                if u not in seen: seen.add(u); found.add(u);stack.append(u)
        components.append(found)
    return components

def two_step_cliques(edges):
    adj=[set() for _ in range(14)]
    for v,w in edges:adj[v].add(w);adj[w].add(v)
    connected=len(components(adj))==1
    # Even disconnected cases are classified as disconnected, not given the graph metric.
    if not connected:return None
    nbr2=[]
    for v in range(14):
        dist={v:0};q=deque([v])
        while q:
            t=q.popleft()
            for w in adj[t]:
                if w not in dist:dist[w]=dist[t]+1;q.append(w)
        assert len(dist)==14
        nbr2.append({w for w in range(14) if w!=v and dist[w]<=2})
    bydim={}
    def visit(simplex, candidates):
        if simplex:bydim.setdefault(len(simplex)-1, []).append(simplex)
        for pos,v in enumerate(candidates):
            nxt=[w for w in candidates[pos+1:] if w in nbr2[v]]
            visit(simplex+(v,),nxt)
    visit((),list(range(14)))
    for j in bydim:bydim[j].sort()
    return bydim

def rank_mod2(columns):
    basis={}
    for vec in columns:
        while vec:
            pivot=vec.bit_length()-1
            if pivot in basis:vec^=basis[pivot]
            else:basis[pivot]=vec;break
    return len(basis)

def reduced_bettis(bydim):
    ranks={0:1} # Reduced augmentation from 0-chains to (-1)-chains.
    for d in range(1,max(bydim)+1):
        lower={face:i for i,face in enumerate(bydim[d-1])}
        columns=[]
        for face in bydim[d]:
            v=0
            for i in range(len(face)):
                v^=1<<lower[face[:i]+face[i+1:]]
            columns.append(v)
        ranks[d]=rank_mod2(columns)
    return {d:len(bydim[d])-ranks[d]-ranks.get(d+1,0) for d in bydim}

def expected_rank(deleted,lines):
    if len(deleted)<3:return 8-len(deleted)
    ps=[i for i,j in deleted];ls=[j for i,j in deleted]
    disjoint=(len(set(ps))==3 and len(set(ls))==3 and all(
        i not in lines[j-7] for i,l in deleted for p,j in deleted if (i,l)!=(p,j)))
    if not disjoint:return 5
    collinear=any(set(ps)==line for line in lines)
    concurrent=any(all(p in lines[j-7] for j in ls) for p in range(7))
    return 5+int(collinear)+int(concurrent)

def run():
    lines,edges=incidence(); totals={}; classifications={}
    for t in range(4):
        classes=Counter();disconnected=0
        for deleted in combinations(edges,t):
            remaining=set(edges)-set(deleted)
            complex_=two_step_cliques(remaining)
            if complex_ is None:
                disconnected+=1;continue
            b=reduced_bettis(complex_)
            k=expected_rank(deleted,lines)
            assert b.get(2,0)==k,(deleted,b,k)
            assert all(x==0 for d,x in b.items() if d!=2),(deleted,b)
            classes[k]+=1
        totals[t]={'connected':sum(classes.values()),'disconnected':disconnected,'ranks':dict(sorted(classes.items()))}
    assert totals=={
        0:{'connected':1,'disconnected':0,'ranks':{8:1}},
        1:{'connected':21,'disconnected':0,'ranks':{7:21}},
        2:{'connected':210,'disconnected':0,'ranks':{6:210}},
        3:{'connected':1316,'disconnected':14,'ranks':{5:1232,6:56,7:28}}
    },totals
    print('PASS: exhaustive Fano incidence graph edge deletion t=0,1,2,3')
    for t,v in totals.items():print('deletions',t,v)
    print('PASS: all connected cases have mod-2 reduced homology only in degree 2')
    print('PASS: induced matching & collinearity/concurrency formula')
if __name__=='__main__':run()
