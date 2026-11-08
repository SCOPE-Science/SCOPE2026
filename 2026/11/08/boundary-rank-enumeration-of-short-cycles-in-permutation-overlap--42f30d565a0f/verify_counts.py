#!/usr/bin/env python3
"""Replay the exact boundary-rank census and a separate direct-graph check."""
import csv
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent

def main():
    with (ROOT / 'three_cycle_census.csv').open(newline='', encoding='utf-8') as stream:
        expected = list(csv.DictReader(stream))
    assert [int(r['n']) for r in expected] == list(range(6, 25))
    with tempfile.TemporaryDirectory() as tmp:
        exe = pathlib.Path(tmp) / 'census'
        subprocess.run(['g++', '-std=c++17', '-O2', '-Wall', '-Wextra',
                        str(ROOT / 'count_three_cycles.cpp'), '-o', str(exe)], check=True)
        proc = subprocess.run([str(exe), '6', '24'], check=True,
                              capture_output=True, text=True)
    actual = []
    for line in proc.stdout.splitlines():
        columns = dict(chunk.split('=', 1) for chunk in line.split())
        actual.append({'n': columns['n'],
                       'candidate_vertices': columns['candidates'],
                       'rooted_closed_3_walks': columns['closed3'],
                       'directed_3_cycles': columns['directed3cycles']})
    assert actual == expected, 'Finite census disagrees with supplied integer table'
    for row in actual:
        w, c = int(row['rooted_closed_3_walks']), int(row['directed_3_cycles'])
        assert w - 2 == 3 * c
    print('BOUNDARY_RANK_CHECK_OK')
    independent = subprocess.run(['python3', str(ROOT / 'direct_graph_check.py')],
                                 capture_output=True, text=True, check=True)
    assert 'DIRECT_GRAPH_CHECK_OK' in independent.stdout
    assert 'n=6 closed3=170 directed3cycles=56' in independent.stdout
    assert 'n=8 closed3=296 directed3cycles=98' in independent.stdout
    print('DIRECT_GRAPH_CHECK_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
