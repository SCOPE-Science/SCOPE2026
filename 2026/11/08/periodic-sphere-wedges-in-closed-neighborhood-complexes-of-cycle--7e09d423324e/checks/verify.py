#!/usr/bin/env python3
"""Finite checks for closed-neighborhood complexes of cycle-deleted K_{n,n}.

Self-contained Python 3 verifier.  It tests small instances; the infinite
homotopy assertion is established by the separate written argument.
"""
from itertools import combinations
from collections import defaultdict

def subfaces(mask):
    verts = [j for j in range(mask.bit_length()) if mask >> j & 1]
    for k in range(len(verts) + 1):
        for subset in combinations(verts, k):
            yield sum(1 << j for j in subset)

def data(n):
    # u_i=i, v_j=n+j.  Delete u_i v_i and u_i v_(i+1).
    E = {(i, n + j) for i in range(n) for j in range(n)
         if j not in (i, (i + 1) % n)}
    A = [(1 << i) | sum(1 << (n + j) for j in range(n)
                               if (i, n + j) in E) for i in range(n)]
    B = [(1 << (n + j)) | sum(1 << i for i in range(n)
                               if (i, n + j) in E) for j in range(n)]
    return E, A, B

def full_complex(facets):
    result = set()
    for F in facets:
        result.update(subfaces(F))
    return result

def reduced_betti_mod2(faces):
    by = defaultdict(list)
    for m in faces:
        by[m.bit_count() - 1].append(m)
    # Finite nonempty complex: ordinary homology rank in dimension 0
    # is converted into reduced homology by subtracting one.
    ranks = {}
    for dim in sorted(by):
        if dim < 1: continue
        positions = {m:j for j,m in enumerate(by[dim-1])}
        pivots = {}
        for f in by[dim]:
            bd = 0
            x = f
            while x:
                b = x & -x
                x ^= b
                bd ^= 1 << positions[f ^ b]
            while bd:
                t = bd.bit_length() - 1
                if t in pivots: bd ^= pivots[t]
                else:
                    pivots[t] = bd
                    break
        ranks[dim] = len(pivots)
    ans = {dim:len(by[dim]) - ranks.get(dim,0) - ranks.get(dim+1,0)
           for dim in by if dim >= 0}
    ans[0] = ans.get(0,0) - 1
    return {dim:v for dim,v in ans.items() if v}

def cycle_independent(n):
    return {m for m in range(1 << n)
            if all(not ((m >> i & 1) and (m >> ((i+1)%n) & 1))
                   for i in range(n))}

def cycle_dual(n):
    indep = cycle_independent(n)
    mask = (1 << n)-1
    return {m for m in range(1 << n) if (mask ^ m) not in indep}

def predicted(n):
    ans = {2: n*n - 4*n + 1}
    k, r = divmod(n, 3)
    if r == 0: dim,multiplicity = 2*k-2, 4
    else: dim,multiplicity = 2*k-1, 2
    ans[dim] = ans.get(dim, 0) + multiplicity
    return ans

def run():
    for n in (7,8,9,10,11):
        E,A,B = data(n)
        assert len(E) == n * (n-2)
        allfaces=full_complex(A+B)
        faces_a=full_complex(A)
        faces_b=full_complex(B)
        # A∩B is exactly the original bipartite graph.
        graphfaces={0} | {1<<i for i in range(2*n)}
        graphfaces |= {(1<<i)|(1<<j) for i,j in E}
        assert faces_a & faces_b == graphfaces
        assert faces_a | faces_b == allfaces
        # Shore complexes are exactly Alexander duals of cycle independence.
        KA=full_complex([f & ((1<<n)-1) for f in B])
        KV=full_complex([f >> n for f in A])
        expected=cycle_dual(n)
        assert KA == expected == KV
        assert all(m in expected for m in range(1<<n) if m.bit_count()<=3)
        got=reduced_betti_mod2(allfaces)
        assert got == predicted(n),(n,got,predicted(n))
        print(f'n={n} edges={len(E)} faces={len(allfaces)} '
              f'complex_A={len(faces_a)} complex_B={len(faces_b)} '
              f'reduced_betti_mod2={got}', flush=True)
    print('ALL_VERIFY_OK',flush=True)

if __name__=='__main__':run()
