#!/usr/bin/env python3
"""Exact polynomial certificate for maximal inscribed tetrahedra in 3D parking-function polytopes.

Run: python3 verify.py. Only Python standard library is required.
"""
from itertools import permutations, combinations, product
from collections import Counter

Z = {(0, 0, 0): 0}

def add(p, q):
    r = p.copy()
    for m, v in q.items():
        r[m] = r.get(m, 0) + v
        if r[m] == 0:
            del r[m]
    return r

def neg(p): return {m: -v for m, v in p.items()}
def sub(p, q): return add(p, neg(q))
def mul(p, q):
    r = {}
    for m, a in p.items():
        for n, b in q.items():
            t = tuple(m[i] + n[i] for i in range(3))
            r[t] = r.get(t, 0) + a*b
    return {m:v for m,v in r.items() if v}

def lin(v): return {(1 if j==0 else 0,1 if j==1 else 0,1 if j==2 else 0):a for j,a in enumerate(v) if a}

zero = {}
C = lin((1,0,0))
A = lin((1,1,0))
B = lin((1,1,1))
T_A = add(mul(mul(A,A),A),mul(mul(B,B),B))
T_B = mul(mul(B,B),add(C,A))

def determinant(rows):
    x,y,z=rows
    return add(sub(mul(x[0],sub(mul(y[1],z[2]),mul(y[2],z[1]))),
                   mul(x[1],sub(mul(y[0],z[2]),mul(y[2],z[0])))),
               mul(x[2],sub(mul(y[0],z[1]),mul(y[1],z[0]))))

# Entries are three-variate linear polynomials. The four rank-orbits are
# (0,0,0), (0,0,B), (0,A,B), (C,A,B), where 0 <= C < A < B.
vertex_data = {}
SYMBOL = {"0":zero,"C":C,"A":A,"B":B}
for label, values in [('apex',tuple("000")),
                      ('axes',tuple("00B")),
                      ('mixed',tuple("0AB")),
                      ('top',tuple("CAB"))]:
    for v in set(permutations(values)):
        vertex_data[v] = label
V = sorted(vertex_data, key=str)
assert len(V) == 16
nchecked = 0
special_A, special_B, rest = [], [], []
weak_c_zero = []
for idx in combinations(range(16),4):
    q = [V[i] for i in idx]
    rows = [tuple(sub(SYMBOL[q[i][j]],SYMBOL[q[0][j]]) for j in range(3)) for i in (1,2,3)]
    d = determinant(rows)
    typ = tuple(sorted(vertex_data[v] for v in q))
    if typ == ('apex','mixed','mixed','mixed') and (d == T_A or d == neg(T_A)):
        special_A.append(idx)
    elif typ == ('axes','axes','axes','top') and (d == T_B or d == neg(T_B)):
        special_B.append(idx)
    else:
        for signed_d in (d,neg(d)):
            margin = sub(T_A,signed_d)
            assert all(coef >= 0 for coef in margin.values()), (idx, typ, margin)
            assert margin != {}, (idx,typ)
            # A vanishing margin at C=0 must represent a duplicate of an A maximizer.
            if all(power[0]>0 for power in margin):
                weak_c_zero.append(idx)
        rest.append(idx)
    nchecked += 1
assert (nchecked,len(special_A),len(special_B),len(rest))==(1820,2,6,1812)
# At C=0 a top-layer symbol equals a zero symbol. Every otherwise
# equality candidate collapses to one of the two expected rigid tetrahedra.
def collapse(point): return tuple('0' if letter=='C' else letter for letter in point)
canonical_A = {frozenset(collapse(V[i]) for i in ids) for ids in special_A}
assert len(canonical_A)==2
for ids in weak_c_zero:
    assert frozenset(collapse(V[i]) for i in ids) in canonical_A, ids


def evaluate(poly, vals):
    return sum(v*vals[0]**p[0]*vals[1]**p[1]*vals[2]**p[2] for p,v in poly.items())

# Exact check at C=0 by collapsing coincident symbolic orbit vertices;
# this additionally settles strict equality cases with first parking parameter one.
for d,e in [(1,1),(1,2),(2,1),(3,4),(10,100)]:
    images = {tuple(evaluate(SYMBOL[a],(0,d,e)) for a in v): vertex_data[v] for v in V}
    distinct = list(images)
    winners=[]
    maxval = evaluate(T_A,(0,d,e))
    for q in combinations(distinct,4):
        rows = [[u[i]-q[0][i] for i in range(3)] for u in q[1:]]
        dd=abs(rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])-
               rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])+
               rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0]))
        assert dd <= maxval
        if dd==maxval:winners.append(q)
    assert len(winners)==2, (d,e,len(winners))

# Extra exact enumeration across disparate parameter scales, including both regimes.
counts=Counter()
for c,d,e in product([0,1,2,5,100,10000], [1,2,5], [1,2,5,100]):
    images = list({tuple(evaluate(SYMBOL[a],(c,d,e)) for a in v) for v in V})
    max_det = max(abs((q[1][0]-q[0][0])*((q[2][1]-q[0][1])*(q[3][2]-q[0][2])-(q[2][2]-q[0][2])*(q[3][1]-q[0][1]))
                      -(q[1][1]-q[0][1])*((q[2][0]-q[0][0])*(q[3][2]-q[0][2])-(q[2][2]-q[0][2])*(q[3][0]-q[0][0]))
                      +(q[1][2]-q[0][2])*((q[2][0]-q[0][0])*(q[3][1]-q[0][1])-(q[2][1]-q[0][1])*(q[3][0]-q[0][0]))) for q in combinations(images,4))
    assert max_det == max(evaluate(T_A,(c,d,e)),evaluate(T_B,(c,d,e)))
    counts['parameter_triples']+=1
print('PARKING_TETRA_EXACT_PASS symbolic_quadruples=1820 coefficientwise=1812 rigid=2 facet=6 sample_parameter_triples=%d zero_first_checks=5' % counts['parameter_triples'])
