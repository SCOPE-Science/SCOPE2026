#!/usr/bin/env python3
"""Exact-rational checks for a split-graph negative-type statement.
Run: python3 verify_split_graph.py; uses only Python's standard library.
These finite checks corroborate, but do not replace, the proof for all sizes.
"""
from fractions import Fraction as F
from random import Random


def qform(m, n, q, x):
    total = F(0)
    assert len(x) == m + n
    for i in range(m + n):
        for j in range(m + n):
            if i != j:
                total += x[i] * x[j] * (q if i >= m and j >= m else 1)
    return total


def dot(x, y):
    return sum((a*b for a,b in zip(x,y)), F(0))


def critical(m, n):
    return F(n*(m+1),m*(n-1))


def block(m, n):
    return [F(1,m)]*m + [-F(1,n)]*n


def projection_eigenvalues(m, n, q):
    return [F(-1)]*(m-1) + [-q]*(n-1) + [
        (q*(1-F(1,n))-1-F(1,m))/(F(1,m)+F(1,n))]


def matrix_action(m, n, q, x):
    return [sum((x[j]*(0 if i==j else q if i>=m and j>=m else 1)
                 for j in range(m+n)),F(0)) for i in range(m+n)]


def main():
    num_actions = num_vectors = num_witnesses = 0
    rnd = Random(101072026)
    for m in range(1, 10):
        for n in range(2, 10):
            qc = critical(m,n)
            b = block(m,n)
            for q in (F(1),F(5,4),F(3,2),F(2),F(5,2),F(4),qc):
                d = matrix_action(m,n,q,b)
                eig = projection_eigenvalues(m,n,q)[-1]
                assert sum(b) == 0
                assert dot(b,d) == eig*dot(b,b)
                num_actions += 1
                # The two within-block mean-zero eigenspaces.
                for i in range(m-1):
                    v = [F(0)]*(m+n)
                    v[i] = F(1); v[m-1] = F(-1)
                    assert matrix_action(m,n,q,v) == [-z for z in v]
                    assert dot(v,b) == 0
                    num_actions += 1
                for j in range(n-1):
                    v = [F(0)]*(m+n)
                    v[m+j] = F(1); v[m+n-1] = F(-1)
                    assert matrix_action(m,n,q,v) == [-q*z for z in v]
                    assert dot(v,b) == 0
                    num_actions += 1
                for _ in range(12):
                    x = [F(rnd.randint(-5,5)) for _ in range(m+n-1)]
                    x += [-sum(x)]
                    s = sum(x[:m])
                    formula = (q-1)*s*s-sum(v*v for v in x[:m])-q*sum(v*v for v in x[m:])
                    actual = qform(m,n,q,x)
                    assert actual == formula
                    assert actual <= (q*(1-F(1,n))-1-F(1,m))*s*s
                    num_vectors += 1
                # Uniform-block extremizer is critical and changes sign on either side.
                witness_at = qform(m,n,qc,b)
                assert witness_at == 0
                small,large = (qc+1)/2, qc+F(1,8)
                assert qform(m,n,small,b)<0<qform(m,n,large,b)
                num_witnesses += 1
    failures = {(m,n) for m in range(1,7) for n in range(2,7)
                if m+n==7 and n*(m-1)>2*m}
    assert failures == {(2,5),(3,4),(4,3)}
    for N in range(3,7):
        for m in range(1,N-1):
            n=N-m
            assert n*(m-1)<=2*m
    print('PASS exact actions:', num_actions)
    print('PASS exact arbitrary zero-sum vector checks:', num_vectors)
    print('PASS exact critical witnesses:', num_witnesses)
    print('PASS first failure family at total order 7:', sorted(failures))


if __name__ == '__main__':
    main()
