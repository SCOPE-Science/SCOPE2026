#!/usr/bin/env python3
"""Rebuild and cross-check two exhaustive five-prism swapping enumerators."""
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
HISTOGRAM = [1, 15, 135, 895, 4734, 20606, 73914, 213600, 478259,
             789069, 908113, 691531, 332274, 96706, 16840, 1974, 130, 4]
ANTIPODES = {'7895623401', '7895634012', '8956723401', '8956734012'}


def check_source(source, destination):
    subprocess.run(['g++', '-std=c++17', '-O3', str(HERE / source), '-o', str(destination)],
                   check=True)
    return subprocess.run([str(destination)], capture_output=True, text=True,
                          check=True, timeout=180).stdout


def check_factoradic(output):
    head = re.search(r'reached=(\d+) edges=(\d+) diameter=(\d+) shell=([\d,]+)', output)
    assert head, 'Missing factorial-encoding header'
    n, edges, diam = map(int, head.group(1, 2, 3))
    hist = list(map(int, head.group(4).split(',')))
    assert (n, edges, diam, hist) == (3628800, 15, 17, HISTOGRAM)
    summary = re.search(r'antipodes=(\d+) maxgap=(\d+) gapmaxcount=(\d+)', output)
    assert summary and tuple(map(int, summary.groups())) == (4, 4, 1440)
    far = set(re.findall(r'^ANT \d+ (\d{10})$', output, flags=re.M))
    assert far == ANTIPODES, (far, ANTIPODES)
    return hist, far


def check_packed(output):
    head = re.search(r'num=(\d+) diameter=(\d+) antipodes=(\d+) maxgap=(\d+) gapcount=(\d+)', output)
    assert head and tuple(map(int, head.groups())) == (3628800, 17, 4, 4, 1440)
    hist = list(map(int, output.splitlines()[1].split(',')))
    assert hist == HISTOGRAM
    far = set(re.findall(r'^FAR (\d{10})$', output, flags=re.M))
    assert far == ANTIPODES
    return hist, far


def check_witness():
    state = list(range(10))
    ring_moves = [(0, 1), (1, 2), (2, 3), (4, 0), (0, 1), (1, 2)]
    moves = [(i, i + 5) for i in range(5)] + ring_moves + [
        (a + 5, b + 5) for a, b in ring_moves]
    assert len(moves) == 17
    for a, b in moves:
        state[a], state[b] = state[b], state[a]
    assert ''.join(map(str, state)) == '7895623401'


def main():
    with tempfile.TemporaryDirectory() as t:
        first = check_factoradic(check_source('enum_factoradic.cpp', Path(t) / 'a'))
        second = check_packed(check_source('enum_packed.cpp', Path(t) / 'b'))
        assert first == second
        assert sum(first[0]) == 3628800
        check_witness()
    print('VERIFY_OK: 3628800 states; diameter 17; four listed antipodes; max transportation deficit 4, 1440 states; identical distance histograms; 17-swap witness')


if __name__ == '__main__':
    main()
