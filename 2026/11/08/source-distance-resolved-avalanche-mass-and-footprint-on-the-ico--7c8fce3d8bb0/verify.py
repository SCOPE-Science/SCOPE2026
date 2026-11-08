#!/usr/bin/env python3
"""Standalone repeatable proof-by-exhaustion for the stated finite icosahedral census.
Requires Python 3 and a C++17 compiler. No Python packages or input data beyond
AVALANCHE_COUNTS.csv and the two independently implemented C++ programs.
"""
import csv, pathlib, subprocess, tempfile, collections
BASE=pathlib.Path(__file__).resolve().parent
rows=list(csv.DictReader((BASE/'AVALANCHE_COUNTS.csv').open(encoding='utf-8')))
expected={int(d):{} for d in range(1,4)}
for r in rows:
 d,t,s,c=map(int,(r['source_distance'],r['total_topplings'],r['distinct_toppled_vertices'],r['recurrent_states']))
 assert (t,s) not in expected[d] and c>0
 expected[d][(t,s)]=c
assert sum(map(len,expected.values()))==100
for d in expected:
 assert sum(expected[d].values())==5184000
 assert expected[d][(0,0)]==[0,3283200,3462398,3492388][d]
 assert max(t for t,s in expected[d])==[0,11,28,29][d]
assert all(t==s for t,s in expected[1])
for t in range(1,12):
 assert expected[1][(t,t)]==expected[1][(12-t,12-t)]

def decode(text):
 lines=text.splitlines()
 assert lines[0]=='recurrent 5184000',lines[0]
 ret={}
 for d in range(1,4):
  tokens=lines[2*d].strip().split()
  ret[d]={tuple(map(int,key.split(','))):int(value) for key,value in (tok.split(':') for tok in tokens)}
 return ret
with tempfile.TemporaryDirectory(prefix='ico-aval-') as temp:
 for name in ('icosa_avalanche','verify_dhar'):
  src=BASE/(name+'.cpp'); exe=pathlib.Path(temp)/name
  subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',str(src),'-o',str(exe)],check=True,capture_output=True,text=True)
  run=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=180)
  assert decode(run.stdout)==expected, name
  print(name+': exact census matches all 100 CSV coefficients')
print('VERIFY_OK: 5^11 stable states, 5,184,000 recurrent; distance classes 1/2/3, full joint avalanche law')
