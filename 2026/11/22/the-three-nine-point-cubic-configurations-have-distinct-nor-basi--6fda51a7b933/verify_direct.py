#!/usr/bin/env python3
"""Independent complete functional-graph census of 262,144 states per incidence graph.

Uses direct per-vertex OR/NOR updates, not the closure formulas.
Run beside CONFIGURATIONS.json and EXPECTED_COUNTS.json:
    python verify_direct.py
"""
import json
from pathlib import Path
from collections import Counter, defaultdict
from itertools import combinations

base = Path(__file__).resolve().parent
sets = json.loads((base / 'CONFIGURATIONS.json').read_text(encoding='utf-8'))['configurations']
expected = json.loads((base / 'EXPECTED_COUNTS.json').read_text(encoding='utf-8'))
N = 1 << 18
for name, lines in sets.items():
    # Build adjacency lists independently from the input triples.
    nbrs = [[] for _ in range(18)]
    for j, line in enumerate(lines):
        for p in line:
            nbrs[p].append(9+j)
            nbrs[9+j].append(p)
    assert all(len(x)==3 for x in nbrs)
    def update(state):
        val=0
        for v, ns in enumerate(nbrs):
            if all((state & (1<<w))==0 for w in ns):val|=1<<v
        return val
    succ = [update(s) for s in range(N)]
    assert all(succ[succ[succ[s]]] == succ[s] for s in range(N))
    recurrent=set(succ)
    assert all(succ[succ[s]]==s for s in recurrent)
    fixed=[s for s in recurrent if succ[s]==s]
    orbit_key=lambda s:tuple(sorted((s,succ[s])))
    cycles={orbit_key(s) for s in recurrent if succ[s]!=s}
    fixed_basin=Counter();cycle_basin=Counter()
    for initial in range(N):
        dest=succ[initial]
        if succ[dest]==dest:fixed_basin[dest]+=1
        else:cycle_basin[orbit_key(dest)]+=1
    fixed_hist=Counter(fixed_basin.values())
    cycle_hist=Counter(cycle_basin.values())
    canonical = cycle_basin[tuple(sorted((0,N-1)))]
    # Independently recover the noncollinearity cycle decomposition.
    not_collinear=[]
    for p in range(9):
        adjacent_points={q for j in nbrs[p] for q in nbrs[j] if q != p}
        not_collinear.append({q for q in range(9) if q != p and q not in adjacent_points})
    assert all(len(ns)==2 for ns in not_collinear)
    components=[]; unseen=set(range(9))
    while unseen:
        seed=next(iter(unseen)); stack=[seed];unseen.remove(seed); count=0
        while stack:
            p=stack.pop();count+=1
            for q in not_collinear[p]:
                if q in unseen:unseen.remove(q);stack.append(q)
        components.append(count)
    found = {
        'noncollinearity_cycle_lengths':sorted(components),
        'fixed_orbits':len(fixed), 'two_cycle_orbits':len(cycles),
        'recurrent_states':len(recurrent), 'transient_states':N-len(recurrent),
        'fixed_attraction_states':sum(fixed_basin.values()),
        'oscillation_attraction_states':sum(cycle_basin.values()),
        'empty_full_cycle_basin':canonical,
        'fixed_basin_histogram':sorted([list(t) for t in fixed_hist.items()]),
        'two_cycle_basin_histogram':sorted([list(t) for t in cycle_hist.items()]),
    }
    for key, value in found.items():assert value==expected[name][key],(name,key,value,expected[name][key])
    assert len(fixed_basin)==len(fixed) and len(cycle_basin)==len(cycles)
    assert sum(fixed_basin.values())+sum(cycle_basin.values())==N
    print(name,'PASS',json.dumps(found,sort_keys=True))
