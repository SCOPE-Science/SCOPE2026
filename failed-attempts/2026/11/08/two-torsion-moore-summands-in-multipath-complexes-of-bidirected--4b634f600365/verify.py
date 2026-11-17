"""Exact finite verification of multipath complexes of bidirected K_{2,n}, n=4,5.

Requires Python 3 standard library only. All assertions are mathematical checks.
"""
from itertools import combinations
from collections import defaultdict, deque
from functools import lru_cache

ORDERS = {
    4: [4, 6, 15, 2, 3, 12, 8, 9, 5, 10, 1, 13, 0, 14, 11, 7],
    5: [10, 18, 3, 12, 13, 15, 2, 11, 6, 0, 19, 16, 1, 5, 7, 17, 9, 14, 8, 4],
}
EXPECTED = {
    4: ((16, 80, 144, 72), {0: 1, 2: 8, 3: 1}, {0: 0, 1: 0, 2: 8, 3: 1}, {0: 0, 1: 0, 2: 7, 3: 0}),
    5: ((20, 130, 320, 240), {0: 1, 2: 1, 3: 32}, {0: 0, 1: 0, 2: 1, 3: 32}, {0: 0, 1: 0, 2: 0, 3: 31}),
}


def make_arcs(n):
    return [(u, v) for u in range(n+2) for v in range(n+2)
            if (u < 2) != (v < 2)]


def valid_by_components(ids, arcs, n):
    indeg = [0]*(n+2)
    outdeg = [0]*(n+2)
    outgoing = {}
    for j in ids:
        u,v = arcs[j]
        indeg[v] += 1
        outdeg[u] += 1
        if indeg[v] > 1 or outdeg[u] > 1:
            return False
        outgoing[u] = v
    # A finite directed graph of indegree/outdegree at most one is a
    # disjoint union of paths iff there is no directed cycle.
    for source in outgoing:
        observed = set()
        vertex = source
        while vertex in outgoing:
            if vertex in observed:
                return False
            observed.add(vertex)
            vertex = outgoing[vertex]
    return True


def valid_by_reachability(mask, arcs, n):
    indeg = [0]*(n+2)
    outdeg = [0]*(n+2)
    selected = []
    for j,(u,v) in enumerate(arcs):
        if mask>>j & 1:
            selected.append((u,v))
            indeg[v] += 1
            outdeg[u] += 1
    if max(indeg) > 1 or max(outdeg) > 1:
        return False
    # Independent directed graph reachability check: a directed cycle
    # exists iff some vertex reaches itself by a positive-length path.
    reach = [[False]*(n+2) for _ in range(n+2)]
    for u,v in selected:reach[u][v] = True
    for k in range(n+2):
        for i in range(n+2):
            if reach[i][k]:
                for j in range(n+2):
                    if reach[k][j]:reach[i][j] = True
    return not any(reach[i][i] for i in range(n+2))


def complete_complex(n, arcs):
    # Source A: enumerate every subset with at most four arcs. This is
    # exhaustive because the two vertices on the short side contribute
    # at most two outgoing and two incoming arcs altogether.
    faces_a = set()
    for k in range(5):
        for inds in combinations(range(len(arcs)),k):
            if valid_by_components(inds,arcs,n):
                faces_a.add(sum(1<<j for j in inds))
    # Source B: independent monotone breadth-first generation and a
    # reachability-based predicate, without using source A's face list.
    faces_b = {0}
    frontier = {0}
    while frontier:
        nxt = set()
        for mask in frontier:
            for j in range(len(arcs)):
                bit = 1<<j
                if mask&bit:continue
                other = mask|bit
                if other not in faces_b and valid_by_reachability(other, arcs, n):
                    nxt.add(other)
        faces_b |= nxt
        frontier = nxt
    assert faces_a == faces_b, 'independent construction mismatch'
    return faces_a


def matching(faces, order):
    unmatched = faces-{0}
    pairs = []
    for j in order:
        bit=1<<j
        for x in sorted(unmatched):
            if not x & bit and x|bit in unmatched:
                unmatched.remove(x)
                unmatched.remove(x|bit)
                pairs.append((x,x|bit))
    assert len(set(order)) == len(order)
    assert len({x for p in pairs for x in p}) == 2*len(pairs)
    assert all(u.bit_count() == l.bit_count()+1 and (l&u)==l and l and u in faces for l,u in pairs)
    return pairs,unmatched


def hasse_acyclic(faces,pairs):
    # Reverse the matched Hasse arrows, then topologically sort the
    # ENTIRE directed Hasse graph, including all unmatched incidences.
    matched=set(pairs)
    nodes=faces-{0}
    outgoing={x:[] for x in nodes}
    indeg={x:0 for x in nodes}
    h=0
    for u in nodes:
        x=u
        while x:
            bit=x&-x; x-=bit
            l=u^bit
            if l==0:continue
            h+=1
            src,dst=(l,u) if (l,u) in matched else (u,l)
            outgoing[src].append(dst);indeg[dst]+=1
    queue=deque(x for x in nodes if indeg[x]==0)
    visited=0
    while queue:
        x=queue.popleft(); visited+=1
        for y in outgoing[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert visited==len(nodes),'matching is not globally acyclic'
    return h


def incidence(upper,bit):
    assert upper&bit and bit.bit_count()==1
    return -1 if (upper & (bit-1)).bit_count()%2 else 1


def integral_morse_3_to_2(faces, pairs,crit):
    paired_low={a:b for a,b in pairs}
    paired_upper={b:a for a,b in pairs}
    critical_twos=sorted(x for x in crit if x.bit_count()==3)
    critical_threes=sorted(x for x in crit if x.bit_count()==4)
    idx={x:i for i,x in enumerate(critical_twos)}
    visits=set()
    @lru_cache(None)
    def projection(x):
        assert x.bit_count()==3
        if x in idx:
            return {idx[x]:1}
        if x in paired_upper:
            return {}
        assert x in paired_low, 'unclassified 2-cell'
        if x in visits:raise AssertionError('cyclic reduction')
        visits.add(x)
        u=paired_low[x]
        assert u.bit_count()==4
        p=u^x
        multiplier=incidence(u,p)
        out=defaultdict(int)
        bits=u
        while bits:
            bit=bits & -bits; bits-=bit
            y=u^bit
            if y==x:continue
            sign=-multiplier*incidence(u,bit)
            for j,c in projection(y).items():out[j]+=sign*c
        visits.remove(x)
        return {j:c for j,c in out.items() if c}
    boundary=[]
    for u in sorted(critical_threes):
        row=defaultdict(int)
        bits=u
        while bits:
            bit=bits&-bits;bits-=bit
            for j,c in projection(u^bit).items():row[j]+=incidence(u,bit)*c
        boundary.append(tuple(row.get(j,0) for j in range(len(idx))))
    from math import gcd
    from functools import reduce
    div = reduce(gcd,(abs(c) for row in boundary for c in row),0)
    assert div==2, f'unexpected attaching-degree content {div}'
    return len(boundary),len(idx),div,projection.cache_info().currsize,boundary



def direct_signed_pivot_elimination(faces,pairs,critical):
    # Independently reduce the original 3-to-2 integer boundary matrix,
    # using exact unit-pivot column operations for all 2-to-3 pairs.
    # This algorithm does not use or call the recursive Morse projection.
    three_cells=sorted(x for x in faces if x.bit_count()==4)
    columns={u:{} for u in three_cells}
    for u in three_cells:
        bits=u
        while bits:
            bit=bits&-bits;bits-=bit
            columns[u][u^bit]=incidence(u,bit)
    for lower,upper in pairs:
        if lower.bit_count()!=3:continue
        assert upper in columns
        pivot=columns[upper].get(lower,0)
        assert abs(pivot)==1
        replacement=columns[upper]
        for u in list(columns):
            if u==upper:continue
            c=columns[u].get(lower,0)
            if c:
                for r,value in replacement.items():
                    v=columns[u].get(r,0)-c*value//pivot
                    if v:columns[u][r]=v
                    else:columns[u].pop(r,None)
        del columns[upper]
        assert all(lower not in col for col in columns.values())
    crit2=sorted(x for x in critical if x.bit_count()==3)
    crit3=sorted(x for x in critical if x.bit_count()==4)
    assert set(columns)==set(crit3)
    return [tuple(columns[u].get(r,0) for r in crit2) for u in crit3]


def gf2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in pivots:x ^= pivots[p]
            else:pivots[p]=x; break
    return len(pivots)


def mod2_homology(faces):
    by_dim=defaultdict(list)
    for x in faces-{0}:by_dim[x.bit_count()-1].append(x)
    ranks={}
    for k in range(1,max(by_dim)+1):
        idx={x:i for i,x in enumerate(by_dim[k-1])}
        cols=[]
        for u in by_dim[k]:
            column=0;bits=u
            while bits:
                bit=bits&-bits;bits-=bit
                column ^= 1<<idx[u^bit]
            cols.append(column)
        ranks[k]=gf2_rank(cols)
    bettis={k:len(by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0)-(k==0) for k in by_dim}
    return bettis



def field_rank(columns, p):
    pivots={}
    for col in columns:
        v=dict(col)
        while v:
            i=max(v)
            if i not in pivots:
                inv=pow(v[i],-1,p)
                pivots[i]={j:(c*inv)%p for j,c in v.items() if c%p}
                break
            factor=v[i]
            for j,c in pivots[i].items():
                rem=(v.get(j,0)-factor*c)%p
                if rem:v[j]=rem
                else:v.pop(j,None)
    return len(pivots)

def homology_over_field(faces,p):
    by_dim=defaultdict(list)
    for x in faces-{0}:by_dim[x.bit_count()-1].append(x)
    ranks={}
    for k in range(1,4):
        idx={x:i for i,x in enumerate(by_dim[k-1])}
        cols=[]
        for u in by_dim[k]:
            entries={};bits=u
            while bits:
                bit=bits&-bits; bits-=bit
                entries[idx[u^bit]]=incidence(u,bit)%p
            cols.append(entries)
        ranks[k]=field_rank(cols,p)
    return {k:len(by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0)-(k==0)
            for k in range(4)}


def run(n):
    arcs=make_arcs(n)
    assert len(arcs)==4*n
    faces=complete_complex(n,arcs)
    fvec=tuple(sum(x.bit_count()==k+1 for x in faces) for k in range(4))
    pairs,critical=matching(faces,ORDERS[n])
    counts=dict(sorted((k,sum(x.bit_count()==k+1 for x in critical)) for k in range(4)
                        if any(x.bit_count()==k+1 for x in critical)))
    assert fvec==EXPECTED[n][0] and counts==EXPECTED[n][1]
    h=hasse_acyclic(faces,pairs)
    b=mod2_homology(faces)
    b2=homology_over_field(faces,2)
    b3=homology_over_field(faces,3)
    b5=homology_over_field(faces,5)
    assert b==b2==EXPECTED[n][2] and b3==b5==EXPECTED[n][3]
    rows,cols,content,cache,boundary=integral_morse_3_to_2(faces,pairs,critical)
    assert boundary==direct_signed_pivot_elimination(faces,pairs,critical)
    print(f'n={n} arcs={len(arcs)} faces={len(faces)-1} f={fvec}')
    print(f'n={n} pairs={len(pairs)} critical={counts} directed_Hasse={h}')
    print(f'n={n} independent_mod2_Betti={b} mod3_mod5_Betti={b3}')
    print(f'n={n} integral_Morse_D3_D2={rows}x{cols} Smith_factor={content} projection_states={cache} independent_pivot_elimination=AGREES')
    print(f'n={n} HOMOTOPY_OK M(Z/2,2) wedge {7 if n==4 else 0} S2 and {31 if n==5 else 0} S3')

if __name__=='__main__':
    for n in (4,5):run(n)
    print('ALL_VERIFY_OK')
