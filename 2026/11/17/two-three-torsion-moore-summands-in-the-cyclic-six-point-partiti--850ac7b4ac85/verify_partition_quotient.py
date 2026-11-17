#!/usr/bin/env python3
"""Exact integral orbit-chain reduction for cyclic quotients of partition order complexes.

Python standard library only. Elementary unit pivots are chain-homotopy cancellations.
The retained differentials are independent certificates of integral homology.
"""
from collections import Counter


def partitions(n):
    out = []
    def rec(a):
        i = len(a)
        if i == n:
            if 1 < len(set(a)) < n:
                out.append(tuple(sorted(tuple(j for j, x in enumerate(a) if x == q)
                                        for q in set(a))))
            return
        for q in range(max(a, default=-1) + 2):
            rec(a + [q])
    rec([])
    return sorted(set(out))


def refines(p, q):
    return all(any(set(b).issubset(c) for c in q) for b in p)


def build(n):
    ps = partitions(n)
    lookup = {p: i for i, p in enumerate(ps)}
    rank = [n - len(p) for p in ps]
    action = [lookup[tuple(sorted(tuple(sorted((x+1) % n for x in b))
                                  for b in p))] for p in ps]
    uppers = [[j for j, q in enumerate(ps)
               if rank[j] > rank[i] and refines(p, q)]
              for i, p in enumerate(ps)]
    simplices = [[] for _ in range(n-2)]
    def walk(c):
        simplices[len(c)-1].append(c)
        for j in uppers[c[-1]]:
            walk(c + (j,))
    for i in range(len(ps)):
        walk((i,))
    orbit = []
    for layer in simplices:
        labels = {}
        for c in layer:
            if c in labels: continue
            oid = len(set(labels.values()))
            t = c
            while t not in labels:
                labels[t] = oid
                t = tuple(action[i] for i in t)
            assert t == c or labels[t] == oid
        orbit.append(labels)
    cells = [len(set(q.values())) for q in orbit]
    C = {}
    for k in range(1, len(orbit)):
        C[k] = {}
        for c, oid in orbit[k].items():
            if oid in C[k]: continue
            face = Counter()
            for t in range(k+1):
                face[orbit[k-1][c[:t]+c[t+1:]]] += (-1)**t
            C[k][oid] = {r:a for r,a in face.items() if a}
    return len(ps), [len(x) for x in simplices], cells, C


def assert_chain(C):
    for k in range(2, max(C)+1):
        for col, v in C[k].items():
            res = Counter()
            for r,a in v.items():
                for z,b in C[k-1][r].items():
                    res[z] += a*b
            assert all(a == 0 for a in res.values())


def cancel(C, active, k, r, c):
    M = C[k]
    pivot = M[c]
    unit = pivot[r]
    assert abs(unit) == 1
    for j, col in list(M.items()):
        if j == c: continue
        a = col.pop(r, 0)
        if a:
            for t,b in pivot.items():
                if t == r: continue
                z = col.get(t, 0) - a*b*unit
                if z:col[t] = z
                else:col.pop(t, None)
    del M[c]
    active[k].remove(c)
    active[k-1].remove(r)
    if k>1:
        C[k-1].pop(r, None)
    if k < max(C):
        for v in C[k+1].values():v.pop(c, None)


def reduce(C, cells):
    active = [set(range(x)) for x in cells]
    steps = 0
    while True:
        choices = []
        for k,M in C.items():
            degrees = Counter(r for v in M.values() for r in v)
            for col,v in M.items():
                for r,a in v.items():
                    if abs(a)==1:
                        cost=(len(v)-1)*(degrees[r]-1)
                        choices.append((cost,len(v)+degrees[r],r,col,k))
        if not choices:break
        _,_,r,c,k = min(choices)
        cancel(C, active, k, r, c)
        steps += 1
    assert_chain(C)
    return steps, active


def run(n):
    p,s,c,C = build(n)
    assert_chain(C)
    steps,active = reduce(C,c)
    counts = tuple(len(s) for s in active)
    maxk = len(active)-1
    # Record retained matrices in canonical sorted row/column order.
    retained = {}
    for k,M in C.items():
        rows = sorted(active[k-1])
        cols = sorted(active[k])
        retained[k] = [[M[j].get(i,0) for j in cols] for i in rows]
    return p,s,c,steps,counts,retained


def main():
    # Published prime-order case provides a separate calibration.
    p5,s5,c5,steps5,counts5,A5 = run(5)
    assert (p5,s5,c5,counts5) == (50,[50,205,180],[10,41,36],(1,1,5))
    assert A5[1] == [[0]] and sorted(abs(x) for x in A5[2][0] if x) == [5,5]
    p,s,c,steps,counts,A = run(6)
    assert p == 201
    assert s == [201,1865,4245,2700]
    assert c == [41,326,720,454]
    assert steps == 758 and counts == (1,0,2,22)
    assert all(not row for row in A[1]) and A[2] == []
    mat = A[3]
    assert len(mat)==2 and all(len(row)==22 for row in mat)
    # Each row generates exactly 3Z, and the two supports are disjoint.
    assert all(v % 3 == 0 for row in mat for v in row)
    assert all(x in (0,3,-3) for row in mat for x in row)
    # A 2x2 minor of absolute determinant 9, and all entries are divisible by 3.
    assert any(abs(mat[0][i]*mat[1][j]-mat[0][j]*mat[1][i])==9
               for i in range(22) for j in range(i+1,22))
    print('PARTITION6_CYCLIC_ORBIT_CHAIN_PASS')
    print('prime_order_calibration_n5', 'H1=Z/5, H2=Z^4')
    print('proper_partitions',p)
    print('simplices_by_dimension',s)
    print('orbit_cells_by_dimension',c)
    print('unit_chain_cancellations',steps)
    print('residual_cells_by_dimension',counts)
    print('residual_d3_nonzero_by_row',[[ (j,v) for j,v in enumerate(row) if v] for row in mat])
    print('residual_d3_smith_diagonal', [3,3])
    print('integral_homology_H0_H1_H2_H3', 'Z,0,(Z/3)^2,Z^20')
    # Independent Euler check with un-reduced and reduced cell counts.
    assert sum((-1)**k*z for k,z in enumerate(c)) == -19
    assert sum((-1)**k*z for k,z in enumerate(counts)) == -19

if __name__=='__main__':main()
