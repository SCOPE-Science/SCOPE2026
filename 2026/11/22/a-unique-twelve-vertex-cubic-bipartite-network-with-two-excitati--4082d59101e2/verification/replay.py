#!/usr/bin/env python3
"""Recompute the finite graph catalog and both exact functional-graph tables."""
import hashlib
import pathlib
import re
import subprocess
import tempfile
ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED_CODES = ['EFz_', 'G?zTb_', 'I?BeeOwM?', 'I?BedPWM?',
 'K??FFBOJ?wB_', 'K??FEbGL@WB_', 'K??FEagT@WB_', 'K??FEQoT@WB_', 'K??EUIo[@WB_']

def run(*cmd):
    return subprocess.check_output([str(x) for x in cmd], cwd=ROOT)

def equal_output(name, data):
    expected = (ROOT/name).read_bytes()
    if data != expected:
        raise AssertionError(name + ' differs from packaged expected output')
    print(name, 'OK', len(data), 'bytes', hashlib.sha256(data).hexdigest())

enum = run('python3', 'enumerate_bip.py')
equal_output('enumerate_bip.out', enum)
lines = [l.strip() for l in enum.decode('ascii').splitlines() if l.startswith('  ')]
assert lines == EXPECTED_CODES, (lines,EXPECTED_CODES)
assert 'order 12 connected sorted matrices 540 nonisomorphic 5' in enum.decode()
# Confirm that the independent row-mask graphs have the asserted graph6 encodings.
from enumerate_bip import graph6
cpp = (ROOT/'verify_paths.cpp').read_text()
rows_literal = cpp.split('const int rows[9][6]={', 1)[1].split('};', 1)[0]
rows_list = [tuple(int(v) for v in re.findall(r'\d+', entry)) for entry in re.findall(r'\{([^}]*)\}', rows_literal)]
order_list = [3,4,5,5,6,6,6,6,6]
assert len(rows_list) == 9
assert [graph6(row[:m],m) for row,m in zip(rows_list, order_list)] == EXPECTED_CODES
with tempfile.TemporaryDirectory() as tmp:
    outputs = []
    for source in ['verify_peel.cpp','verify_paths.cpp']:
        exe = pathlib.Path(tmp) / source.replace('.cpp','')
        run('g++','-std=c++17','-O2','-Wall','-Wextra','-pedantic',source,'-o',exe)
        got = run(exe)
        equal_output(source.replace('.cpp','.out'),got)
        outputs.append(got)
    assert outputs[0] == outputs[1], 'two independent algorithms disagree'
    text = outputs[0].decode()
    rows = text.strip().splitlines()
    assert len(rows) == 9
    special = next(line for line in rows if 'code=K??FEQoT@WB_' in line)
    assert '8/4=1208' in special and '10/5=4784' in special
    assert sum('8/4=' in line and '10/5=' in line for line in rows)==1
witness = run('python3','witness.py')
equal_output('witness.out',witness)
assert '11002' in witness.decode() and '2939' in witness.decode()
print('PASS: all 9 isomorphism classes, 2 exact functional-graph classifiers, and both witnesses')
