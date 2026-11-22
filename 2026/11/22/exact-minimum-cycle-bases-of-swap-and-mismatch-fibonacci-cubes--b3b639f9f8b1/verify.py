#!/usr/bin/env python3
"""Independent exact finite-instance checks of cycle-space theorem for Fibonacci swap-mismatch graphs.
This finite verification supplements (does not replace) the all-length proof.
Run: python3 verify.py
"""
from itertools import combinations
from collections import Counter

def fibs(n):
    a,b=0,1
    F=[a]
    for _ in range(n+2):
        F.append(b)
        a,b=b,a+b
    return F

def rank2(vectors):
    piv={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i in piv: v^=piv[i]
            else: piv[i]=v; break
    return len(piv)

def main():
    for n in range(1,12):
        vert=[''.join(map(str,b)) for b in __import__('itertools').product((0,1),repeat=n) if '11' not in ''.join(map(str,b))]
        pos={w:i for i,w in enumerate(vert)}
        edges={}; bit_edges=set(); swap_edges=set()
        for a,b in combinations(vert,2):
            diff=[i for i in range(n) if a[i]!=b[i]]
            key=(pos[a],pos[b])
            if len(diff)==1:
                edges[key]=len(edges); bit_edges.add(key)
            elif len(diff)==2 and diff[1]==diff[0]+1 and a[diff[0]]!=a[diff[1]]:
                edges[key]=len(edges); swap_edges.add(key)
        neighbors={i:set() for i in pos.values()}
        for (a,b) in edges: neighbors[a].add(b); neighbors[b].add(a)
        triangles=[]
        for a in neighbors:
            for b,c in combinations(sorted(neighbors[a]),2):
                if a<b<c and c in neighbors[b]: triangles.append((a,b,c))
        squares=[]
        for a in range(len(vert)):
            for c in range(a+1,len(vert)):
                if sum(vert[a][i]!=vert[c][i] for i in range(n))!=2: continue
                commons=sorted(neighbors[a]&neighbors[c]); commons=[b for b in commons if (min(a,b),max(a,b)) in bit_edges and (min(b,c),max(b,c)) in bit_edges]
                for b,d in combinations(commons,2): squares.append((a,b,c,d))
        def vec(cyc):
            ans=0
            for a,b in zip(cyc,cyc[1:]+cyc[:1]): ans ^= 1<<edges[(min(a,b),max(a,b))]
            return ans
        tri_vec=[vec(list(t)) for t in triangles]; sq_vec=[vec(list(s)) for s in squares]
        F=fibs(n)
        H=(n*F[n+1]+2*(n+1)*F[n])//5
        T=(2*n*F[n+1]-(n+1)*F[n])//5
        betaH=H-F[n+2]+1
        beta=H+T-F[n+2]+1
        L=(2*n-4)*F[n+1]+(n-3)*F[n]+4
        assert len(vert)==F[n+2],(n,len(vert),F[n+2])
        assert len(bit_edges)==H,(n,len(bit_edges),H)
        assert len(swap_edges)==T,(n,len(swap_edges),T)
        assert len(triangles)==T,(n,len(triangles),T)
        assert all(sum((min(a,b),max(a,b)) in swap_edges for a,b in zip(t,t[1:]+t[:1]))==1 for t in triangles)
        ctr=Counter(e for t in triangles for e in ((min(a,b),max(a,b)) for a,b in zip(t,t[1:]+t[:1])) if e in swap_edges)
        assert all(ctr[e]==1 for e in swap_edges)
        assert rank2(sq_vec)==betaH,(n,'square rank',rank2(sq_vec),betaH)
        assert rank2(tri_vec+sq_vec)==beta,(n,'full rank',rank2(tri_vec+sq_vec),beta)
        assert 3*T+4*betaH==L
        print(f'n={n:2} vertices={len(vert):4} bit_edges={H:5} swap_edges=triangles={T:5} squares={len(squares):5} cycle_rank={beta:5} min_basis_length={L:6} PASS')
if __name__=='__main__': main()
