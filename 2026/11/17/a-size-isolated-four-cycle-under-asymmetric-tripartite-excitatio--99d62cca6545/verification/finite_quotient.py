#!/usr/bin/env python3
"""Exact finite colored-initial-color class proof for a three-shore (1,1,2) excitable system.
No third-party packages or external inputs are needed.
"""
import itertools
import collections
import csv
import pathlib
import sys

THRESHOLDS = (1, 1, 2)
CAPS = [x for x in itertools.product(range(3), repeat=3) if any(x)]


def trajectory(initial):
    # Each initial-color initial-color class is forever monochromatic. Carry initial-color class identity
    # and its capped population, so a periodic color histogram is never mistaken
    # for a periodic labelled configuration.
    shore, weight, colors = [], [], []
    for i, triple in enumerate(initial):
        for color, number in enumerate(triple):
            if number:
                shore.append(i)
                weight.append(number)
                colors.append(color)
    shore, weight, colors = tuple(shore), tuple(weight), tuple(colors)
    first_seen = {}
    t = 0
    while colors not in first_seen:
        first_seen[colors] = t
        excited = [0, 0, 0]
        for i, c, mass in zip(shore, colors, weight):
            if c == 1:
                excited[i] += mass
        firing = tuple(sum(excited[j] for j in range(3) if j != i)
                       >= THRESHOLDS[i] for i in range(3))
        colors = tuple(0 if (c == 0 and not firing[i]) else (c + 1) % 3
                       for i, c in zip(shore, colors))
        t += 1
        assert t <= 64, 'unexpected orbit longer than proved finite bound'
    return first_seen[colors], t - first_seen[colors]


def feasible(triple, size):
    minimum = sum(triple)
    return minimum <= size and (minimum == size or 2 in triple)


def main():
    states = list(itertools.product(CAPS, repeat=3))
    assert len(CAPS) == 26 and len(states) == 17576
    entries = [(s, *trajectory(s)) for s in states]
    hist = collections.Counter((t, p) for s, t, p in entries)
    expected = {
        (0, 1): 8, (0, 3): 5600, (0, 4): 4,
        (1, 1): 504, (1, 3): 1380, (1, 4): 28,
        (2, 1): 1008, (2, 3): 2096, (2, 4): 52,
        (3, 1): 980, (3, 3): 2600, (3, 4): 40,
        (4, 1): 552, (4, 3): 1408, (4, 4): 32,
        (5, 1): 144, (5, 3): 668,
        (6, 1): 72, (6, 3): 268,
        (7, 1): 56, (7, 3): 76,
    }
    assert hist == expected, (hist - expected, expected - hist)
    assert set(p for _, p in hist) == {1, 3, 4}
    assert max(t for t, _ in hist) == 7
    p4 = [s for s, t, p in entries if t == 0 and p == 4]
    expected_p4 = {
        ((1, 0, 1), (1, 1, 0), (1, 0, 0)),
        ((1, 0, 1), (1, 1, 0), (2, 0, 0)),
        ((1, 1, 0), (1, 0, 1), (1, 0, 0)),
        ((1, 1, 0), (1, 0, 1), (2, 0, 0)),
    }
    assert set(p4) == expected_p4
    assert trajectory(((1,0,0),(1,1,0),(0,1,1))) == (7,1)
    # Explicitly check universal period identity F^19=F^7 at the initial-color class level
    # by structural implications from the histogram, not by sampled sizes.
    assert all(t <= 7 and 12 % p == 0 for _, t, p in entries)
    # Every population at fixed size is represented by a feasible signature;
    # sizes beyond 7 have identical feasible signatures to 7.
    for tr in CAPS:
        for size in range(7, 13):
            assert feasible(tr, size) == feasible(tr, 7)
    for a in range(1, 8):
        for b in range(1, 8):
            for c in range(1, 8):
                periodic = [p for s, t, p in entries if t == 0 and all(
                    feasible(s[i], (a,b,c)[i]) for i in range(3))]
                assert (4 in periodic) == (a == 2 and b == 2)
                assert (3 in periodic) == (a >= 2 or b >= 2)
    root = pathlib.Path(__file__).resolve().parents[1]
    cert = root / 'certificates' / 'all_signatures.csv'
    with cert.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(('A0','A1','A2','B0','B1','B2','C0','C1','C2','entry','period'))
        for s, t, p in entries:
            writer.writerow((*s[0],*s[1],*s[2],t,p))
    # Reopen and compare every certificate line with actual calculation.
    with cert.open(newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    assert len(rows) == len(states)+1
    assert [tuple(map(int, row)) for row in rows[1:]] == [
        (*s[0],*s[1],*s[2],t,p) for s,t,p in entries]
    print('ALL_SIGNATURES',len(entries),'HISTOGRAM',dict(sorted(hist.items())))
    print('GLOBAL_CUTOFF',max(t for _,t,p in entries),
          'PERIODS',sorted({p for _,t,p in entries}))
    print('PERIOD_FOUR_PROFILES',p4)
    print('SHARP_SEVEN_WITNESS',((1,0,0),(1,1,0),(0,1,1)))
    print('CERTIFICATE',cert.name,'ROWS',len(rows)-1)
    print('PASS')

if __name__ == '__main__':
    main()
