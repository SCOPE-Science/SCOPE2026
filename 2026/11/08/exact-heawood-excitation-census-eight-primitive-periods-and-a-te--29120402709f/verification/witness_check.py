"""Direct per-vertex transition checks for representative Heawood trajectories."""
import json
from pathlib import Path

N = 14
lines = [tuple((j + k) % 7 for k in (0, 1, 3)) for j in range(7)]
neighbors = [[] for _ in range(N)]
for j, line in enumerate(lines):
    for v in line:
        neighbors[v].append(7 + j)
        neighbors[7 + j].append(v)
assert all(len(x) == 3 for x in neighbors)


def unpack(x):
    return [(x // (3 ** i)) % 3 for i in range(N)]


def step(x):
    a = unpack(x)
    b = [2 if a[i] == 1 else
         (1 if a[i] == 0 and any(a[j] == 1 for j in neighbors[i]) else 0)
         for i in range(N)]
    return sum(v * 3**i for i, v in enumerate(b))

reps = {1: 0, 3: 39208, 4: 29913, 5: 10942, 6: 2189,
        8: 30641, 10: 8756, 14: 28457}
cert = {'graph': {'vertices': N, 'lines': [list(x) for x in lines]}, 'cycles': []}
for p, start in sorted(reps.items()):
    states = [start]
    for j in range(p):
        nxt = step(states[-1])
        if j + 1 < p:
            assert nxt not in states
            states.append(nxt)
        else:
            assert nxt == start
    assert len(states) == p
    cert['cycles'].append({'period': p, 'representative': start,
        'states_base3_0_to_13': [''.join(str(k) for k in unpack(x)) for x in states],
        'states_integer': states})

start = 29084
trail = [start]
for _ in range(14):
    trail.append(step(trail[-1]))
assert len(set(trail[:14])) == 14
assert trail[10] == trail[14]
assert all(trail[t] != trail[t+4] for t in range(10))
cert['max_transient'] = {'representative': start,
    'preperiod': 10, 'period': 4,
    'trajectory_integer_0_to_14': trail,
    'trajectory_base3_0_to_13': [''.join(str(k) for k in unpack(x)) for x in trail]}

p = Path(__file__).with_name('witnesses.json')
p.write_text(json.dumps(cert, indent=2, ensure_ascii=False)+'\n',encoding='utf-8')
print('WITNESS_CHECK_PASS periods',','.join(map(str,reps)), 'maxT=10 P=4')
