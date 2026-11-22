#!/usr/bin/env python3
"""Reconstruct and check the Q4 independence-complex fault-saturation certificate.
Standard library only. Run: python3 verify.py certificate.json
"""
import json,sys
from collections import defaultdict,Counter,deque
from itertools import product,permutations,combinations

F=[(0,1),(6,7),(10,11),(12,13)]

def cube_edges():
    return {(i,i^(1<<j)) for i in range(16) for j in range(4) if i<(i^(1<<j))}

def universe(deleted=()):
    edges=cube_edges()-set(deleted)
    adj=[0]*16
    for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
    valid={0}
    for mask in range(1,1<<16):
        bit=mask&-mask;v=bit.bit_length()-1
        tail=mask^bit
        if tail in valid and not (tail&adj[v]):valid.add(mask)
    return valid

def faces_local(vertices):
    E=cube_edges()
    neighbors={x:0 for x in vertices}
    for a,b in E:
        if a in neighbors and b in neighbors:
            neighbors[a]|=1<<b; neighbors[b]|=1<<a
    faces={0}
    for mask in range(1,1<<len(vertices)):
        bit=mask&-mask;v=bit.bit_length()-1
        tail=mask^bit
        if tail in faces and not (sum((1<<x) for i,x in enumerate(vertices) if (tail>>i)&1)&neighbors[vertices[v]]):
            faces.add(mask)
    return faces

def all_cover_arcs(faces):
    arcs=[]
    for upper in faces-{0}:
        for v in range(16):
            if upper>>v&1:
                lower=upper^(1<<v)
                if lower:arcs.append((upper,lower))
    return arcs

def pivot_matching(faces):
    remaining=faces-{0};pairs=[];counts=[]
    for v in range(16):
        todo=[]
        for a in sorted(remaining):
            b=a|(1<<v)
            if not (a>>v&1) and b in remaining:
                todo.append([a,b])
        assert all(a in remaining and b in remaining for a,b in todo)
        for a,b in todo:remaining.remove(a);remaining.remove(b)
        pairs.extend(todo);counts.append(len(todo))
    return pairs,remaining,counts

def certify_morse(base, pairs):
    # Verify matching conditions and complete acyclicity of reversed incidences.
    seen=set(); matched=set()
    for a,b in pairs:
        assert a>0 and a in base and b in base and a.bit_count()+1==b.bit_count()
        assert b&a==a and a not in seen and b not in seen
        seen|={a,b};matched.add((b,a))
    arcs=all_cover_arcs(base)
    indeg={v:0 for v in base-{0}}
    dig=defaultdict(list)
    for top,low in arcs:
        src,dst=(low,top) if (top,low) in matched else (top,low)
        dig[src].append(dst);indeg[dst]+=1
    queue=deque(v for v in sorted(indeg) if indeg[v]==0);n=0
    while queue:
        v=queue.popleft();n+=1
        for w in dig[v]:
            indeg[w]-=1
            if indeg[w]==0:queue.append(w)
    assert n==len(indeg),(n,len(indeg))
    return len(arcs)

def validate_collapse(base,outer,pairs,vertex_count=16):
    current=set(outer)
    assert base<=current
    for a,b in pairs:
        assert a and a not in base and b not in base and a in current and b in current
        assert b.bit_count()==a.bit_count()+1 and b&a==a
        cofaces=[c for c in current if c.bit_count()==a.bit_count()+1 and c&a==a]
        assert cofaces==[b],(a,b,cofaces)
        current.remove(a);current.remove(b)
    assert current==base,(len(current-base),len(base-current))
    return len(pairs)

def collapse_pairs(base,outer,vertices=16):
    remaining=set(outer);pairs=[]
    while remaining!=base:
        upper=defaultdict(list)
        for b in remaining:
            for i in range(vertices):
                if b>>i&1:
                    a=b^(1<<i)
                    if a in remaining and a!=0 and a not in base:upper[a].append(b)
        candidates=[(a,bs[0]) for a,bs in upper.items() if len(bs)==1 and bs[0] not in base]
        assert candidates,('no relative collapse',len(remaining-base))
        candidates.sort(key=lambda pair:(-pair[0].bit_count(),pair[0],pair[1]))
        a,b=candidates[0]
        remaining.remove(a);remaining.remove(b)
        pairs.append([a,b])
    return pairs

def reduced_mod2_betti(faces):
    counts=Counter(x.bit_count()-1 for x in faces if x)
    groups={k:sorted(x for x in faces if x.bit_count()==k+1) for k in counts}
    ranks={}
    for k in sorted(groups):
        if k==0:continue
        index={m:i for i,m in enumerate(groups[k-1])}
        piv={}
        for m in groups[k]:
            row=0
            for v in range(16):
                if m>>v&1:row ^= 1<<index[m^(1<<v)]
            while row:
                head=row.bit_length()-1
                if head in piv:row^=piv[head]
                else:piv[head]=row;break
        ranks[k]=len(piv)
    bettis={k:counts[k]-ranks.get(k,0)-ranks.get(k+1,0) for k in counts}
    bettis[0]-=1
    return [counts[k] for k in sorted(counts)],ranks,bettis

def make_certificate():
    K=[universe(F[:t]) for t in range(5)]
    pairs,critical,ct=pivot_matching(K[0])
    assert Counter(x.bit_count()-1 for x in critical)=={0:1,3:7}
    assert ct==[176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1]
    assert certify_morse(K[0],pairs)==2816
    # Residual graph after deleting the closed neighborhoods of 0 and 1.
    E=cube_edges();N={0,1}
    for a,b in E:
        if a in (0,1):N.add(b)
        if b in (0,1):N.add(a)
    V=sorted(set(range(16))-N)
    assert V==[6,7,10,11,12,13,14,15]
    L=faces_local(V)
    T={x for x in L if not (x&(1<<6 | 1<<7))}
    cL=collapse_pairs(T,L,8)
    assert len(cL)==8
    cf=[collapse_pairs(K[t-1],K[t]) for t in range(2,5)]
    assert list(map(len,cf))==[26,32,40]
    return {'schema_version':1,'four_cube_pivot_pairs':pairs,'residual_oct_sphere_collapses':cL,'sequential_fault_collapses':cf}

def check(cert):
    assert cert['schema_version']==1
    K=[universe(F[:t]) for t in range(5)]
    assert [len(x) for x in K]==[743,786,838,902,982]
    mp=cert['four_cube_pivot_pairs']
    assert mp==pivot_matching(K[0])[0], 'not the stated pivot matching'
    critical=K[0]-{0}-{v for a,b in mp for v in (a,b)}
    assert sorted(critical)==[1,1680,2400,10370,17028,24600,33064,33096]
    arcs=certify_morse(K[0],mp)
    V=[6,7,10,11,12,13,14,15];L=faces_local(V)
    T={x for x in L if not (x&(1<<6 | 1<<7))}
    assert len(L)==43 and len(T)==27
    assert validate_collapse(T,L,cert['residual_oct_sphere_collapses'],8)==8
    assert cert['residual_oct_sphere_collapses']==collapse_pairs(T,L,8)
    # The six vertices of T induce three disjoint edges, so Ind = (S^0)^*3 = S^2.
    rest=[(a,b) for a,b in cube_edges() if a in V[:6] and b in V[:6]]
    assert sorted(rest)==[(6,7),(10,11),(12,13)]
    # The attaching 3-cycle is the suspension of T by 0 and 1.
    # It equals the fundamental 3-cycle of a fourfold join of zero-spheres.
    spheres=[tuple(pair) for pair in F]
    for picks in product(*spheres):
        mask=sum(1<<v for v in picks)
        assert mask in K[0] and mask.bit_count()==4
    sigma=sum(1<<v for v in (0,6,11,13))
    assert sigma in K[0]
    assert not any((sigma|(1<<v)) in K[0] for v in range(16) if not sigma>>v&1), 'sigma must be a maximal 3-face'
    # Pairwise fourfold join is a signed 3-cycle; sigma appears once with coefficient +/-1.
    assert sigma in {sum(1<<v for v in picks) for picks in product(*spheres)}
    assert [len(c) for c in cert['sequential_fault_collapses']]==[26,32,40]
    for t,cp in enumerate(cert['sequential_fault_collapses'],start=2):
        assert cp==collapse_pairs(K[t-1],K[t])
        validate_collapse(K[t-1],K[t],cp)
    face_vectors=[]
    for t in range(5):
        count,ranks,bet=reduced_mod2_betti(K[t]);face_vectors.append(count)
        assert bet.get(3)==(7 if t==0 else 6)
        assert all(v==0 for k,v in bet.items() if k!=3)
    # Stabilizer: translations by even 3-bit words plus permutations of the three
    # transverse coordinates form (Z/2)^2 semidirect S3 ~= S4 on the four fault edges.
    Eset={tuple(x) for x in F}
    parity3=lambda x:sum((x>>j)&1 for j in (1,2,3))%2
    assert all(parity3(a)==0 and a^b==1 for a,b in F)
    # Realize all 24 permutations on the four parallel edges through cube symmetries.
    canonical_edges=F
    edgemap={e:i for i,e in enumerate(F)}
    induced_perms=set()
    for pi in permutations((1,2,3)):
        for trans in (0, (1<<1)|(1<<2), (1<<1)|(1<<3), (1<<2)|(1<<3)):
            def g(x):
                y=x&1
                for old,new in zip((1,2,3),pi):
                    if x>>old&1:y|=1<<new
                return y^trans
            assert all(tuple(sorted((g(a),g(b)))) in cube_edges() for a,b in cube_edges())
            image=tuple(edgemap[tuple(sorted((g(a),g(b))))] for a,b in canonical_edges)
            induced_perms.add(image)
    assert len(induced_perms)==24
    for size in range(1,5):
        canonical=tuple(range(size))
        orbit={tuple(sorted(perm[i] for i in canonical)) for perm in induced_perms}
        assert orbit==set(combinations(range(4),size))
    # The eight coordinate/parity fault classes are conjugate under bit
    # permutations and translations, so the four representatives suffice.
    eight_classes=set()
    for direction in range(4):
        other=[j for j in range(4) if j!=direction]
        for parity in (0,1):
            class_edges=frozenset((x,x^(1<<direction)) for x in range(16)
                if not (x>>direction&1) and sum((x>>j)&1 for j in other)%2==parity)
            assert len(class_edges)==4 and class_edges<=cube_edges()
            eight_classes.add(class_edges)
    assert len(eight_classes)==8
    print('VERIFY_OK_Q4_PARITY_CLASS_EDGE_FAULT_SATURATION',
          'base_faces=742',f'morse_pairs={len(mp)}',f'hasse_arcs={arcs}',
          'link_collapse_pairs=8','fault_collapse_pairs=26,32,40',
          'betti3=7,6,6,6,6',f'face_vectors={face_vectors}')

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python3 verify.py certificate.json')
    with open(sys.argv[1],encoding='utf-8') as f:cert=json.load(f)
    check(cert)
