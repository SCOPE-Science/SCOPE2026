"""Independent exhaustive NFA census by reverse distinguishability closure.

Run: python3 verify/distinguishability_enumeration.py data/joint_spectrum.csv
"""
import csv
import sys
from collections import Counter
from itertools import product


def image_actions(code):
    row = ((code >> (3*i)) & 7 for i in range(3))
    row = tuple(row)
    return tuple(
        (row[0] if mask & 1 else 0)
        | (row[1] if mask & 2 else 0)
        | (row[2] if mask & 4 else 0)
        for mask in range(8)
    )


def measure(aa, bb, final_state):
    reachable = [1]  # initial state {0}
    visited = {1}
    for subset in reachable:
        for successor in (aa[subset], bb[subset]):
            if successor not in visited:
                visited.add(successor)
                reachable.append(successor)

    # Pair is distinguishable if some finite continuation has different acceptance.
    f = 1 << final_state
    different = {
        (u, v) for u in reachable for v in reachable
        if bool(u & f) != bool(v & f)
    }
    while True:
        grown = different | {
            (u, v) for u in reachable for v in reachable
            if (aa[u], aa[v]) in different or (bb[u], bb[v]) in different
        }
        if len(grown) == len(different):
            break
        different = grown

    representatives = []
    for u in reachable:
        if all((u, v) in different for v in representatives):
            representatives.append(u)

    accessible = 0
    for s in reachable:
        accessible |= s
    coaccessible = f
    while True:
        nxt = coaccessible
        for i in range(3):
            if (aa[1 << i] | bb[1 << i]) & coaccessible:
                nxt |= 1 << i
        if nxt == coaccessible:
            break
        coaccessible = nxt
    return len(reachable), len(representatives), (accessible == 7 and coaccessible == 7)


def run():
    assert len(sys.argv) == 2, 'Pass expected CSV path'
    with open(sys.argv[1], newline='', encoding='utf-8') as f:
        reference = {
            (row['case'], int(row['reachable']), int(row['minimal'])):
            (int(row['all']), int(row['trim']))
            for row in csv.DictReader(f)
        }
    actions = tuple(map(image_actions, range(512)))
    observed = Counter()
    trim_observed = Counter()
    for a, b in product(range(512), repeat=2):
        for case, final_state in (('coincident', 0), ('distinct', 2)):
            r, m, trim = measure(actions[a], actions[b], final_state)
            observed[case, r, m] += 1
            if trim:
                trim_observed[case, r, m] += 1
    got = {key: (count, trim_observed[key]) for key, count in observed.items()}
    assert got == reference, (got, reference)
    assert len(got) == 62 and sum(observed.values()) == 524288
    assert sum(v for (case, _, _), v in trim_observed.items() if case == 'coincident') == 190080
    assert sum(v for (case, _, _), v in trim_observed.items() if case == 'distinct') == 209664
    print('PASS distinguishability census: 62 cells, 524288 transition/final cases')

if __name__ == '__main__':
    run()
