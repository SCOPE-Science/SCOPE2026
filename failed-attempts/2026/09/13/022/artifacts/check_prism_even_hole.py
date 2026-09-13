"""Verify: every (long) prism contains an induced even hole.
Prism: triangles A={a1,a2,a3}, B={b1,b2,b3}, paths Pi: ai->bi of length Li>=1
(long prism: Li>=3), interiors disjoint, no edges between distinct paths
except triangle edges. Then for i<j, Cij = Pi + Pj + ai-aj + bi-bj is a cycle
of length Li+Lj+2; two of L1,L2,L3 share parity (pigeonhole) -> even cycle;
check it is induced (chordless) in the prism.
"""
import itertools

def build_prism(L):
    verts = ['a1','a2','a3','b1','b2','b3']
    idx = {v: k for k, v in enumerate(verts)}
    for i in (1,2,3):
        for t in range(1, L[i-1]):
            idx[f'p{i}_{t}'] = len(verts); verts.append(f'p{i}_{t}')
    n = len(verts)
    adj = [[0]*n for _ in range(n)]
    def e(u, v):
        adj[idx[u]][idx[v]] = adj[idx[v]][idx[u]] = 1
    for u,v in [('a1','a2'),('a2','a3'),('a1','a3'),
                ('b1','b2'),('b2','b3'),('b1','b3')]:
        e(u, v)
    for i in (1,2,3):
        chain = [f'a{i}'] + [f'p{i}_{t}' for t in range(1, L[i-1])] + [f'b{i}']
        for u, v in zip(chain, chain[1:]):
            e(u, v)
    return verts, adj

def chain(L, k):
    return [f'a{k}'] + [f'p{k}_{t}' for t in range(1, L[k-1])] + [f'b{k}']

def is_induced_cycle(verts, adj, cyc):
    idx = {v: k for k, v in enumerate(verts)}
    m = len(cyc)
    if m < 4:
        return False
    ids = [idx[v] for v in cyc]
    for t in range(m):
        for s in range(t+1, m):
            want = (s == t+1) or (t == 0 and s == m-1)
            if bool(adj[ids[t]][ids[s]]) != want:
                return False
    return True

ok = True
nchecked = 0
for L in itertools.product([1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]):
    verts, adj = build_prism(L)
    for (i, j) in [(1,2),(1,3),(2,3)]:
        if (L[i-1]+L[j-1]) % 2 == 0:
            cyc = chain(L,i) + chain(L,j)[::-1]
            assert len(cyc) == L[i-1]+L[j-1]+2, (L,i,j)
            nchecked += 1
            if not is_induced_cycle(verts, adj, cyc):
                print('FAIL induced cycle', L, i, j); ok = False
    # pigeonhole: some pair shares parity
    assert any((L[a]+L[b])%2==0 for a,b in [(0,1),(0,2),(1,2)])
print('even-parity induced cycles checked:', nchecked)
# long prisms: even cycle length >= 3+3+2 = 8
bad = [L for L in itertools.product([3,4,5,6,7],[3,4,5,6,7],[3,4,5,6,7])
       if not any((L[a]+L[b])%2==0 and L[a]+L[b]+2>=8 for a,b in [(0,1),(0,2),(1,2)])]
print('long-prism counterexamples to even-cycle>=8:', bad[:3] if bad else 'none')
print('RESULT:', 'OK -- every prism contains an induced even hole; every long prism contains an induced even cycle of length >= 8' if ok and not bad else 'FAILED')
