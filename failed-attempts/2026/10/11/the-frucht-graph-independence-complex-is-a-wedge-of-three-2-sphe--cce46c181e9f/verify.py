from collections import Counter, deque

N = 12
EDGES = {
    (0,1),(0,6),(0,7),
    (1,2),(1,7),
    (2,3),(2,8),
    (3,4),(3,9),
    (4,5),(4,9),
    (5,6),(5,10),
    (6,10),
    (7,11),
    (8,9),(8,11),
    (10,11),
}
EDGES = {tuple(sorted(e)) for e in EDGES}

# One of the order-1 LCF notations listed for the Frucht graph by MathWorld.
LCF = [-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]
# Explicit isomorphism from the labeled graph above to that LCF realization.
TO_LCF = {4:0,3:1,2:2,1:3,7:4,0:5,6:6,5:7,10:8,11:9,8:10,9:11}

MORSE_ORDER = [8,11,4,6,3,5,7,10,0,9,1,2]
EXPECTED_F_VECTOR = [12,48,73,34,1]
EXPECTED_CRITICAL = {
    1 << 8,
    (1 << 5) | (1 << 7) | (1 << 9),
    (1 << 1) | (1 << 9) | (1 << 10),
    (1 << 0) | (1 << 3) | (1 << 11),
}

def adjacency(edges):
    A=[set() for _ in range(N)]
    for a,b in edges:
        A[a].add(b); A[b].add(a)
    return A

def lcf_edges():
    E=set()
    for i in range(N):
        E.add(tuple(sorted((i,(i+1)%N))))
        E.add(tuple(sorted((i,(i+LCF[i])%N))))
    return E

def connected(A):
    seen={0}; q=[0]
    while q:
        v=q.pop()
        for w in A[v]:
            if w not in seen:
                seen.add(w); q.append(w)
    return len(seen)==N

def automorphism_count(A):
    # Exact adjacency-preserving backtracking. stop is not used; the result is asserted to be 1.
    deg=[len(x) for x in A]
    mapping={}
    used=set()
    count=0
    def choose_u():
        unmapped=[u for u in range(N) if u not in mapping]
        return max(unmapped, key=lambda u:(sum(v in mapping for v in A[u]), -u))
    def rec():
        nonlocal count
        if len(mapping)==N:
            count += 1
            return
        u=choose_u()
        for v in range(N):
            if v in used or deg[v] != deg[u]:
                continue
            ok=True
            for u2,v2 in mapping.items():
                if ((u2 in A[u]) != (v2 in A[v])):
                    ok=False
                    break
            if not ok:
                continue
            mapping[u]=v; used.add(v)
            rec()
            used.remove(v); del mapping[u]
    rec()
    return count

def independent(mask):
    for a,b in EDGES:
        if ((mask>>a)&1) and ((mask>>b)&1):
            return False
    return True

def all_faces():
    return [m for m in range(1,1<<N) if independent(m)]

def f_vector(faces):
    c=Counter(m.bit_count() for m in faces)
    return [c[k] for k in range(1,max(c)+1)]

def staged_matching(faces):
    unmatched=set(faces)
    pairs=[]
    for v in MORSE_ORDER:
        bit=1<<v
        lows=sorted(m for m in unmatched if not (m & bit) and (m|bit) in unmatched)
        for lo in lows:
            hi=lo|bit
            if lo in unmatched and hi in unmatched:
                pairs.append((lo,hi))
                unmatched.remove(lo); unmatched.remove(hi)
    return pairs, sorted(unmatched)

def hasse_acyclic(faces,pairs):
    F=set(faces); P=set(pairs)
    indeg={m:0 for m in F}
    out={m:[] for m in F}
    covers=0
    for hi in F:
        t=hi
        while t:
            b=t & -t
            t-=b
            lo=hi^b
            if lo==0 or lo not in F:
                continue
            covers += 1
            # Matched covers are reversed relative to the ordinary face-poset orientation.
            if (lo,hi) in P:
                a,z=hi,lo
            else:
                a,z=lo,hi
            out[a].append(z); indeg[z]+=1
    q=deque([m for m,d in indeg.items() if d==0])
    seen=0
    while q:
        x=q.popleft(); seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:
                q.append(y)
    return covers, seen==len(F)

def rank_mod_p(mat,p):
    if not mat:
        return 0
    A=[row[:] for row in mat]
    nr=len(A); nc=len(A[0]); r=0
    for c in range(nc):
        piv=None
        for i in range(r,nr):
            if A[i][c] % p:
                piv=i; break
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c] % p, -1, p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(nr):
            if i!=r and A[i][c] % p:
                f=A[i][c] % p
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(nc)]
        r+=1
        if r==nr:
            break
    return r

def boundary_ranks(faces,p):
    byk={}
    for m in faces:
        byk.setdefault(m.bit_count(),[]).append(m)
    ranks=[]
    maxk=max(byk)
    for k in range(2,maxk+1):
        low=sorted(byk[k-1]); high=sorted(byk[k])
        idx={m:i for i,m in enumerate(low)}
        M=[[0]*len(high) for _ in low]
        for j,m in enumerate(high):
            verts=[v for v in range(N) if (m>>v)&1]
            for pos,v in enumerate(verts):
                lo=m^(1<<v)
                M[idx[lo]][j]=1 if pos%2==0 else -1
        ranks.append(rank_mod_p(M,p))
    return ranks

def betti_from_ranks(faces,ranks):
    c=Counter(m.bit_count() for m in faces)
    maxk=max(c)
    # ranks[j] is boundary C_{j+1}->C_j for simplicial dimension j+1? Here k cardinality 2 starts d1.
    d=[0]+ranks  # d[1]=rank d_1, d[2]=rank d_2, ...
    betti=[]
    for dim in range(maxk):
        cdim=c[dim+1]
        rank_d = d[dim] if dim>=1 else 0
        rank_next = d[dim+1] if dim+1 < len(d) else 0
        betti.append(cdim-rank_d-rank_next)
    return betti

def fmt(mask):
    return tuple(i for i in range(N) if (mask>>i)&1)

A=adjacency(EDGES)
assert len(EDGES)==18
assert all(len(A[v])==3 for v in range(N))
assert connected(A)
assert automorphism_count(A)==1

LE=lcf_edges()
mapped={tuple(sorted((TO_LCF[a],TO_LCF[b]))) for a,b in EDGES}
assert mapped==LE
assert len(LE)==18

faces=all_faces()
assert len(faces)==168
assert f_vector(faces)==EXPECTED_F_VECTOR
assert max(m.bit_count() for m in faces)==5

pairs,critical=staged_matching(faces)
assert len(pairs)==82
assert set(critical)==EXPECTED_CRITICAL
assert Counter(m.bit_count()-1 for m in critical)==Counter({0:1,2:3})
covers,acyclic=hasse_acyclic(faces,pairs)
assert covers==456
assert acyclic

for p in (2,3,5):
    ranks=boundary_ranks(faces,p)
    assert ranks==[11,37,33,1], (p,ranks)
    b=betti_from_ranks(faces,ranks)
    assert b==[1,0,3,0,0], (p,b)

chi=sum(((-1)**(m.bit_count()-1)) for m in faces)
assert chi==4

print("vertices=12 edges=18 cubic=true connected=true automorphisms=1")
print("lcf_identification=true")
print("nonempty_faces=168")
print("f_vector=(12,48,73,34,1)")
print("hasse_covers=456")
print("morse_order="+str(MORSE_ORDER))
print("matched_pairs=82")
print("critical_faces="+str([fmt(m) for m in critical]))
print("critical_cells=(1 in dim0, 3 in dim2)")
print("boundary_ranks_mod_2_3_5=(11,37,33,1)")
print("betti_mod_2_3_5=(1,0,3,0,0)")
print("euler_characteristic=4")
print("VERIFY_OK")
