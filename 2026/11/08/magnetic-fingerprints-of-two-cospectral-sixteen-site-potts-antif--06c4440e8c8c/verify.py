"""Independently recompute every colour-sector minimum and multiplicity."""
from pathlib import Path
import subprocess
import tempfile

here = Path(__file__).resolve().parent
expected = (here / 'expected.tsv').read_bytes()
assert expected.count(b'rook\n') == 1 and expected.count(b'shrikhande\n') == 1
with tempfile.TemporaryDirectory() as folder:
    for source in ('verify_subsets.cpp', 'verify_recursive.cpp'):
        executable = Path(folder) / source.removesuffix('.cpp')
        subprocess.run(['g++', '-std=c++20', '-O3', '-Wall', '-Wextra',
                        str(here / source), '-o', str(executable)], check=True)
        output = subprocess.check_output([str(executable)], timeout=120)
        assert output == expected, f'{source} disagrees with exact sector table'
        print(f'{source}: complete independent census agrees')
print('Both exhaust all 3^16 labelled configurations per graph; all sectors verified.')

from fractions import Fraction
rows = {}
current = None
for line in expected.decode('ascii').splitlines():
    if line in ('rook', 'shrikhande'):
        current = line
        rows[current] = {}
    else:
        index, minimum, degeneracy = map(int, line.split())
        rows[current][index] = (minimum, degeneracy)
assert all(len(x) == 17 for x in rows.values())

checks = {
    'rook': ([0, 4, 8, 12, 16],
             [Fraction(-2), Fraction(0), Fraction(4), Fraction(6)],
             [46170, 90936, 11352, 1473],
             [90, 10800, 216, 384, 1]),
    'shrikhande': ([0, 4, 6, 8, 10, 12, 16],
                   [Fraction(-5, 2), Fraction(0), Fraction(1), Fraction(7, 2),
                    Fraction(9, 2), Fraction(6)],
                   [138, 288, 288, 352, 512, 1345],
                   [42, 96, 192, 96, 256, 256, 1]),
}
for graph, data in rows.items():
    hull = []
    for k in range(17):
        while len(hull) >= 2:
            i, j = hull[-2:]
            prev = Fraction(data[j][0] - data[i][0], j - i)
            new = Fraction(data[k][0] - data[j][0], k - j)
            if prev >= new:
                hull.pop()
            else:
                break
        hull.append(k)
    slopes = [Fraction(data[b][0] - data[a][0], b - a)
              for a, b in zip(hull, hull[1:])]
    critical_counts = []
    for x in slopes:
        floor = min(Fraction(m) - x*k for k, (m, _) in data.items())
        critical_counts.append(sum(c for k, (m,c) in data.items()
                                   if Fraction(m)-x*k == floor))
    interval_counts = [data[k][1] for k in hull]
    assert (hull, slopes, critical_counts, interval_counts) == checks[graph]
    print(f'{graph}: exact rational field hull and all degeneracies verified')

# A separate structural cross-check of the two explicit low-energy witnesses.
witnesses = {
    'rook': (('0112', '1012', '1120', '2201'), 8, (4, 7, 5)),
    'shrikhande': (('0102', '1212', '1020', '2211'), 6, (4, 6, 6)),
}
for graph, (matrix, expected_bonds, sizes) in witnesses.items():
    spins = [int(ch) for row in matrix for ch in row]
    assert tuple(spins.count(c) for c in range(3)) == sizes
    edges = 0
    bad = 0
    for u in range(16):
        x, y = divmod(u, 4)
        for v in range(u + 1, 16):
            a, b = divmod(v, 4)
            delta = ((a-x) % 4, (b-y) % 4)
            if graph == 'rook':
                adjacent = x == a or y == b
            else:
                adjacent = delta in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
            if adjacent:
                edges += 1
                bad += int(spins[u] == spins[v])
    assert edges == 48 and bad == expected_bonds
    print(f'{graph}: explicit structural ground-state witness has {bad} bad bonds')
