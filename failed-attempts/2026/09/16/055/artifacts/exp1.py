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

def d_faces_from_K(Kfaces, d):
    agg = collections.defaultdict(int)
    faces = {}
    for Kf in Kfaces:
        for sub in itertools.combinations(Kf, d+1):
            key = tuple(sorted(sub))
            agg[key] += 1
            faces[key] = face_type(key)
    return faces, agg

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

def run_case(V, E, K, s, d, ratios):
    Eset = set(E)
    verts, Kfaces = build_Kfaces(V, Eset, K, s)
    faces, agg = d_faces_from_K(Kfaces, d)
    types = sorted(set(faces.values()))
    print(f"G: |V|={len(V)} |E|={len(E)} K={K} s={s} d={d}: |VxL|={len(verts)} Kfaces={len(Kfaces)} dfaces={len(faces)} types={types}", flush=True)
    codim = set()
    for T in faces:
        for sub in itertools.combinations(T, d-1):
            codim.add(tuple(sorted(sub)))
    print(f"  codim2 faces: {len(codim)}", flush=True)
    for r in ratios:
        fw = {}
        for T, tp in faces.items():
            fw[T] = r if tp[0]=='fiber' else 1.0
        worst = 0; worstF=None; disc=0
        for F in codim:
            sp = link_spectrum(F, fw)
            if sp is None: continue
            if sp[0]=='disconnected': disc+=1; worst=float('inf'); continue
            if sp[2]>worst: worst=sp[2]; worstF=(F,sp[0],sp[1])
        print(f"  ratio(fiber/trans)={r}: worst={worst:.4f} {worstF} disc={disc}", flush=True)

V = [0,1,2,3]; E = [(0,1),(1,2),(2,3),(3,0)]
print("=== d=2, K=3, s=4 (vertex links, bound 1/2) ===", flush=True)
run_case(V, E, K=3, s=4, d=2, ratios=[0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 100.0])
