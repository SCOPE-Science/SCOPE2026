#!/usr/bin/env python3
"""Generate certified tables: b4_orbits.csv/json, b5_summary.json, certificate.json. Stdlib only."""
import itertools, json, hashlib, time, csv, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from census import (brute_force_antichains, independent_set_antichains,
    antichain_to_truth, truth_to_minimal, dual_truth, popcount)
from orbits import all_perms, canonical_of_fam, orbit_partition, rank_profile, apply_perm_mask
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()
log = {}

# ---- B4 ----
t = time.time()
ac4 = brute_force_antichains(4)
log['b4_enum_s'] = round(time.time() - t, 3)
assert len(ac4) == 168
ac4x = independent_set_antichains(4)
assert len(ac4x) == 168 and set(ac4x) == set(ac4)
# Dedekind recursion D3->D4, D4->D5
ac3 = brute_force_antichains(3)
assert len(ac3) == 20
tr3 = [antichain_to_truth(a, 3) for a in ac3]
assert sum(1 for a in tr3 for b in tr3 if (a | b) == b) == 168
tr4 = sorted(antichain_to_truth(a, 4) for a in ac4)
assert len(set(tr4)) == 168
t = time.time()
d5 = sum(1 for a in tr4 for b in tr4 if (a | b) == b)
log['dedekind_recursion_D5'] = d5
log['dedekind_recursion_s'] = round(time.time() - t, 3)
assert d5 == 7581

perms4 = all_perms(4)
orbits4 = orbit_partition(ac4, perms4, 4)
assert len(orbits4) == 30 and sum(len(v) for v in orbits4.values()) == 168
assert all(24 % len(v) == 0 for v in orbits4.values())

# Burnside by cycle type n=4
def apply_perm_truth(tt, perm, n):
    N = 1 << n; r = 0
    for x in range(N):
        if (tt >> x) & 1:
            r |= (1 << apply_perm_mask(x, perm, n))
    return r
def burnside(truths, perms, n):
    from collections import defaultdict
    tab = defaultdict(list)
    for g in perms:
        vis = [0]*n; cyc = []
        for i in range(n):
            if not vis[i]:
                j = i; L = 0
                while not vis[j]: vis[j] = 1; j = g[j]; L += 1
                cyc.append(L)
        key = tuple(sorted(cyc))
        tab[key].append(sum(1 for tt in truths if apply_perm_truth(tt, g, n) == tt))
    return {str(k): {'class_size': len(v), 'fix': v[0], 'unanimous': len(set(v)) == 1} for k, v in tab.items()}
b4burn = burnside(tr4, perms4, 4)
assert all(v['unanimous'] for v in b4burn.values())
assert sum(v['class_size']*v['fix'] for v in b4burn.values()) == 720  # 24*30

# B4 rows
rows = []
sd_list, seppair = None, None
truthmap = {a: antichain_to_truth(a, 4) for a in ac4}
sd4 = sorted(a for a in ac4 if dual_truth(truthmap[a], 4) == truthmap[a])
assert len(sd4) == 12
for rep in sorted(orbits4):
    members = orbits4[rep]
    has_sd = any(dual_truth(truthmap[m], 4) == truthmap[m] for m in members)
    prof = rank_profile(rep, 4)
    rows.append({'rep': list(rep), 'orbit_size': len(members), 'width': len(rep),
                 'rank_profile': [[k, v] for k, v in prof],
                 'truth': antichain_to_truth(rep, 4),
                 'has_self_dual': has_sd})
# explicit witnesses
maj = (3, 5, 6)
assert maj in sd4  # 2-of-3 majority on vars 0..2, self-dual
A = (1, 2); Ad = truth_to_minimal(dual_truth(antichain_to_truth(A, 4), 4), 4)
assert Ad == (3,)
assert canonical_of_fam(A, perms4, 4) != canonical_of_fam(Ad, perms4, 4)
seppair = {'A': list(A), 'Ad': list(Ad)}
w6 = [a for a in ac4 if len(a) == 6]
assert len(w6) == 1 and tuple(sorted(w6[0])) == (3, 5, 6, 9, 10, 12)

with open(os.path.join(HERE, 'b4_orbits.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['rep', 'orbit_size', 'width', 'rank_profile', 'truth', 'has_self_dual'])
    for r in rows:
        w.writerow(['+'.join(map(str, r['rep'])), r['orbit_size'], r['width'],
                    ';'.join(f'{k}:{v}' for k, v in r['rank_profile']), r['truth'], int(r['has_self_dual'])])
b4data = {'n': 4, 'dedekind': 168, 'num_orbits': 30,
          'orbit_size_hist': dict(Counter(r['orbit_size'] for r in rows)),
          'width_hist_all': dict(Counter(len(a) for a in ac4)),
          'width_hist_reps': dict(Counter(r['width'] for r in rows)),
          'burnside': b4burn,
          'self_dual_count': 12, 'self_dual_list': [list(a) for a in sd4],
          'self_dual_orbit_reps': sorted(list(set(canonical_of_fam(a, perms4, 4) for a in sd4))),
          'fixed_witness': list(maj), 'fixed_witness_truth': antichain_to_truth(maj, 4),
          'separating_pair': seppair,
          'width6_witness': [3, 5, 6, 9, 10, 12],
          'orbits': rows}
with open(os.path.join(HERE, 'b4_orbits.json'), 'w') as f:
    json.dump(b4data, f, indent=1, sort_keys=True)

# ---- B5 ----
t = time.time()
ac5 = independent_set_antichains(5)
log['b5_enum_s'] = round(time.time() - t, 3)
assert len(ac5) == 7581
mid2 = tuple(sorted(m for m in range(32) if popcount(m) == 2))
mid3 = tuple(sorted(m for m in range(32) if popcount(m) == 3))
w10 = sorted(tuple(sorted(a)) for a in ac5 if len(a) == 10)
assert w10 == sorted([mid2, mid3])
tr5 = sorted(antichain_to_truth(a, 5) for a in ac5)
t = time.time()
perms5 = all_perms(5)
orbits5 = orbit_partition(ac5, perms5, 5)
log['b5_orbit_s'] = round(time.time() - t, 3)
assert len(orbits5) == 210 and sum(len(v) for v in orbits5.values()) == 7581
assert all(120 % len(v) == 0 for v in orbits5.values())
t = time.time()
b5burn = burnside(tr5, perms5, 5)
log['b5_burnside_s'] = round(time.time() - t, 3)
assert all(v['unanimous'] for v in b5burn.values())
assert sum(v['class_size']*v['fix'] for v in b5burn.values()) == 25200  # 120*210
sd5 = [a for a in ac5 if dual_truth(antichain_to_truth(a, 5), 5) == antichain_to_truth(a, 5)]
assert len(sd5) == 81
assert dual_truth(antichain_to_truth(mid3, 5), 5) == antichain_to_truth(mid3, 5)  # rank-3 mid is self-dual
assert dual_truth(antichain_to_truth(mid2, 5), 5) != antichain_to_truth(mid2, 5)
A5 = (1, 2); Ad5 = truth_to_minimal(dual_truth(antichain_to_truth(A5, 5), 5), 5)
assert Ad5 == (3,) and canonical_of_fam(A5, perms5, 5) != canonical_of_fam(Ad5, perms5, 5)
# duality preserves orbit sizes
for a in ac5:
    da = truth_to_minimal(dual_truth(antichain_to_truth(a, 5), 5), 5)
    assert len(orbits5[canonical_of_fam(a, perms5, 5)]) == len(orbits5[canonical_of_fam(da, perms5, 5)])
b5data = {'n': 5, 'dedekind': 7581, 'num_orbits': 210,
          'orbit_size_hist': dict(Counter(len(v) for v in orbits5.values())),
          'width_hist_all': dict(Counter(len(a) for a in ac5)),
          'burnside': b5burn,
          'self_dual_count': 81,
          'self_dual_width_hist': dict(Counter(len(a) for a in sd5)),
          'width10_witnesses': [list(mid2), list(mid3)],
          'self_dual_witness': list(mid3),
          'singleton_self_dual_witness': [16],
          'separating_pair': {'A': [1, 2], 'Ad': [3]}}
with open(os.path.join(HERE, 'b5_summary.json'), 'w') as f:
    json.dump(b5data, f, indent=1, sort_keys=True)

def sha(p):
    import hashlib
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()
cert = {'log': log, 'total_s': round(time.time() - t_start, 3),
        'sha256': {f: sha(os.path.join(HERE, f)) for f in
                   ['census.py', 'orbits.py', 'generate.py', 'b4_orbits.csv', 'b4_orbits.json', 'b5_summary.json']}}
with open(os.path.join(HERE, 'certificate.json'), 'w') as f:
    json.dump(cert, f, indent=1, sort_keys=True)
print(json.dumps(cert, indent=1))
print('ALL TABLES OK')
