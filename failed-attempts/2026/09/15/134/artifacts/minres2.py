"""Minimal resolutions v2: gen vertex from lowest-term path endpoints.
Homogeneous lift splitting: group path-terms by (length), take minimal length L;
vertex set = {tgt(p) : coeff != 0, len L}. For mixed vertices, split lift into
per-vertex parts (terms grouped by tgt of length-L terms... approximate: group ALL
terms by tgt? No: higher terms belong to the gen they extend. Proper: quotient
K/JK is semisimple; classes have well-defined vertex support. Compute class in
K/JK, decompose by vertex via top-idempotents e_w acting on the right: class*e_w.
Implement: for lift v in F, per-vertex part v*e_w (right action of lazy path),
which projects to the S_w-isotypic part of its class. Use these as gen images."""
import numpy as np
from minres import basis_P, ract, full_matrix, offs_of, dimF, ARROWS, rmult_path, paths, src, tgt
def eact(F, v, w):
    return ract(F, f'e{w}') @ v
def resolve(start, steps=12):
    F=[start]; d0=dimF(F)
    M=np.zeros((1,d0)); M[0,0]=1.0
    u,ss,vv=np.linalg.svd(M); K=vv[np.sum(ss>1e-8):].copy()
    betti=[]
    for step in range(steps):
        k=int(np.linalg.matrix_rank(K,1e-8)) if len(K) else 0
        if k==0: betti.append(0); return betti,True
        d=dimF(F)
        JK=np.array([ract(F,m)@v for m in ARROWS for v in K])
        rJK=int(np.linalg.matrix_rank(JK,1e-8)) if len(JK) else 0
        b=k-rJK
        betti.append(b)
        if b==0: return betti,True
        base=JK.copy() if len(JK) else np.zeros((0,d))
        rb=rJK; lifts=[]
        for v in K:
            t=np.vstack([base,v]) if len(base) else v.reshape(1,-1)
            r=np.linalg.matrix_rank(t,1e-8)
            if r>rb: lifts.append(v.copy()); base=t; rb=r
            if len(lifts)==b: break
        o=offs_of(F); newF=[]; gen_imgs=[]
        for v in lifts:
            for w in [0,1]:
                comp=eact(F,v,w)
                if np.any(np.abs(comp)>1e-9):
                    newF.append(w); gen_imgs.append(comp)
        A=full_matrix(newF, F, gen_imgs)
        # sanity: image of each gen top must equal its lift class mod JK (exact here)
        uu,s2,v2=np.linalg.svd(A); K=v2[np.sum(s2>1e-8):].copy()
        F=newF
    return betti,False
for s in [0,1]:
    print(f"S{s}:", resolve(s, steps=12))
