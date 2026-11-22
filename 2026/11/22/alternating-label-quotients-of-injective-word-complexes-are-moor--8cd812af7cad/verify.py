#!/usr/bin/env python3
"""Exact orbit-cell boundary checks for alternating-label quotients of injective-word CW complexes.

No external datasets are needed. The quotient is constructed from the original
ordered-word cells via generators of the alternating group, without assuming
parity-based orbit formulas.
"""
from collections import deque
from itertools import permutations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def orbit_cells(n, size):
    """Partition injective words of fixed length under adjacent 3-cycles."""
    gens = []
    for i in range(n-2):
        g = list(range(n))
        g[i], g[i+1], g[i+2] = i+1, i+2, i
        gens.append(tuple(g))
    unvisited = set(permutations(range(n), size))
    where = {}
    reps = []
    while unvisited:
        first = min(unvisited)
        reps.append(first)
        index = len(reps)-1
        todo = deque([first])
        unvisited.remove(first)
        where[first] = index
        while todo:
            w = todo.popleft()
            for g in gens:
                v = tuple(g[x] for x in w)
                if v in unvisited:
                    unvisited.remove(v)
                    where[v] = index
                    todo.append(v)
    return reps, where


def matrices(n):
    found=[orbit_cells(n,k+1) for k in range(n)]
    D={}
    for k in range(1,n):
        reps=found[k][0]
        lower=found[k-1][1]
        M=Matrix.zeros(len(found[k-1][0]),len(reps))
        for col,w in enumerate(reps):
            for i in range(k+1):
                subword=w[:i]+w[i+1:]
                M[lower[subword],col]+=(-1)**i
        D[k]=M
    return [len(v[0]) for v in found],D


def check(n):
    counts,D=matrices(n)
    assert counts == [1]*(n-2)+[2,2],(n,counts)
    for k in range(2,n):
        assert D[k-1]*D[k]==Matrix.zeros(D[k-1].rows,D[k].cols)
    for k in range(1,n-2):
        assert D[k] == Matrix([[0 if k%2 else 1]]),(n,k,D[k])
    expected_middle=Matrix([[1,1]]) if n%2==0 else Matrix([[0,0]])
    assert D[n-2] == expected_middle,(n,D[n-2])
    snf=smith_normal_form(D[n-1],domain=ZZ)
    diagonal=sorted(abs(int(snf[i,i])) for i in range(min(snf.rows,snf.cols)))
    expected=sorted([0,n//2]) if n%2==0 else [1,n]
    assert diagonal==expected,(n,diagonal)
    print(f'n={n}: cell_orbits={counts}; final Smith diagonal={diagonal}; OK')


if __name__=='__main__':
    for n in range(3,9):
        check(n)
    print('ALTERNATING_INJECTIVE_WORD_QUOTIENT_ORBITS_OK')
