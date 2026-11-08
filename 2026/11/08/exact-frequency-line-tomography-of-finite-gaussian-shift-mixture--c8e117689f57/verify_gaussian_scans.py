#!/usr/bin/env python3
"""Exact algebraic illustration of the Gaussian-scan lifting rank theorem.

Requires SymPy. Input time nodes x=(log 2)*index/pi, and all positive
column factors exp(-pi*(shift_j**2+shift_k**2)/2) are removed.
The off-diagonal imaginary unknown is -Im(H_jk), hence +sin columns.
"""
from itertools import combinations
from sympy import Integer, Matrix, Rational, cos, sin, pi


def lift_matrix(shifts, frequencies, node_lists):
    assert len(frequencies)==len(node_lists)
    pairs=list(combinations(range(len(shifts)), 2))
    rows=[]
    for w, nodes in zip(frequencies,node_lists):
        for x in nodes:
            row=[Integer(2)**(2*x*t) for t in shifts]
            for j,k in pairs:
                a=2*Integer(2)**(x*(shifts[j]+shifts[k]))
                delta=shifts[k]-shifts[j]
                row.extend([a*cos(pi*w*delta),a*sin(pi*w*delta)])
            rows.append(row)
    return Matrix(rows)

sidon=lift_matrix([0,1,3],[0,Rational(1,4)],[list(range(6)),list(range(3))])
assert sidon.shape==(9,9)
assert sidon.rank()==9
assert sidon.det()==-275285327836977561600
non_sid_2=lift_matrix([0,1,2],[0,Rational(1,4)],[list(range(5)),list(range(5))])
assert non_sid_2.shape==(10,9) and non_sid_2.rank()==8
non_sid_3=lift_matrix([0,1,2],[0,Rational(1,4),Rational(1,2)],[list(range(5))]*3)
assert non_sid_3.shape==(15,9) and non_sid_3.rank()==9
print('GAUSSIAN_SCAN_RANK_CHECK_PASS 3')
