from itertools import combinations, product

N=64

def rows(x):
    return [(x>>0)&7,(x>>3)&7]

def rank2x3(x):
    a,b=rows(x)
    if a==0 and b==0: return 0
    if a==0 or b==0 or a==b: return 1
    return 2

def rank_vecs(vs,ncols):
    vs=list(vs); r=0
    for c in range(ncols):
        p=next((i for i in range(r,len(vs)) if (vs[i]>>c)&1),None)
        if p is None: continue
        vs[r],vs[p]=vs[p],vs[r]
        for i in range(len(vs)):
            if i!=r and ((vs[i]>>c)&1): vs[i]^=vs[r]
        r+=1
    return r

def span3(a,b,c):
    return frozenset((i*a)^(j*b)^(k*c) for i in (0,1) for j in (0,1) for k in (0,1))

# compatibility graph for rank distance >=2 (here exactly 2 for distinct matrices)
adj=[set() for _ in range(N)]
for a in range(N):
    for b in range(a+1,N):
        if rank2x3(a^b)==2:
            adj[a].add(b); adj[b].add(a)

# exact maximal-clique enumeration
max_cliques=[]; maxsize=0; branch_nodes=0
def bronk(R,P,X):
    global maxsize,max_cliques,branch_nodes
    branch_nodes+=1
    if not P and not X:
        s=len(R)
        if s>maxsize: maxsize=s; max_cliques=[frozenset(R)]
        elif s==maxsize: max_cliques.append(frozenset(R))
        return
    if len(R)+len(P)<maxsize: return
    u=max(P|X,key=lambda v:len(P&adj[v])) if P or X else None
    cand=list(P-(adj[u] if u is not None else set()))
    for v in cand:
        bronk(R|{v}, P&adj[v], X&adj[v])
        P.remove(v); X.add(v)

bronk(set(),set(range(N)),set())
max_cliques=sorted(set(max_cliques), key=lambda C:tuple(sorted(C)))
assert maxsize==8
assert len(max_cliques)==384
zero=[C for C in max_cliques if 0 in C]
assert len(zero)==48
assert all(all((x^y) in C for x in C for y in C) for C in zero)

# independent enumeration of all 3-spaces in F_2^6
spaces=set()
for a,b,c in combinations(range(1,64),3):
    if rank_vecs([a,b,c],6)==3:
        spaces.add(span3(a,b,c))
assert len(spaces)==1395
mrd_spaces={S for S in spaces if all(rank2x3(x)==2 for x in S if x)}
assert len(mrd_spaces)==48
assert set(zero)==mrd_spaces

# all affine cosets of the 48 linear MRD spaces reproduce all 384 maxima
cosets=set()
for S in mrd_spaces:
    for t in range(64):
        cosets.add(frozenset(x^t for x in S))
assert len(cosets)==384
assert cosets==set(max_cliques)

# GL helpers

def mat_rank(rows_,ncols): return rank_vecs(rows_,ncols)
GL2=[]
for r0 in range(4):
  for r1 in range(4):
    if mat_rank([r0,r1],2)==2: GL2.append((r0,r1))
GL3=[]
for r0 in range(8):
  for r1 in range(8):
    for r2 in range(8):
      if mat_rank([r0,r1,r2],3)==3: GL3.append((r0,r1,r2))
assert len(GL2)==6 and len(GL3)==168

def bitdot(a,b): return (a&b).bit_count()&1

def left(A,x):
    r=rows(x)
    out=[]
    for ar in A:
        out.append(((ar&1)*r[0])^(((ar>>1)&1)*r[1]))
    return out[0]|(out[1]<<3)

def right(B,x):
    r=rows(x)
    # output row j = row * B, with B represented by rows; compute columns
    out=[]
    for rr in r:
        val=0
        for j in range(3):
            col=((B[0]>>j)&1)|(((B[1]>>j)&1)<<1)|(((B[2]>>j)&1)<<2)
            val |= bitdot(rr,col)<<j
        out.append(val)
    return out[0]|(out[1]<<3)

def act(A,B,x): return right(B,left(A,x))

rep=min(mrd_spaces,key=lambda S:tuple(sorted(S)))
orbit={frozenset(act(A,B,x) for x in rep) for A in GL2 for B in GL3}
assert orbit==mrd_spaces
stab=sum(1 for A in GL2 for B in GL3 if frozenset(act(A,B,x) for x in rep)==rep)
assert stab==21

def mstr(x):
    a,b=rows(x)
    return f"[{(a>>0)&1}{(a>>1)&1}{(a>>2)&1};{(b>>0)&1}{(b>>1)&1}{(b>>2)&1}]"
print('VERIFY_OK')
print('vertices=64')
print('maximum=8')
print('labeled_maxima=384')
print('zero_containing_maxima=48')
print('all_zero_containing_linear=true')
print('all_3spaces=1395')
print('linear_mrd_3spaces=48')
print('affine_cosets=384')
print('GL2_order=6 GL3_order=168 product=1008')
print('linear_orbits=1 orbit_size=48 stabilizer=21')
print('branch_nodes='+str(branch_nodes))
print('representative='+','.join(mstr(x) for x in sorted(rep)))
