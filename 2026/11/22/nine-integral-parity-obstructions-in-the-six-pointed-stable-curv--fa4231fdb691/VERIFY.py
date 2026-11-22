#!/usr/bin/env python3
"""Exact integer replay of the boundary-curve / boundary-point incidence certificate.

Usage: python3 VERIFY.py (from the directory containing SMITH_CERT.json).
Uses only the Python standard library.
"""
import json
from itertools import combinations
from collections import Counter
from pathlib import Path

LABEL_COUNT = 6
ALL = (1 << LABEL_COUNT) - 1


def normalized_partition(mask):
    return min(mask, ALL ^ mask)


def compatible(a, b):
    a_complement, b_complement = ALL ^ a, ALL ^ b
    return (not (a & b) or not (a & b_complement) or
            not (a_complement & b) or not (a_complement & b_complement))


def incidence_matrix():
    divisions = sorted({normalized_partition(i) for i in range(1, ALL)
                        if 2 <= i.bit_count() <= LABEL_COUNT - 2})
    curves = [pair for pair in combinations(divisions, 2)
              if compatible(*pair)]
    points = [triple for triple in combinations(divisions, 3)
              if all(compatible(a,b) for a,b in combinations(triple,2))]
    assert len(divisions) == 25
    assert len(curves) == len(points) == 105
    index = {curve: i for i,curve in enumerate(curves)}
    matrix = [[0 for _ in points] for _ in curves]
    for j,triple in enumerate(points):
        for pair in combinations(triple,2):
            matrix[index[pair]][j] = 1
    assert all(sum(row) == 3 for row in matrix)
    assert all(sum(matrix[i][j] for i in range(105)) == 3 for j in range(105))
    return matrix


def replay(matrix,operations):
    n = len(matrix)
    for op in operations:
        kind = op[0]
        if kind == 'Rswap':
            _,i,j = op
            assert 0 <= i < n and 0 <= j < n
            matrix[i],matrix[j] = matrix[j],matrix[i]
        elif kind == 'Cswap':
            _,i,j = op
            assert 0 <= i < n and 0 <= j < n
            for row in matrix:
                row[i],row[j] = row[j],row[i]
        elif kind == 'Radd':
            _,i,j,q = op
            assert 0 <= i < n and 0 <= j < n and i != j and isinstance(q,int)
            matrix[i] = [a+q*b for a,b in zip(matrix[i],matrix[j])]
        elif kind == 'Cadd':
            _,i,j,q = op
            assert 0 <= i < n and 0 <= j < n and i != j and isinstance(q,int)
            for row in matrix:row[i] += q*row[j]
        elif kind == 'Rneg':
            _,i = op
            assert 0 <= i < n
            matrix[i] = [-a for a in matrix[i]]
        else:
            raise AssertionError('unknown unimodular operation')
    for i in range(n):
        for j in range(n):
            if i != j:assert matrix[i][j] == 0, ('off diagonal',i,j)
    diagonal = [matrix[i][i] for i in range(n)]
    for i in range(n-1):
        if diagonal[i] == 0:assert diagonal[i+1] == 0
        elif diagonal[i+1] != 0:assert diagonal[i+1]%diagonal[i] == 0
    return diagonal


def main():
    data=json.loads(Path(__file__).with_name('SMITH_CERT.json').read_text(encoding='utf-8'))
    assert data['dimensions']==[105,105]
    assert data['construction']=='six-label stable split compatibility, unsigned codimension-two-to-three incidence'
    A=incidence_matrix()
    diagonal=replay(A,data['unimodular_operations'])
    assert diagonal == data['smith_diagonal']
    assert Counter(diagonal) == Counter({1:81,2:9,0:15})
    print('VERIFIED_M06_BOUNDARY_INCIDENCE_SNF_1x81_2x9_0x15',len(data['unimodular_operations']))

if __name__=='__main__':main()
