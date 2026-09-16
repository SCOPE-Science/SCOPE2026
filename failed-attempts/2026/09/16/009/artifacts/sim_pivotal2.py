"""Scaled-up recovery test: per-pair pivotal asymmetry Delta_delta(v)/delta^2
for the central II/III pair, q in {0.0, 0.25}, L in {6,8,12,16}.
Paired design: both pivotalities measured on the SAME base configuration
(save/force/restore each vertex), so Delta has a paired standard error.
Crossing: open-chain left-right crossing on centered square lattice
(Z vertices + face centers, alternating adjacency).
Outputs: per-(L,q) estimates with SEs + log-log scaling fit of |Delta| vs delta.
"""
import random, math
from collections import deque
from collections import namedtuple

def build(L):
    adj = {}
    for i in range(L+1):
        for j in range(L+1):
            adj[('z',i,j)] = []
    for i in range(L):
        for j in range(L):
            adj[('f',i,j)] = []
    for i in range(L):
        for j in range(L):
            f = ('f',i,j)
            for (ii,jj) in ((i,j),(i+1,j),(i,j+1),(i+1,j+1)):
                z = ('z',ii,jj)
                adj[f].append(z)
                adj[z].append(f)
    # Original square-lattice edges between Z2 vertices (full Gs adjacency)
    for i in range(L+1):
        for j in range(L+1):
            z = ('z',i,j)
            if i < L:
                w = ('z',i+1,j)
                adj[z].append(w); adj[w].append(z)
            if j < L:
                w = ('z',i,j+1)
                adj[z].append(w); adj[w].append(z)
    return adj

def has_crossing(L, adj, st):
    # Full centered-square adjacency: Z-Z nearest-neighbor edges are added
    # to adj once at build time (see build()). BFS unchanged.
    seen = set()
    dq = deque()
    for j in range(L+1):
        z = ('z',0,j)
        if st[z]:
            dq.append(z); seen.add(z)
    while dq:
        u = dq.popleft()
        if u[0]=='z' and u[1]==L:
            return True
        for w in adj[u]:
            if w not in seen and st[w]:
                seen.add(w); dq.append(w)
    return False

def run_cell(L, q, n, seed):
    rng = random.Random(seed)
    adj = build(L)
    ic, jc = L//2, L//2
    if (ic+jc)%2==1: ic-=1
    if ic+1>=L: ic-=2
    v, vp = ('f',ic,jc), ('f',ic+1,jc)
    zlist = [('z',i,j) for i in range(L+1) for j in range(L+1)]
    flist = [('f',i,j) for i in range(L) for j in range(L)]
    s_d = s_d2 = 0.0
    c_v = c_vp = 0
    for _ in range(n):
        st = {}
        for z in zlist: st[z] = (rng.random()<0.5)
        for (fi,fj) in ((f[1],f[2]) for f in flist):
            st[('f',fi,fj)] = (rng.random()<q) if (fi+fj)%2==0 else (rng.random()<(1-q))
        bv, bvp = st[v], st[vp]
        st[v]=True; c1 = has_crossing(L,adj,st)
        st[v]=False; c0 = has_crossing(L,adj,st)
        a = 1 if c1!=c0 else 0
        st[v]=bv
        st[vp]=True; c1 = has_crossing(L,adj,st)
        st[vp]=False; c0 = has_crossing(L,adj,st)
        b = 1 if c1!=c0 else 0
        st[vp]=bvp
        d = a-b
        s_d+=d; s_d2+=d*d; c_v+=a; c_vp+=b
    mean = s_d/n
    var = (s_d2 - s_d*s_d/n)/(n-1) if n>1 else 0.0
    se = math.sqrt(max(var,0.0)/n)
    delta = 1.0/L
    return {'L':L,'q':q,'n':n,'PII':c_v/n,'PIII':c_vp/n,
            'Delta':mean,'SE':se,'ratio':mean/delta**2,
            'ratioSE':se/delta**2}

if __name__=='__main__':
    import json
    plan = [(6,20000),(8,12000),(12,6000),(16,4000)]
    out = []
    k=0
    for (L,n) in plan:
        for q in (0.0,0.25):
            k+=1
            r = run_cell(L,q,n,seed=9000+k)
            out.append(r)
            print(f"L={r['L']:3d} q={r['q']:.2f} n={r['n']:6d} PII={r['PII']:.4f} "
                  f"PIII={r['PIII']:.4f} Delta={r['Delta']:+.4f}±{r['SE']:.4f} "
                  f"Delta/d^2={r['ratio']:+.2f}±{r['ratioSE']:.2f}", flush=True)
    with open('output/artifacts/sim_results.json','w') as f:
        json.dump(out,f,indent=1)
    # log-log fit per q: log|Delta| = a + b*log(delta)
    for q in (0.0,0.25):
        xs=[];ys=[]
        for r in out:
            if r['q']==q and r['Delta']!=0:
                xs.append(math.log(1.0/r['L'])); ys.append(math.log(abs(r['Delta'])))
        mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
        den=sum((x-mx)**2 for x in xs)
        b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/den
        a=my-b*mx
        print(f"q={q}: fitted |Delta| ~ delta^{b:.3f} (target needs exponent >= 2; 4-arm prediction 1.25)")


def run_total(L, q, n, seed, margin=1):
    """Estimate E[S], S = sum_II 1{piv} - sum_III 1{piv}, with interior split.
    Returns dict with total, interior (|face inset by margin|), boundary parts."""
    rng = random.Random(seed)
    adj = build(L)
    zlist = [('z',i,j) for i in range(L+1) for j in range(L+1)]
    flist = [('f',i,j) for i in range(L) for j in range(L)]
    def interior(f):
        _,i,j = f
        return (margin <= i < L-margin) and (margin <= j < L-margin)
    s_tot=s_tot2=0.0; s_in=s_in2=0.0
    for _ in range(n):
        st = {}
        for z in zlist: st[z] = (rng.random()<0.5)
        for (fi,fj) in ((f[1],f[2]) for f in flist):
            st[('f',fi,fj)] = (rng.random()<q) if (fi+fj)%2==0 else (rng.random()<(1-q))
        base = has_crossing(L,adj,st)
        # For each face center: pivotal iff forcing open vs closed straddles base.
        # Open-forced crossing: if st[v] open then equals base else recompute; same closed.
        tot=in_ = 0
        for f in flist:
            b = st[f]
            st[f]=True; c1 = base if b else has_crossing(L,adj,st)
            st[f]=False; c0 = has_crossing(L,adj,st) if b else base
            st[f]=b
            if c1!=c0:
                sgn = 1 if ((f[1]+f[2])%2==0) else -1
                tot += sgn
                if interior(f): in_ += sgn
        s_tot+=tot; s_tot2+=tot*tot; s_in+=in_; s_in2+=in_*in_
    import math
    def ms(s,s2):
        m = s/n
        v = (s2-s*s/n)/(n-1) if n>1 else 0.0
        return m, math.sqrt(max(v,0.0)/n)
    mt,set_ = ms(s_tot,s_tot2); mi,sei = ms(s_in,s_in2)
    return {'L':L,'q':q,'n':n,'margin':margin,'E_Stot':mt,'SE_tot':set_,
            'E_Sint':mi,'SE_int':sei,'E_Sbdy':mt-mi}

if __name__=='__main__2__':
    pass
