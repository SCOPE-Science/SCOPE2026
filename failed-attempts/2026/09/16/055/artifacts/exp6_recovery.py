# Recovery test: closest tiny instance of Mao Thm-1.3 family (1-cube base, d=3, K=6).
# s=8 below the s>=2K requirement (fast) + s=12 exact-requirement if feasible.
# Question: can translation-invariant reweighting of the 3 tet orbits push max
# codim-2 second-eigenvalue strictly below 1/d=1/3?
import itertools, collections
import numpy as np

def build(V, Eset, K, s):
    verts=[(v,b) for v in V for b in range(s)]
    Kf=[]
    for combo in itertools.combinations(verts,K+1):
        S=set(v for (v,b) in combo)
        if len(S)!=2: continue
        u,v=tuple(S)
        if (u,v) not in Eset and (v,u) not in Eset: continue
        if len(set(b for (vv,b) in combo))!=K+1: continue
        Kf.append(combo)
    return verts,Kf

def stype(T):
    p={}
    for (v,b) in T: p.setdefault(v,[]).append(b)
    return tuple(sorted([len(x) for x in p.values()],reverse=True))

def l2max(F, fw):
    Fs=set(F); rm=[]
    for T,w in fw.items():
        if Fs.issubset(set(T)):
            r=[v for v in T if v not in Fs]; rm.append((r,w))
    lv=sorted(set(v for (r,w) in rm for v in r))
    if not lv: return None
    ix={v:i for i,v in enumerate(lv)}; m=len(lv)
    W=np.zeros((m,m))
    for r,w in rm:
        if len(r)==2:
            i,j=ix[r[0]],ix[r[1]]; W[i,j]+=w; W[j,i]+=w
    dg=W.sum(1)
    if np.any(dg<=1e-12): return float('inf')
    if np.any(dg<=0): return float('inf')
    D=np.diag(1.0/np.sqrt(dg)); N=D@W@D
    ev=np.linalg.eigvalsh(N)
    # connectivity check: eigenvalue 1 multiplicity 1
    if np.sum(ev>1-1e-8)>1: return float('inf')
    return float(ev[-2])

def run(s):
    V=[0,1]; Eset={(0,1)}; K=6; d=3
    verts,Kf=build(V,Eset,K,s)
    faces={}
    for Kface in Kf:
        for sub in itertools.combinations(Kface,d+1):
            k=tuple(sorted(sub)); faces[k]=faces.get(k,0)+1
    print(f"s={s}: |Vxs|={len(verts)} Kfaces={len(Kf)} dfaces={len(faces)} types={dict(collections.Counter(stype(T) for T in faces))}",flush=True)
    codim=set()
    for T in faces:
        for sub in itertools.combinations(T,d-1): codim.add(tuple(sorted(sub)))
    print(f"  codim2 faces: {len(codim)}",flush=True)
    base={T:float(w) for T,w in faces.items()}
    def worst(fw):
        w=-9; wF=None; dc=0
        for F in codim:
            v=l2max(F,fw)
            if v is None: continue
            if v==float('inf'): dc+=1; continue
            if v>w: w=v; wF=F
        return w,wF,dc
    w0,F0,dc0=worst(base)
    print(f"  induced weights: max-l2={w0:.4f} at {F0} disc={dc0}",flush=True)
    types=sorted(set(stype(T) for T in faces))
    grids=[(1,1,1),(3,1,1),(1,3,1),(1,1,3),(5,1,2),(1,4,1),(2,2,3),(4,1,1),(1,1,6),(0.2,1,1)]
    for g in grids:
        m=dict(zip(types,g))
        fw={T:float(m[stype(T)]) for T in faces}
        w,F,dc=worst(fw)
        print(f"  reweight {g}: max-l2={w:.4f} at {F} disc={dc}",flush=True)
run(8)
