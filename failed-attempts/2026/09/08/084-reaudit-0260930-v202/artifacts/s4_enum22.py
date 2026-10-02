import json, itertools
# encode rep as 12-bit int: A0(4b)|A1(4b)|A2(4b), bit (i*a+j)
def mat_apply_bits():
    import itertools
    G2=[m for m in itertools.product([0,1],repeat=4) if (m[0]*m[3]^m[1]*m[2])==1]
    return G2
G2=mat_apply_bits(); print('GL2 size',len(G2))
def matmul2(X,Y):
    return [X[0]*Y[0]^X[1]*Y[2], X[0]*Y[1]^X[1]*Y[3], X[2]*Y[0]^X[3]*Y[2], X[2]*Y[1]^X[3]*Y[3]]
def matinv2(M):
    a,b,c,d=M; return [d,b,c,a]  # det=1
def act(rep,g,h):
    # rep: 3 mats 2x2 as flat lists; new_k = h A_k g^-1
    gi=matinv2(g)
    out=[]
    for A in rep:
        T=matmul2(h,A); out.append(matmul2(T,gi))
    return tuple(out)
def dec(x):
    return [[(x>>(k*4+t))&1 for t in range(4)] for k in range(3)]
def enc(M):
    x=0
    for k in range(3):
        for t in range(4): x|=(M[k][t]&1)<<(k*4+t)
    return x
def indecomp(rep):
    # decomposable iff has 1-dim subrep at dim (1,0),(0,1),(1,1) proper... brute force: check idempotents in End
    # simple: check for common invariant subspace dimensions: subrep dims (1,0)? never (arrows force 0). check (1,1),(1,0),(0,1),(2,1),(1,2)... use direct: isom to block triangular with both diag blocks reps
    # easiest: check decomposable = exists nontrivial idempotent endomorphism: enumerate End basis then search idempotents
    import itertools
    # build End equations: (X 2x2, Y 2x2): YA=AX
    rows=[]
    for k in range(3):
        A=rep[k]
        A2=[[A[0],A[1]],[A[2],A[3]]]
        for i in range(2):
            for j in range(2):
                r=[0]*8
                for l in range(2):
                    if A2[l][j]: r[i*2+l]^=A2[l][j]
                for m in range(2):
                    if A2[i][m]: r[4+m*2+j]^=A2[i][m]
                rows.append(r)
    # nullspace
    M2=[r[:] for r in rows]; piv=0; where=[-1]*8; R=len(M2)
    for c in range(8):
        f=next((i for i in range(piv,R) if M2[i][c]),None)
        if f is None: continue
        M2[piv],M2[f]=M2[f],M2[piv]; where[c]=piv
        for i in range(R):
            if i!=piv and M2[i][c]:
                for j in range(c,8): M2[i][j]^=M2[piv][j]
        piv+=1
    free=[c for c in range(8) if where[c]==-1]; d=len(free)
    basis=[]
    for c in free:
        v=[0]*8; v[c]=1
        for c2 in range(8):
            if where[c2]>=0: v[c2]=M2[where[c2]][c]
        basis.append(v)
    # search nonzero idempotents e^2=e that split (trace pieces): enumerate 2^d endos
    for mask in range(1,(1<<d)-1):
        v=[0]*8
        for j in range(d):
            if mask>>j &1:
                for c in range(8): v[c]^=basis[j][c]
        X=[v[4],v[5],v[6],v[7]]; Y=[v[0],v[1],v[2],v[3]]
        # idempotent?
        X2=matmul2(X,X); Y2=matmul2(Y,Y)
        if X2==X and Y2==Y:
            # nontrivial (not 0, not identity)? identity=(I2,I2)
            if X==[0,0,0,0] and Y==[0,0,0,0]: continue
            if X==[1,0,0,1] and Y==[1,0,0,1]: continue
            return False
    return True
seen={}; ncl=0; nind=0; nbrick=0
reps={}
for x in range(4096):
    if x in seen: continue
    r=dec(x)
    # orbit
    orb=set()
    for g in G2:
        for h in G2:
            orb.add(enc(act(r,g,h)))
    for o in orb: seen[o]=ncl
    ind=indecomp(r)
    nind+=ind
    reps[ncl]={'rep':r,'orbsize':len(orb),'indec':ind}
    ncl+=1
print('classes',ncl,'indec_classes',nind)
# verify orbit partition
assert sum(v['orbsize'] for v in reps.values())==4096
json.dump({'n_classes':ncl,'n_indec':nind,'orbit_sizes':sorted(v['orbsize'] for v in reps.values()),'reps':{k:{'rep':v['rep'],'orbsize':v['orbsize'],'indec':v['indec']} for k,v in reps.items()}},open('output/artifacts/s4_enum22.json','w'))
