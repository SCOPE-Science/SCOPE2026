#!/usr/bin/env python3
"""Exact-cover-time certificate and an independent covered-set recursion check.

Requirements: Python 3 standard library, C++17 compiler (g++).
Run: python3 verify.py
All exact arithmetic is integral Bareiss elimination plus Python fractions.
"""
import json
import math
from fractions import Fraction
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
N = 16
FULL = (1 << N) - 1


def neighbors(kind):
    a = [[0] * N for _ in range(N)]
    for v in range(N):
        x, y = divmod(v, 4)
        for w in range(N):
            if w == v:
                continue
            z, t = divmod(w, 4)
            if kind == 'rook':
                edge = x == z or y == t
            else:
                dx, dy = (z-x) % 4, (t-y) % 4
                edge = (dx,dy) in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
            a[v][w] = int(edge)
    for i in range(N):
        assert sum(a[i]) == 6
        for j in range(N):
            assert a[i][j] == a[j][i]
            common = sum(a[i][v]*a[v][j] for v in range(N))
            assert common == (6 if i == j else 2)
    return a


def exact_gaussian_hitting(graph, mask):
    vertices = [i for i in range(N) if (mask >> i) & 1]
    k = len(vertices)
    mat = [[Fraction(6 if i == j else -graph[vertices[i]][vertices[j]]) for j in range(k)] + [Fraction(6)] for i in range(k)]
    for c in range(k):
        pivot = next(r for r in range(c, k) if mat[r][c])
        mat[c], mat[pivot] = mat[pivot], mat[c]
        q = mat[c][c]
        for j in range(c, k+1):
            mat[c][j] /= q
        for r in range(k):
            if r != c:
                q = mat[r][c]
                for j in range(c, k+1):
                    mat[r][j] -= q*mat[c][j]
    return mat[0][k]


def exact_cover(exe, kind, graph):
    cp = subprocess.run([str(exe), kind], text=True, capture_output=True, check=True)
    lines = cp.stdout.splitlines()
    assert len(lines) == 32767
    total = Fraction(0)
    bysize = [Fraction(0) for _ in range(16)]
    test_masks = {1, 0x001f, 0x011f, 0x111f, 0x7fff, 0x5555}
    for expected_mask, line in zip(range(1, FULL, 2), lines):
        mask, numerator, denominator = map(int, line.split(','))
        assert mask == expected_mask
        assert numerator > 0 and denominator > 0
        if mask in test_masks:
            assert Fraction(numerator, denominator) == exact_gaussian_hitting(graph, mask)
        k = mask.bit_count()
        term = Fraction(numerator, denominator)
        if (17 - k) % 2:
            term = -term
        total += term
        bysize[k] += term
    return total, bysize


def main():
    graphs = {kind: neighbors(kind) for kind in ('rook','shrikhande')}
    cert = json.loads((HERE / 'CERTIFICATE.json').read_text(encoding='utf-8'))
    with tempfile.TemporaryDirectory() as tmp:
        exact = Path(tmp)/'exact_cover'
        numerical = Path(tmp)/'cover_dp'
        subprocess.run(['g++','-O3','-std=c++17',str(HERE/'exact_cover.cpp'),'-o',str(exact)], check=True)
        values = {}
        groups = {}
        for kind in ('rook','shrikhande'):
            values[kind], groups[kind] = exact_cover(exact, kind, graphs[kind])
            saved = cert[kind]
            assert values[kind] == Fraction(int(saved['numerator']),int(saved['denominator']))
        delta = values['shrikhande'] - values['rook']
        assert delta == Fraction(int(cert['difference']['numerator']),int(cert['difference']['denominator']))
        assert delta > 0
        assert Fraction(40429484,10**11) < delta < Fraction(40429485,10**11)
        for k in (1,2,3,13,14,15):
            assert groups['shrikhande'][k] == groups['rook'][k]
        assert groups['shrikhande'][4] - groups['rook'][4] == Fraction(28850,11491337)
        subprocess.run(['g++','-O3','-std=c++17',str(HERE/'cover_dp.cpp'),'-o',str(numerical)],check=True)
        out = subprocess.run([str(numerical)],text=True,capture_output=True,check=True).stdout
        parts = out.split()
        assert parts[0] == 'rook' and parts[2] == 'shrikhande' and parts[4] == 'difference'
        assert abs(float(parts[1]) - float(values['rook'])) < 1e-9
        assert abs(float(parts[3]) - float(values['shrikhande'])) < 1e-9
        assert abs(float(parts[5]) - float(delta)) < 1e-9
        print('PASS: exact independent-set hitting-time inclusion/exclusion for 32767 subsets per graph')
        print('PASS: graph degree/common-neighbor constraints (16,6,2,2), both kinds')
        print('PASS: independent exact Gaussian solves for sampled killed-walk matrices')
        print('PASS: independent covered-state 2^16-state recurrence')
        print('rook:',float(values['rook']))
        print('shrikhande:',float(values['shrikhande']))
        print('difference:',float(delta))
        print('first distinct grouped contribution (k=4):',groups['shrikhande'][4]-groups['rook'][4])

if __name__ == '__main__':
    main()
