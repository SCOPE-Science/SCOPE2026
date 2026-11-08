"""Exact integral Frucht-graph forest-filtration verification.

Usage: python3 frucht_filtration_verify.py
Python standard library only. Every finite face, incidence and chain calculation
is performed directly from the twelve-vertex LCF definition. This script does
not assert an equivariant decomposition or any infinite-family theorem.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N=12
LCF=(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)
EDGES=sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)}|
             {tuple(sorted((i,(i+LCF[i])%N))) for i in range(N)})
assert len(EDGES)==18
assert all(sum(i in e for e in EDGES)==3 for i in range(N))

def is_forest_union_find(mask):
    roots=list(range(N))
    def root(v):
        while roots[v]!=v:v=roots[v]
        return v
    for u,v in EDGES:
        if mask>>u&1 and mask>>v&1:
            a,b=root(u),root(v)
            if a==b:return False
            roots[a]=b
    return True

def is_forest_depth_first(mask):
    a=[[] for _ in range(N)]
    for u,v in EDGES:
        if mask>>u&1 and mask>>v&1:
            a[u].append(v);a[v].append(u)
    seen=set()
    def dfs(v,parent):
        seen.add(v)
        for w in a[v]:
            if w==parent:continue
            if w in seen or not dfs(w,v):return False
        return True
    return all(v in seen or dfs(v,-1) for v in range(N) if mask>>v&1)

def max_induced_degree(mask):
    return max((sum(mask>>v&1 for u,v in EDGES if u==i)+
                sum(mask>>u&1 for u,v in EDGES if v==i)
                for i in range(N) if mask>>i&1),default=0)

def enumerate_faces(d):
    faces={m for m in range(1<<N) if is_forest_union_find(m)
           and max_induced_degree(m)<=d}
    assert 0 in faces
    assert all(((m in faces)==(is_forest_depth_first(m) and max_induced_degree(m)<=d))
               for m in range(1<<N))
    assert all((m&~(1<<v)) in faces for m in faces for v in range(N) if m>>v&1)
    return faces

def matching(faces,order):
    # Leave the vertex {0} critical, and work only on nonempty simplices.
    remain=set(faces)-{0,1}
    pairs=[]
    for v in order:
        bit=1<<v
        this_stage=[(s,s|bit) for s in sorted(remain)
                    if not s&bit and (s|bit) in remain]
        for lo,hi in this_stage:
            remain.remove(lo);remain.remove(hi)
        pairs.extend(this_stage)
    return pairs,remain|{1}

def check_acyclic(faces,pairs):
    active=faces-{0};mate={}
    for a,b in pairs:
        assert a in active and b in active and a.bit_count()+1==b.bit_count()
        assert a & b==a and b not in mate and a not in mate
        mate[a]=b;mate[b]=a
    in_degree={s:0 for s in active}
    for h in active:
        for v in range(N):
            if h>>v&1:
                lo=h&~(1<<v)
                if not lo:continue
                if mate.get(h)==lo:in_degree[lo]+=1
                else:in_degree[h]+=1
    queue=deque(s for s in active if in_degree[s]==0)
    count=0;cover_count=0
    while queue:
        s=queue.popleft();count+=1
        for v in range(N):
            bit=1<<v
            if s&bit:
                lo=s&~bit
                if lo and mate.get(s)==lo:
                    cover_count+=1;in_degree[lo]-=1
                    if not in_degree[lo]:queue.append(lo)
            elif (s|bit) in active and mate.get(s)!=(s|bit):
                hi=s|bit;cover_count+=1;in_degree[hi]-=1
                if not in_degree[hi]:queue.append(hi)
    assert count==len(active)
    assert cover_count==sum(s.bit_count() for s in active)-N
    return cover_count

def chain_boundary(chain):
    out=defaultdict(int)
    for s,c in chain.items():
        for j,v in enumerate(i for i in range(N) if s>>i&1):
            out[s&~(1<<v)]+=((-1)**j)*c
    return {s:c for s,c in out.items() if c}

def get_projection(pairs,critical):
    lo_to_hi={lo:hi for lo,hi in pairs}
    critical=set(critical)
    @lru_cache(None)
    def proj(face):
        if face in critical:return {face:1}
        if face not in lo_to_hi:return {}
        h=lo_to_hi[face]
        bits=[i for i in range(N) if h>>i&1]
        missing=(h^face).bit_length()-1
        eps=(-1)**bits.index(missing)
        out=defaultdict(int)
        for j,v in enumerate(bits):
            f=h&~(1<<v)
            if f!=face:
                for t,c in proj(f).items():out[t]-=eps*((-1)**j)*c
        return {s:c for s,c in out.items() if c}
    def project_chain(chain):
        out=defaultdict(int)
        for face,c in chain.items():
            for t,a in proj(face).items():out[t]+=c*a
        return {t:c for t,c in out.items() if c}
    return project_chain

def morse_boundaries(critical,projection):
    out={}
    for h in sorted(critical):
        if h.bit_count()>1:
            out[h]=projection(chain_boundary({h:1}))
            assert all(t.bit_count()+1==h.bit_count() for t in out[h])
    return out

def lift_cycle(simplex,pairs):
    """Construct a genuine simplicial cycle from a critical cell.

    Iteratively eliminate the components of its boundary indexed by matched
    lower faces by adding upper faces. Each iteration is verified exactly.
    """
    p={a:b for a,b in pairs}
    sign={a:(-1)**[i for i in range(N) if b>>i&1].index((b^a).bit_length()-1)
          for a,b in pairs}
    chain={simplex:1}
    for t in range(100):
        boundary=chain_boundary(chain)
        piv={a:c for a,c in boundary.items() if a in p}
        if not piv:
            assert not boundary, (simplex,boundary)
            return chain
        new=defaultdict(int,chain)
        for a,c in piv.items():new[p[a]]-=c*sign[a]
        chain={a:c for a,c in new.items() if c}
    raise AssertionError('Gradient chain lifting did not terminate')

def gf2_rank(cols):
    piv={}
    for c in cols:
        while c:
            j=c.bit_length()-1
            if j not in piv:piv[j]=c;break
            c^=piv[j]
    return len(piv)

def independent_mod2_inclusion_rank(F2,F3):
    """Unmatched-matrix calculation of inclusion on degree-six mod-2 homology.

    Find the full kernel of the source simplicial d6, embed every kernel
    vector in target C6, and quotient by target simplicial d7 boundaries.
    This does not use Morse reductions or their chain maps.
    """
    six2=sorted(s for s in F2 if s.bit_count()==7)
    five2=sorted(s for s in F2 if s.bit_count()==6)
    six3=sorted(s for s in F3 if s.bit_count()==7)
    seven3=sorted(s for s in F3 if s.bit_count()==8)
    row2={s:i for i,s in enumerate(five2)}
    row3={s:i for i,s in enumerate(six3)}
    pivot={}; kernel=[]
    for idx,s in enumerate(six2):
        boundary=0
        for v in range(N):
            if s>>v&1:boundary^=1<<row2[s&~(1<<v)]
        combination=1<<idx
        while boundary:
            j=boundary.bit_length()-1
            if j not in pivot:
                pivot[j]=(boundary,combination)
                break
            q,r=pivot[j]
            boundary^=q;combination^=r
        if not boundary:kernel.append(combination)
    assert len(kernel)==58,(len(kernel),len(six2),len(pivot))
    target_piv={}
    def insert(x):
        while x:
            j=x.bit_length()-1
            if j not in target_piv:target_piv[j]=x;return 1
            x^=target_piv[j]
        return 0
    for s in seven3:
        x=0
        for v in range(N):
            if s>>v&1:x^=1<<row3[s&~(1<<v)]
        insert(x)
    target_boundary_rank=len(target_piv)
    count=0
    for k in kernel:
        x=0
        for j,s in enumerate(six2):
            if k>>j&1:x^=1<<row3[s]
        count+=insert(x)
    assert target_boundary_rank==93
    return count

def mod2_betti(faces):
    nmax=max(s.bit_count()-1 for s in faces)
    by_dim={d:sorted(s for s in faces if s.bit_count()==d+1)
            for d in range(nmax+1)}
    ranks={}
    for d in range(1,nmax+1):
        idx={s:i for i,s in enumerate(by_dim[d-1])}
        cols=[]
        for s in by_dim[d]:
            col=0
            for v in range(N):
                if s>>v&1:col^=1<<idx[s&~(1<<v)]
            cols.append(col)
        ranks[d]=gf2_rank(cols)
    answer={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
            for d in by_dim}
    answer[0]-=1
    return {d:k for d,k in answer.items() if k}

if __name__=='__main__':
    print('LCF',list(LCF))
    print('edges',EDGES)
    expect_f={
       0:[1,12,48,73,34,1,0,0,0,0],
       1:[1,12,66,190,293,209,53,1,0,0],
       2:[1,12,66,217,464,653,580,287,55,0],
       3:[1,12,66,217,467,675,642,368,94,0],
    }
    expect_betti={0:{2:3},1:{3:1},2:{6:4,7:1},3:{6:3,7:1}}
    DATA={}
    for d in range(4):
        faces=enumerate_faces(d)
        fvector=[sum(s.bit_count()==k for s in faces) for k in range(10)]
        assert fvector==expect_f[d],(d,fvector)
        betti=mod2_betti(faces)
        assert betti==expect_betti[d],(d,betti)
        print('degree',d,'faces_including_empty',len(faces),'f_vector_-1_to_8',fvector,
              'independent_mod2_reduced_betti',betti)
        order=list(reversed(range(N))) if d==1 else list(range(N))
        pairs,crit=matching(faces,order)
        covering=check_acyclic(faces,pairs)
        counts=dict(sorted(Counter(s.bit_count()-1 for s in crit).items()))
        expect_counts={0:{0:1,2:3},1:{0:1,3:1},2:{0:1,6:4,7:1},3:{0:1,6:4,7:2}}
        assert counts==expect_counts[d],(d,counts)
        assert len(pairs)*2+len(crit)==len(faces)-1
        projection=get_projection(pairs,crit)
        differential=morse_boundaries(crit,projection)
        # Verify the projection is an integral chain map on every simplex,
        # not merely on the critical generators.
        for simplex in faces-{0}:
            lhs=projection(chain_boundary({simplex:1}))
            rhs=defaultdict(int)
            for t,c in projection({simplex:1}).items():
                for u,a in differential.get(t,{}).items():rhs[u]+=c*a
            assert lhs=={t:c for t,c in rhs.items() if c},(d,simplex)
        assert all(not coeffs for h,coeffs in differential.items()
                   if d<=2)
        if d==3:
            six=sorted(m for m in crit if m.bit_count()==7)
            seven=sorted(m for m in crit if m.bit_count()==8)
            assert six==[926,3506,3762,3890]
            assert seven==[1782,3828]
            assert differential[1782]=={}
            assert differential[3828]=={3762:1}
        print('degree',d,'matched_pairs',len(pairs),'directed_covering_relations',covering)
        print('degree',d,'critical_faces',counts,'positive_dim_masks',sorted(s for s in crit if s!=1))
        print('degree',d,'nonzero_morse_differentials',
              {str(s):co for s,co in differential.items() if co})
        DATA[d]=(faces,pairs,crit,projection,differential)
    # Explicit integral inclusion matrix for F_2 -> F_3.
    F2,p2,c2,pr2,d2=DATA[2]
    F3,p3,c3,pr3,d3=DATA[3]
    images={}
    for s in sorted(c2):
        if s.bit_count()<7:continue
        cycle=lift_cycle(s,p2)
        assert all(t in F2 for t in cycle)
        assert not chain_boundary(cycle)
        assert pr2(cycle)=={s:1}
        images[s]=pr3(cycle)
    assert images=={926:{926:1},1782:{1782:1},3308:{},
                    3506:{3506:1},3762:{3762:1}},images
    mod2_inclusion_rank=independent_mod2_inclusion_rank(F2,F3)
    assert mod2_inclusion_rank==2
    print('independent_direct_mod2_H6_inclusion_rank',mod2_inclusion_rank)
    print('integral_chain_inclusion_F2_to_F3',images)
    print('H6_F2_to_H6_F3: free_rank_4_to_3, rank_2, split_image_and_cokernel')
    print('H7_F2_to_H7_F3: isomorphism_Z_to_Z')
    print('reduced_integral_persistence: H2 3*[0,1); H3 [1,2); '
          'H6 2*[2,3) + 2*[2,infty) + [3,infty); H7 [2,infty)')
    print('FRUCHT_FOREST_FILTRATION_INTEGRAL_CERTIFICATE_PASS')
