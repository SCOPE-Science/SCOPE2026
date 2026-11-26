#!/usr/bin/env python3
"""Independent standard-library check of the asymmetric finite generalized quadrangle GQ(2,4).
The 27-point Schlaefli double-six model gives lines as its 45 geometric triangles.
"""
import itertools,json,hashlib,collections
from collections import deque

def run():
    six=range(6)
    pts=[('a',i) for i in six]+[('b',i) for i in six]+[('c',i,j) for i,j in itertools.combinations(six,2)]
    m=len(pts);assert m==27
    def meet(x,y):
        if x==y:return False
        if x[0]==y[0]:
            if x[0]!='c':return False
            return set(x[1:]).isdisjoint(y[1:])
        if set([x[0],y[0]])==set(['a','b']):return x[1]!=y[1]
        if x[0]=='c':x,y=y,x
        assert x[0] in ('a','b') and y[0]=='c'
        return x[1] in y[1:]
    pg=[{j for j in range(m) if meet(pts[i],pts[j])} for i in range(m)]
    assert {len(v) for v in pg}=={10}
    line_sets={tuple(C) for C in itertools.combinations(range(m),3) if all(y in pg[x] for x,y in itertools.combinations(C,2))}
    lines=sorted(line_sets);assert len(lines)==45
    n=m+len(lines)
    thru=[set() for _ in pts]
    adj=[set() for _ in range(n)]
    for j,L in enumerate(lines):
        for x in L:thru[x].add(j);adj[x].add(m+j);adj[m+j].add(x)
    assert {len(x) for x in thru}=={5}
    assert {len(x) for x in adj[:m]}=={5}
    assert {len(x) for x in adj[m:]}=={3}
    for p in range(m):
        for j,L in enumerate(lines):
            if p not in L:assert sum(x in pg[p] for x in L)==1
    def dists(src):
        d=[-1]*n;d[src]=0;q=deque([src])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==-1:d[v]=d[u]+1;q.append(v)
        assert min(d)>=0
        return d
    distances=[dists(i) for i in range(n)]
    assert max(map(max,distances))==4
    mmd={(i,j) for i in range(n) for j in range(i+1,n) if all(distances[w][j]<=distances[i][j] for w in adj[i]) and all(distances[w][i]<=distances[i][j] for w in adj[j])}
    assert mmd=={(i,j) for i in range(n) for j in range(i+1,n) if distances[i][j]==4}
    # An independent direct maximal clique solver, applied to collinearity/concurrence graphs.
    def maximal_cliques(N,edge):
        out=[]
        def visit(R,P,X):
            if not P and not X:out.append(frozenset(R));return
            if P or X:
                pivot=max(P|X,key=lambda v:len(P&edge[v]))
                todo=list(P-edge[pivot])
            else:todo=list(P)
            for v in todo:
                visit(R|{v},P&edge[v],X&edge[v]);P.remove(v);X.add(v)
        visit(set(),set(range(N)),set())
        return out
    point_cliques=maximal_cliques(m,pg)
    pencil_sets={frozenset(thru[i]) for i in range(m)}
    lg=[set() for _ in lines]
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            if set(lines[i])&set(lines[j]):lg[i].add(j);lg[j].add(i)
    line_cliques=maximal_cliques(len(lines),lg)
    assert {frozenset(C) for C in point_cliques}=={frozenset(L) for L in lines}
    assert {frozenset(C) for C in line_cliques}==pencil_sets
    bases=[]
    for j,L in enumerate(lines):
        for i in range(m):
            omit=set(L)|{m+k for k in thru[i]}
            assert len(omit)==8
            assert all(not (a in omit and b in omit) for a,b in mmd)
            bases.append(frozenset(range(n))-omit)
    assert len(bases)==1215 and len(set(bases))==1215
    hist=collections.Counter()
    edges={i:set() for i in range(len(bases))}
    for i in range(len(bases)):
        for j in range(i+1,len(bases)):
            c=len(bases[i]-bases[j]);assert c==len(bases[j]-bases[i])
            hist[c]+=1
            if c<=4:edges[i].add(j);edges[j].add(i)
    assert {len(E) for E in edges.values()}=={54}
    assert sum(map(len,edges.values()))//2==32805
    d={0:0};q=deque([0])
    while q:
        v=q.popleft()
        for w in edges[v]:
            if w not in d:d[w]=d[v]+1;q.append(w)
    assert len(d)==1215 and max(d.values())==3
    # At the threshold s<t, any two distinct line centers may be exchanged,
    # while changing point centers requires collinearity.
    for i in range(len(bases)):
        j,p=divmod(i,m)
        expected={jj*m+p for jj in range(len(lines)) if jj!=j}
        expected|={j*m+pp for pp in pg[p]}
        assert expected==edges[i]
    encoded=';'.join(','.join(map(str,sorted(b))) for b in bases).encode()
    return {'geometry':'GQ(2,4)','points':m,'lines':len(lines),'vertices':n,'strong_metric_dimension':64,'mmd_pairs':len(mmd),'min_bases':len(bases),'threshold_exchange':4,'threshold_degree':54,'threshold_edges':32805,'threshold_diameter':3,'distance_profile_from_first':[sum(a==k for a in d.values()) for k in range(4)],'exchange_cost_histogram':{str(k):v for k,v in sorted(hist.items())},'bases_sha256':hashlib.sha256(encoded).hexdigest()}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,separators=(',',':')))
