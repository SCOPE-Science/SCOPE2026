#!/usr/bin/env python3
"""Finite Heawood-graph excitation census: reproducible two-method comparison."""
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
import csv

here = Path(__file__).resolve().parent
expected = {}
with (here / 'heawood4_census.csv').open(encoding='utf-8', newline='') as stream:
    for row in csv.DictReader(stream):
        key = (int(row['entry_time']), int(row['eventual_period']))
        assert key not in expected
        expected[key] = int(row['states'])
assert sum(expected.values()) == 4**14
assert sum(c for (d, p), c in expected.items() if d == 0) == 3753

def run_method(source, binary):
    run(['g++', '-std=c++17', '-O3', str(here / source), '-o', str(binary)], check=True)
    output = run([str(binary)], capture_output=True, text=True, check=True).stdout
    values = {}
    for line in output.splitlines():
        if not line.startswith('COUNT,'):
            continue
        _, d, p, c = line.split(',')
        key = int(d), int(p)
        assert key not in values
        values[key] = int(c)
    assert values == expected, (source, 'census mismatch')
    return output

with TemporaryDirectory() as workspace:
    for name in ('heawood4_walk.cpp', 'heawood4_pruning.cpp'):
        output = run_method(name, Path(workspace) / name.replace('.cpp', ''))
        print(name, 'PASS', len(expected), 'joint classes')
print('Two distinct full-state enumerations agree on all 268435456 labelled states.')
