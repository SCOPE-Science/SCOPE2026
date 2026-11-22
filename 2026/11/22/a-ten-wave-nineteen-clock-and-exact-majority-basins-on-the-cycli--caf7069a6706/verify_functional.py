"""Complete Boolean functional-graph census for the cyclic tournament of order 19.

Usage: python3 verify_functional.py [--json OUTPUT]
Only the Python standard library is required.
"""
import json
import sys
from collections import Counter, defaultdict

N = 19
STATES = 1 << N
MASK = STATES - 1
OUT = tuple(sum(1 << ((i + j) % N) for j in range(1, 10)) for i in range(N))


def step(x):
    y = 0
    for i, adjacent in enumerate(OUT):
        if (x & adjacent).bit_count() >= 5:
            y |= 1 << i
    return y


def arc(k):
    return (1 << k) - 1


def rotate(x, t):
    t %= N
    return ((x << t) | (x >> (N - t))) & MASK if t else x


def census():
    successor = [step(x) for x in range(STATES)]
    depths = [-1] * STATES
    periods = [0] * STATES
    roots = [-1] * STATES
    cycles = {}
    for start in range(STATES):
        if depths[start] >= 0:
            continue
        path = []
        place = {}
        u = start
        while depths[u] < 0 and u not in place:
            place[u] = len(path)
            path.append(u)
            u = successor[u]
        if depths[u] >= 0:
            d, p, r = depths[u], periods[u], roots[u]
            for v in reversed(path):
                d += 1
                depths[v], periods[v], roots[v] = d, p, r
        else:
            j = place[u]
            cycle = path[j:]
            r = min(cycle)
            p = len(cycle)
            assert r not in cycles
            cycles[r] = cycle
            for v in cycle:
                depths[v], periods[v], roots[v] = 0, p, r
            d = 0
            for v in reversed(path[:j]):
                d += 1
                depths[v], periods[v], roots[v] = d, p, r
    assert all(d >= 0 for d in depths)
    assert all(successor[successor[u]] == successor[u] for u in (0, MASK))
    length_histogram = Counter(len(c) for c in cycles.values())
    assert length_histogram == {1: 2, 19: 10}, length_histogram
    expected_cycles = {frozenset(rotate(arc(k), t) for t in range(N)): k
                       for k in range(5, 15)}
    assert len(expected_cycles) == 10
    assert {frozenset(c) for c in cycles.values() if len(c) == 19} == set(expected_cycles)
    assert all(step(rotate(arc(k),t)) == rotate(arc(k),t-5)
               for k in range(5,15) for t in range(N))
    representatives = {r: (0 if r == 0 else (N if r == MASK else expected_cycles[frozenset(c)]))
                       for r, c in cycles.items()}
    basins = Counter(roots)
    by_length = Counter(len(c) for c in cycles.values())
    depth_period = Counter(zip(depths,periods))
    depth_hist = Counter(depths)
    maxdepth = max(depths)
    witness = min(u for u in range(STATES) if depths[u] == maxdepth)
    per_arc = {str(representatives[r]): basins[r]
               for r, c in cycles.items() if len(c) == 19}
    assert len(per_arc) == 10
    # Complement and cyclic rotation symmetry.
    assert all(basins[r] == basins[roots[MASK ^ r]] for r in cycles)
    assert all(depths[u] == depths[rotate(u,1)] for u in range(STATES))
    assert all(depths[u] == depths[MASK ^ u] for u in range(STATES))
    output = {
        'model': 'cyclic tournament on Z/19Z, arcs i->i+j for 1<=j<=9, synchronous strict out-neighbor majority',
        'states': STATES, 'cycles_by_period': dict(sorted(by_length.items())),
        'first_entry_by_period': [{'entry':d,'period':p,'count':count}
            for (d,p),count in sorted(depth_period.items())],
        'first_entry_total': {str(d):v for d,v in sorted(depth_hist.items())},
        'maximal_first_entry': max(depths), 'least_maximal_entry_state': witness,
        'basin_of_zero': basins[0], 'basin_of_one': basins[MASK],
        'arc_cycle_basin_by_ones': dict(sorted(per_arc.items(),key=lambda e:int(e[0]))),
        'periodic_states_by_period': {str(p):sum(1 for d,pp in zip(depths,periods) if d==0 and pp==p) for p in sorted(by_length)},
        'attracted_states_by_period': dict(sorted(Counter(periods).items())),
        'periodic_arc_lengths': list(range(5,15)),
        'cycle_representatives': [{'ones':representatives[r], 'root_mask':r,'basin_size':basins[r]}
            for r in sorted(cycles) if len(cycles[r]) == 19],
    }
    assert sum(basins.values())==STATES
    assert sum(depth_hist.values())==STATES
    return output


if __name__=='__main__':
    x=census()
    data=json.dumps(x,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if len(sys.argv)==3 and sys.argv[1]=='--json':
        with open(sys.argv[2],'w',encoding='utf-8') as f:f.write(data)
    print(data,end='')
