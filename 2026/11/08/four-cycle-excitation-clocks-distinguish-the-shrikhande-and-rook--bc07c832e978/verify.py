#!/usr/bin/env python3
"""Replay the complete finite functional-graph census and its symmetry refinement."""
from pathlib import Path
import subprocess
import tempfile
import sys
import csv

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    'rook': {'cycles': {1: 1, 3: 3987936, 4: 98}, 'periodic': 11964201, 'max': 8, 'sym': [18, 32, 48]},
    'shri': {'cycles': {1: 1, 3: 4109384, 4: 6}, 'periodic': 12328177, 'max': 9, 'sym': [6]},
}

def run(args, cwd=None):
    return subprocess.run(args, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout

def parse_class(text):
    return {(int(x[1]), int(x[2])): int(x[3]) for l in text.splitlines() if (x := l.split()) and x[0] == 'CLASS'}

with tempfile.TemporaryDirectory() as scratch:
    td = Path(scratch)
    for stem in ('exhaustive_graphs', 'independent_orbits', 'cycle_reps'):
        run(['c++', '-std=c++17', '-O3', '-o', str(td / stem), str(ROOT / (stem + '.cpp'))])
    for name, record in EXPECTED.items():
        outputs = {}
        for stem, suffix in [('exhaustive_graphs','A'), ('independent_orbits','B'), ('cycle_reps','reps')]:
            outputs[suffix] = run([str(td / stem), name])
            assert outputs[suffix] == (ROOT / f'{name}_{suffix}.txt').read_text()
        classes = parse_class(outputs['A'])
        assert classes == parse_class(outputs['B']) == parse_class(outputs['reps'])
        assert sum(classes.values()) == 3**16
        assert max(t for t,p in classes) == record['max']
        assert sum(n for (t,p),n in classes.items() if t==0) == record['periodic']
        for period, count in record['cycles'].items():
            assert classes.get((0,period),0) == period*count
        assert set(p for t,p in classes) == set(record['cycles'])
        assert sum(l.startswith('REP4 ') for l in outputs['reps'].splitlines()) == record['cycles'][4]
        print(name, 'complete states', sum(classes.values()), 'periodic', record['periodic'], 'cycles', record['cycles'])
        (td / f'{name}_reps.txt').write_text(outputs['reps'])
    # Symmetry calculation is independently encoded in modular-coordinate and graph automorphism permutations.
    symmetry_output = run([sys.executable, str(ROOT / 'analyze_symmetries.py')], cwd=td)
    for name in EXPECTED:
        assert (td / f'{name}_symmetry.txt').read_bytes() == (ROOT / f'{name}_symmetry.txt').read_bytes()
    assert '[(3320, 6, 32)]' in symmetry_output
    assert '[(41, 32, 36), (44, 48, 24), (3608, 18, 64)]' in symmetry_output
    expected_census = []
    for name in ('shri','rook'):
        classes = parse_class((ROOT / f'{name}_A.txt').read_text())
        expected_census.extend((name,str(t),str(p),str(n)) for (t,p),n in sorted(classes.items()))
    with (ROOT/'temporal_census.csv').open(newline='') as stream:
        records = list(csv.reader(stream))
    assert records[0] == ['graph','first_periodic_entry_time','primitive_period','labelled_initial_configurations']
    assert [tuple(row) for row in records[1:]] == expected_census
    print('4-cycle automorphism classes confirmed:', symmetry_output.strip().replace('\n','; '))
    check=run([sys.executable, str(ROOT / 'check_graph_invariants.py')], cwd=ROOT)
    assert check == (ROOT / 'graph_invariants_output.txt').read_text()
    assert 'GRAPH_INVARIANTS_OK' in check
    print('VERIFICATION_OK')
