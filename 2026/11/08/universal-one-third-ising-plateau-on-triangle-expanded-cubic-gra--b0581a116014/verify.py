#!/usr/bin/env python3
"""Exact finite certificates for triangle-expanded cubic Ising graphs.

Uses only the Python standard library. A general analytic proof is in RESULT.md.
No finite computation is used to infer the universal theorem.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations


def expansion(base_edges):
    nodes=sorted(set(x for e in base_edges for x in e))
    assert all(sum(u in e for e in base_edges)==3 for u in nodes)
    sites=sorted((u,v) for u in nodes for v in nodes if (min(u,v),max(u,v)) in base_edges)
    assert len(sites)==3*len(nodes)
    index={x:i for i,x in enumerate(sites)}
    triangles=[tuple(sorted((index[(u,v)],index[(u,w)])))
               for u in nodes
               for v,w in combinations([x for x in nodes if x!=u and
                      (min(u,x),max(u,x)) in base_edges],2)]
    reversals=[tuple(sorted((index[(u,v)],index[(v,u)]))) for u,v in base_edges]
    assert len(triangles)==3*len(nodes) and len(reversals)*2==3*len(nodes)
    assert len(set(triangles+reversals))==len(triangles+reversals)
    return sites,triangles,reversals


def energy_terms(mask,triangle_edges,matching_edges,count):
    # A selected bit is a negative spin; M is the total spin (not a spin-half quantity).
    triangle_sum=sum(1 if (mask>>a&1)==(mask>>b&1) else -1 for a,b in triangle_edges)
    matching_sum=sum(1 if (mask>>a&1)==(mask>>b&1) else -1 for a,b in matching_edges)
    return triangle_sum,matching_sum,count-2*mask.bit_count()


def enumerate_states(edges):
    nodes,tri,cross=expansion(edges)
    N=len(nodes)
    n=N//3
    tri_neighbors=[[] for _ in range(N)]
    cross_neighbors=[[] for _ in range(N)]
    for a,b in tri:
        tri_neighbors[a].append(b);tri_neighbors[b].append(a)
    for a,b in cross:
        cross_neighbors[a].append(b);cross_neighbors[b].append(a)
    spins=[1]*N
    t,b,m=len(tri),len(cross),N
    by_terms=Counter({(t,b,m):1})
    for step in range(1,1<<N):
        flip=(step & -step).bit_length()-1
        old=spins[flip]
        t-=2*old*sum(spins[v] for v in tri_neighbors[flip])
        b-=2*old*sum(spins[v] for v in cross_neighbors[flip])
        m-=2*old
        spins[flip]=-old
        by_terms[(t,b,m)]+=1
    return by_terms,tri,cross


def lower_energy(n,j,k,h):
    a=abs(h)
    if a<=k:return -n*j-(3*n//2)*k
    if a<=k+2*j:return -n*j-(n//2)*k-n*a
    return 3*n*j+(3*n//2)*k-3*n*a


def verify_general_examples():
    graphs={
       'tetrahedron_K4': [(u,v) for u in range(4) for v in range(u+1,4)],
       'bipartite_K33': [(u,v) for u in range(3) for v in range(3,6)],
       'triangular_prism': [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)],
    }
    for name,edges in graphs.items():
        counter,_,_=enumerate_states(edges)
        n=len(set(u for pair in edges for u in pair))
        assert sum(counter.values())==2**(3*n)
        for j,k in [(1,2),(3,1),(2,5)]:
            fields=[0, k-0.5, k, k+j, k+2*j, k+2*j+0.5]
            for h in fields:
                got=min(j*a+k*b-h*m for (a,b,m) in counter)
                want=lower_energy(n,j,k,h)
                assert got==want,(name,j,k,h,got,want)
        print('UNIVERSAL_EXAMPLE_OK',name,'base_vertices',n,'states',sum(counter.values()))


# Independent 12-vertex adjacency, using conventional consecutive labels.
# The 12 triangular edges are inferred from graph three-cycles, NOT from arc labels.
STANDARD_EDGES=[(0,1),(0,2),(0,9),(1,2),(1,6),(2,3),
 (3,4),(3,11),(4,5),(4,11),(5,6),(5,7),
 (6,7),(7,8),(8,9),(8,10),(9,10),(10,11)]


def standard_graph_bond_types():
    es={tuple(sorted(e)) for e in STANDARD_EDGES}
    assert len(es)==18
    triangle_edges=set()
    for a,b,c in combinations(range(12),3):
        e1=tuple(sorted((a,b)));e2=tuple(sorted((a,c)));e3=tuple(sorted((b,c)))
        if all(e in es for e in (e1,e2,e3)):
            triangle_edges.update((e1,e2,e3))
    outer=es-triangle_edges
    assert len(triangle_edges)==12 and len(outer)==6
    assert len({v for edge in outer for v in edge})==12
    return sorted(triangle_edges),sorted(outer)


def components(states):
    allowed=set(states)
    unseen=set(states)
    sizes=[]
    degrees=Counter()
    for mask in allowed:
        degrees[sum((mask^(1<<i)) in allowed for i in range(12))]+=1
    while unseen:
        start=unseen.pop(); stack=[start];size=0
        while stack:
            v=stack.pop();size+=1
            for i in range(12):
                w=v^(1<<i)
                if w in unseen:
                    unseen.remove(w);stack.append(w)
        sizes.append(size)
    return sorted(sizes,reverse=True),degrees


def verify_tetrahedron():
    tri,cross=standard_graph_bond_types()
    census=defaultdict(Counter)
    configurations=[]
    for mask in range(4096):
        t,b,m=energy_terms(mask,tri,cross,12)
        census[(t,b)][m]+=1
        configurations.append((mask,t,b,m))
    def ground(j,k,h):
        emin=min(j*t+k*b-h*m for _,t,b,m in configurations)
        masks=[mask for mask,t,b,m in configurations if j*t+k*b-h*m==emin]
        return emin,masks
    for j,k in [(1,1),(2,5),(3,2)]:
        critical_fields={0:24,k:114,k+j:30,k+2*j:163,k+3*j:1}
        for h,num in critical_fields.items():
            e,ss=ground(j,k,h)
            assert e==lower_energy(4,j,k,h),(j,k,h,e)
            assert len(ss)==num,(j,k,h,len(ss),num)
        e,ss=ground(j,k,k)
        assert Counter(12-2*m.bit_count() for m in ss)=={0:24,2:60,4:30}
        e,ss=ground(j,k,k+2*j)
        assert Counter(m.bit_count() for m in ss)=={0:1,1:12,2:48,3:72,4:30}
    j=k=1
    for h,expected_size,expected_degree,expected_edges in [
        (0,[1]*24,{0:24},0),
        (1,[114],{3:24,4:90},216),
        (2,[1]*30,{0:30},0),
        (3,[163],{3:4,4:54,5:36,6:32,7:24,9:12,12:1},444),
        (4,[1],{0:1},0),
    ]:
        _,ss=ground(j,k,h)
        sizes,deg=components(ss)
        assert sizes==expected_size,(h,sizes)
        assert deg==expected_degree,(h,deg)
        assert sum(a*b for a,b in deg.items())//2==expected_edges
    print('TETRAHEDRON_EXACT_OK', 'critical_114_163', 'flip_components_1_1')

if __name__=='__main__':
    verify_general_examples()
    verify_tetrahedron()
    print('ALL_EXACT_CHECKS_OK')
