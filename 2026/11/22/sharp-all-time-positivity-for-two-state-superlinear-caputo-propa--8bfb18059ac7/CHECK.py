#!/usr/bin/env python3
"""Finite numerical diagnostics for a two-state Caputo matrix kernel.

These tests are not a proof of an all-time or all-parameter theorem.
Only the Python standard library is required.
"""
import math

N = 0

def check(cond, label):
    global N
    N += 1
    if not cond:
        raise AssertionError(label)

def ml(a, s):
    z = s ** a
    terms = [(-z) ** j / math.gamma(1.0 + a * j) for j in range(52)]
    return math.fsum(terms)

def matrix(a, u, v, s):
    f = ml(a, s)
    k = u + v
    return ((v / k + u / k * f, v / k * (1 - f)),
            (u / k * (1 - f), u / k + v / k * f)), f

def main():
    for a in [1.1, 1.3, 1.5, 1.7, 1.9]:
        check(abs(ml(a, 0.0)-1) < 1e-13, 'initial value')
        for u, v in [(1, 1), (1, 2), (2, 1), (1, 4), (4, 1)]:
            for s in [0, .25, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4]:
                m, f = matrix(a, u, v, s)
                check(abs(m[0][0]+m[1][0]-1) < 3e-10, 'column 1')
                check(abs(m[0][1]+m[1][1]-1) < 3e-10, 'column 2')
                check(abs(m[0][0]*m[1][1]-m[0][1]*m[1][0]-f)<3e-10, 'determinant')
                check(abs(m[1][0]/u-m[0][1]/v)<3e-10, 'offdiagonal ratio')
        for s in [.2, .8, 1.4, 2, 3, 4]:
            m, f = matrix(a, 1, 1, s)
            check(min(m[0][0],m[1][1],m[0][1],m[1][0])>=-1e-10, 'balanced positivity samples')
    m, f = matrix(1.5, 4.0, 1.0, 3.0)
    check(f < -0.29, 'fractional negative trough')
    check(m[0][0] < -0.02, 'strictly negative diagonal for unbalanced rates')
    for a,s in [(1.1,4.4),(1.3,3.2),(1.5,2.95),(1.7,2.95),(1.9,3.05)]:
        check(ml(a,s)<0,'negative fractional scalar value')
    print('PASS:', N, 'finite diagnostic assertions')

if __name__ == '__main__':
    main()
