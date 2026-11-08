#!/usr/bin/env python3
"""Replay and cross-check the complete finite-state census and symmetry classification."""
import pathlib
import subprocess
import tempfile
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
DATA = ROOT / 'data'

def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=True, timeout=180)
    return result.stdout, result.stderr

def records(text):
    result={}
    for row in text.splitlines():
        a=row.split()
        if a[0] in ('P','J'):
            result[tuple(a[:-1])] = int(a[-1])
    return result

with tempfile.TemporaryDirectory() as td:
    wd=pathlib.Path(td)
    for name in ('census','forward_verify','symmetry'):
        run(['g++', '-std=c++17', '-O3', '-Wall', '-Wextra', str(SRC / (name+'.cpp')), '-o', str(wd/name)],wd)
    _, cstderr=run([str(wd/'census')],wd)
    fout,_=run([str(wd/'forward_verify')],wd)
    sout,_=run([str(wd/'symmetry')],wd)
    raw=(wd/'raw_census.txt').read_text()
    frwd=(wd/'forward_census.txt').read_text()
    assert records(raw)==records(frwd)
    assert raw==(DATA/'raw_census.txt').read_text()
    assert frwd==(DATA/'forward_census.txt').read_text()
    assert (wd/'representatives.txt').read_text()==(DATA/'representatives.txt').read_text()
    assert sout==(DATA/'symmetry_results.txt').read_text()
    assert 'aut_count 720' in sout and 'PERIOD 7 cycles 180 symmetry_classes 1' in sout
    assert 'PERIOD 4 cycles 90 symmetry_classes 2' in sout
    assert 'VERIFIED_ALL_STATES 14348907 maxT 10' in fout
    rr=records(raw)
    periods={int(k[1]):v for k,v in rr.items() if k[0]=='P'}
    assert periods=={1:1,3:1258232,4:90,7:180}
    joint={tuple(map(int,k[1:])):v for k,v in rr.items() if k[0]=='J'}
    assert sum(joint.values())==3**15
    assert sum(v for (t,p),v in joint.items() if t==10)==1440
    assert all(t<=10 for t,p in joint)
    assert all(p in periods for t,p in joint)
    print('PASS: full 14348907-state double census, 26 joint cells, complete 270-cycle symmetry verification')
    print('PASS: 1/3/4/7 primitive periods, max transient 10, S6 orbit sizes 45/45/180')
