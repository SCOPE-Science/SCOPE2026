import itertools, collections
from math import comb
import numpy as np

def build_Kfaces(V, Eset, K, s):
    verts = [(v,b) for v in V for b in range(s)]
    Kfaces = []
    for combo in itertools.combinations(verts, K+1):
        projs = set(v for (v,b) in combo)
        if len(projs) != 2: continue
        u, v = tuple(projs)
        if (u,v) not in Eset and (v,u) not in Eset: continue
        labels = [b for (vv,b) in combo]
        if len(set(labels)) != K+1: continue
        Kfaces.append(combo)
    return verts, Kfaces

def face_type(T):
    projs = {}
    for (v,b) in T:
        projs.setdefault(v, []).append(b)
    if len(projs) == 1: return ('fiber',)
    vs = sorted(projs)
    return ('trans', len(projs[vs[0]]))

def link_spectrum(F, faces_w):
    Fset = set(F)
    rest_map = []
    for T, w in faces_w.items():
        s = set(T)
        if Fset.issubset(s):
            rest = [v for v in T if v not in Fset]
            rest_map.append((rest, w))
    link_verts = sorted(set(v for (rest,w) in rest_map for v in rest))
    if not link_verts: return None
    idx = {v:i for i,v in enumerate(link_verts)}
    m = len(link_verts)
    W = np.zeros((m,m))
    for rest, w in rest_map:
        if len(rest) == 2:
            i, j = idx[rest[0]], idx[rest[1]]
            W[i,j] += w; W[j,i] += w
    deg = W.sum(axis=1)
    if np.any(deg <= 1e-12): return ('disconnected',)
    adj = W > 1e-12
    seen = {0}; stack=[0]
    while stack:
        a = stack.pop()
        for b in np.where(adj[a])[0]:
            if int(b) not in seen: seen.add(int(b)); stack.append(int(b))
    if len(seen) != m: return ('disconnected',)
    Dinv = np.diag(1.0/np.sqrt(deg))
    N = Dinv @ W @ Dinv
    ev = np.linalg.eigvalsh(N)
    l2 = ev[-2] if m >= 2 else -np.inf
    lmin = ev[0]
    return (float(l2), float(lmin), float(max(abs(l2), abs(lmin))), ev)

def worst_codim2(faces_w, d):
    codim = set()
    for T in faces_w:
        for sub in itertools.combinations(T, d-1):
            codim.add(tuple(sorted(sub)))
    worst=0; worstF=None; disc=0; l2max=-9; l2F=None
    for F in codim:
        sp = link_spectrum(F, faces_w)
        if sp is None: continue
        if sp[0]=='disconnected': disc+=1; worst=float('inf'); continue
        if sp[2]>worst: worst=sp[2]; worstF=(F,sp[0],sp[1])
        if sp[0]>l2max: l2max=sp[0]; l2F=F
    return worst, worstF, disc, len(codim), l2max, l2F

def oneskeleton_edges(top_faces):
    E=set()
    for T in top_faces:
        for u,v in itertools.combinations(T,2):
            E.add(tuple(sorted((u,v))))
    return E

def all_cliques(edges, verts, size):
    # brute force subsets of verts of given size all of whose pairs are edges
    Eset=set(edges)
    out=[]
    for combo in itertools.combinations(sorted(verts), size):
        ok=True
        for u,v in itertools.combinations(combo,2):
            if tuple(sorted((u,v))) not in Eset: ok=False; break
        if ok: out.append(tuple(sorted(combo)))
    return out

# ---- E2a: d=2 clique completion on C4 model K=3 s=4
V=[0,1,2,3]; E=[(0,1),(1,2),(2,3),(3,0)]; Eset=set(E)
verts,Kfaces=build_Kfaces(V,Eset,K=3,s=4)
d=2
faces={}; 
for Kf in Kfaces:
    for sub in itertools.combinations(Kf,d+1):
        key=tuple(sorted(sub))
        faces[key]=faces.get(key,0)+1  # induced multiplicity weight
edges=oneskeleton_edges(faces)
cliques=all_cliques(edges,verts,d+1)
missing=[c for c in cliques if c not in faces]
print(f"E2a d=2: dfaces={len(faces)} edges={len(edges)} cliques={len(cliques)} missing={len(missing)}",flush=True)
base={T:float(w) for T,w in faces.items()}
w0,wF,dc,nc,l2m,l2F=worst_codim2(base,d)
print(f"  base worst={w0:.4f} {wF} l2max={l2m:.4f} at {l2F}",flush=True)
for eps in [0.1,0.5,1.0,2.0]:
    fw=dict(base)
    for c in missing: fw[c]=eps
    # note: base weights are multiplicities (1..); missing get eps
    w,wF2,dc2,nc2,l2m2,l2F2=worst_codim2(fw,d)
    print(f"  eps={eps}: worst={w:.4f} {wF2} l2max={l2m2:.4f} at {l2F2} disc={dc2}",flush=True)

# ---- E2b: d=3 tightness on small models
for (K,s) in [(3,4),(4,4)]:
    verts,Kfaces=build_Kfaces(V,Eset,K=K,s=s)
    d=3
    faces2={}
    for Kf in Kfaces:
        for sub in itertools.combinations(Kf,d+1):
            key=tuple(sorted(sub))
            faces2[key]=faces2.get(key,0)+1
    fw={T:float(w) for T,w in faces2.items()}
    w,wF,dc,nc,l2m,l2F=worst_codim2(fw,d)
    print(f"E2b d=3 K={K} s={s}: dfaces={len(faces2)} codim2={nc} worst={w:.4f} {wF} l2max={l2m:.4f} at {l2F} disc={dc}",flush=True)
