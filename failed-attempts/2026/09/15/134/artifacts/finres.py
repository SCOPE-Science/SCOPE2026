"""Finite minimal free resolution over the 8-dim algebra, block-diagonal action.
Right modules; free F=(+) P_{v}; arrow action block-diagonal by left concat."""
import numpy as np
paths=['e0','e1','a','b','c','ba','cb','cba']
src={'e0':0,'e1':1,'a':0,'b':1,'c':0,'ba':1,'cb':0,'cba':0}
tgt={'e0':0,'e1':1,'a':1,'b':0,'c':1,'ba':1,'cb':0,'cba':1}
def lmult(m,g):
    # left concat m*g (maps act on right modules by left multiplication): needs tgt(m)==src(g)
    if m in ('e0','e1'):
        v=int(m[1]); return g if tgt[g]==v else None
    if g in ('e0','e1'):
        v=int(g[1]); return m if src[m]==v else None
    if tgt[m]!=src[g]: return None
    cand=m+g
    if 'ab' in cand or 'bc' in cand: return None
    return cand
def basis_P(i): return ['e0','a','c','cb','cba'] if i==0 else ['e1','b','ba']
ARROWS=['a','b','c']
def offs_of(F):
    o=[];s=0
    for i in F: o.append(s);s+=len(basis_P(i))
    return o
def act(F,m):
    o=offs_of(F); d=sum(len(basis_P(i)) for i in F)
    A=np.zeros((d,d))
    for a,i in enumerate(F):
        B=basis_P(i)
        for t,g in enumerate(B):
            r=lmult(m,g)
            if r is None: continue
            assert src[r]==i, (m,g,r)
            A[o[a]+B.index(r), o[a]+t]+=1
    return A

def rmult_path(g,x):
    # right concat g*x on paths: needs tgt(g)==src(x); result src(g)->tgt(x), same summand
    if x in ('e0','e1'):
        v=int(x[1]); return g if tgt[g]==v else None
    if g in ('e0','e1'):
        v=int(g[1]); return x if src[x]==v else None
    if tgt[g]!=src[x]: return None
    cand=g+x
    if 'ab' in cand or 'bc' in cand: return None
    return cand
def actJ(F,m):
    # J-action on F by right concat with arrow m: block-diagonal
    o=offs_of(F); d=sum(len(basis_P(i)) for i in F)
    A=np.zeros((d,d))
    for a,i in enumerate(F):
        B=basis_P(i)
        for t,g in enumerate(B):
            r=rmult_path(g,m)
            if r is None: continue
            assert src[r]==i,(g,m,r)
            A[o[a]+B.index(r), o[a]+t]+=1
    return A

def resolve(start, steps=10):
    F=[start]; d=len(basis_P(start))
    M=np.zeros((1,d)); M[0,0]=1.0
    u,ss,vv=np.linalg.svd(M); K=vv[np.sum(ss>1e-8):].copy()
    betti=[]
    for step in range(steps):
        k=int(np.linalg.matrix_rank(K,1e-8)) if len(K) else 0
        if k==0: betti.append(0); return betti,True
        JK=np.array([actJ(F,m)@v for m in ARROWS for v in K]) if k else np.zeros((0,d))
        rJK=int(np.linalg.matrix_rank(JK,1e-8)) if len(JK) else 0
        b=k-rJK
        betti.append(b)
        if b==0: return betti,True
        base=JK.copy() if len(JK) else np.zeros((0,d))
        rb=rJK; lifts=[]
        for v in K:
            t=np.vstack([base,v]) if len(base) else v.reshape(1,-1)
            r=np.linalg.matrix_rank(t,1e-8)
            if r>rb: lifts.append(v); base=t; rb=r
            if len(lifts)==b: break
        lifts=np.array(lifts)
        o=offs_of(F); newF=[]; cols=[]
        for v in lifts:
            for vert in [0,1]:
                comp=np.zeros_like(v); nz=False
                for a,i in enumerate(F):
                    if i==vert:
                        seg=v[o[a]:o[a]+len(basis_P(i))]
                        if np.any(np.abs(seg)>1e-9): nz=True
                        comp[o[a]:o[a]+len(basis_P(i))]=seg
                if nz: newF.append(vert); cols.append(comp)
        A=np.column_stack(cols)
        uu,s2,v2=np.linalg.svd(A); K=v2[np.sum(s2>1e-8):].copy()
        F=newF
    return betti,False
for s in [0,1]:
    print(f"S{s}:", resolve(s, steps=10))
