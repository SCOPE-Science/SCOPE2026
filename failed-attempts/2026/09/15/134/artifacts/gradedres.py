"""Graded minimal resolutions for shape 4 with deg(a)=deg(c)=1-d, deg(b)=d, integer d.
Track homogeneous degrees; minimality = images in J (positive length). Gen vertex =
endpoint of lowest-DEGREE term. Verify finite graded pd for several d + general proof data."""
import numpy as np
from minres import basis_P, full_matrix, offs_of, dimF, ARROWS, rmult_path, ract, paths, src, tgt
DEG={'a':None,'b':None,'c':None,'e0':0,'e1':0,'ba':None,'cb':None,'cba':None}
def setup(d):
    DEG.update({'a':1-d,'b':d,'c':1-d,'ba':(1-d)+d,'cb':(1-d)+d,'cba':(1-d)+d+(1-d)})
    # ba: b then a: deg b+a = d+1-d=1; cb: 1; cba: 1-d+d+1-d=2-2d? c(1-d)+b(d)+a(1-d)=2-d... c+b+a=(1-d)+d+(1-d)=2-d. recompute: (1-d)+d+(1-d) = 2-d. And ba=(d)+(1-d)=1, cb=(1-d)+d=1.
    DEG.update({'ba':1,'cb':1,'cba':2-d})
    return DEG
def deg_of(p): return DEG[p]
def resolve_gr(start, d, steps=12):
    DEG=setup(d)
    F=[start]; d0=dimF(F)
    M=np.zeros((1,d0)); M[0,0]=1.0
    u,ss,vv=np.linalg.svd(M); K=vv[np.sum(ss>1e-8):].copy()
    Kdeg=[0]*K.shape[0]  # syzygy gens in degree 0 initially? augmentation kills top in deg 0
    # track degrees of basis elts of F: Fdeg list aligned with coords
    Fdeg=[]
    for i in F:
        for g in basis_P(i): Fdeg.append(deg_of(g))
    betti=[]  # list of dict vertex->list of shifts
    for step in range(steps):
        k=int(np.linalg.matrix_rank(K,1e-8)) if len(K) else 0
        if k==0: betti.append({}); return betti,True
        dd=dimF(F)
        JK=np.array([ract(F,m)@v for m in ARROWS for v in K])
        rJK=int(np.linalg.matrix_rank(JK,1e-8)) if len(JK) else 0
        b=k-rJK
        cur_shift_info={}
        if b==0:
            betti.append({}); return betti,True
        base=JK.copy() if len(JK) else np.zeros((0,dd))
        rb=rJK; lifts=[]
        for v in K:
            t=np.vstack([base,v]) if len(base) else v.reshape(1,-1)
            r=np.linalg.matrix_rank(t,1e-8)
            if r>rb: lifts.append(v.copy()); base=t; rb=r
            if len(lifts)==b: break
        o=offs_of(F); newF=[]; gen_imgs=[]; newFdeg_top=[]
        for v in lifts:
            for w in [0,1]:
                comp=ract(F,f'e{w}')@v
                if np.any(np.abs(comp)>1e-9):
                    # shift = degree of lowest-degree term in comp
                    terms=[]
                    for a,i in enumerate(F):
                        B=basis_P(i)
                        for t,g in enumerate(B):
                            c=comp[o[a]+t]
                            if abs(c)>1e-9: terms.append(Fdeg[o[a]+t])
                    sh=min(terms)
                    newF.append(w); gen_imgs.append(comp); newFdeg_top.append(sh)
                    cur_shift_info.setdefault(w,[]).append(sh)
        betti.append(cur_shift_info)
        A=full_matrix(newF, F, gen_imgs)
        uu,s2,v2=np.linalg.svd(A); K=v2[np.sum(s2>1e-8):].copy()
        # new F degrees: gen top in degree sh, other basis elts shifted
        Fdeg=[]
        for j,vj in enumerate(newF):
            for g in basis_P(vj): Fdeg.append(newFdeg_top[j]+deg_of(g))
        F=newF
    return betti,False
for d in [0,1,2,-1,3,5]:
    for s in [0,1]:
        b,fin=resolve_gr(s,d)
        print(f"d={d} S{s}: betti={b} finite={fin}")
