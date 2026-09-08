#!/usr/bin/env python3
"""Step 5 (audit plan Step 5): independent replay with a second script.

Checks:
 (a) every logged coset table is closed, deterministic, inverse-consistent,
     connected (transitive action), and both relators act trivially at every point;
 (b) |G| is divisible by the abelianization order (necessary condition);
 (c) every growth ball recomputes: independent BFS from scratch over normal forms
     reproduces sphere/ball counts and the claimed lower bound holds.
"""
import csv, json, os, sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results.csv")
CTAB = os.path.join(HERE, "coset_tables")
G2I = {'a': 0, 'A': 1, 'b': 2, 'B': 3}
INV = [1, 0, 3, 2]
fails = []

rows = list(csv.DictReader(open(RES)))
n_tab = 0
for r in rows:
    if r['status'] != 'finite_closed_table':
        continue
    pid, w1, w2, order = r['id'], r['w1'], r['w2'], int(r['order'])
    p = os.path.join(CTAB, f'{pid}.json')
    if not os.path.exists(p):
        fails.append(f'{pid}: missing table file'); continue
    t = json.load(open(p))
    tab = {int(k): v for k, v in t['table'].items()}
    assert t['w1'] == w1 and t['w2'] == w2 and t['order'] == order
    n = order
    if set(tab.keys()) != set(range(1, n + 1)):
        fails.append(f'{pid}: keys not 1..{n}'); continue
    ok = True
    for c, row in tab.items():
        for g in range(4):
            d = row[g]
            if not (1 <= d <= n) or tab[d][INV[g]] != c:
                fails.append(f'{pid}: inverse-inconsistent at {c},{g}'); ok = False; break
        if not ok:
            break
    # connectivity from 1
    seen = {1}; q = deque([1])
    while q:
        c = q.popleft()
        for g in range(4):
            d = tab[c][g]
            if d not in seen:
                seen.add(d); q.append(d)
    if len(seen) != n:
        fails.append(f'{pid}: disconnected ({len(seen)}/{n}))')
    # relators trivial everywhere
    for w in (w1, w2):
        for c in range(1, n + 1):
            x = c
            for ch in w:
                x = tab[x][G2I[ch]]
            if x != c:
                fails.append(f'{pid}: relator {w} nontrivial at {c}'); break
    # ab divisibility
    if order % int(r['ab_order']) != 0:
        fails.append(f'{pid}: ab-order does not divide group order')
    n_tab += 1

print(f'coset tables replayed: {n_tab}, failures: {len(fails)}')
for f in fails[:20]:
    print(' FAIL:', f)

# growth recompute
def mult(s, gen, m, n):
    g, k = gen
    if not s:
        return ((g, k % (m if g == 'a' else n)),)
    lg, lk = s[-1]
    if lg == g:
        mod = m if g == 'a' else n
        nk = (lk + k) % mod
        if nk == 0:
            return s[:-1]
        return s[:-1] + ((g, nk),)
    return s + ((g, k),)

import math
gfails = []
for name, (m, n) in {'g1': (2, 3), 'g2': (2, 4), 'g3': (3, 3)}.items():
    rec = json.load(open(os.path.join(HERE, f'growth_{name}.json')))
    R = rec['radius']
    seen = {(): 0}; q = deque([()])
    dist = {}
    while q:
        s = q.popleft(); d = seen[s]
        dist[d] = dist.get(d, 0) + 1
        if d == R:
            continue
        for gen in (('a', 1), ('a', m - 1), ('b', 1), ('b', n - 1)):
            ns = mult(s, gen, m, n)
            if ns not in seen:
                seen[ns] = d + 1; q.append(ns)
    sp = [dist.get(k, 0) for k in range(R + 1)]
    b = []; c = 0
    for k in range(R + 1):
        c += sp[k]; b.append(c)
    if sp != rec['sphere_sizes'] or b != rec['ball_sizes']:
        gfails.append(f'{name}: ball mismatch')
    lb = rec['lower_bound_values']
    if not all(x >= y for x, y in zip(b, lb)):
        gfails.append(f'{name}: lower bound fails on recompute')
    print(name, 'recomputed balls match:', sp == rec['sphere_sizes'], 'bound holds:', all(x >= y for x, y in zip(b, lb)))

print(f'growth logs replayed: 3, failures: {len(gfails)}')
if fails or gfails:
    sys.exit(1)
print('REPLAY: ALL PASS')
