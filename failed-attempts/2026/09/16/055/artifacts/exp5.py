# Analytic check of the attaining eigenvector + a SMALL cube model (2-cube, K=4, s=8, d=3).
import itertools, collections
import numpy as np

def build_Kfaces(V, Eset, K, s):
    verts=[(v,b) for v in V for b in range(s)]
    out=[]
    for combo in itertools.combinations(verts,K+1):
        S=set(v for (v,b) in combo)
        if len(S)!=2: continue
        u,v=tuple(S)
        if (u,v) not in Eset and (v,u) not in Eset: continue
        if len(set(b for (vv,b) in combo))!=K+1: continue
        out.append(combo)
    return verts,out

def split_type(T):
    projs={}
    for (v,b) in T: projs.setdefault(v,[]).append(b)
    return tuple(sorted([len(x) for x in projs.values()],reverse=True))

def link_spec(F, faces_w, eigvec=False):
    Fset=set(F); rest_map=[]
    for T,w in faces_w.items():
        if Fset.issubset(set(T)):
            rest=[v for v in T if v not in Fset]; rest_map.append((rest,w))
    lv=sorted(set(v for (r,w) in rest_map for v in r))
    if not lv: return None
    idx={v:i for i,v in enumerate(lv)}; m=len(lv)
    W=np.zeros((m,m))
    for r,w in rest_map:
        if len(r)==2:
            i,j=idx[r[0]],idx[r[1]]; W[i,j]+=w; W[j,i]+=w
    deg=W.sum(1)
    if np.any(deg<=1e-12): return ('disconnected',)
    adj=W>1e-12; seen={0}; stack=[0]
    while stack:
        a=stack.pop()
        for b in np.where(adj[a])[0]:
            if int(b) not in seen: seen.add(int(b)); stack.append(int(b))
    if len(seen)!=m: return ('disconnected',)
    D=np.diag(1.0/np.sqrt(deg)); N=D@W@D
    if eigvec: ev,U=np.linalg.eigh(N); return ev,U,lv,W,deg
    ev=np.linalg.eigvalsh(N); return (float(ev[-2]),float(ev[0]),float(max(abs(ev[-2]),abs(ev[0]))),ev)

def worst(fw,d):
    codim=set()
    for T in fw:
        for sub in itertools.combinations(T,d-1): codim.add(tuple(sorted(sub)))
    w=0;wF=None;dc=0
    for F in codim:
        sp=link_spec(F,fw)
        if sp is None: continue
        if sp[0]=='disconnected': dc+=1; w=float('inf'); continue
        if sp[0]>w: w=sp[0]; wF=(F,sp[1],sp[2])
    return w,wF,dc,len(codim)

# square base: V=4-cycle... use single square: V={0,1,2,3}, E=C4. K=4,s=8,d=3
V=[0,1,2,3]; E=[(0,1),(1,2),(2,3),(3,0)]; Eset=set(E)
K=4; s=8; d=3
verts,Kfaces=build_Kfaces(V,Eset,K,s)
print(f"square model: Kfaces={len(Kfaces)}",flush=True)
faces={}
for Kf in Kfaces:
    for sub in itertools.combinations(Kf,d+1):
        key=tuple(sorted(sub)); faces[key]=faces.get(key,0)+1
print(f"  dfaces={len(faces)} types={dict(collections.Counter(split_type(T) for T in faces))}",flush=True)
base={T:float(w) for T,w in faces.items()}
w,wF,dc,nc=worst(base,d)
print(f"  base worst={w:.4f} {wF} disc={dc} codim2={nc}",flush=True)
F=wF[0]
ev,U,lv,W,deg=link_spec(F,base,eigvec=True)
es=np.sort(ev)
print(f"  F={F}; link n={len(lv)} top4={es[-4:]} bot3={es[:3]}",flush=True)
# top eigenvector: aggregate by (fiber==F-fiber?, label)
from collections import defaultdict
top=U[:,np.argmax(ev)]
pi=deg/deg.sum()
# decompose top vector vs sqrt(pi) (trivial)
triv=np.sqrt(pi); triv/=np.linalg.norm(triv)
overlap=float(top@triv)
print(f"  overlap(top,triv)={overlap:.4f}",flush=True)
res=top-overlap*triv
agg=defaultdict(float)
for v,r in zip(lv,res):
    agg[v[0]]+=r
print(f"  residual mass by fiber: {dict(agg)}",flush=True)
