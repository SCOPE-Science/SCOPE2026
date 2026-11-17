"""Exact rational diagnostics for graph fused-lasso perturbation seminorm.

Runs without third-party dependencies: python check.py
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb


def restricted_growth_partitions(n):
    def rec(i, tags, highest):
        if i == n:
            blocks = [[] for _ in range(highest + 1)]
            for v, k in enumerate(tags):
                blocks[k].append(v)
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(highest + 2):
            yield from rec(i + 1, tags + (j,), max(highest, j))
    yield from rec(1, (0,), 0)


def connected(vertices, edges):
    vertex = set(vertices)
    reached = {vertices[0]}
    queue = [vertices[0]]
    for u in queue:
        for a, b, _ in edges:
            v = b if a == u else a if b == u else None
            if v in vertex and v not in reached:
                reached.add(v)
                queue.append(v)
    return len(reached) == len(vertex)


def connected_partitions(n, edges):
    for blocks in restricted_growth_partitions(n):
        if all(connected(b, edges) for b in blocks):
            yield blocks


def tv(vec, edges):
    return sum((w * abs(vec[a] - vec[b]) for a, b, w in edges), Q(0))


def ave(blocks, h):
    o = [Q(0)] * len(h)
    for b in blocks:
        x = sum((h[i] for i in b), Q(0))/len(b)
        for j in b:
            o[j] = x
    return o


def cut_norm(n, edges, blocks):
    best = Q(0)
    best_mask = 0
    for mask in range(1, (1 << n)-1):
        h = [Q((mask >> i) & 1) for i in range(n)]
        ratio = tv(ave(blocks, h), edges) / tv(h, edges)
        if ratio > best:
            best, best_mask = ratio, mask
    return best, best_mask


def direct_norm_ternary(n, edges, blocks):
    best = Q(0)
    for v in product((-1, 0, 1), repeat=n):
        v = tuple(map(Q, v))
        den = tv(v, edges)
        if den:
            best = max(best, tv(ave(blocks, v), edges)/den)
    return best


def kkt_pair(n, edges, blocks, mask, eps=Q(1, 10000)):
    # The same block partition is the exact active face for two nearby inputs.
    h = [Q((mask >> j) & 1) for j in range(n)]
    ph = ave(blocks, h)
    levels = [Q(100*i) for i in range(len(blocks))]
    label = [0] * n
    for idx, b in enumerate(blocks):
        for j in b:
            label[j] = idx
    u0 = [levels[label[i]] for i in range(n)]
    u1 = [u0[i]+eps*ph[i] for i in range(n)]
    z0 = []
    for a, b, w in edges:
        if label[a] == label[b]:
            z0.append(Q(0))
        else:
            z0.append(w * (1 if u0[a] > u0[b] else -1))
    z1 = z0[:]
    r = [h[i]-ph[i] for i in range(n)]
    # On a spanning tree in each fused block, solve D^T dz=r exactly.
    for block in blocks:
        members = set(block)
        root = block[0]
        parent = {root: (-1, -1)}
        order = [root]
        for node in order:
            for eid, (a, b, w) in enumerate(edges):
                nb = b if a == node else a if b == node else None
                if nb in members and nb not in parent:
                    parent[nb] = (node, eid)
                    order.append(nb)
        assert len(order) == len(block)
        sub = {node: r[node] for node in block}
        for node in reversed(order[1:]):
            p, eid = parent[node]
            a, b, w = edges[eid]
            z1[eid] += eps * sub[node] * (1 if node == a else -1)
            sub[p] += sub[node]
        assert sub[root] == 0
    def Dt(z):
        v = [Q(0)] * n
        for k, (a, b, _) in enumerate(edges):
            v[a] += z[k]
            v[b] -= z[k]
        return v
    y0 = [u0[i] + Dt(z0)[i] for i in range(n)]
    y1 = [y0[i] + eps * h[i] for i in range(n)]
    assert all(y1[i] - u1[i] == Dt(z1)[i] for i in range(n))
    for k,(a,b,w) in enumerate(edges):
        if label[a]==label[b]:
            assert u0[a]==u0[b] and u1[a]==u1[b]
            assert abs(z0[k]) < w and abs(z1[k]) < w
        else:
            assert (u0[a]-u0[b])*(u1[a]-u1[b])>0
            assert z0[k] == z1[k] == w*(1 if u1[a]>u1[b] else -1)
    den = tv([y1[i]-y0[i] for i in range(n)], edges)
    assert den > 0
    assert tv([u1[i]-u0[i] for i in range(n)], edges)/den == tv(ph, edges)/tv(h, edges)
    return True


def bare(n, pairs, weights=None):
    if weights is None:
        weights=[1]*len(pairs)
    return [(a,b,Q(w)) for (a,b),w in zip(pairs, weights)]


def barbell(q):
    edges = bare(2*q, list(combinations(range(q),2)) + list(combinations(range(q,2*q),2)) + [(0,q)])
    a = b = q//2
    left = [0] + list(range(1,a))
    right = [q] + list(range(q+1,q+b))
    block = tuple(left + right)
    blocks = [block] + [(v,) for v in range(2*q) if v not in block]
    cutmask = (1<<q)-1
    h = [Q((cutmask>>i)&1) for i in range(2*q)]
    actual = tv(ave(blocks,h),edges)/tv(h,edges)
    predicted = Q(a*b*(2*q-a-b),a+b)
    assert actual == predicted
    assert kkt_pair(2*q,edges,blocks,cutmask)
    return actual


def main():
    c = 0
    for n in (3,4,5):
        graphs = {
            'path':bare(n,[(i,i+1) for i in range(n-1)]),
            'cycle':bare(n,[(i,(i+1)%n) for i in range(n)]),
            'star':bare(n,[(0,i) for i in range(1,n)]),
            'clique':bare(n,list(combinations(range(n),2)))
        }
        for name,edges in graphs.items():
            best = Q(0)
            best_case = None
            for blocks in connected_partitions(n,edges):
                cn,mask = cut_norm(n,edges,blocks)
                assert cn == direct_norm_ternary(n,edges,blocks)
                best = max(best,cn)
                c += 1
                if cn > 0 and 0<mask<(1<<n)-1:
                    assert kkt_pair(n,edges,blocks,mask)
            if name in ('path','cycle','clique'):
                assert best == 1, (n,name,best)
            if name=='star':
                assert best == max(Q(1),Q(n-2,2)),(n,name,best)
    for wts in ((1,2,3),(2,5,7),(3,1,4)):
        edges=bare(4,[(0,1),(1,2),(2,3)],wts)
        for blocks in connected_partitions(4,edges):
            assert cut_norm(4,edges,blocks)[0] == direct_norm_ternary(4,edges,blocks)
            c+=1
    for wts in ((2,3,5),(1,6,4)):
        edges=bare(3,[(0,1),(1,2),(0,2)],wts)
        for blocks in connected_partitions(3,edges):
            assert cut_norm(3,edges,blocks)[0] == direct_norm_ternary(3,edges,blocks)
            c+=1
    print('EXACT_CUT_REDUCTION_VS_TERNARY_POTENTIALS_PASSED',c)
    for q in (2,4,6,8,10):
        val=barbell(q)
        if q%2==0:
            assert val==Q(q*q,4)
    print('EXACT_KKT_REALIZABILITY_AND_QUADRATIC_BARBELL_WITNESSES_PASSED',5)
    print('ALL_GRAPH_ROF_PERTURBATION_TESTS_PASSED')

if __name__=='__main__':main()
