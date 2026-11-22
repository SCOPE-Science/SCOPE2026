#!/usr/bin/env python3
"""Independent exact S6 check for genus-two Kummer node-trope flags.

This program enumerates finite label sets and permutation actions, without
finite-field experiments and without external Python packages.
"""
import collections
import itertools
import math
import csv
import sys

B = tuple(range(6))
BSET = frozenset(B)
NODES = [('zero',)] + [('pair', a) for a in itertools.combinations(B, 2)]
PAIR_PARTITIONS = set()
for a in itertools.combinations(B, 3):
    t = tuple(a)
    u = tuple(sorted(BSET - set(a)))
    PAIR_PARTITIONS.add(min(t, u))
TROPES = [('odd', i) for i in B] + [('even', t) for t in sorted(PAIR_PARTITIONS)]

def contains(n, t):
    if t[0] == 'odd':
        return n[0] == 'zero' or t[1] in n[1]
    if n[0] == 'zero':
        return False
    a = set(t[1]); p = set(n[1])
    return p <= a or p <= (BSET - a)

FLAGS = [(n, t) for n in NODES for t in TROPES if contains(n, t)]
assert len(NODES) == len(TROPES) == 16
assert len(FLAGS) == 96
assert all(sum(contains(n, t) for t in TROPES) == 6 for n in NODES)
assert all(sum(contains(n, t) for n in NODES) == 6 for t in TROPES)

def act_node(p, node):
    if node[0] == 'zero':
        return node
    return ('pair', tuple(sorted(p[i] for i in node[1])))

def act_trope(p, trope):
    if trope[0] == 'odd':
        return ('odd', p[trope[1]])
    a = tuple(sorted(p[i] for i in trope[1]))
    a = min(a, tuple(sorted(BSET - set(a))))
    return ('even', a)

def act_flag(p, flag):
    return (act_node(p, flag[0]), act_trope(p, flag[1]))

def cycle_multiset(objects, action, perm):
    indices = {x: i for i, x in enumerate(objects)}
    induced = [indices[action(perm, x)] for x in objects]
    visited = set()
    counts = collections.Counter()
    for i in range(len(objects)):
        if i in visited:
            continue
        j = i; d = 0
        while j not in visited:
            visited.add(j); d += 1; j = induced[j]
        assert j == i
        counts[d] += 1
    return tuple(sorted(counts.items()))

def type_of(p):
    seen = set(); typ = []
    for i in B:
        if i not in seen:
            j = i; d = 0
            while j not in seen:
                seen.add(j); d += 1; j = p[j]
            typ.append(d)
    return tuple(sorted(typ))

def fixed_from_cycles(cycles, power):
    return sum(d * m for d, m in cycles if power % d == 0)

def flag_formula(p):
    f = sum(p[i] == i for i in B)
    twos = sum(i < p[i] and p[p[i]] == i for i in B)
    return f*f + math.comb(f, 2) * max(f-2, 0) + f*twos

alltypes = {}
for p in itertools.permutations(B):
    ncyc = cycle_multiset(NODES, act_node, p)
    tcyc = cycle_multiset(TROPES, act_trope, p)
    fcyc = cycle_multiset(FLAGS, act_flag, p)
    assert ncyc == tcyc, ('node/trope mismatch', p)
    assert fixed_from_cycles(fcyc, 1) == flag_formula(p), ('formula mismatch', p)
    typ = type_of(p)
    signature = (ncyc, tcyc, fcyc)
    if typ in alltypes:
        assert alltypes[typ] == signature, ('conjugacy mismatch', typ)
    else:
        alltypes[typ] = signature

assert len(alltypes) == 11
signatures_3 = {}
signatures_2 = {}
node_profiles = collections.defaultdict(list)
rows = []
for typ, (ncyc, tcyc, fcyc) in sorted(alltypes.items()):
    fvalues = [fixed_from_cycles(fcyc, k) for k in (1, 2, 3)]
    sig3 = tuple(fvalues)
    assert sig3 not in signatures_3
    signatures_3[sig3] = typ
    signatures_2.setdefault(sig3[:2], []).append(typ)
    node_profiles[ncyc].append(typ)
    rows.append((typ, ncyc, tcyc, fcyc, fvalues))

assert len(signatures_2) == 10
assert sorted(v for v in signatures_2.values() if len(v) > 1) == [[(3, 3), (6,)]]
assert len(node_profiles) == 9
assert sorted(v for v in node_profiles.values() if len(v) > 1) == [
    [(1, 1, 2, 2), (2, 2, 2)], [(1, 1, 4), (2, 4)]
]
assert signatures_3[(0, 0, 96)] == (3, 3)
assert signatures_3[(0, 0, 0)] == (6,)
assert sum(m*d for d, m in alltypes[(6,)][2]) == 96

def stringify_cycles(cycles):
    return ' '.join('%d^%d' % (length, count) for length, count in cycles)

if len(sys.argv) > 1:
    with open(sys.argv[1], 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(('branch_partition', 'node_cycles', 'trope_cycles', 'flag_cycles', 'flags_Fq', 'flags_Fq2', 'flags_Fq3'))
        for typ, ncyc, tcyc, fcyc, vals in rows:
            w.writerow((','.join(map(str, typ)), stringify_cycles(ncyc), stringify_cycles(tcyc), stringify_cycles(fcyc), *vals))
print('KUMMER_96_FLAGS_720_SIX_POINT_ACTIONS_11_TYPES_SHARP_THREE_EXTENSIONS_VERIFIED')
