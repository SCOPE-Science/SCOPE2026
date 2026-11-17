"""Independent exhaustive incidence check for triple-tuplings of three polygon joins."""
from itertools import combinations, product
from collections import defaultdict, deque


def calc(a,b,c):
    sizes=(a,b,c)
    offsets=(0,a,a+b)
    cyclic_edges=[]
    for z,off in zip(sizes,offsets):
        cyclic_edges.append([frozenset((off+i,off+(i+1)%z)) for i in range(z)])
    # The facets are the unions of one edge from each polygon.
    facets=[frozenset.union(*t) for t in product(*cyclic_edges)]
    vertices=set()
    actual=set()
    for F in facets:
        triangles=[frozenset(x) for x in combinations(sorted(F),3)]
        vertices.update(triangles)
        for T in triangles:
            S=F-T
            actual.add(frozenset((T,S)))
    # Independent graph recognition: a triangle can occupy (1,1,1)
    # or (2,1,0); a union is a six-face precisely when each polygon
    # receives a pair of consecutive vertices.
    def occupancy(T):
        return tuple(sum(o<=v<o+s for v in T) for o,s in zip(offsets,sizes))
    classes=defaultdict(set)
    for T in vertices:
        o=occupancy(T)
        if o==(1,1,1): name='tensor'
        else:
            assert sorted(o)==[0,1,2]
            name='single-'+str(o.index(1))
        classes[name].add(T)
    # Independent adjacency from categorical graph products only.
    # Do NOT inspect facet unions or use their six-face membership test.
    predicted=set()
    for key,group in classes.items():
        for T,S in combinations(group,2):
            ct=occupancy(T);cs=occupancy(S)
            if key=='tensor':
                pairs=[frozenset((next(v for v in T if o<=v<o+z),
                                  next(v for v in S if o<=v<o+z)))
                       for o,z in zip(offsets,sizes)]
                good=all(pair in cyc for pair,cyc in zip(pairs,cyclic_edges))
            else:
                i=int(key[-1]);o=offsets[i];z=sizes[i]
                complementary=all((ct[j],cs[j]) in ((0,2),(2,0))
                                  for j in range(3) if j!=i)
                pair=frozenset((next(v for v in T if o<=v<o+z),
                                next(v for v in S if o<=v<o+z)))
                good=(ct[i]==cs[i]==1 and complementary and pair in cyclic_edges[i])
            if good: predicted.add(frozenset((T,S)))
    assert actual==predicted, (a,b,c,len(actual),len(predicted))
    adj={T:set() for T in vertices}
    for pair in actual:
        T,S=tuple(pair)
        adj[T].add(S);adj[S].add(T)
    groups=[]
    unvisited=set(vertices)
    while unvisited:
        root=next(iter(unvisited));q=[root];unvisited.remove(root);component={root}
        for T in q:
            for S in adj[T]:
                if S in unvisited:
                    unvisited.remove(S);q.append(S);component.add(S)
        groups.append(component)
    b_even=sum(1 for z in sizes if z%2==0)
    count0=2**max(b_even-1,0)
    expected_counts={'tensor':count0}
    for i,z in enumerate(sizes):expected_counts['single-'+str(i)]=1+(z%2==0)
    bytype=defaultdict(list)
    for group in groups:
        types={next(k for k,st in classes.items() if T in st) for T in group}
        assert len(types)==1,types
        ty=next(iter(types))
        local_v=len(group)
        local_e=sum(len(adj[t]) for t in group)//2
        bytype[ty].append((local_v,local_e,local_e-local_v+1))
    assert {k:len(v) for k,v in bytype.items()}==expected_counts
    for ty,count in expected_counts.items():
        if ty=='tensor':rank=3*a*b*c//count+1
        else:
            i=int(ty[-1]);z=sizes[i];others=sum(sizes[j] for j in range(3) if j!=i)
            rank=(2*a*b*c-z*others)//count+1
        assert all(row[-1]==rank for row in bytype[ty]),(ty,rank,bytype[ty])
    v=a*b*c+2*(a*b+a*c+b*c)
    e=10*a*b*c
    ncomp=count0+3+b_even
    rank=e-v+ncomp
    assert len(vertices)==v and len(actual)==e
    assert len(groups)==ncomp and sum(x[2] for xs in bytype.values() for x in xs)==rank
    return (a,b,c,v,e,ncomp,rank,{k:sorted(t) for k,t in sorted(bytype.items())})

if __name__=='__main__':
    tests=[(4,4,4),(4,4,5),(4,5,5),(5,5,5),(4,5,6),(5,6,7),(6,6,7),(5,7,7)]
    for x in tests:
        print('PARAM',x,'RESULT',calc(*x))
    print('POLYGON_TRIPLE_TUPLING_COMPLETE_GRAPH_CHECK_PASS')
