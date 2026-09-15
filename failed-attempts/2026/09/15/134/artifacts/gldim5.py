"""Correct minimal Betti: b_{n+1} = dim K - dim(JK), K syzygy subspace of free F, J arrow ideal acting by left concat."""
import numpy as np
paths=['e0','e1','a','b','c','ba','cb','cba']
src={'e0':0,'e1':1,'a':0,'b':1,'c':0,'ba':1,'cb':0,'cba':0}
tgt={'e0':0,'e1':1,'a':1,'b':0,'c':1,'ba':1,'cb':0,'cba':1}
def lmult(m,g):
    if m in ('e0','e1'):
        v=int(m[1]); return g if src[g]==v else None
    if g in ('e0','e1'):
        v=int(g[1]); return m if tgt[m]==v else None
    if tgt[m]!=src[g]: return None
    cand=m+g
    if 'ab' in cand or 'bc' in cand: return None
    return cand
def basis_P(i): return ['e0','a','c','cb','cba'] if i==0 else ['e1','b','ba']
ARROWS=['a','b','c']

def free_dim(F): return sum(len(basis_P(i)) for i in F)
def coords_info(F):
    offs=[];s=0
    for i in F: offs.append(s);s+=len(basis_P(i))
    return offs
def act_matrix(F, m):
    """matrix of left-mult by arrow m on F (dimF x dimF)."""
    offs=coords_info(F); d=free_dim(F)
    A=np.zeros((d,d))
    for a,i in enumerate(F):
        for t,g in enumerate(basis_P(i)):
            r=lmult(m,g)
            if r is None: continue
            # r starts at src(m): lands in summand(s) b with F[b]==src[r]; take first
            for b,j in enumerate(F):
                if j==src[r]:
                    A[offs[b]+basis_P(j).index(r), offs[a]+t]+=1
                    break
    return A

def syzygy_betti(F, K, steps=10):
    """F: summand list, K: row-basis matrix (k x dimF) of syzygy submodule. Returns betti list."""
    betti=[]
    for step in range(steps):
        k=K.shape[0]
        if k==0:
            betti.append(0); return betti, True
        # JK = span{ A_m v : m arrow, v row of K }
        JK=[]
        for m in ARROWS:
            A=act_matrix(F,m)
            for v in K:
                JK.append(A@v)
        JK=np.array(JK) if JK else np.zeros((0,free_dim(F)))
        # dim(K cap ... ) : JK rows lie in K? They should (K submodule? K=ker of module map, yes submodule).
        # b = dim K - dim JK as subspaces of F... but JK ⊂ K needed; verify
        # dim(K+JK)-dim(JK): use stacked rank
        rK=np.linalg.matrix_rank(K,1e-8)
        rJK=np.linalg.matrix_rank(JK,1e-8) if len(JK) else 0
        b=int(rK-rJK)
        betti.append(b)
        if b==0: return betti, True
        # new generators: complement of JK in K: rows of K independent of JK
        S=np.vstack([JK,K]) if len(JK) else K
        # greedy pick rows of K that raise rank over JK
        base=JK.copy() if len(JK) else np.zeros((0,free_dim(F)))
        rb=np.linalg.matrix_rank(base,1e-8) if len(base) else 0
        lifts=[]
        for v in K:
            t=np.vstack([base,v]) if len(base) else v.reshape(1,-1)
            r=np.linalg.matrix_rank(t,1e-8)
            if r>rb: lifts.append(v); base=t; rb=r
            if len(lifts)==b: break
        lifts=np.array(lifts)
        # new free G: vertex of each lift = vertex where its top component sits.
        # lifts may mix vertices; split homogenędous components: component at summand-block with vertex i.
        offs=coords_info(F)
        newF=[]; cols=[]
        for v in lifts:
            # per-vertex homogeneous parts
            for vert in [0,1]:
                comp=np.zeros_like(v)
                nz=False
                for a,i in enumerate(F):
                    if i==vert:
                        seg=v[offs[a]:offs[a]+len(basis_P(i))]
                        if np.any(np.abs(seg)>1e-9): nz=True
                        comp[offs[a]:offs[a]+len(basis_P(i))]=seg
                if nz:
                    newF.append(vert); cols.append(comp)
        A=np.column_stack(cols)
        u,ss,vv=np.linalg.svd(A); rr=np.sum(ss>1e-8)
        K=vv[rr:].copy()
        F=newF
    return betti, False

for s in [0,1]:
    F=[s]; d=free_dim(F)
    M=np.zeros((1,d)); M[0,0]=1
    u,sig,vt=np.linalg.svd(M); r=np.sum(sig>1e-8); K=vt[r:].copy()
    b,fin=syzygy_betti(F,K,steps=8)
    print(f"S{s}: Betti={b} done={fin}")
