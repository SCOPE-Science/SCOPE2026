"""Minimal free resolutions, correct freeness extension.
Represent free module elements in path-coords; map G->F from gen images extended by right action.
Simpler robust approach: work with matrices over the algebra via path-coefficient
linear algebra: represent map F1->F0 by gen-image matrix with entries in A (as dicts),
kernel computed by expanding to full path-coord matrices (block: image of basis elt
g of summand j = m_j * g, left concat)."""
import numpy as np
paths=['e0','e1','a','b','c','ba','cb','cba']
src={'e0':0,'e1':1,'a':0,'b':1,'c':0,'ba':1,'cb':0,'cba':0}
tgt={'e0':0,'e1':1,'a':1,'b':0,'c':1,'ba':1,'cb':0,'cba':1}
def lmult(m,g):
    if m in ('e0','e1'):
        v=int(m[1]); return g if tgt[g]==v else None
    if g in ('e0','e1'):
        v=int(g[1]); return m if src[m]==v else None
    if tgt[m]!=src[g]: return None
    cand=m+g
    if 'ab' in cand or 'bc' in cand: return None
    return cand
def rmult_path(g,x):
    if x in ('e0','e1'):
        v=int(x[1]); return g if tgt[g]==v else None
    if g in ('e0','e1'):
        v=int(g[1]); return x if src[x]==v else None
    if tgt[g]!=src[x]: return None
    cand=g+x
    if 'ab' in cand or 'bc' in cand: return None
    return cand
def basis_P(i): return ['e0','a','c','cb','cba'] if i==0 else ['e1','b','ba']
ARROWS=['a','b','c']
def offs_of(F):
    o=[];s=0
    for i in F: o.append(s);s+=len(basis_P(i))
    return o
def dimF(F): return sum(len(basis_P(i)) for i in F)

def full_matrix(F1, F0, gen_imgs):
    """gen_imgs[j] = image of top gen e of summand j, as coord vector in F0.
    Full map: basis elt (g in summand j) |-> gen_img_j * g?? NO: f(g) = f(e_j * g) = f(e_j)*g = right action of g on f(e_j).
    Right action of path g on vector in F0: each summand block: rmult_path-coords. Implement J-action matrices R(F0, path)."""
    o1=offs_of(F1); o0=offs_of(F0)
    M=np.zeros((dimF(F0), dimF(F1)))
    # precompute right-action matrices on F0 for every path
    R={p: ract(F0,p) for p in paths}
    for j,vj in enumerate(F1):
        Bj=basis_P(vj)
        for t,g in enumerate(Bj):
            M[:, o1[j]+t] = R[g] @ gen_imgs[j]
    return M

def ract(F, p):
    o=offs_of(F); d=dimF(F)
    A=np.zeros((d,d))
    for a,i in enumerate(F):
        B=basis_P(i)
        for t,g in enumerate(B):
            r=rmult_path(g,p)
            if r is None: continue
            assert src[r]==i
            A[o[a]+B.index(r), o[a]+t]+=1
    return A

def top_vertex_of_vec(F, v):
    o=offs_of(F)
    for a,i in enumerate(F):
        if abs(v[o[a]])>1e-9: return i
    return None

def resolve(start, steps=12):
    F0=[start]; d0=dimF(F0)
    # augmentation: gen_imgs none; M0 = [1,0..] kills top
    M=np.zeros((1,d0)); M[0,0]=1.0
    u,ss,vv=np.linalg.svd(M); K=vv[np.sum(ss>1e-8):].copy()
    F=F0
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
        # split lifts into homogeneous components -> new summands
        o=offs_of(F); newF=[]; gen_imgs=[]
        for v in lifts:
            for vert in [0,1]:
                comp=np.zeros_like(v); nz=False
                for a,i in enumerate(F):
                    if i==vert:
                        seg=v[o[a]:o[a]+len(basis_P(i))]
                        if np.any(np.abs(seg)>1e-9): nz=True
                        comp[o[a]:o[a]+len(basis_P(i))]=seg
                if nz: newF.append(vert); gen_imgs.append(comp)
        A=full_matrix(newF, F, gen_imgs)
        uu,s2,v2=np.linalg.svd(A); K=v2[np.sum(s2>1e-8):].copy()
        F=newF
    return betti,False

for s in [0,1]:
    print(f"S{s}:", resolve(s, steps=12))
