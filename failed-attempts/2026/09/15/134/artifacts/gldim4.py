"""Iterate minimal resolution with Betti tracking to test finite global dimension."""
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
def hom_basis(i,j): return [p for p in paths if src[p]==i and tgt[p]==j]
def mat_of_map(dom,cod,comps):
    db=sum([basis_P(i) for i in dom],[]); cb=sum([basis_P(i) for i in cod],[])
    doff=[];s=0
    for i in dom: doff.append(s);s+=len(basis_P(i))
    coff=[];s=0
    for i in cod: coff.append(s);s+=len(basis_P(i))
    M=np.zeros((len(cb),len(db)))
    for a,i in enumerate(dom):
        for b,j in enumerate(cod):
            m=comps.get((a,b),{})
            for t,g in enumerate(basis_P(i)):
                gi=doff[a]+t
                for mp,c in m.items():
                    r=lmult(mp,g)
                    if r is None: continue
                    row=coff[b]+basis_P(j).index(r)
                    M[row,gi]+=c
    return M

def min_betti_resolution(start, steps=8):
    """start: 'S0' or 'S1'. Build minimal resolution greedily:
    At each step, kernel K of current map (as subspace of source free module F).
    Next Betti = dim(K / rad K) computed via top projection; choose lifts.
    But kernel subspace isn't a free module quotient directly; Betti = dim Tor.
    We compute Tor_{n+1} dim via top projection rank, and continue with syzygy generators.
    Full iteration needs syzygy as module: represent K by basis matrix; next map from
    free module on top-classes. For gldim-finiteness test, track whether Betti dies.
    Here: implement syzygy representation: K subset F free; next free G with map G->F
    sending gens to chosen lifts of top-classes; then new syzygy = ker(G->F) + ... careful:
    minimal => new kernel contains rad G image... Standard: syzygy Omega = K as module
    with gen set = minimal gen set; represent elements of K as coords in F; multiply by arrows.
    """
    # Represent submodule K of F= (+) P_{dom} by row-space basis (ker of M) in coords of F.
    # Tops of F: coords at lazy positions. Minimal gens of K: rows whose top-projection is a basis.
    # New free G = (+) P over those top classes (vertex = top vertex of that summand... but top
    # class of K at summand a has vertex dom[a]).
    # Map G->F: gen e -> chosen lift vector v in K.
    # Next syzygy K2 = ker(G->F) as submodule of G, where G->F composed... but ker as subspaces suffices
    # since map lands in K and K=ker(prev). Yes: K2 = ker(matrix with cols v).
    # Action for minimality automatic.
    # Init: F0=P_start, M0=aeps (augmentation): K0 = rad.
    F=[start]  # F0 summands: single P
    # augmentation matrix: 1 x dim: [1,0,...]
    d=len(basis_P(start))
    M=np.zeros((1,d)); M[0,0]=1  # augmentation kills top
    betti=[1]
    K = None
    # K0 = ker M
    u,sig,vt=np.linalg.svd(M); r=np.sum(sig>1e-8); K=vt[r:]  # rows in F0 coords
    for step in range(steps):
        # F coords info
        # tops mask
        mask=[]
        for i in F:
            for g in basis_P(i): mask.append(0 if g in ('e0','e1') else 1)
        mask=np.array(mask)
        T=K[:,mask==0]
        rk=int(np.linalg.matrix_rank(T,1e-8))
        betti.append(rk)
        if rk==0:
            return betti, True
        # choose rk lifts: row-reduce T to find independent rows
        uu,ss,vv=np.linalg.svd(T)
        rr=np.sum(ss>1e-8)
        # independent rows: QR on T.T? use row echelon via SVD: take rows with pivot in column-pivoted QR
        import scipy.linalg as sl
        try:
            Q,R,Pv=sl.qr(T.T,pivoting=True)
            piv=sorted(Pv[:rr])
        except Exception:
            # fallback: greedy
            piv=[]; cur=None
            sel=np.zeros((0,T.shape[1]))
            for i in range(T.shape[0]):
                trial=np.vstack([sel,T[i:i+1]])
                if np.linalg.matrix_rank(trial,1e-8)>np.linalg.matrix_rank(sel,1e-8):
                    sel=trial; piv.append(i)
                if len(piv)==rr: break
        lifts=K[piv]
        # new free G: vertex of summand = F-vertex of each pivot's top position?
        # Each pivot row's top class: the nonzero top coords determine vertex; but a row may mix
        # vertices. Minimal gens are homogeneous: split each lift into vertex components.
        # Simpler: G has one summand per (pivot, vertex) with nonzero top part? That overcovers but
        # still computes Tor correctly? Overcover adds contractible summands; top-projection rank
        # next step still right? It inflates. Instead split lifts by vertex:
        newF=[]
        newlifts=[]
        for v in lifts:
            # split v into vertex parts according to F summand vertices
            offs=[];s=0
            for i in F: offs.append((s,i));s+=len(basis_P(i))
            parts={}
            for (s0,i) in offs:
                seg=v[s0:s0+len(basis_P(i))]
                # top coord of this segment:
                if abs(seg[0])>1e-9:
                    parts.setdefault(i,np.zeros_like(v))
                    parts[i][s0]=seg[0]
                    # hmm: generator at vertex i maps to top part + rad part; must include FULL v, not just top.
            # full v may mix vertices -> not homogeneous; split v into per-vertex sub-vectors
            for i,part in parts.items():
                # homogeneous component of v at vertex i:
                comp=np.zeros_like(v)
                for (s0,j) in offs:
                    if j==i: comp[s0:s0+len(basis_P(j))]=v[s0:s0+len(basis_P(j))]
                newF.append(i); newlifts.append(comp)
        # map G->F matrix columns = newlifts (in F coords): M2 is (dimF x dimG)? we need ker in G coords:
        A=np.column_stack(newlifts)  # dimF x dimG
        # K2 = ker A
        uu2,ss2,vv2=np.linalg.svd(A)
        rr2=np.sum(ss2>1e-8)
        K=vv2[rr2:]
        F=newF
        if len(K)==0:
            # need pad? if A injective, syzygy=0 -> resolution ends, but Betti recorded rk; append 0
            betti.append(0)
            return betti, True
    return betti, False

for s in [0,1]:
    try:
        b,fin=min_betti_resolution(s,steps=6)
        print(f"S{s}: Betti={b} finite={fin}")
    except Exception as e:
        import traceback; traceback.print_exc()
