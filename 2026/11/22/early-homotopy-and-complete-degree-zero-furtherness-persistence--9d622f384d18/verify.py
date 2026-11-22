"""Exact finite checks for early furtherness filtrations of upper-truncated Boolean posets.

Python 3 standard library only. Homology comparisons use independent mod-2
simplicial boundary reductions, not the graph-collapse argument in the proof.
"""
from itertools import combinations
from math import comb


def rank_gf2(vectors):
    piv = {}
    for v in vectors:
        while v:
            p = v.bit_length() - 1
            if p not in piv:
                piv[p] = v
                break
            v ^= piv[p]
    return len(piv), piv


def truncated_poset(n, r, k):
    root = (1 << k) - 1
    points = [a for a in range(1, 1 << n) if a.bit_count() >= r]
    def U(a):
        return [b for b in points if a & b == b]
    root_down = set(U(root))
    # Literal down-set differences; no closed formula used here.
    w = {a: sum(b not in root_down for b in U(a)) for a in points}
    return points, w


def simplicial_data(points, w, stage):
    pts = [a for a in points if w[a] <= stage]
    vertices = {a: i for i, a in enumerate(pts)}
    pairs = [(a, b) for a in pts for b in pts if a != b and a & b == a]
    E = {p: i for i, p in enumerate(pairs)}
    three = [(a,b,c) for a,b in pairs for c in pts if b != c and b & c == b]
    d1 = [(1 << vertices[a]) ^ (1 << vertices[b]) for a,b in pairs]
    d2 = [(1 << E[(a,b)]) ^ (1 << E[(a,c)]) ^ (1 << E[(b,c)]) for a,b,c in three]
    rank1, _ = rank_gf2(d1)
    rank2, basis2 = rank_gf2(d2)
    beta0 = len(pts) - rank1
    beta1 = len(pairs) - rank1 - rank2
    return pts, pairs, three, d1, d2, beta0, beta1, basis2


def cycle_basis(pts, pairs):
    # Edge vectors whose vertex boundary vanishes; construct by chord cycles.
    father = {v: v for v in pts}
    def find(x):
        while father[x] != x:
            father[x] = father[father[x]]
            x = father[x]
        return x
    tree = []
    chords = []
    for i, (a,b) in enumerate(pairs):
        aa,bb=find(a),find(b)
        if aa != bb:
            father[aa]=bb
            tree.append((i,a,b))
        else:
            chords.append((i,a,b))
    adj = {v:[] for v in pts}
    for i,a,b in tree:
        adj[a].append((b,i)); adj[b].append((a,i))
    cycles=[]
    for i,a,b in chords:
        stack=[(a,0)]; seen={a}
        path=None
        while stack:
            x,m=stack.pop()
            if x==b: path=m; break
            for y,j in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append((y,m^(1<<j)))
        assert path is not None
        cycles.append(path^(1<<i))
    return cycles


def test():
    tested=0; simplices2=0; injective_tests=0
    for n in range(3, 8):
        for r in range(2, n):
            for k in range(r, n):
                points,w=truncated_poset(n,r,k)
                stages=[0,1,r,r+1,r+2]
                results={t:simplicial_data(points,w,t) for t in stages}
                N0=comb(n,r)-comb(k,r)
                A=comb(k,r-1)*(n-k)
                I=N0-A
                B=(n-k)*(k-r)*comb(k,r-1)
                C=r*(comb(n,r+1)-comb(k,r+1))-N0
                assert I>=0 and B>=0 and C>=B, (n,r,k,I,B,C)
                targets={0:(1,0),1:(1+N0,0),r:(1+N0,0),
                         r+1:(1+I,B),r+2:(1,C)}
                for t in stages:
                    got=results[t]
                    assert (got[5],got[6])==targets[t], (n,r,k,t,(got[5],got[6]),targets[t])
                    simplices2 += len(got[2])
                # Independently test injectivity of H_1 at the first two
                # nontrivial stages by reducing prior cycles modulo new 2-boundaries.
                prev=results[r+1]; curr=results[r+2]
                index={p:i for i,p in enumerate(curr[1])}
                old_cycles=cycle_basis(prev[0],prev[1])
                embedded=[]
                for v in old_cycles:
                    z=0
                    for j,p in enumerate(prev[1]):
                        if (v>>j)&1:z^=1<<index[p]
                    embedded.append(z)
                rank_old_bound=rank_gf2(prev[4])[0]
                old_h1=len(old_cycles)-rank_old_bound
                rank_full_bound=rank_gf2(curr[4])[0]
                rank_joint=rank_gf2(curr[4]+embedded)[0]
                assert rank_joint-rank_full_bound == old_h1 == B, (n,r,k)
                injective_tests+=1;tested+=1
    print('VERIFY_OK cases=%d 2_simplices_scanned=%d H1_injections=%d'%(tested,simplices2,injective_tests))

if __name__=='__main__':
    test()
