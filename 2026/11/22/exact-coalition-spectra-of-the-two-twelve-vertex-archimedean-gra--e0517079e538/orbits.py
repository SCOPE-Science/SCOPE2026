import itertools,collections, pathlib, json
W=pathlib.Path(__file__).resolve().parent
def construct(mode):
    if mode==0:
        vertices=[(x,x^(1<<k)) for x in range(8) for k in range(3) if not x&(1<<k)]
        vertices=[tuple(sorted(e)) for e in vertices]
        aut=[]
        for swap in itertools.permutations(range(3)):
          for flip in range(8):
            def vmap(x):
                return flip^sum((((x>>j)&1)<<swap[j]) for j in range(3))
            aut.append(tuple(vertices.index(tuple(sorted((vmap(a),vmap(b))))) for a,b in vertices))
    else:
        vertices=[(a,b) for a in range(4) for b in range(4) if a!=b]
        aut=[tuple(vertices.index((p[a],p[b])) for a,b in vertices) for p in itertools.permutations(range(4))]
    return vertices,aut

def action(perm,s):
    return sum(1<<perm[v] for v in range(12) if (s>>v)&1)
def orb_calc(mode):
    vertices,aut=construct(mode)
    fn=W/('opt_cubo.txt' if mode==0 else 'opt_trunc.txt')
    raw=fn.read_text().splitlines()[2:]
    allp={tuple(sorted(map(int,line.split()))) for line in raw};assert len(allp)==(762 if mode==0 else 93)
    orbits=[];left=allp.copy()
    while left:
        seed=min(left)
        orbit={tuple(sorted(action(perm,s) for s in seed)) for perm in aut}
        assert orbit<=allp
        left-=orbit
        ps=tuple(sorted(s.bit_count() for s in seed))
        # partner graph by domination
        neigh=[]
        for i in range(12):
            N=1<<i
            for j in range(12):
                if i==j:continue
                a,b=vertices[i],vertices[j]
                adjacent=(len(set(a)&set(b))>0 if mode==0 else (a[0]==b[0] or a==b[::-1]))
                if adjacent:N|=1<<j
            neigh.append(N)
        def dominating(m):return all(any((m>>j)&1 for j in range(12) if neigh[i]>>j&1) for i in range(12))
        pairs=[(i,j) for i in range(8) for j in range(i+1,8) if dominating(seed[i]|seed[j])]
        deg=sorted([sum(a==i or b==i for a,b in pairs) for i in range(8)])
        tri=sum({(i,j),(i,k),(j,k)} <= set(pairs) for i in range(8) for j in range(i+1,8) for k in range(j+1,8))
        orbits.append(dict(size=len(orbit),profile=list(ps),representative=list(seed),coalition_graph_degrees=deg,coalition_graph_edges=len(pairs),coalition_graph_triangles=tri))
    orbits.sort(key=lambda o:(o['profile'],o['coalition_graph_degrees'],o['size']))
    print('mode',mode,'automorphisms',len(aut),'orbits',len(orbits),'counts',collections.Counter((tuple(o['profile']),o['size']) for o in orbits))
    (W/('orbit_cubo.json' if mode==0 else 'orbit_trunc.json')).write_text(json.dumps(orbits,indent=2))
orb_calc(0)
orb_calc(1)
