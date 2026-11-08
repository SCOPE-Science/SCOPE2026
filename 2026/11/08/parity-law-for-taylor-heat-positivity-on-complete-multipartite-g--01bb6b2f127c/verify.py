"""Exact-arithmetic finite checks for Taylor heat updates on complete multipartite graphs.

Run: python3 verify.py
The infinite-order/graph-family proof is in RESULT.md; finite tests are support only.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import product


def taylor(order, x):
    return sum(((-x)**j / Q(factorial(j)) for j in range(order + 1)), Q(0))


def graph_laplacian(partition):
    n = sum(partition)
    classes = [j for j, a in enumerate(partition) for _ in range(a)]
    return [[Q(n - partition[classes[i]]) if i == j else
             (Q(-1) if classes[i] != classes[j] else Q(0))
             for j in range(n)] for i in range(n)], classes


def mul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def update(L, p, x):
    n = len(L)
    P = [[Q(i == j) for j in range(n)] for i in range(n)]
    T = [[Q(i == j) for j in range(n)] for i in range(n)]
    for k in range(1, p + 1):
        P = mul(P, L)
        coeff = (-x/Q(n))**k/Q(factorial(k))
        for i in range(n):
            for j in range(n):
                T[i][j] += coeff * P[i][j]
    return T


def closed(partition, classes, p, x, i, j):
    n = sum(partition)
    F = taylor(p, x)
    if classes[i] != classes[j]:
        return (1 - F)/n
    a = partition[classes[i]]
    c = Q(n-a,n)
    other = (c*F + 1-c - taylor(p,c*x))/a
    return other + (taylor(p,c*x) if i==j else 0)


def compositions(n):
    for mask in range(1 << (n-1)):
        cut = [0] + [i for i in range(1,n) if (mask >> (i-1)) & 1] + [n]
        if len(cut)>2:
            yield [cut[i+1]-cut[i] for i in range(len(cut)-1)]


def main():
    checks = 0
    partitions = 0
    for n in range(2,9):
        for partition in compositions(n):
            L, classes = graph_laplacian(partition)
            # All periods and both signs of the sharp barriers are tested.
            for p, x in product(range(1,9), [Q(1,3),Q(1),Q(7,4),Q(3)]):
                T = update(L, p, x)
                for i in range(n):
                    assert sum(T[i]) == 1, ('rowsum', partition,p,x,i)
                    for j in range(n):
                        exact = closed(partition,classes,p,x,i,j)
                        assert T[i][j] == exact, (partition,p,x,i,j,T[i][j],exact)
                        checks += 1
                if p % 2 == 0:
                    f = taylor(p,x)
                    # The graph has cross-part pairs, so negativity is exactly f(x)>1.
                    positive = all(v>=0 for row in T for v in row)
                    assert positive == (f <= 1), ('even', partition,p,x)
                if p==3:
                    a_non = [a for a in partition if a>=2]
                    off_thresh = min((Q(3,1)/(2-Q(a,n)) for a in a_non), default=None)
                    if 1 in partition:
                        single_ok = 1+Q(n-1)*taylor(3,x) >= 0
                    else:
                        single_ok=True
                    pred = single_ok and (off_thresh is None or x<=off_thresh)
                    assert all(v>=0 for row in T for v in row) == pred, ('odd3', partition,x)
            partitions += 1
    # Symbolic-level coefficient comparison as rational identities for cubic gap.
    for n in range(3,100):
        for a in range(2,n):
            c=Q(n-a,n)
            for x in [Q(1,7),Q(3,2),Q(7,3),Q(5)]:
                J=c*taylor(3,x)+(1-c)-taylor(3,c*x)
                assert J == c*(1-c)*x*x*(3-(1+c)*x)/6
                checks+=1
    print('VERIFY_OK exact_matrix_entry_and_cubic_identity_checks=', checks,
          'partitions=',partitions)


if __name__ == '__main__':
    main()
