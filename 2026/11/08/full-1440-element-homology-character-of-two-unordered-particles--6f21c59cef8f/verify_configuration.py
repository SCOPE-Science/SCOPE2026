#!/usr/bin/env python3
"""Exact finite cellular certificate for two unordered points on the Tutte--Coxeter graph.

No third-party Python packages required. An elementary bound from sixteen
parked-octagon cycles upgrades the modular boundary rank to rational rank.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations


def perfect_matchings(elements):
    if not elements:
        yield ()
        return
    a, *rest = elements
    for b in rest:
        for tail in perfect_matchings([x for x in rest if x != b]):
            yield tuple(sorted(((a, b),) + tail))


def partitions(n, upper=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n, n if upper is None else upper), 0, -1):
            for rest in partitions(n-k, k):
                yield (k,) + rest


def Specht_rim_hooks(shape, length):
    for smaller in partitions(sum(shape) - length):
        if len(smaller) > len(shape) or any(smaller[i] > shape[i] for i in range(len(smaller))):
            continue
        strip = {(i, j) for i, v in enumerate(shape)
                 for j in range(smaller[i] if i < len(smaller) else 0, v)}
        if len(strip) != length:
            continue
        if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)} <= strip for i,j in strip):
            continue
        reached = {next(iter(strip))}
        queue = list(reached)
        while queue:
            i,j = queue.pop()
            for p in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if p in strip and p not in reached:
                    reached.add(p)
                    queue.append(p)
        if len(reached) == len(strip):
            yield smaller, (-1) ** (len({i for i,j in strip}) - 1)


@lru_cache(None)
def specht_character(shape, cycle_type):
    if not cycle_type:
        return int(not shape)
    return sum(s * specht_character(smaller, cycle_type[1:])
               for smaller,s in Specht_rim_hooks(shape, cycle_type[0]))


def rank_mod_sparse(columns, p):
    pivot_rows = {}
    for c in columns:
        v = {j: x % p for j, x in c if x % p}
        while v:
            k = min(v)
            if k not in pivot_rows:
                z = pow(v[k], -1, p)
                pivot_rows[k] = {j: (x*z) % p for j,x in v.items()}
                break
            factor = v[k]
            for j, x in pivot_rows[k].items():
                y = (v.get(j, 0) - factor*x) % p
                if y:
                    v[j] = y
                else:
                    v.pop(j, None)
    return len(pivot_rows)


def cycle_type(permutation):
    unseen = set(range(len(permutation)))
    lengths = []
    while unseen:
        i = min(unseen)
        k = 0
        while i in unseen:
            unseen.remove(i)
            k += 1
            i = permutation[i]
        lengths.append(k)
    return tuple(sorted(lengths, reverse=True))


def main():
    duads = list(combinations(range(6), 2))
    synthemes = sorted(perfect_matchings(list(range(6))))
    assert len(duads) == len(synthemes) == 15
    vertices = [('d', x) for x in duads] + [('s', x) for x in synthemes]
    vertex_index = {v:i for i,v in enumerate(vertices)}
    edges = sorted((vertex_index[('d', pair)], vertex_index[('s', m)])
                   for m in synthemes for pair in m)
    assert len(edges) == 45 and all(a < b for a,b in edges)
    edge_index = {e:i for i,e in enumerate(edges)}
    adj = [set() for _ in range(30)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    assert all(len(x)==3 for x in adj)

    # All unordered pairs of vertices; all edge--vertex cells with disjoint
    # closures; all unordered pairs of edges with disjoint closures.
    cells0 = list(combinations(range(30), 2))
    cells1 = [(e,v) for e,(a,b) in enumerate(edges) for v in range(30) if v not in (a,b)]
    cells2 = [(e,f) for e,f in combinations(range(45), 2)
              if not (set(edges[e]) & set(edges[f]))]
    assert (len(cells0),len(cells1),len(cells2)) == (435,1260,900)
    index0 = {c:i for i,c in enumerate(cells0)}
    index1 = {c:i for i,c in enumerate(cells1)}
    cell2_index = {c:i for i,c in enumerate(cells2)}
    d2 = []
    for e,f in cells2:
        a,b = edges[e]; c,d = edges[f]
        d2.append(((index1[(f,b)],1),(index1[(f,a)],-1),
                   (index1[(e,d)],-1),(index1[(e,c)],1)))
    for col in d2:
        boundary = Counter()
        for j,s in col:
            e,v = cells1[j]
            a,b = edges[e]
            boundary[index0[tuple(sorted((b,v)))]] += s
            boundary[index0[tuple(sorted((a,v)))]] -= s
        assert all(v==0 for v in boundary.values())

    # Connectivity of the one-skeleton: rank(d1) = 434 over every field.
    link = [[] for _ in cells0]
    for e,v in cells1:
        a,b = edges[e]
        i = index0[tuple(sorted((a,v)))]; j = index0[tuple(sorted((b,v)))]
        link[i].append(j);link[j].append(i)
    seen={0}; todo=[0]
    while todo:
        for j in link[todo.pop()]:
            if j not in seen:seen.add(j);todo.append(j)
    assert len(seen)==435

    # The rank-810 certificate over two odd fields and a check over F2.
    ranks={p:rank_mod_sparse(d2,p) for p in (2,3,5)}
    assert ranks=={2:809,3:810,5:810}, ranks

    # Ninety octagons; sixteen independent mod-two octagon classes generate
    # H1 of the 30-vertex, 45-edge graph.  Park the second point at any
    # vertex outside an octagon to lift its cycle to two-point homology.
    cycles=set()
    for start in range(30):
        def search(path):
            if len(path)==8:
                if start in adj[path[-1]]:
                    normal=tuple(path)
                    reverse=(start,)+tuple(reversed(path[1:]))
                    cycles.add(min(normal,reverse))
                return
            for w in adj[path[-1]]:
                if w>start and w not in path:search(path+[w])
        search([start])
    assert len(cycles)==90
    pivots={};chosen=[]
    for seq in sorted(cycles):
        bits=0
        for a,b in zip(seq,seq[1:]+(seq[0],)):
            bits ^= 1 << edge_index[tuple(sorted((a,b)))]
        v=bits
        while v:
            k=v.bit_length()-1
            if k not in pivots:
                pivots[k]=v
                chosen.append(seq)
                break
            v ^= pivots[k]
    assert len(chosen)==16
    # Since rank H1(graph) is E-V+1=16, these octagons form a basis.
    # Thus b1(UConf2) >=16 and rank_Q(d2)<=810.  The mod-3 lower
    # bound gives rank_Q(d2)=810, hence (b1,b2)=(16,90).

    def natural_action(p):
        result=[]
        for side,ob in vertices:
            if side=='d':
                new=('d',tuple(sorted(p[x] for x in ob)))
            else:
                new=('s',tuple(sorted(tuple(sorted(p[x] for x in pair)) for pair in ob)))
            result.append(vertex_index[new])
        return tuple(result)

    S6 = list(permutations(range(6)))
    preserving = [natural_action(p) for p in S6]
    assert len(set(preserving))==720
    preserving_set=set(preserving)
    preserving_index={h:i for i,h in enumerate(preserving)}
    # A color-swapping involution, with vertices ordered as the above duads
    # followed by the lexicographically ordered synthemes.
    dual = (15,22,20,28,24,27,25,19,23,16,26,18,21,29,17,
            0,9,14,11,7,2,12,1,8,4,6,10,5,3,13)
    assert all(dual[dual[i]]==i for i in range(30))
    swapping=[tuple(dual[x] for x in h) for h in preserving]
    group=preserving+swapping
    assert len(set(group))==1440

    def edge_action(h):
        action=[]
        for a,b in edges:
            x,y=h[a],h[b]
            if x<y: action.append((edge_index[(x,y)],1))
            else: action.append((edge_index[(y,x)],-1))
        return action

    # Complete equivariance check of both cellular boundaries under all
    # 1440 generated graph automorphisms.
    representatives={}
    value_counts=Counter()
    for h in group:
        ea=edge_action(h)
        assert all(tuple(sorted((h[a],h[b]))) in edge_index for a,b in edges)
        for k,(e,f) in enumerate(cells2):
            i,si=ea[e];j,sj=ea[f]
            if i<j: target=(i,j);sigma=si*sj
            else: target=(j,i);sigma=-si*sj
            transformed=Counter()
            for u,coeff in d2[k]:
                edge,vertex=cells1[u]
                ee,sgn=ea[edge]
                transformed[index1[(ee,h[vertex])]]+=coeff*sgn
            image_cell_index=cell2_index.get(target)
            assert image_cell_index is not None
            expected=Counter()
            for u,coeff in d2[image_cell_index]:expected[u]+=sigma*coeff
            assert transformed==expected

        t0=sum(tuple(sorted((h[a],h[b])))==(a,b) for a,b in cells0)
        t1=sum(sign for e,v in cells1
               for ee,sign in (ea[e],) if ee==e and h[v]==v)
        t2=0
        for e,f in cells2:
            i,si=ea[e];j,sj=ea[f]
            if (i,j)==(e,f):t2+=si*sj
            elif (i,j)==(f,e):t2-=si*sj
        tgraph=1-sum(h[i]==i for i in range(30)) + sum(s for e,(ee,s) in enumerate(ea) if e==ee)
        h2=t0-t1+t2-1+tgraph
        value_counts[h2]+=1
        if h in preserving_set:
            typ=cycle_type(S6[preserving_index[h]])
            if typ in representatives:assert representatives[typ]==h2
            representatives[typ]=h2
            if typ==(1,)*6:assert (t0,t1,t2,tgraph,h2)==(435,1260,900,16,90)
        else:
            assert h2==0
    assert value_counts=={90:1,-6:75,2:180,0:1184}, value_counts
    assert len(representatives)==11
    assert representatives=={
        (1,1,1,1,1,1):90,(2,1,1,1,1):-6,(2,2,1,1):-6,(2,2,2):-6,
        (3,1,1,1):0,(3,2,1):0,(3,3):0,(4,1,1):2,(4,2):2,
        (5,1):0,(6,):0},representatives
    class_sizes=Counter(cycle_type(p) for p in S6)
    decomposition={}
    for shape in partitions(6):
        numerator=sum(class_sizes[t]*representatives[t]*specht_character(shape,t)
                      for t in class_sizes)
        assert numerator%720==0
        mult=numerator//720
        assert mult>=0
        if mult:decomposition[shape]=mult
    assert decomposition=={(4,1,1):2,(3,2,1):2,(3,1,1,1):2,(2,2,1,1):2}
    assert sum(value_counts[t]*t for t in value_counts)==0
    print('TUTTE_COXETER_TWO_POINT_CHARACTER_PASS')
    print('graph_vertices=30 graph_edges=45 cells=(435,1260,900)')
    print('boundary_ranks_mod_2_3_5=809,810,810 graph_octagon_basis=16')
    print('rational_h1=16 integral_h2_free_rank=90 automorphisms=1440')
    print('character_value_counts=90:1,-6:75,2:180,0:1184')
    print('S6_Specht_shapes_411_321_3111_2211_each_multiplicity_2')
    print('every_color_swapping_automorphism_h2_trace_zero=True')
    print('full_group_h2_invariant_dimension=0')


if __name__=='__main__':
    main()
