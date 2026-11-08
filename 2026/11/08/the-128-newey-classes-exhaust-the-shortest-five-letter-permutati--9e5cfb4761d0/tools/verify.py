#!/usr/bin/env python3
"""Reproduce the finite census from its embedded C++ sources and data."""
from collections import Counter
from itertools import permutations
from pathlib import Path
import csv
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
expected = (root / 'data' / 'canonical_optima.txt').read_text(encoding='utf-8').splitlines()
assert len(expected) == len(set(expected)) == 128
assert expected == sorted(expected)

def canonical(s):
    names = {}
    return ''.join(names.setdefault(c, str(len(names))) for c in s)

with tempfile.TemporaryDirectory() as td:
    for source in ('enum_greedy', 'enum_subseq'):
        binary = Path(td) / source
        subprocess.run(['g++','-std=c++17','-O3',str(root / 'code' / (source+'.cpp')),'-o',str(binary)],check=True)
        for length, answer in ((18, []),(19, expected)):
            result=subprocess.run([str(binary),str(length)],capture_output=True,text=True,check=True)
            got=result.stdout.splitlines()
            assert got==answer,(source,length,len(got),len(answer))
        print(source + ': correct 18/19 exhaustive census')
    binary = Path(td) / 'subalphabet_minima'
    subprocess.run(['g++','-std=c++17','-O3',str(root/'code'/'subalphabet_minima.cpp'),'-o',str(binary)],check=True)
    result=subprocess.run([str(binary)],capture_output=True,text=True,check=True)
    assert result.stdout.splitlines() == [
        'q=1 length=1 normalized_complete=1',
        'q=2 length=2 normalized_complete=0',
        'q=2 length=3 normalized_complete=1',
        'q=3 length=6 normalized_complete=0',
        'q=3 length=7 normalized_complete=7',
        'q=4 length=11 normalized_complete=0',
        'q=4 length=12 normalized_complete=9',
    ]
    print('subalphabet_minima: correct small-alphabet cutoffs')

perms = [''.join(p) for p in permutations('01234')]
for s in expected:
    assert len(s)==19
    assert s.startswith('01234')
    assert s==canonical(s)
    assert all(a!=b for a,b in zip(s,s[1:]))
    assert sorted(Counter(s).values())==[3,3,4,4,5]
    for p in perms:
        j=0
        for x in s:
            if j!=5 and x==p[j]:j+=1
        assert j==5,(s,p)
with (root/'data'/'reversal_orbits.tsv').open(newline='',encoding='utf-8') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==72
seen=set()
fixed=0
for row in rows:
    a,b=row['representative'],row['paired_representative']
    assert a<=b and a in expected and b in expected
    assert canonical(a[::-1])==b and canonical(b[::-1])==a
    assert int(row['relabeling_orbit_size'])==(1 if a==b else 2)
    fixed+=(a==b)
    assert a not in seen and b not in seen
    seen|={a,b}
assert fixed==16 and seen==set(expected)
print('Python direct-permutation and reversal check: 128 canonical, 15360 labeled, 72 reversal orbits')
print('VERIFY_OK')
