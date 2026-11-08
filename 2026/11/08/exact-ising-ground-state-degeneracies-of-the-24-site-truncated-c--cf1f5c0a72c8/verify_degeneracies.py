#!/usr/bin/env python3
"""Exact independent counting of truncated-cube Ising ground-state sets.

Only standard-library integer enumeration, without storing or referring to an external table.
The graph has one triangle of three directed-edge ports for each cube vertex.
"""
from itertools import product

V = tuple(range(8))
E = tuple((u, u ^ (1 << bit)) for u in V for bit in range(3) if u < (u ^ (1 << bit)))
assert len(E) == 12
port = {(u, u ^ (1 << bit)): bit for u in V for bit in range(3)}

def no_double_minus_count(options):
    """One local minus-port subset per cube vertex, no edge selected at both ends."""
    assign = [0] * 8
    totals = {}
    def dfs(u, number_of_minus):
        if u == 8:
            k = 24 - number_of_minus
            totals[k] = totals.get(k, 0) + 1
            return
        for mask in options:
            if all(not ((mask >> port[(u,v)] & 1) and
                        (assign[v] >> port[(v,u)] & 1))
                   for v in V if v < u and (u,v) in port):
                assign[u] = mask
                dfs(u+1, number_of_minus+mask.bit_count())
    dfs(0,0)
    return totals

def count_orientations():
    cnt = 0
    for choices in product((0,1),repeat=len(E)):
        plus = [0] * 8
        for (u,v),choice in zip(E,choices):
            plus[u if choice==0 else v] += 1
        if all(1<=a<=2 for a in plus): cnt += 1
    return cnt

low = count_orientations()
mid = no_double_minus_count((1,2,4))
first = no_double_minus_count((1,2,4,3,5,6))
second = no_double_minus_count((0,1,2,4))
print('low',low,'middle',mid,'first',first,'second',second)
assert low == 450
assert mid == {16:828}
assert first == {12:450,13:2520,14:4572,15:3312,16:828}
assert second == {16:828,17:4272,18:8056,19:7632,20:4092,21:1296,22:240,23:24,24:1}
assert sum(first.values()) == 11682
assert sum(second.values()) == 26441
print('VERIFIED EXACT DEGENERACIES')
