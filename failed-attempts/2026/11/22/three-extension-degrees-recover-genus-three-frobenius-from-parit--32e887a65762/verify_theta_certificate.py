#!/usr/bin/env python3
"""Reproduce and verify 30 theta-spectrum rows using exact arithmetic only."""
import csv
import io
import pathlib
import subprocess
import tempfile
from collections import Counter
ROOT = pathlib.Path(__file__).resolve().parent

def fixed(cycles, n):
    return sum(int(x) for x in cycles if n % int(x) == 0)

def recompute():
    with tempfile.TemporaryDirectory() as d:
        exe = str(pathlib.Path(d) / 'theta_exact')
        subprocess.run(['g++','-std=c++17','-O2',str(ROOT/'verify_sp6_theta.cpp'),'-o',exe],check=True)
        p = subprocess.run([exe],capture_output=True,text=True,check=True,timeout=180)
    assert 'ORDER 1451520' in p.stderr, p.stderr
    assert 'SPECTRA 30' in p.stderr, p.stderr
    assert 'prefix=1 distinct=18 collisions=12' in p.stdout
    assert 'prefix=2 distinct=24 collisions=6' in p.stdout
    assert 'prefix=3 distinct=30 collisions=0' in p.stdout
    rows=[]
    for ln in p.stdout.splitlines():
        if not ln.startswith('SPEC,'):continue
        k, num, rec = ln.split(',',2)
        o_e,c = rec.rsplit(',',1)
        odd,even = o_e.split(';')
        co = [int(x) for x in odd.split(',')]
        ce = [int(x) for x in even.split(',')]
        assert sum(co)==28 and sum(ce)==36
        vals=[fixed(z,n) for n in (1,2,3) for z in (co,ce)]
        rows.append({'index':int(num),'odd_cycles':'.'.join(map(str,co)),
          'even_cycles':'.'.join(map(str,ce)),'group_elements':int(c),
          **dict(zip(('o1','e1','o2','e2','o3','e3'),vals))})
    assert len(rows)==30 and sum(r['group_elements'] for r in rows)==1451520
    # Independent ATLAS S6(2) centralizer orders, in displayed class order.
    centralizers=[1451520,23040,4608,1536,384,2160,648,108,384,192,192,128,32,30,144,144,72,48,36,36,12,7,16,16,9,10,24,24,12,15]
    assert Counter(r['group_elements'] for r in rows)==Counter(1451520//z for z in centralizers)
    assert len(set((r['o1'],r['e1']) for r in rows))==18
    assert len(set((r['o1'],r['e1'],r['o2'],r['e2']) for r in rows))==24
    assert len(set((r['o1'],r['e1'],r['o2'],r['e2'],r['o3'],r['e3']) for r in rows))==30
    assert len(set((r['odd_cycles'],r['even_cycles']) for r in rows))==30
    assert [r['index'] for r in rows]==list(range(1,31))
    return rows

def main():
    rows=recompute()
    with (ROOT/'theta_frobenius_30_spectra.csv').open(newline='',encoding='utf-8') as f:
        got=list(csv.DictReader(f))
    assert len(got)==len(rows)
    for a,b in zip(rows,got):
        assert {k:str(v) for k,v in a.items()}==b,(a,b)
    p=subprocess.run(['python3',str(ROOT/'verify_hyperelliptic_theta.py')],text=True,capture_output=True,check=True)
    assert 'PARTS 22' in p.stdout
    assert 'DEGREE 3 distinct 22 collisions []' in p.stdout
    assert '(7, 1) ((0, 1), (0, 1), (0, 1))' in p.stdout
    assert '(5, 3) ((0, 1), (0, 1), (3, 1))' in p.stdout
    print('VERIFIED_GROUP_1451520_CLASSES_30_PREFIX_18_24_30_SHARP_3')
if __name__=='__main__':main()
