"""Independent finite checks for acyclic sink counts on square bouquets.

Usage: python artifacts/verify.py
No nonstandard dependencies. A finite check does not establish the root-count theorem.
"""
from collections import Counter
from itertools import product
from math import comb


def graph(r):
    # Vertex 0 is the shared vertex; each block has three private vertices.
    ed = []
    for i in range(r):
        a, b, c = 3*i + 1, 3*i + 2, 3*i + 3
        ed.extend(((0, a), (a, b), (b, c), (c, 0)))
    return 3*r + 1, ed


def direct_counts(r):
    n, ed = graph(r)
    coeff = Counter()
    for dirs in product((0, 1), repeat=len(ed)):
        indeg = [0]*n
        outdeg = [0]*n
        out = [[] for _ in range(n)]
        for (a, b), flip in zip(ed, dirs):
            if flip:
                a, b = b, a
            out[a].append(b)
            outdeg[a] += 1
            indeg[b] += 1
        # Kahn check: orientation must be acyclic.
        available = [v for v in range(n) if indeg[v] == 0]
        reached = 0
        while available:
            v = available.pop()
            reached += 1
            for w in out[v]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    available.append(w)
        if reached == n:
            coeff[sum(d == 0 for d in outdeg)] += 1
    return coeff


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x*y
    return c


def poly_pow(a, r):
    v = [1]
    for _ in range(r):
        v = poly_mul(v, a)
    return v


def expected_counts(r):
    t = poly_pow([3, 10, 1], r)
    b = poly_mul([-1, 1], poly_pow([3, 1], r))
    out = [0]*max(len(t), len(b))
    for i, x in enumerate(t):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while out and out[-1] == 0:
        out.pop()
    return out


def check_local_cycle():
    n, edges = graph(1)
    T = Counter()
    B = Counter()
    for flip in product((0, 1), repeat=4):
        outdeg = [0]*n
        indeg = [0]*n
        out = [[] for _ in range(n)]
        for (a,b),bit in zip(edges,flip):
            if bit:
                a,b=b,a
            outdeg[a]+=1
            indeg[b]+=1
            out[a].append(b)
        q=[i for i in range(n) if indeg[i]==0]
        seen=0
        while q:
            v=q.pop()
            seen+=1
            for w in out[v]:
                indeg[w]-=1
                if indeg[w]==0:
                    q.append(w)
        if seen!=n:
            continue
        k=sum(outdeg[v]==0 for v in range(1,n))
        T[k]+=1
        if outdeg[0]==0:
            B[k]+=1
    assert [T[k] for k in range(3)] == [3,10,1]
    assert [B[k] for k in range(2)] == [3,1]
    print('LOCAL_C4_TABLE_OK',dict(T),dict(B))


def coeff_derivative_at_zero(c):
    return c[1] if len(c)>1 else 0


def main():
    check_local_cycle()
    for r in range(1, 5):
        got=direct_counts(r)
        want=expected_counts(r)
        assert all(got[k]==want[k] for k in range(len(want)))
        assert not any(k>=len(want) for k in got)
        assert sum(got.values())==14**r
        print('DIRECT_ACYCLIC_ORIENTATIONS_OK',r,14**r,'coefficients',want)
    for r in range(1,101):
        c=expected_counts(r)
        assert c[0]==0
        assert coeff_derivative_at_zero(c)==(3*r+1)*3**r
        assert sum(c)==14**r
        assert all(v>0 for v in c[1:])
        assert len(c)==2*r+1
    print('COEFFICIENT_IDENTITIES_OK r=1..100')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
