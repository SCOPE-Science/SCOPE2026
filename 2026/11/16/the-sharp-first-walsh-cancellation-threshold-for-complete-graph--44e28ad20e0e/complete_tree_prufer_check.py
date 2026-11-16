"""Independent Prüfer-code and integer Walsh transform verification for n=3..6.
Run with Python 3 (standard library only).
"""
from itertools import product
from math import comb

def spectrum(n):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    edge_id = {e:i for i,e in enumerate(edges)}
    N = 1 << len(edges)
    a = [0] * N
    for word in product(range(n),repeat=n-2):
        degree = [1] * n
        for v in word:
            degree[v] += 1
        mask = 0
        for v in word:
            u = next(i for i in range(n) if degree[i] == 1)
            degree[u] -= 1
            degree[v] -= 1
            mask |= 1 << edge_id[tuple(sorted((u,v)))]
        u,v = [i for i in range(n) if degree[i] == 1]
        mask |= 1 << edge_id[(u,v)]
        a[mask] += 1
    h=1
    while h<N:
        for i in range(0,N,2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]
                a[j],a[j+h]=u+v,u-v
        h*=2
    return a

for n in (3,4,5,6):
    W = spectrum(n)
    if n%2:
        assert all(x%2 for x in W) and all(x for x in W)
        print(f'n={n}: all Walsh coefficients odd/nonzero')
    else:
        p=n//2
        assert all(W[s]>0 for s in range(len(W)) if s.bit_count()<p-1)
        zeros=[s for s,v in enumerate(W) if s.bit_count()==p-1 and v==0]
        expected=comb(n,2) if p==2 else n*comb(n-1,p-1)
        assert len(zeros)==expected
        assert all(W[s]>0 for s in range(len(W)) if s.bit_count()==p-1 and s not in zeros)
        print(f'n={n}: first Walsh zeros at degree {p-1}, count {len(zeros)}')
print('COMPLETE_TREE_PRUFER_PASS')
