"""Independent finite check of doubling of connected sums of joins of two cycles."""
from itertools import combinations
from collections import defaultdict, deque

def join_cycles(m,n):
    V=[('a',i) for i in range(m)]+[('b',j) for j in range(n)]
    ea=[frozenset((('a',i),('a',(i+1)%m))) for i in range(m)]
    eb=[frozenset((('b',j),('b',(j+1)%n))) for j in range(n)]
    faces=set(frozenset(a|b) for a in ea for b in eb)
    return V,faces

def dbl(facets):
    vertices=set(); edges=set()
    for f in facets:
        assert len(f)==4
        for a,b in combinations(f,2):vertices.add(frozenset((a,b)))
        for e in combinations(f,2):
            e=frozenset(e);t=f-e
            edges.add(frozenset((e,t)))
    return vertices,edges

def comps(vertices,edges):
    adj={v:set() for v in vertices}
    for e in edges:
        a,b=tuple(e);adj[a].add(b);adj[b].add(a)
    cs=[];todo=set(vertices)
    while todo:
        cur={todo.pop()}; stack=list(cur)
        for v in stack:
            for w in adj[v]:
                if w in todo:todo.remove(w);cur.add(w);stack.append(w)
        cs.append((len(cur),sum(len(adj[v]) for v in cur)//2))
    return sorted([(v,e,e-v+1) for v,e in cs])

def connected_sum(m,n,perm):
    V,F=join_cycles(m,n)
    x=[('a',0),('a',1),('b',0),('b',1)]
    assert frozenset(x) in F
    maps=[]
    for copy in (0,1):
      mapping={v:('u',copy)+v for v in V}
      for i,v in enumerate(x):mapping[v]=('port',perm[i] if copy else i)
      maps.append(mapping)
    result={frozenset(maps[i][v] for v in f) for i in (0,1) for f in F if f!=frozenset(x)}
    vs,es=dbl(result)
    return len(result),len(vs),len(es),comps(vs,es)
if __name__=='__main__':
    V,F=join_cycles(4,5)
    v,e=dbl(F)
    print('X base:',len(F),len(v),len(e),comps(v,e))
    for p in [(0,1,2,3),(0,2,1,3),(1,0,2,3),(2,3,0,1)]:
        print('permutation',p,'connected_sum',connected_sum(4,5,p))
    print('parameter_sweep:')
    cases=0
    for m in range(4,9):
      for n in range(4,9):
        if m%2==0 and n%2==0:continue
        _,f=join_cycles(m,n)
        v,e=dbl(f)
        assert len(v)==m+n+m*n
        assert len(e)==3*m*n
        assert comps(v,e)==sorted([(m+n,m*n,(m-1)*(n-1)),(m*n,2*m*n,m*n+1)])
        nfac,nv,ne,c=connected_sum(m,n,(0,1,2,3))
        assert (nfac,nv,ne)==(2*m*n-2,2*(m+n+m*n)-6,6*m*n-6)
        assert c==sorted([(2*(m+n)-2,2*m*n-2,2*m*n-2*m-2*n+1), (2*m*n-4,4*m*n-4,2*m*n+1)])
        nfac,nv,ne,c=connected_sum(m,n,(0,2,1,3))
        assert c==[(2*(m+n+m*n)-6,6*m*n-6,4*m*n-2*m-2*n+1)]
        cases+=1
    print('PASS',cases,'parameter pairs; both facet identification types')
