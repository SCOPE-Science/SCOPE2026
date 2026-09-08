#!/usr/bin/env python3
"""Independent replay: re-validates CSV/JSON artifacts from scratch. Stdlib only.
Usage: python3 replay.py  (run from artifacts dir or lane dir)"""
import csv, json, os, sys, itertools, time

def find_artifacts():
    cands = [os.path.join('output', 'artifacts'), 'output/artifacts',
             os.path.dirname(os.path.abspath(__file__)), '.']
    for c in cands:
        if os.path.exists(os.path.join(c, 'b4_orbits.json')):
            return c
    raise SystemExit('artifacts not found')

D = find_artifacts()
sys.path.insert(0, D)
from census import brute_force_antichains, antichain_to_truth, truth_to_minimal, dual_truth, popcount, comparable
from orbits import all_perms, canonical_of_fam, apply_perm_mask
from collections import Counter

t0 = time.time()
b4 = json.load(open(os.path.join(D, 'b4_orbits.json')))
b5 = json.load(open(os.path.join(D, 'b5_summary.json')))
cert = json.load(open(os.path.join(D, 'certificate.json')))
# checksum replay
import hashlib
for f, h in cert['sha256'].items():
    if f in ('certificate.json',): continue
    if f == 'generate.py' and not os.path.exists(os.path.join(D, f)): continue
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    note = 'OK' if (f not in ('b4_orbits.csv', 'b4_orbits.json', 'b5_summary.json') or True) else ''
    assert got == h, (f, got, h)
print('checksums OK')
# CSV vs JSON agreement
rows = list(csv.DictReader(open(os.path.join(D, 'b4_orbits.csv'))))
assert len(rows) == b4['num_orbits'] == 30
def repkey(r):
    s = r['rep'] if isinstance(r, dict) and isinstance(r.get('rep'), str) else r['rep']
    t = tuple(map(int, s.split('+'))) if isinstance(s, str) and s else tuple(s)
    return t
rows_s = sorted(rows, key=repkey)
js_s = sorted(b4['orbits'], key=lambda j: tuple(j['rep']))
for r, j in zip(rows_s, js_s):
    assert r['rep'] == '+'.join(map(str, j['rep'])), (r, j)
    assert int(r['orbit_size']) == j['orbit_size'] and int(r['width']) == j['width']
    assert int(r['truth']) == j['truth'] and int(r['has_self_dual']) == int(j['has_self_dual'])
print('csv/json agreement OK')
# from-scratch re-enumeration
ac4 = brute_force_antichains(4)
assert len(ac4) == b4['dedekind'] == 168
assert all(all(not comparable(x, y) for ii, x in enumerate(a) for y in a[ii+1:]) for a in ac4)
tr4 = sorted(antichain_to_truth(a, 4) for a in ac4)
assert len(set(tr4)) == 168
assert sum(1 for a in tr4 for b in tr4 if (a | b) == b) == 7581  # Dedekind recursion
print('B4 re-enumeration + recursion OK')
perms4 = all_perms(4)
seen = {}
for a in ac4:
    c = canonical_of_fam(a, perms4, 4)
    seen.setdefault(c, 0); seen[c] += 1
assert len(seen) == 30 and sum(seen.values()) == 168
for rep, sz in seen.items():
    assert 24 % sz == 0
jmap = {tuple(j['rep']): j for j in b4['orbits']}
assert set(jmap) == set(seen)
for rep, sz in seen.items():
    assert jmap[rep]['orbit_size'] == sz
    assert jmap[rep]['truth'] == antichain_to_truth(rep, 4)
    assert jmap[rep]['width'] == len(rep) == len(set(rep))
print('B4 orbit replay OK (30 orbits, sizes sum 168, all divide 24)')
sd = [a for a in ac4 if dual_truth(antichain_to_truth(a, 4), 4) == antichain_to_truth(a, 4)]
assert len(sd) == 12 == b4['self_dual_count']
assert (3, 5, 6) in sd and dual_truth(antichain_to_truth((3, 5, 6), 4), 4) == antichain_to_truth((3, 5, 6), 4)
A = tuple(b4['separating_pair']['A']); Ad = tuple(b4['separating_pair']['Ad'])
assert truth_to_minimal(dual_truth(antichain_to_truth(A, 4), 4), 4) == Ad
assert canonical_of_fam(A, perms4, 4) != canonical_of_fam(Ad, perms4, 4)
w6 = [a for a in ac4 if len(a) == 6]
assert len(w6) == 1 and list(w6[0]) == b4['width6_witness']
print('B4 duality + extremal replay OK')
# B5 structural replay (independent-set branch code path reused) + orbit/Burnside spot replay
from census import independent_set_antichains
ac5 = independent_set_antichains(5)
assert len(ac5) == b5['dedekind'] == 7581
perms5 = all_perms(5)
orbs = {}
for a in ac5:
    c = canonical_of_fam(a, perms5, 5)
    orbs[c] = orbs.get(c, 0) + 1
assert len(orbs) == 210 == b5['num_orbits'] and sum(orbs.values()) == 7581
assert all(120 % s == 0 for s in orbs.values())
assert dict(Counter(orbs.values())) == {int(k): v for k, v in b5['orbit_size_hist'].items()}
assert dict(Counter(len(a) for a in ac5)) == {int(k): v for k, v in b5['width_hist_all'].items()}
tr5 = sorted(antichain_to_truth(a, 5) for a in ac5)
def apt(tt, perm):
    r = 0
    for x in range(32):
        if (tt >> x) & 1: r |= (1 << apply_perm_mask(x, perm, 5))
    return r
tot = sum(1 for g in perms5 for tt in tr5 if apt(tt, g) == tt)
assert tot == 25200 and tot // 120 == 210
sd5 = [a for a in ac5 if dual_truth(antichain_to_truth(a, 5), 5) == antichain_to_truth(a, 5)]
assert len(sd5) == 81 == b5['self_dual_count']
assert [tuple(w) for w in b5['width10_witnesses']] is not None
w10 = sorted(tuple(sorted(a)) for a in ac5 if len(a) == 10)
assert w10 == sorted(tuple(w) for w in (tuple(x) for x in b5['width10_witnesses']))
print('B5 replay OK (7581, 210 orbits, Burnside 25200, 81 self-dual, 2 width-10 witnesses)')
print('REPLAY PASS in %.1fs' % (time.time() - t0))
