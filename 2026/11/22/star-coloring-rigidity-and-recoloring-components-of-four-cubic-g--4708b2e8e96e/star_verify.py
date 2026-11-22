"""Independent self-contained enumerator of optimal star colorings and their single-vertex recoloring graphs."""
from itertools import combinations,permutations
from collections import Counter,deque

def graph(name):
    if name=='Heawood':
        n=14
        e={(i,7+(i+d)%7) for i in range(7) for d in (0,1,3)}
    elif name=='Mobius-Kantor':
        n=16;e=set()
        for i in range(8):
            e|={tuple(sorted((i,(i+1)%8))), (i,i+8),tuple(sorted((i+8,8+(i+3)%8)))}
    elif name=='Pappus':
        n=18;e=set()
        for x in range(3):
          for y in range(3):
            p=3*x+y
            e|={(p,9+x),(p,12+y),(p,15+(x+y)%3)}
    elif name=='Desargues':
        a=[v for v in range(32) if v.bit_count()==2]
        b=[v for v in range(32) if v.bit_count()==3]
        n=20;e={(i,10+j) for i,x in enumerate(a) for j,y in enumerate(b) if x&y==x}
    else: raise ValueError(name)
    assert len(e)==3*n//2
    return n,e

def canonical_colorings(n,ed,k):
    nbr=[set() for _ in range(n)]
    for a,b in ed:nbr[a].add(b);nbr[b].add(a)
    # Directly enumerate all ordered P4s from the graph, including chordless and chorded paths.
    paths=set()
    for b in range(n):
      for a,c in permutations(nbr[b],2):
        for d in nbr[c]-{a,b}:
            if len({a,b,c,d})==4:
              p=(a,b,c,d)
              paths.add(min(p,p[::-1]))
    latest=[[] for _ in range(n)]
    for p in paths:latest[max(p)].append(p)
    col=[-1]*n;answer=[]
    def rec(i,used):
      if i==n:
        if used==k:answer.append(tuple(col))
        return
      for v in range(min(used+1,k)):
        if any(col[w]==v for w in nbr[i] if w<i):continue
        col[i]=v
        if all(not (col[a]==col[c] and col[b]==col[d]) for a,b,c,d in latest[i]):
          rec(i+1,max(used,v+1))
      col[i]=-1
    rec(0,0)
    return answer

def component_shape(q,adj):
    d={v:len(adj[v]) for v in q}
    m=len(q);edges=sum(d.values())//2
    if m==1 and edges==0:return 'K1'
    if m==2 and edges==1:return 'K2'
    if m==3 and edges==2 and sorted(d.values())==[1,1,2]:return 'P3'
    if m==4 and edges==4 and all(x==2 for x in d.values()):return 'C4'
    if m==8 and edges==12 and all(x==3 for x in d.values()):
        side={q[0]:0};z=deque([q[0]])
        while z:
            v=z.popleft()
            for w in adj[v]:
                if w not in side:side[w]=1-side[v];z.append(w)
                else:assert side[w]!=side[v]
        assert Counter(side.values())==Counter({0:4,1:4})
        # A three-regular bipartite graph with four vertices per side
        # is K_{4,4} minus a perfect matching, hence Q3.
        return 'Q3'
    if m==9 and edges==12 and Counter(d.values())==Counter({2:4,3:4,4:1}):
        center=next(v for v in q if d[v]==4)
        assert all(d[x]==3 for x in adj[center])
        rim=set(q)-{center}
        assert all(sum(w in rim for w in adj[v])==2 for v in rim)
        assert all(d[v]!=d[w] for v in rim for w in adj[v] if w in rim)
        seen={next(iter(rim))};z=deque(seen)
        while z:
            v=z.popleft()
            for w in adj[v]:
                if w in rim and w not in seen:seen.add(w);z.append(w)
        assert len(seen)==8
        # The rim is an eight-cycle alternating boundary-edge and corner
        # vertices, with four boundary-edge vertices joined to center.
        return 'P3xP3'
    raise AssertionError(('unrecognized component',m,edges,sorted(d.values())))

def component_profile(partitions,n):
    palette=tuple(range(4))
    colors=set(tuple(p[v] for v in c) for c in partitions for p in permutations(palette))
    adj={c:[] for c in colors}
    for c in colors:
        for i in range(n):
            for k in palette:
                if k!=c[i]:
                    t=c[:i]+(k,)+c[i+1:]
                    if t in colors: adj[c].append(t)
    remain=set(colors);shapes=Counter()
    edgecount=sum(map(len,adj.values()))//2
    while remain:
        start=next(iter(remain));q=[start];remain.remove(start)
        for u in q:
            for v in adj[u]:
                if v in remain:
                    remain.remove(v);q.append(v)
        shapes[component_shape(q,adj)]+=1
    return len(colors),edgecount,shapes

if __name__=='__main__':
    expected={'Heawood':(112,2688,4032,{'Q3':336}),'Mobius-Kantor':(223,5352,1920,{'K1':2280,'K2':1152,'C4':192}),'Pappus':(365,8760,4320,{'K1':3072,'K2':1296,'P3':648,'Q3':144}),'Desargues':(850,20400,15840,{'K1':7200,'K2':1440,'Q3':480,'P3xP3':720})}
    for name in expected:
        n,e=graph(name)
        assert not canonical_colorings(n,e,3)
        partitions=canonical_colorings(n,e,4)
        N,E,shapes=component_profile(partitions,n)
        assert (len(partitions),N,E,dict(shapes))==expected[name],(name,len(partitions),N,E,shapes)
        print(name, 'vertices',n,'partitions',len(partitions),'named',N,'edges',E,'components',dict(shapes))
    print('PASS')
