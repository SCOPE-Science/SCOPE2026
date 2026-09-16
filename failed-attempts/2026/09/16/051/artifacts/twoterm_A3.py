"""Attempt search for 'large' 2-term silting interval over A3 3-cycle cluster-tilted
algebra B = kQ/I, Q = 3-cycle, I = (rad^2 within cycle).

We work over GF(p), p=7, enumerating 2-term complexes P1 -> P0 with P_i projective,
up to small multiplicities, testing presilting condition Hom_{K^b}(P,P[1])=0 and
g-vector distinctness. Goal: bounded evidence that 2-silt is finite (list them),
NOT a proof. Full mathematical proof uses gentle/derived-discrete classification.
"""
import itertools
import numpy as np

p = 7
# Algebra B dim 6: basis: e0,e1,e2, a:0->1, b:1->2, c:2->0.
# Multiplication table for basis elements (right-to-left function order avoided;
# use path concatenation: x*y = path x followed by y if t(x)=s(y)).
verts = ['e0','e1','e2','a','b','c']
s = {'e0':0,'e1':1,'e2':2,'a':0,'b':1,'c':2}
t = {'e0':0,'e1':1,'e2':2,'a':1,'b':2,'c':0}
idx = {v:i for i,v in enumerate(verts)}
mult = np.zeros((6,6,6), dtype=int)
def add_prod(x,y,z,coef=1):
    mult[idx[x],idx[y],idx[z]] = (mult[idx[x],idx[y],idx[z]]+coef)%p
for v in verts: add_prod(v,verts[verts.index(v)] if False else v, v)  # placeholder
# reset and define properly
mult = np.zeros((6,6,6), dtype=int)
def set_prod(x,y,z):
    mult[idx[x],idx[y],idx[z]] = 1
for v in verts:
    set_prod(v,'e'+str(t[v]),v)  # x*e_{t(x)} = x
    set_prod('e'+str(s[v]),v,v)  # e_{s(x)}*x = x
# length-2 products a*b? a:0->1,b:1->2 gives path 0->1->2 = 0 by relation.
# b*c=0, c*a=0 similarly. All other length>=2 products are 0 (no matching or relation).
# e_i*e_j = delta.
# (Already e products set; products a*b etc. remain 0.) Fix: e_i*e_i should be e_i,
# but above set e_i*e_i twice; fine (=1 mod p, set twice -> need fix to 1).
mult[idx['e0'],idx['e0'],idx['e0']]=1
mult[idx['e1'],idx['e1'],idx['e1']]=1
mult[idx['e2'],idx['e2'],idx['e2']]=1

def mat_mul_rep():
    # right regular representation: R[x]_{z,y} : (z*x) coefficient of y? Use row vectors.
    R = {}
    for x in verts:
        M = np.zeros((6,6), dtype=int)
        for z in verts:
            for y in verts:
                M[idx[z],idx[y]] = mult[idx[z],idx[x],idx[y]]
        R[x]=M
    return R
R = mat_mul_rep()
# Projectives P_i = e_i B as row-spaces: basis subset
P_basis = {0:['e0','a'], 1:['e1','b'], 2:['e2','c']}
for i,b in P_basis.items():
    print(f"P{i} basis {b} dim {len(b)}")
print("Cartan check: dim e_i B e_j:")
C = np.zeros((3,3),dtype=int)
for i in range(3):
    for j in range(3):
        C[i,j] = sum(1 for v in P_basis[i] if s[v]==i and t[v]==j)
print(C)
# Maps between projectives: Hom(P_i,P_j) = e_i B e_j as vector space.
# Enumerate 2-term complexes with terms in add(P0,P1,P2), total rank <=3 per degree,
# differential = matrices over B. Count presilting ones up to iso is hard; instead
# enumerate g-vectors realized by presilting complexes found by random search.
rng = np.random.default_rng(0)
def basis_elem_matrix(src_decomp, tgt_decomp):
    # Hom(oisum P_src, oisum P_tgt) basis: for each pair (r,s), basis paths src_r -> tgt_s.
    pairs=[]
    for r,i in enumerate(src_decomp):
        for s2,j in enumerate(tgt_decomp):
            for v in P_basis[j]:
                pass
    return None

# Simpler invariant: enumerate all multiplicity-free 2-term complexes
# (P^{-1} -> P^0 with each projective used <=once) with differentials given by
# linear combos of paths, test presilting via homotopy linear algebra over GF(p).
def proj_dim(i): return len(P_basis[i])

def hom_space_basis(src, tgt):
    # src,tgt: lists of vertex ids; returns list of matrices (dim_tgt x dim_src over GF(p))
    # in coords of P_basis.
    # A map f: P_src -> P_tgt determined by images of e-generators: f(e_i part)...
    # Use: Hom(P_i,P_j) basis = paths i->j in B.
    # Coordinates: P_i has basis {e_i} U {arrows out of i}.
    paths = {(0,0):['e0'],(0,1):['a'],(1,1):['e1'],(1,2):['b'],(2,2):['e2'],(2,0):['c']}
    basis=[]
    ds=sum(proj_dim(i) for i in src); dt=sum(proj_dim(j) for j in tgt)
    # offsets
    offs=[]; o=0
    for i in src: offs.append(o); o+=proj_dim(i)
    offt=[]; o=0
    for j in tgt: offt.append(o); o+=proj_dim(j)
    for r,i in enumerate(src):
        for s2,j in enumerate(tgt):
            for _ in paths.get((i,j),[]):
                M=np.zeros((dt,ds),dtype=int)
                # right multiplication by path q:i->j maps generator e_i (slot 0 of block r)
                # to q (slot of block s2: 0 if q=e, 1 if arrow). Arrow post-products zero.
                M[offt[s2]+ (0 if len(paths[(i,j)][0])>1 or paths[(i,j)][0][0]=='e' else 1), offs[r]+0]=1
                basis.append(M)
    return basis, (dt,ds)

def all_maps(src,tgt):
    basis,_ = hom_space_basis(src,tgt)
    d=len(basis)
    if d==0:
        yield np.zeros((sum(proj_dim(j) for j in tgt), sum(proj_dim(i) for i in src)),dtype=int)
        return
    for coef in itertools.product(range(p), repeat=d):
        M=sum(c*B for c,B in zip(coef,basis))%p
        yield M

def rank_gf(M):
    M=np.array(M)%p; r=0; R2=M.copy()
    m,n=R2.shape
    row=0
    for col in range(n):
        piv=None
        for i in range(row,m):
            if R2[i,col]%p!=0: piv=i; break
        if piv is None: continue
        R2[[row,piv]]=R2[[piv,row]]
        inv=pow(int(R2[row,col]),-1,p)
        R2[row]=(R2[row]*inv)%p
        for i in range(m):
            if i!=row and R2[i,col]!=0:
                R2[i]=(R2[i]-R2[i,col]*R2[row])%p
        row+=1; r+=1
    return r

def is_presilting(src,tgt,D):
    # complex P: P^{-1}=oisum P_src --D--> P^0=oisum P_tgt. Presilting iff every
    # chain map P->P[1] is null-homotopic. Chain map P->P[1] is single map h:P^0->P^0? No:
    # P[1]: P^0 in degree -1? P has terms deg -1,0. P[1] has terms deg -2,-1.
    # Hom(P,P[1]): map f0: P^0 -> P^{-1} (deg -1 part of target? ) let's compute:
    # Hom^i = prod_j Hom(P^j, P^{j+i}). i=1: Hom(P^{-1},P^0) via f with f o? condition
    # D f? cycle: D f = 0? and boundaries f = D h + h D with h: P^0->P^{-1}... Standard:
    # cycles Z = {f in Hom(P^{-1},P^0)... } hmm cochain indexing: d^{-1}=D:P^{-1}->P^0.
    # Hom^1 = Hom(P^0,P^0)? No: Hom(P^j, P^{j+1}): j=-1: Hom(P^{-1},P^0); j=0: Hom(P^0,P^1=0)=0.
    # So cycles = {f: P^{-1}->P^0 : f D? } target differential d^0=0, source: f d^{-1}?
    # cycle cond: d f - f d = 0 -> 0*f? d^0 f = f d^{-1} -> 0 = f D? No: f: P^{-1}->P^0,
    # condition d^0 o f = f o d^{-1} i.e. 0 = f D? f D: P^{-1}->P^0? D:P^{-1}->P^0, f:P^{-1}->P^0;
    # f D not composable. Correct: cycle iff D? Let's use: g in Hom(P^0, P^0)?? Hom(P^j,P^{j+1}):
    # j=0 gives Hom(P^0, P^1)=0; j=-1 gives Hom(P^{-1}, P^0). Cycle: d_{P[1]} f = f d_P:
    # d_{P[1]}^{-1} = -D: P^0(=P[1]^{-1}) -> ... hmm confusing.
    # Direct: chain map of degree 1 = maps f_j: P^j -> P^{j+1} with d f_j = f_{j+1} d.
    # f_{-1}: P^{-1}->P^0, f_0: P^0->0. Cond: d^0 f_{-1} = f_0 d^{-1} -> 0=0. So ALL
    # f: P^{-1}->P^0 are cycles. Boundaries: f = d h + h d with h_j: P^j -> P^j
    # (degree 0 maps shifted): f_{-1} = d^{-1}_{P[1]} h_{-1} + h_0 d^{-1}_P = (-D) h_{-1} + h_0 D
    # where h_{-1}: P^{-1}->P^0? wait h: P->P degree 0: h_{-1}: P^{-1}->P[1]^{-1}=P^0? and
    # h_0: P^0 -> P[1]^0 = 0. So h_0=0, f = -D h_{-1}: post-compose? f = -D o h? D:P^{-1}->P^0,
    # h_{-1}: P^{-1}->P^0: -D h not composable either. Sign/order: use left-action
    # convention consistently: maps act on right? We use matrices acting on column?
    # We set maps as matrices tgt-coords x src-coords, composition = matrix product.
    # f_{-1}: matrix (dim P^0 x dim P^{-1}). h_{-1}: P^{-1}->P^0 same shape? Then
    # boundary f = d^0_{P[1]} h + h d: d^0_{P[1]}: P[1]^0=0 ->.. = 0; h_0 d^{-1}: h_0: P^0->0 =0.
    # So f = d^{-1}_{P[1]} h_{-1}? d_{P[1]} = -d_P shifted: d^{-2}_{P[1]} = -D: P^0 -> P^{-1}??
    # indices: P[1]^j = P^{j+1}: P[1]^{-2} = P^{-1}, P[1]^{-1} = P^0. differential
    # d^{-2}_{P[1]} = -D: P^{-1} -> P^0. h_{-1}: P^{-1} -> P[1]^{-1} = P^0. Not composable
    # with d^{-2}. hmm h_{-2}: P^{-1}... I think cleanest: brute force with total Hom
    # complex: Hom^n = oisum_{j} Hom(P^j, P^{j+n}), diff (d f) = d_P f - (-1)^n f d_P.
    # n=1: f = (f_{-1}: P^{-1}->P^0, f_0=0). df in Hom^2 = Hom(P^{-1}, P^1)=0. So all cycles.
    # Boundaries from Hom^0 = {(h_{-1}:P^{-1}->P^{-1}, h_0:P^0->P^0)}: d h has
    # (dh)_{-1} = D h_{-1} - h_0 D. So f presilting-iness: every f factors as D h_{-1} - h_0 D.
    Hb0,_ = hom_space_basis(src,src); Hb1,_ = hom_space_basis(tgt,tgt)
    Hf,_ = hom_space_basis(src,tgt)
    # vectorize over GF(p)
    import numpy as _np
    def vec(M): return _np.array(M).reshape(-1)%p
    Bnd = [vec(D@A) for A in Hb0] + [vec(-H@D) for H in Hb1]
    if not Hf: return True
    B = np.stack(Bnd,axis=1)%p if Bnd else np.zeros((Hf[0].size,0))
    # every F in span(Hf) must be in col-span(B)
    for F in Hf:
        v=vec(F)
        # solve B x = v
        M=np.concatenate([B, v.reshape(-1,1)],axis=1)%p
        m2,n2=M.shape
        R2=M.copy(); row=0
        for col in range(n2-1):
            piv=None
            for i in range(row,m2):
                if R2[i,col]%p!=0: piv=i;break
            if piv is None: continue
            R2[[row,piv]]=R2[[piv,row]]
            inv=pow(int(R2[row,col]),-1,p); R2[row]=(R2[row]*inv)%p
            for i in range(m2):
                if i!=row and R2[i,col]!=0: R2[i]=(R2[i]-R2[i,col]*R2[row])%p
            row+=1
        # inconsistent if pivot in last column with zero rest
        for i in range(m2):
            if np.all(R2[i,:-1]==0) and R2[i,-1]!=0:
                return False
    return True

sils=[]
for src_mask in itertools.product([0,1],repeat=3):
    for tgt_mask in itertools.product([0,1],repeat=3):
        src=[i for i,m in enumerate(src_mask) if m]; tgt=[i for i,m in enumerate(tgt_mask) if m]
        if not src and not tgt: continue
        if not src or not tgt: continue  # proper 2-term
        for D in all_maps(src,tgt):
            if is_presilting(src,tgt,D):
                # g-vector: [P^0]-[P^{-1}] in K0
                g=np.zeros(3,dtype=int)
                for j in tgt: g[j]+=1
                for i in src: g[i]-=1
                sils.append((tuple(src),tuple(tgt),tuple(g),D.reshape(-1).tolist()))
print("multiplicity-free presilting 2-term count (with differential multiplicity):", len(sils))
gs=sorted(set(s[2] for s in sils))
print("distinct g-vectors:", len(gs))
for g in gs: print(g)
