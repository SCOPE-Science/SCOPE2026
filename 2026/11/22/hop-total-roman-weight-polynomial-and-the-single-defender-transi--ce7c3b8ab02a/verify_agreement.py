#!/usr/bin/env python3
"""Cross-check the exact polynomial and direct graph-distance enumeration."""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
from verify_formula import poly

ROOT = Path(__file__).resolve().parent
CASES = [(2,2),(2,3),(3,3),(2,2,2),(3,4),(2,3,3),(4,4),(2,2,3,3),(3,3,3),(4,4,4)]


def parse(line):
    sizes, terms = line.strip().split(' ', 1)
    shape = tuple(map(int, sizes.split(',')))
    counts = {}
    for pair in terms.split():
        k, v = pair.split(':')
        counts[int(k)] = int(v)
    return shape, counts


def main():
    golden = dict(parse(line) for line in (ROOT/'direct_counts.txt').read_text().splitlines())
    assert set(golden) == set(CASES)
    with TemporaryDirectory() as d:
        exe = Path(d)/'direct_enumerator'
        subprocess.run(['g++','-O3','-std=c++17','-Wall','-Wextra',
                        str(ROOT/'verify_bruteforce.cpp'),'-o',str(exe)],check=True)
        checked = 0
        total_labelings = 0
        for shape in CASES:
            raw = subprocess.check_output([str(exe),*map(str,shape)],text=True,timeout=40)
            shape2, actual = parse(raw)
            symbolic = poly(shape)
            assert shape2 == shape
            assert actual == symbolic == golden[shape], (shape,actual,symbolic,golden[shape])
            w = min(actual)
            r2 = sum(x == 2 for x in shape)
            r3 = sum(x == 3 for x in shape)
            expected = 2*r2 if r2 else 3*r3 + sum(shape[i]*shape[j] for i in range(len(shape)) for j in range(i+1,len(shape)))
            assert w == (4 if r2 else 5) and actual[w] == expected
            assert set(actual) == set(range(w,2*(1+sum(shape))+1))
            checked += 1
            total_labelings += 3**(1+sum(shape))
            print('shape', shape, 'minimum',w,'minima',actual[w],'total',sum(actual.values()),'coefficients',len(actual),'OK')
    print('DIRECT_AND_FORMULA_AGREE', 'cases='+str(checked),'labelings='+str(total_labelings))

if __name__=='__main__':
    main()
