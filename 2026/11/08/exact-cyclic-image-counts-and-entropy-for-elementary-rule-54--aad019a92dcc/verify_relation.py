#!/usr/bin/env python3
"""Exact Boolean relation-monoid certificate for cyclic Rule 54 image counts."""
from collections import deque

RULE = 54
NODES = range(4)  # state 2*a+b stores two consecutive predecessor bits

def symbol_matrix(bit):
    result = []
    for start in NODES:
        a, b = divmod(start, 2)
        row = 0
        for c in (0, 1):
            local = (a << 2) | (b << 1) | c
            if ((RULE >> local) & 1) == bit:
                row |= 1 << (2*b+c)
        result.append(row)
    return tuple(result)

def boolean_product(left, right):
    out = []
    for a in NODES:
        row = 0
        for b in NODES:
            if (left[a] >> b) & 1:
                row |= right[b]
        out.append(row)
    return tuple(out)

def contains_diagonal(relation):
    return any((relation[i] >> i) & 1 for i in NODES)

def build():
    identity = tuple(1 << i for i in NODES)
    alphabet = (symbol_matrix(0), symbol_matrix(1))
    states = [identity]
    index = {identity: 0}
    transitions = []
    for relation in states:
        edges = []
        for letter in alphabet:
            successor = boolean_product(relation, letter)
            if successor not in index:
                index[successor] = len(states)
                states.append(successor)
            edges.append(index[successor])
        transitions.append(tuple(edges))
    return states, transitions

def advance(transition, vec):
    return [vec[a]+vec[b] for a,b in transition]

def coefficients(vectors):
    return [vectors[n][0] for n in range(len(vectors))]

def run():
    states, trans = build()
    assert len(states) == 109, len(states)
    assert sum(map(contains_diagonal,states)) == 77
    assert len(trans) == len(states)
    assert len(set(states)) == len(states)
    # Complete closure, no excluded successor: all products of generated relations.
    for i, relation in enumerate(states):
        for bit in (0,1):
            assert states[trans[i][bit]] == boolean_product(relation,symbol_matrix(bit))
    v = [int(contains_diagonal(r)) for r in states]
    vectors = [v]
    for _ in range(20):
        vectors.append(advance(trans,vectors[-1]))
    # Exact 109-component identity, NOT an extrapolation from initial scalars.
    residual = [vectors[8][j]-2*vectors[7][j]+vectors[6][j]
                -vectors[5][j]-vectors[4][j]+vectors[3][j]
                -vectors[2][j] for j in range(len(states))]
    assert all(x==0 for x in residual), residual
    # Applying T repeatedly proves the same relation in every subsequent degree.
    a = coefficients(vectors)
    assert a[:16] == [1,1,2,5,14,22,41,79,150,275,512,959,1793,3343,6239,11650]
    # D(z) = 1-2z+z^2-z^3-z^4+z^5-z^6.
    d = [1,-2,1,-1,-1,1,-1]
    num = [sum(d[k]*a[n-k] for k in range(len(d)) if n >= k)
           for n in range(21)]
    assert num == [1,-1,1,1,4,-3,4,1] + [0]*13
    # Removing the formal length-zero term gives the stated generating function.
    assert [num[i]-d[i] if i<len(d) else num[i] for i in range(21)] == [0,1,0,2,5,-4,5,1]+[0]*13
    # Integer Newton-sum check of the exact quartic-root representation.
    q = [4,2,4,5]
    for n in range(4,21):
        q.append(2*q[n-1]-q[n-3]+q[n-4])
    oscillator = (2,0,-2,0)
    assert all(a[n] == q[n]+oscillator[n%4] for n in range(2,21))
    assert a[1] == 1 and q[1]+oscillator[1] == 2
    print('QUARTIC_ROOT_POWER_IDENTITY_OK',19,'positive lengths')
    print('RELATION_CERTIFICATE_OK',len(states),'states',sum(map(contains_diagonal,states)),'accepting')
    print('FIRST_COUNTS',a[1:17])
    print('VECTOR_POLYNOMIAL_IDENTITY_ZERO',len(states),'coordinates')

if __name__ == '__main__':
    run()
