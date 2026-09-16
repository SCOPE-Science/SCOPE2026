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

def split_type(T):
    # sorted tuple of fiber-class sizes, e.g. (4,),(3,1),(2,2) for d=3
    projs = {}
    for (v,b) in T:
        projs.setdefault(v, []).append(b)
    return tuple(sorted([len(x) for x in projs.values()], reverse=True))

def link_spectrum_full(F, faces_w):
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
    ev, U = np.linalg.eigh(N)
    l2 = ev[-2] if m >= 2 else -np.inf
    lmin = ev[0]
    return (float(l2), float(lmin), float(max(abs(l2), abs(lmin))), ev, U, link_verts, W, deg)

def worst_codim2(faces_w, d, verbose=False):
    codim = set()
    for T in faces_w:
        for sub in itertools.combinations(T, d-1):
            codim.add(tuple(sorted(sub)))
    worst=0; worstF=None; disc=0
    bytype = collections.defaultdict(list)
    for F in codim:
        sp = link_spectrum_full(F, faces_w)
        if sp is None: continue
        if sp[0]=='disconnected': disc+=1; worst=float('inf'); continue
        # type of F: fiber edge vs transverse edge
        projs = set(v for (v,b) in F)
        ft = 'fiber' if len(projs)==1 else 'trans'
        bytype[ft].append(sp[2])
        if sp[2]>worst: worst=sp[2]; worstF=(F,sp[0],sp[1])
    return worst, worstF, disc, len(codim), {k:max(v) for k,v in bytype.items()}

# single-edge graph: V={0,1}, one edge. K=4, s=8, d=3 (need s>=K+1=5 ok; Thm needs s>=2K=8 ✓)
V=[0,1]; E=[(0,1)]; Eset=set(E)
K=4; s=8; d=3
verts,Kfaces=build_Kfaces(V,Eset,K,s)
faces={}
for Kf in Kfaces:
    for sub in itertools.combinations(Kf,d+1):
        key=tuple(sorted(sub))
        faces[key]=faces.get(key,0)+1
print(f"model: |Vxs|={len(verts)} Kfaces={len(Kfaces)} dfaces={len(faces)}",flush=True)
tc=collections.Counter(split_type(T) for T in faces)
print(f"  tet types: {dict(tc)}",flush=True)
base={T:float(w) for T,w in faces.items()}
w,wF,dc,nc,bt=worst_codim2(base,d)
print(f"  base: worst={w:.4f} {wF} disc={dc} codim2={nc} bytype={bt}",flush=True)
# reweight by split type
types = sorted(set(split_type(T) for T in faces))
print(f"  orbit types: {types}",flush=True)
import itertools as it
for combo in [(1,1,1),(2,1,1),(1,3,1),(1,1,4),(3,2,1),(1,0.2,2)]:
    wmap=dict(zip(types,combo))
    fw={T:float(wmap[split_type(T)]) for T in faces}
    w,wF,dc,nc,bt=worst_codim2(fw,d)
    print(f"  weights {combo}: worst={w:.4f} face={wF} bytype={bt}",flush=True)
