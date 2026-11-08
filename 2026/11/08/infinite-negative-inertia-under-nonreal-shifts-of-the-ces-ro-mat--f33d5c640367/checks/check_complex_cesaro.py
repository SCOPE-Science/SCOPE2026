#!/usr/bin/env python3
"""Finite diagnostic checks for the complex-shift Cesaro inertia theorem.

This checker tests finite-column Gram identities and explicit negative
quadratic-form witnesses. Infinite-dimensional claims are proved in RESULT.md.
No third-party packages are required.
"""
import cmath
import math


def gram(alpha, size):
    cols = []
    for j in range(size):
        b = [0j] * (size + 1)
        for i in range(j + 1):
            b[i] = (j + 1 + alpha) / ((j + 1 + alpha.conjugate()) * (j + 2 + alpha.conjugate()))
        b[j + 1] = -(j + 1 + alpha) / (j + 2 + alpha.conjugate())
        cols.append(b)
    return [[(1.0 if i == j else 0.0) - sum(cols[i][h].conjugate() * cols[j][h] for h in range(size + 1))
             for j in range(size)] for i in range(size)]


def transformed_gram(alpha, size):
    phase = [(j + 1 + alpha) / (j + 1 + alpha.conjugate()) * (j + 2 + alpha) / abs(j + 2 + alpha)
             for j in range(size)]
    d = [1.0 / abs(j + 2 + alpha) for j in range(size)]
    return [[phase[i].conjugate() * phase[j] * d[i] * d[j] *
             ((i + 2 + 2 * alpha.real) if i == j else (alpha if i < j else alpha.conjugate()))
             for j in range(size)] for i in range(size)]


def kform(alpha, vec):
    positive = sum((j + 2 + alpha.real) * abs(c) ** 2 for j, c in vec.items())
    total = sum(vec.values())
    indexes = sorted(vec)
    skew = 0.0
    for a, i in enumerate(indexes):
        for j in indexes[a+1:]:
            skew += (vec[i].conjugate() * vec[j]).imag
    return positive + alpha.real * abs(total)**2 - 2 * alpha.imag * skew


def blocks_witness(alpha, blocks=((0, 10), (11, 100), (101, 1000), (1001, 10000))):
    sig = 1 if alpha.imag > 0 else -1
    phases = (1, 1j*sig, -1, -1j*sig)
    total_diag = 0.0
    mass = []
    for (lo,hi), p in zip(blocks,phases):
        h = sum(1.0/(n + 2 + alpha.real) for n in range(lo, hi + 1))
        total_diag += 1.0/h
        mass.append(p)
    skew = sum((mass[i].conjugate()*mass[j]).imag for i in range(4) for j in range(i+1,4))
    return total_diag + alpha.real*abs(sum(mass))**2 - 2*alpha.imag*skew


def run():
    tests = 0
    for a in (0j, 0.7, -0.6, 0.3+0.7j, -0.3+1.5j, 0.4-2.0j):
        for n in (1,2,3,5,8,12,20):
            one, two = gram(a,n), transformed_gram(a,n)
            for i in range(n):
                for j in range(n):
                    assert abs(one[i][j]-two[i][j]) < 2e-11, (a,n,i,j)
                    tests += 1
    for a in (0.2+1.25j,-0.3-1.25j, 0.4+4j):
        v = blocks_witness(a)
        assert v < -0.05, (a,v)
        tests += 1
    for a in (-0.1, -0.3, -0.6):
        h = sum(1.0/(n+2+a) for n in range(150000))
        form = 1.0/h + a
        assert form < 0, (a,form)
        tests += 1
    print('PASS:', tests, 'finite Gram and witness assertions')


if __name__ == '__main__':
    run()
