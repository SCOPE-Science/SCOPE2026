#!/usr/bin/env python3
"""Exact independent matrix checks for two diametric chords of an even unit cycle."""
from fractions import Fraction as Q

def laplacian(n, t):
    m = n // 2
    a = [[0 for _ in range(n)] for _ in range(n)]
    edges = [(j, (j+1) % n) for j in range(n)] + [(0, m), (t, t+m)]
    for i, j in edges:
        a[i][i] += 1; a[j][j] += 1
        a[i][j] -= 1; a[j][i] -= 1
    return a

def augmented_det_and_inverse(a):
    # Determinant and inverse of the grounded Laplacian using rational elimination.
    n = len(a) - 1
    aug = [[Q(a[i][j]) for j in range(n)] + [Q(int(i==j)) for j in range(n)] for i in range(n)]
    det = Q(1)
    for j in range(n):
        k = next(i for i in range(j, n) if aug[i][j])
        if k != j:
            aug[j], aug[k] = aug[k], aug[j]
            det = -det
        pivot = aug[j][j]
        det *= pivot
        aug[j] = [v / pivot for v in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                c = aug[i][j]
                aug[i] = [u - c*v for u, v in zip(aug[i], aug[j])]
    return det, [row[n:] for row in aug]

def matrix_tree_kf(n, t):
    det, inv = augmented_det_and_inverse(laplacian(n,t))
    kf = Q(n)*sum(inv[i][i] for i in range(n-1)) - sum(sum(row) for row in inv)
    return det, kf

def expected(m,t):
    x = t*(m-t)
    tau = 2*m*(m+1+x)
    gain = Q(m,6) * Q(m*(m*m+2)+(m*m+4)*x+4*x*x,m+1+x)
    base = Q(m*(4*m*m-1),6)
    return Q(tau), base-gain

def main():
    assertions = 0
    for m in range(2,10):
        values = {}
        for t in range(1,m):
            actual = matrix_tree_kf(2*m,t)
            assert actual == expected(m,t), (m,t,actual,expected(m,t))
            assertions += 2
            values[t] = actual
        actual_d = {t for t in values if values[t][0] == max(v[0] for v in values.values())}
        actual_a = {t for t in values if values[t][1] == min(v[1] for v in values.values())}
        opt = {t for t in (m//2,(m+1)//2) if 1<=t<m}
        assert actual_d == actual_a == opt,(m,actual_d,actual_a,opt)
        assertions += 1
    print('PASS: exact matrix and optimizer checks;',assertions,'assertions')

if __name__=='__main__': main()
