#!/usr/bin/env python3
"""Exact incidence Galois enumeration (Python standard library only).

Run beside CONFIGURATIONS.json and EXPECTED_COUNTS.json:
    python verify_closure.py
"""
import json
from pathlib import Path
from collections import Counter
from itertools import combinations, product

base = Path(__file__).resolve().parent
config = json.loads((base / 'CONFIGURATIONS.json').read_text(encoding='utf-8'))['configurations']
expected = json.loads((base / 'EXPECTED_COUNTS.json').read_text(encoding='utf-8'))

for name, lines in config.items():
    lines = [set(v) for v in lines]
    assert len(lines) == 9 and all(len(v) == 3 for v in lines)
    assert all(sum(p in l for l in lines) == 3 for p in range(9))
    assert all(len(a & b) <= 1 for a, b in combinations(lines, 2))
    line_masks = [sum(1 << p for p in line) for line in lines]
    point_masks = [sum(1 << j for j in range(9) if p in lines[j]) for p in range(9)]
    def alpha(point_set):
        return sum(1 << j for j, line in enumerate(line_masks) if not (line & point_set))
    def beta(line_set):
        return sum(1 << p for p, mask in enumerate(point_masks) if not (mask & line_set))
    fa = Counter(alpha(x) for x in range(512))  # preimage count of each line symbol
    fb = Counter(beta(x) for x in range(512))   # preimage count of each point symbol
    assert len(fa) == len(fb)
    for x in range(512):
        assert alpha(beta(alpha(x))) == alpha(x)
        assert beta(alpha(beta(x))) == beta(x)
    fixed_basin_sizes = Counter()
    cycle_basin_sizes = Counter()
    used = set()
    for p, l in product(fb, fa):
        if (p, l) in used:
            continue
        partner = (beta(l), alpha(p))
        assert partner[0] in fb and partner[1] in fa
        wt = fb[p] * fa[l]
        if partner == (p, l):
            fixed_basin_sizes[wt] += 1
        else:
            cycle_basin_sizes[wt + fb[partner[0]] * fa[partner[1]]] += 1
        used.add((p, l))
        used.add(partner)
    # A six-cycle is a triangle of points whose three pairs lie on three distinct lines.
    pair_line = {tuple(sorted((a,b))): j for j, line in enumerate(lines)
                 for a,b in combinations(sorted(line),2)}
    six = sum(1 for a,b,c in combinations(range(9),3)
              if all(tuple(sorted(e)) in pair_line for e in ((a,b),(a,c),(b,c)))
              and len({pair_line[tuple(sorted(e))] for e in ((a,b),(a,c),(b,c))}) == 3)
    # Each point is not collinear with exactly two others. Count component cycles.
    noncol = {p: {q for q in range(9) if q != p and tuple(sorted((p,q))) not in pair_line} for p in range(9)}
    assert all(len(adj)==2 for adj in noncol.values())
    components=[]
    seen_vertices=set()
    for seed in range(9):
        if seed in seen_vertices: continue
        todo=[seed]; seen_vertices.add(seed); size=0
        while todo:
            p=todo.pop();size+=1
            for q in noncol[p]:
                if q not in seen_vertices: seen_vertices.add(q);todo.append(q)
        components.append(size)
    found = {
        'noncollinearity_cycle_lengths': sorted(components),
        'six_cycles': six,
        'closure_symbols': len(fa),
        'fixed_orbits': sum(fixed_basin_sizes.values()),
        'two_cycle_orbits': sum(cycle_basin_sizes.values()),
        'recurrent_states': len(fa)*len(fb),
        'transient_states': 262144-len(fa)*len(fb),
        'fixed_attraction_states': sum(k*v for k,v in fixed_basin_sizes.items()),
        'oscillation_attraction_states': sum(k*v for k,v in cycle_basin_sizes.items()),
        'empty_full_cycle_basin': fa[0]*fb[0] + fa[511]*fb[511],
        'line_fiber_histogram': sorted([list(item) for item in Counter(fa.values()).items()]),
        'fixed_basin_histogram': sorted([list(item) for item in fixed_basin_sizes.items()]),
        'two_cycle_basin_histogram': sorted([list(item) for item in cycle_basin_sizes.items()]),
    }
    assert found == expected[name], (name,found,expected[name])
    print(name, 'PASS',json.dumps(found,sort_keys=True))
