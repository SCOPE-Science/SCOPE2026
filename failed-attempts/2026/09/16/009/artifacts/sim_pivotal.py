"""Recovery test: Monte-Carlo pivotal probabilities for central II/III pair
in mixed percolation on centered square lattice.

Graph: Z2 vertices (L+1)x(L+1), face centers LxL (checkerboard II/III).
Adjacency: each face center <-> its 4 corner Z2 vertices (no direct Z2-Z2 edges).
Open chain alternates I <-> face-center. Left-right crossing: open chain from
x=0 column to x=L column.
Pivotality of a face-center v: flipping v (holding all else fixed) flips crossing.
Estimate P[v piv], P[v' piv] for central adjacent II/III pair, and Delta/delta^2.
If Delta = o(delta^2), then Delta/delta^2 -> 0 as L grows (delta=1/L).
If instead Delta ~ delta^{5/4}, ratio grows like L^{3/4}.
"""
import random
from collections import deque

def build(L):
    # index maps
    def zid(i,j): return ('z',i,j)
    def fid(i,j): return ('f',i,j)
    adj = {}
    for i in range(L+1):
        for j in range(L+1):
            adj[zid(i,j)] = []
    for i in range(L):
        for j in range(L):
            adj[fid(i,j)] = []
    for i in range(L):
        for j in range(L):
            f = fid(i,j)
            for (ii,jj) in [(i,j),(i+1,j),(i,j+1),(i+1,j+1)]:
                z = zid(ii,jj)
                adj[f].append(z)
                adj[z].append(f)
    return adj

def has_crossing(L, adj, openstat):
    # BFS from left column Z vertices that are open
    seen = set()
    dq = deque()
    for j in range(L+1):
        z = ('z',0,j)
        if openstat.get(z, False):
            # must be able to leave via an open face center; BFS handles
            dq.append(z); seen.add(z)
    while dq:
        u = dq.popleft()
        if u[0]=='z' and u[1]==L:
            return True
        for w in adj[u]:
            if w not in seen and openstat.get(w, False):
                seen.add(w); dq.append(w)
    return False

def estimate(L, q, n, seed=0):
    rng = random.Random(seed)
    adj = build(L)
    # central pair: pick face (ic,jc) with (ic+jc) even (type II), neighbor +x type III
    ic, jc = L//2, L//2
    if (ic+jc)%2==1: ic-=1
    v, vp = ('f',ic,jc), ('f',ic+1,jc)
    assert 0<=ic+1<L
    cnt_v = cnt_vp = 0
    # precompute vertex lists
    zlist = [('z',i,j) for i in range(L+1) for j in range(L+1)]
    flist = [('f',i,j) for i in range(L) for j in range(L)]
    for _ in range(n):
        st = {}
        for z in zlist: st[z] = (rng.random()<0.5)
        for (fi,fj) in [(f[1],f[2]) for f in flist]:
            if ((fi+fj)%2==0): st[('f',fi,fj)] = (rng.random()<q)
            else: st[('f',fi,fj)] = (rng.random()<(1-q))
        base = has_crossing(L, adj, st)
        # pivotal v: force open vs closed
        st[v]=True; c1 = has_crossing(L, adj, st)
        st[v]=False; c0 = has_crossing(L, adj, st)
        if c1!=c0: cnt_v+=1
        st[v]=True if rng.random()<0.5 else False  # restore irrelevant
        st[vp]=True; c1 = has_crossing(L, adj, st)
        st[vp]=False; c0 = has_crossing(L, adj, st)
        if c1!=c0: cnt_vp+=1
    pv, pvp = cnt_v/n, cnt_vp/n
    delta = 1.0/L
    return pv, pvp, (pv-pvp), (pv-pvp)/(delta**2)

if __name__=='__main__':
    for L,n in [(4,4000),(6,4000),(8,3000)]:
        for q in [0.0, 0.25]:
            pv,pvp,d,r = estimate(L,q,n,seed=123+L*10+int(q*100))
            print(f"L={L} q={q}: PII={pv:.4f} PIII={pvp:.4f} Delta={d:+.4f} Delta/d^2={r:+.3f}")
