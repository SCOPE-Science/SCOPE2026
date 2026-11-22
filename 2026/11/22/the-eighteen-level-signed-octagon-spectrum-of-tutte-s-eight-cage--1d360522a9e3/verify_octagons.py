#!/usr/bin/env python3
"""Recompute the signed eight-cycle character spectrum of Tutte's eight-cage.

Pure Python 3.10+; no data files, third-party libraries, or network needed.
All intermediate calculations use exact integers.
"""
from collections import Counter, deque
from itertools import combinations, permutations


def build_graph():
    duads = list(combinations(range(6), 2))
    def matchings(left):
        if not left:
            yield ()
            return
        a=left[0]
        for b in left[1:]:
            for rest in matchings(tuple(i for i in left if i not in (a,b))):
                yield ((a,b),) + rest
    synthemes=sorted(tuple(sorted(m)) for m in matchings(tuple(range(6))))
    assert len(duads)==len(synthemes)==15 and len(set(synthemes))==15
    edges=sorted((duads.index(p), 15+j) for j,m in enumerate(synthemes) for p in m)
    assert len(edges)==45
    nbr=[[] for _ in range(30)]
    emap={}
    for i,(u,v) in enumerate(edges):
        nbr[u].append((v,i));nbr[v].append((u,i))
        emap[(u,v)]=i
    for a in nbr:a.sort()
    assert all(len(a)==3 for a in nbr)
    return duads, synthemes, edges, nbr, emap


def octagons_dfs(nbr):
    out=set()
    def visit(root, v, path, used, mask):
        if len(path)==8:
            for w,edge in nbr[v]:
                if w==root:out.add(mask | (1 << edge))
            return
        for w,edge in nbr[v]:
            if w<=root or w in used:continue
            visit(root,w,path+[w],used|{w},mask|(1<<edge))
    for v in range(len(nbr)):
        visit(v,v,[v],{v},0)
    return out


def octagons_duads(duads, synthemes, emap):
    """Every octagon is a 4-cycle of distinct duads and distinct synthemes."""
    line_for_pair={}
    for j,m in enumerate(synthemes):
        p=[duads.index(a) for a in m]
        for x,y in combinations(p,2):
            line_for_pair[tuple(sorted((x,y)))]=15+j
    out=set()
    for a,b,c,d in permutations(range(15),4):
        v=(a,b,c,d)
        pairs=[tuple(sorted((v[i],v[(i+1)%4]))) for i in range(4)]
        if not all(pair in line_for_pair for pair in pairs):continue
        lines=[line_for_pair[pair] for pair in pairs]
        if len(set(lines))!=4:continue
        bits=0
        for i,L in enumerate(lines):
            bits |= 1<<emap[(v[i],L)]
            bits |= 1<<emap[(v[(i+1)%4],L)]
        assert bits.bit_count()==8
        out.add(bits)
    return out


def cotree_coordinates(octagons, nbr, num_edges):
    visited={0};queue=deque([0]);tree=[]
    while queue:
        u=queue.popleft()
        for v,e in nbr[u]:
            if v not in visited:
                visited.add(v);queue.append(v);tree.append(e)
    assert len(visited)==30 and len(tree)==29
    chords=[i for i in range(num_edges) if i not in set(tree)]
    assert len(chords)==16
    masks=[sum(1<<j for j,e in enumerate(chords) if (c>>e)&1) for c in octagons]
    assert len(masks)==len(set(masks))==90
    # A graph cycle is determined uniquely by its cotree edge coordinates.
    # The projected octagon vectors span all 16 cycle-space dimensions.
    basis={}
    for mask in masks:
        x=mask
        while x:
            p=x.bit_length()-1
            if p not in basis:
                basis[p]=x
                break
            x ^= basis[p]
    assert len(basis)==16
    return chords, masks


def walsh_inplace(a):
    n=len(a);h=1
    while h<n:
        for b in range(0,n,2*h):
            for i in range(b,b+h):
                x=a[i];y=a[i+h]
                a[i]=x+y;a[i+h]=x-y
        h*=2
    return a


def check():
    D,M,E,N,emap=build_graph()
    # Removing any edge, the alternate endpoint-to-endpoint route has length 7.
    # Thus the graph has girth eight, not a shorter hidden cycle.
    for e,(u,v) in enumerate(E):
        q=deque([(u,0)]);seen={u};dist=None
        while q:
            w,d=q.popleft()
            if w==v:dist=d;break
            for z,edge in N[w]:
                if edge!=e and z not in seen:
                    seen.add(z);q.append((z,d+1))
        assert dist==7,(e,dist)
    octa=octagons_dfs(N)
    octb=octagons_duads(D,M,emap)
    assert octa==octb and len(octa)==90
    for e in range(45):
        assert sum((c>>e)&1 for c in octa)==16
    chords,words=cotree_coordinates(octa,N,len(E))
    kernel=[0]*(1<<16)
    for w in words:kernel[w]=1
    F=walsh_inplace(kernel)
    wanted={-30:36,-22:450,-18:1080,-14:2520,-10:8280,-6:11580,
            -2:11520,2:10440,6:8520,10:5634,14:1440,18:1740,
            22:1440,30:360,34:360,42:90,58:45,90:1}
    assert Counter(F)==wanted
    assert len(F)==65536 and sum(wanted.values())==65536
    assert all(f%4==2 for f in F)
    assert min(abs(f) for f in F)==2
    assert max(abs(f) for f in F)==90
    assert sum(f*f for f in F)==65536*90
    assert sum(F)==0
    # Second exact method: independently evaluate all signed octagon sums.
    # No Walsh transform is used in this check.
    for mask in range(1<<16):
        direct=sum(1 if ((mask&w).bit_count()%2==0) else -1 for w in words)
        assert direct==F[mask],(mask,direct,F[mask])
    # An explicit sparse witness for the sharp minimum Fourier modulus.
    wit=min((m for m in range(1<<16) if abs(F[m])==2),key=lambda m:(m.bit_count(),m))
    print('vertices=30 edges=45 octagons=90 edge_occurrences=16')
    print('octagon_cycle_space_rank=16 frequency_quotient_size=65536')
    print('signed_histogram_quotient=',sorted(wanted.items()))
    print('ambient_multiplicity_factor=2^29')
    print('invertible=yes least_multiplier_magnitude=2 condition_number=45')
    print('sharp_inverse_l2_norm=1/2')
    print('minimum_witness_chord_sign_mask=',wit,'bit_positions=',[i for i in range(16) if (wit>>i)&1], 'signed_sum=',F[wit])
    print('Parseval_exact=yes orthogonal_character_sum=yes')
    print('independent_duad_and_graph_enumerations=yes')
    print('independent_direct_character_sum_checks=65536')
    print('PASS')

if __name__=='__main__':check()
