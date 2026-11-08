#!/usr/bin/env python3
"""Independent finite checks for spanning-tree incidence traces on K_{3,n}.
No third-party packages or external data are required.
"""
from itertools import combinations
from math import comb


def spanning_trees(n):
    nv = n + 3
    edges = [(i, 3 + j) for j in range(n) for i in range(3)]
    out = []
    for ids in combinations(range(len(edges)), nv - 1):
        parent = list(range(nv))
        def root(v):
            while v != parent[v]:
                v = parent[v]
            return v
        good = True
        for k in ids:
            a, b = map(root, edges[k])
            if a == b:
                good = False
                break
            parent[a] = b
        if good and len({root(v) for v in range(nv)}) == 1:
            out.append(sum(1 << k for k in ids))
    return out


def predicted(mask, n):
    singles, doubles, zero = set(), [], False
    for j in range(n):
        ss = [i for i in range(3) if mask & (1 << (3*j+i))]
        if len(ss) == 3:
            return False
        if not ss:
            zero = True
        elif len(ss) == 1:
            singles.add(ss[0])
        else:
            doubles.append(tuple(ss))
    if len(doubles) > 2 or len(set(doubles)) != len(doubles):
        return False
    return zero or len(singles) >= 2


def poly(n):
    # Binomial expansion of sum_d binom(n,d) (3)_d z^(2d)
    # times [(1+3z)^(n-d) - b_(n-d)*z^(n-d)]
    coeff = [0] * (n + 3)
    for d in range(min(2, n) + 1):
        mult = comb(n,d) * (1 if d == 0 else 3 if d == 1 else 6)
        for k in range(n-d + 1):
            coeff[2*d+k] += mult * comb(n-d,k) * (3**k)
        coeff[n+d] -= mult * (1 if n == d else 3)
    return coeff


def check():
    total_supports = total_trees = 0
    for n in range(1,6):
        trees = spanning_trees(n)
        total_trees += len(trees)
        expected_trees = 3**(n-1)*n*n
        assert len(trees) == expected_trees, (n, len(trees), expected_trees)
        coeff = [0]*(3*n+1)
        for mask in range(1 << (3*n)):
            s = mask.bit_count()
            predicted_shattered = predicted(mask,n)
            if s > n+2:
                actual = False
            else:
                traces = {tree & mask for tree in trees}
                actual = len(traces) == (1 << s)
            assert predicted_shattered == actual, (n,mask,predicted_shattered,actual)
            coeff[s] += actual
            total_supports += 1
        assert coeff[:n+3] == poly(n) and not any(coeff[n+3:]), (n, coeff, poly(n))
        assert max(i for i,c in enumerate(coeff) if c)>0 or n == 1
        print('n',n,'trees',len(trees),'shattering_polynomial_coefficients',coeff)

    # Rank-2 base exchange holds for n=2: selected edges from distinct left rows.
    for mask in range(1 << 6):
        assert predicted(mask,2) == (mask.bit_count() <= 2 and
                  all((mask & (1 << i)) == 0 or (mask & (1 << (i+3))) == 0
                      for i in range(3)))

    # For n>=3, explicit exchange failures between maximal faces.
    for n in range(3,9):
        a = (1<<0)|(1<<2)|(1<<3)|(1<<4)
        b = (1<<0)|(1<<1)|(1<<3)|(1<<5)
        if n == 3:
            pass  # column 2 empty
        else:
            a |= (1 << (3*2+1)) | (1 << (3*3+0))
            b |= (1 << (3*2+1)) | (1 << (3*3+0))
            for j in range(4,n):
                a |= 1 << (3*j)
                b |= 1 << (3*j)
        assert predicted(a,n) and predicted(b,n)
        e = 1<<2
        assert a & e and not b & e
        for f in range(3*n):
            if (b >> f) & 1 and not ((a >> f) & 1):
                assert not predicted((a^e) | (1<<f),n), (n, f)
    print('K3N_SPANNING_TREE_SHATTER_PASS',total_supports,'supports',total_trees,'trees')

if __name__ == '__main__':
    check()
