#!/usr/bin/env python3
"""Finite tests for graph reductions of perfect evolution-algebra isomorphism.

This checker is corroborative: the universal assertions have symbolic proofs.
"""
from itertools import product, permutations


def nonsingular(a, p):
    n = len(a)
    b = [list(map(lambda x: x % p, row)) for row in a]
    r = 0
    for c in range(n):
        k = next((j for j in range(r, n) if b[j][c]), None)
        if k is None:
            continue
        b[r], b[k] = b[k], b[r]
        inv = pow(b[r][c], -1, p)
        b[r] = [(x * inv) % p for x in b[r]]
        for j in range(n):
            if j != r:
                coeff = b[j][c]
                b[j] = [(x - coeff*y) % p for x,y in zip(b[j], b[r])]
        r += 1
    return r == n


def algebra_isomorphic(a, b, p):
    n=len(a)
    for sig in permutations(range(n)):
        for scal in product(range(1,p), repeat=n):
            if all(a[i][j]*scal[j] % p == scal[i]**2*b[sig[i]][sig[j]] % p
                   for i in range(n) for j in range(n)):
                return True
    return False


def colored_graph(a, p):
    n=len(a)
    generator={2:1,3:2}[p]
    verts=list(product(range(n),range(1,p)))
    pos={v:i for i,v in enumerate(verts)}
    edges={}
    for i,t in verts:
        u=pos[(i,t)]
        v=pos[(i,(generator*t)%p)]
        edges[u,v]=edges.get((u,v),0)|1
        for j in range(n):
            if a[i][j]:
                v=pos[(j,(t*t*a[i][j])%p)]
                edges[u,v]=edges.get((u,v),0)|2
    return tuple(edges.get((i,j),0) for i in range(len(verts)) for j in range(len(verts)))


def canonical_colored_graph(a,p):
    n=len(a)*(p-1)
    arcs=colored_graph(a,p)
    return min(tuple(arcs[sig[i]*n+sig[j]] for i in range(n) for j in range(n))
               for sig in permutations(range(n)))


def simple_graphs(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    for bits in product((0,1),repeat=len(edges)):
        yield tuple(tuple(1 if (min(i,j),max(i,j)) in [edges[k] for k,b in enumerate(bits) if b] else 0
                          for j in range(n)) for i in range(n))


def graph_key(a):
    n=len(a)
    return min(tuple(a[sig[i]][sig[j]] for i in range(n) for j in range(n))
               for sig in permutations(range(n)))


def connected_universal_extension(a):
    n=len(a)
    # Original vertices, unique universal hub, and n+2 new leaves.
    m=2*n+3
    hub=n
    h=[[0]*m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            h[i][j]=a[i][j]
    for i in range(m):
        if i!=hub:
            h[hub][i]=h[i][hub]=1
    return h


def encode_simple_evolution(h):
    m=len(h)
    a=[[0]*(2*m) for _ in range(2*m)]
    for i in range(m):
        for j in range(m):
            a[i][j]=h[i][j] if i!=j else 1
        a[i][m+i]=1
        a[m+i][i]=1
    return a


def strong_graph(a):
    n=len(a)
    for start in range(n):
        seen={start}; frontier=[start]
        while frontier:
            i=frontier.pop()
            for j in range(n):
                if a[i][j] and j not in seen:
                    seen.add(j); frontier.append(j)
        if len(seen)!=n:
            return False
    return True


def decode_universal_extension(h, n):
    m=len(h)
    hub=n
    assert m==2*n+3
    assert sum(h[hub])==m-1
    assert all(sum(row)<m-1 for i,row in enumerate(h) if i!=hub)
    # All original nonisolated vertices have degree >= 2, while original
    # isolated vertices and the added leaves have degree exactly 1.
    high=[i for i in range(m) if i!=hub and sum(h[i])>=2]
    adj=tuple(tuple(h[i][j] for j in high) for i in high)
    return graph_key(adj), n-len(high)


def gf4_mul(a,b):
    c=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:
                c ^= 1 << (i+j)
    if c & 4:
        c ^= 7  # X^2 = X + 1.
    return c


def gf4_isomorphic(a,b):
    for sig in permutations(range(2)):
        for s in product((1,2,3),repeat=2):
            if all(gf4_mul(a[i][j],s[j]) ==
                   gf4_mul(gf4_mul(s[i],s[i]),b[sig[i]][sig[j]])
                   for i in range(2) for j in range(2)):
                return True
    return False


def gf4_graph(a):
    verts=list(product(range(2),(1,2,3)))
    pos={v:i for i,v in enumerate(verts)}
    edges={}
    for i,t in verts:
        u=pos[(i,t)]
        v=pos[(i,gf4_mul(2,t))]
        edges[u,v]=edges.get((u,v),0)|1
        for j in range(2):
            if a[i][j]:
                v=pos[(j,gf4_mul(gf4_mul(t,t),a[i][j]))]
                edges[u,v]=edges.get((u,v),0)|2
    arcs=tuple(edges.get((i,j),0) for i in range(6) for j in range(6))
    return min(tuple(arcs[sig[i]*6+sig[j]] for i in range(6) for j in range(6))
               for sig in permutations(range(6)))


def main():
    pairs=0; tested=0
    for p in (2,3):
        mats=[]
        for data in product(range(p),repeat=4):
            a=(data[:2],data[2:]);
            if nonsingular(a,p): mats.append(a)
        assert len(mats)==(6 if p==2 else 48)
        keys={a:canonical_colored_graph(a,p) for a in mats}
        for a in mats:
            for b in mats:
                assert algebra_isomorphic(a,b,p)==(keys[a]==keys[b]), (p,a,b)
                pairs+=1
        tested+=len(mats)
    # Non-prime finite field check: GF(4) = GF(2)[X]/(X^2+X+1).
    gf4_matrices=[]
    for data in product(range(4),repeat=4):
        a=(data[:2],data[2:]);
        det=gf4_mul(a[0][0],a[1][1]) ^ gf4_mul(a[0][1],a[1][0])
        if det: gf4_matrices.append(a)
    assert len(gf4_matrices)==180
    sample=gf4_matrices[::12]
    keys={a:gf4_graph(a) for a in sample}
    for a in sample:
        for b in sample:
            assert gf4_isomorphic(a,b)==(keys[a]==keys[b]),(a,b)
            pairs+=1
    graph_cases=0
    graph_iso_classes={}
    for n in range(1,5):
        graphs=list(simple_graphs(n))
        entries=[]
        for g in graphs:
            h=connected_universal_extension(g)
            a=encode_simple_evolution(h)
            assert nonsingular(a,2) and nonsingular(a,3)
            assert strong_graph(a)
            # Simple algebras have a unique natural basis up to scalings/permutations.
            # The looped/unlooped partition and the unique cross edges recover h.
            m=len(h)
            assert all(a[i][i]==1 for i in range(m))
            assert all(a[m+i][m+i]==0 for i in range(m))
            assert all(sum(a[m+i])==1 and a[m+i][i]==1 for i in range(m))
            recovered=decode_universal_extension(h,n)
            original=(graph_key(g),0)
            nonisolates=[i for i in range(n) if sum(g[i])>0]
            expected=(graph_key(tuple(tuple(g[i][j] for j in nonisolates) for i in nonisolates)), n-len(nonisolates))
            assert recovered==expected
            entries.append((g,recovered))
            graph_cases+=1
        for g,r in entries:
            for g2,r2 in entries:
                assert (graph_key(g)==graph_key(g2)) == (r==r2)
        graph_iso_classes[n]=len(set(r for g,r in entries))
    print('VERIFY_OK fields=2,3,4 prime_field_matrices=%d graph_comparison_pairs=%d simple_graphs=%d graph_iso_classes=%s' %
          (tested,pairs,graph_cases,graph_iso_classes))

if __name__=='__main__': main()
