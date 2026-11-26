"""Check two independently enumerated full reset-threshold spectra.

Requires a C++17 compiler and Python 3. No third-party packages.
From this directory: python3 verify_spectrum.py
"""
from collections import deque
from pathlib import Path
import csv
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
EXPECTED = {}
LABELED = {}
FIXED = {}
with (HERE / 'spectrum.csv').open(newline='') as f:
    for row in csv.DictReader(f):
        t = int(row['reset_threshold'])
        EXPECTED[t] = int(row['rotation_classes'])
        LABELED[t] = int(row['labeled_maps'])
        FIXED[t] = int(row['halfturn_fixed_labeled'])
assert sum(EXPECTED.values()) == 670608
assert sum(LABELED.values()) == 5362560
assert sum(FIXED.values()) == 2304
assert EXPECTED[-1] == 6928 and EXPECTED[36] == 1
assert EXPECTED.get(35) == 1 and EXPECTED.get(34, 0) == 0
assert sum(k > 28 and n for k, n in EXPECTED.items()) == 7
assert all((LABELED[t] + FIXED[t]) // 8 == EXPECTED[t] for t in EXPECTED)

with tempfile.TemporaryDirectory() as td:
    outputs = {}
    for src, name in [('orbit_census.cpp', 'orbit'),
                      ('labeled_crosscheck.cpp', 'labeled')]:
        exe = Path(td) / name
        subprocess.run(['c++', '-std=c++17', '-O2', str(HERE / src), '-o', str(exe)], check=True)
        outputs[name] = subprocess.run([str(exe)], text=True, capture_output=True,
                                       check=True).stdout.splitlines()

orbit = {}
for line in outputs['orbit']:
    words = line.split()
    if len(words) == 2 and words[0].lstrip('-').isdigit():
        orbit[int(words[0])] = int(words[1])
assert orbit == EXPECTED, ('orbit mismatch', orbit, EXPECTED)
assert 'rank6=5362560' in outputs['orbit'][0]
assert 'classes=670608' in outputs['orbit'][0]
assert 'mass=5362560' in outputs['orbit'][0]
assert 'max=36' in outputs['orbit'][0]
assert outputs['orbit'][-1] == '01234017'

labeled = {}
fixed = {}
for line in outputs['labeled']:
    if ',' in line and line.split(',')[0].lstrip('-').isdigit():
        t, count, invariant, orbits = (int(q) for q in line.split(','))
        labeled[t] = count
        fixed[t] = invariant
        assert orbits == EXPECTED[t]
assert labeled == LABELED
assert fixed == FIXED
assert 'labeled=5362560' in outputs['labeled'][0]
assert 'max=36' in outputs['labeled'][0]
assert 'exemplar=01234017' in outputs['labeled'][0]

# Third, differently encoded Python state search checks the extremal witness.
b = (0, 1, 2, 3, 4, 0, 1, 7)
def move(mask, letter):
    value = 0
    for i in range(8):
        if mask & (1 << i):
            value |= 1 << ((i+1) % 8 if letter == 'a' else b[i])
    return value

parents = {255: (None, '')}
queue = deque([255])
terminal = None
while queue:
    state = queue.popleft()
    if state & (state-1) == 0:
        terminal = state
        break
    for symbol in 'ab':
        successor = move(state, symbol)
        if successor not in parents:
            parents[successor] = (state, symbol)
            queue.append(successor)
assert terminal is not None
word = ''
state = terminal
while parents[state][0] is not None:
    parent, symbol = parents[state]
    word = symbol + word
    state = parent
assert len(word) == 36
assert word == 'baaaaabaaaabaaaaaabaaaaabaaaaabaaaab'
assert terminal == 1
print('VERIFIED', len(EXPECTED), 'threshold entries;', sum(EXPECTED.values()),
      'orbits;', sum(LABELED.values()), 'labeled maps; extremal length 36')
print('EXTREMAL_RESET_WORD', word)
