import networkx as nx, time,functools, collections, hashlib

def canonical(G):
    blocks=list(nx.biconnected_components(G))
    vblocks=[[] for _ in G]
    bn=[]
    for j,comp in enumerate(blocks):
        for v in comp: vblocks[v].append(j)
        if len(comp)==2: bn.append(tuple(comp))
        else:
            # cyclic order on a cycle block
            s=min(comp); neighbors=[v for v in G.neighbors(s) if v in comp]
            assert len(neighbors)==2,(len(comp),len(neighbors))
            path=[s,neighbors[0]]
            while len(path)<len(comp):
                t=[v for v in G.neighbors(path[-1]) if v in comp and v!=path[-2]]
                assert len(t)==1,t
                path.append(t[0])
            bn.append(tuple(path))
    @functools.cache
    def vform(v,parent):
        return '('+''.join(sorted(bform(b,v) for b in vblocks[v] if b!=parent))+')'
    @functools.cache
    def bform(b,v):
        vs=bn[b]
        if len(vs)==2:return 'E'+vform(next(w for w in vs if w!=v),b)
        p=vs.index(v)
        n=len(vs)
        a=''.join(vform(vs[(p+i)%n],b) for i in range(1,n))
        c=''.join(vform(vs[(p-i)%n],b) for i in range(1,n))
        return 'C'+str(n)+'['+min(a,c)+']'
    return min(vform(v,-1) for v in G)

def exact_colors(graphs):
    cols=[[0]*len(g) for g in graphs]
    ns=[[tuple(g.neighbors(v)) for v in g] for g in graphs]
    nc=1
    for t in range(50):
        lookup={}
        nextcols=[]
        for c,adj in zip(cols,ns):
            seq=[]
            for v,row in enumerate(adj):
                sig=(c[v],tuple(sorted(c[w] for w in row)))
                if sig not in lookup:lookup[sig]=len(lookup)
                seq.append(lookup[sig])
            nextcols.append(seq)
        if len(lookup)==nc:
            return [tuple(sorted(c)) for c in nextcols],t+1
        cols=nextcols;nc=len(lookup)
    raise AssertionError('global refinement did not stabilize')

graphs={1:[nx.empty_graph(1)]}
for n in range(2,13):
    tic=time.monotonic()
    seen={}
    checked=0
    for k in range(1,n):
        m=n-k+1
        for g in graphs[k]:
            for x in g:
                h=g.copy();h.add_nodes_from(range(k,n))
                for y in range(k,n-1):h.add_edge(y,y+1)
                h.add_edge(x,k)
                if m>=3:h.add_edge(n-1,x)
                checked+=1
                c=canonical(h)
                if c not in seen:seen[c]=h
    gs=list(seen.values()); graphs[n]=gs
    expected=[0,1,1,2,4,9,23,63,188,596,1979,6804,24118]
    assert len(gs)==expected[n],(n,len(gs),expected[n])
    signatures,rounds=exact_colors(gs)
    q=collections.defaultdict(list)
    for g,k in zip(gs,signatures):q[k].append(g)
    mult=[v for v in q.values() if len(v)>1]
    if mult:
        for members in mult:
            assert len(members)==2 and not nx.is_isomorphic(members[0],members[1])
            assert all(nx.is_connected(g) and all(len(c)==2 or g.subgraph(c).number_of_edges()==len(c) for c in nx.biconnected_components(g)) for g in members)
            print('PAIR',[(nx.to_graph6_bytes(g,header=False).decode().strip(), sorted(dict(g.degree()).values())) for g in members])
            for g in members:print('BLOCKS',sorted(len(b) for b in nx.biconnected_components(g)),'EDGES',g.number_of_edges())
        assert n==12 and len(mult)==2 and all(len(v)==2 for v in mult)
    print('n',n,'unlabeled',len(gs),'candidates',checked,'CR_excess',sum(len(z)-1 for z in mult),'multi',len(mult),'max',max(map(len,mult),default=1),'rounds',rounds,'secs',round(time.monotonic()-tic,2),flush=True)

assert len(graphs[12])==24118
print('CENSUS_VERIFIED 24118 TWO_COLLISION_PAIRS')
