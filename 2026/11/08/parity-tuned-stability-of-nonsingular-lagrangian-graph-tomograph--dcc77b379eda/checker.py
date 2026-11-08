#!/usr/bin/env python3
"""Finite checks for the nonsingular-symmetric-graph affine Radon spectrum.
Run with Python 3 and numpy. This is corroboration, not an infinite proof.
"""
import itertools
import numpy as np


def det_mod(a, p):
    a = [list(row) for row in a]
    n = len(a)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j] % p), None)
        if pivot is None:
            return False
        a[j], a[pivot] = a[pivot], a[j]
        inv = pow(int(a[j][j]) % p, -1, p)
        for i in range(j + 1, n):
            c = a[i][j] * inv % p
            for k in range(j, n):
                a[i][k] = (a[i][k] - c * a[j][k]) % p
    return True


def symmetric_matrices(p, d):
    pairs = [(i, j) for i in range(d) for j in range(i, d)]
    for vals in itertools.product(range(p), repeat=len(pairs)):
        a = [[0] * d for _ in range(d)]
        for (i, j), v in zip(pairs, vals):
            a[i][j] = a[j][i] = v
        if det_mod(a, p):
            yield a


def predicted_s(p, d):
    if d == 0:
        return 1
    m = d // 2
    if d % 2 == 0:
        return p ** (m * (m + 1)) * np.prod([p ** (2 * i - 1) - 1 for i in range(1, m + 1)], dtype=object)
    return p ** (m * (m + 1)) * np.prod([p ** (2 * i - 1) - 1 for i in range(1, m + 2)], dtype=object)


def expected_multiplier(p, d, alpha, beta):
    if all(v == 0 for v in alpha + beta):
        return p ** d * int(predicted_s(p, d))
    if not any(alpha) or not any(beta):
        return 0
    dot = sum(x * y for x, y in zip(alpha, beta)) % p
    return p ** d * (int(predicted_s(p, d-1)) if dot else p ** (d-1) * int(predicted_s(p, d-2)))


def check(p, d):
    matrices = list(symmetric_matrices(p, d))
    assert len(matrices) == int(predicted_s(p, d)), (p, d)
    words = list(itertools.product(range(p), repeat=d))
    points = [(x, y) for x in words for y in words]
    frequencies = points
    row_ids = [(mi, c) for mi in range(len(matrices)) for c in words]
    v_to_i = {v: i for i, v in enumerate(words)}
    rows = np.zeros((len(row_ids), len(points)), dtype=np.int32)
    for mi, mat in enumerate(matrices):
        for x in words:
            mx = tuple(sum(mat[i][j] * x[j] for j in range(d)) % p for i in range(d))
            for y in words:
                c = tuple((y[i] - mx[i]) % p for i in range(d))
                rows[mi * len(words) + v_to_i[c], v_to_i[x] * len(words) + v_to_i[y]] = 1
    gram = rows.T @ rows
    coordinate = np.array([x + y for x, y in points], dtype=int)
    lamlist=[]
    maxres=0.0
    for alpha, beta in frequencies:
        omega = np.array(alpha + beta)
        phase = coordinate @ omega % p
        v = np.exp(2j * np.pi * phase / p)
        ev = expected_multiplier(p, d, alpha, beta)
        maxres=max(maxres,float(np.max(np.abs(gram @ v-ev*v))))
        lamlist.append(ev)
    assert maxres < 3e-8, (p, d, maxres)
    spectrum = {int(e): lamlist.count(e) for e in set(lamlist)}
    n0=(p**d-1)*(p**(d-1)-1)
    n1=(p**d-1)*(p-1)*p**(d-1)
    assert sum(e>0 for e in lamlist) == 1 + (p**d-1)**2
    assert sum(e==0 for e in lamlist) == 2*(p**d-1)
    assert sum(lamlist) == int(np.trace(gram)), (p,d)
    assert n0+n1==(p**d-1)**2
    print(f'q={p} d={d} |Sym^×|={len(matrices)} rows={len(row_ids)} '
          f'cols={len(points)} rank={sum(e>0 for e in lamlist)} '
          f'spectrum={dict(sorted(spectrum.items()))} maxres={maxres:.2e}')


if __name__=='__main__':
    for p, d in [(2, 2), (2, 3), (3, 2)]:
        check(p, d)
    for p, d in [(2, 4), (3, 3)]:
        matrices = list(symmetric_matrices(p, d))
        assert len(matrices) == int(predicted_s(p, d))
        words = list(itertools.product(range(p), repeat=d))
        checked = 0
        for beta in words:
            for alpha in words:
                count = sum(all(sum(M[i][j]*beta[j] for j in range(d)) % p == (-alpha[i]) % p for i in range(d)) for M in matrices)
                assert p**d * count == expected_multiplier(p,d,alpha,beta), (p,d,alpha,beta,count)
                checked += 1
        print(f'q={p} d={d} all_frequency_incidence_checks={checked} matrices={len(matrices)}')
    for p in [2,3,4,5,7,8,11]:
        s=[int(predicted_s(p,d)) for d in range(8)]
        for d in range(2,8):
            assert s[d] == (p-1)*p**(d-1)*s[d-1] + (p**(d-1)-1)*p**(d-1)*s[d-2]
        for d in range(2,8):
            c1=s[d-1]; c0=p**(d-1)*s[d-2]
            if d%2:
                assert c1==c0
                assert s[d] == (p**d-1)*c1
            else:
                assert c1*(p**(d-1)) == c0*(p**(d-1)-1)
                assert s[d] == p**d*c1
    print('NONSINGULAR_SYMMETRIC_LAGRANGIAN_RADON_CHECKS_PASS')
