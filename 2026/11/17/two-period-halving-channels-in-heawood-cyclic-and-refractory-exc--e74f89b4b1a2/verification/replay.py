#!/usr/bin/env python3
"""Recompile and compare two exhaustive classifiers; independently check witnesses."""
import pathlib
import subprocess
import tempfile
import re
import itertools

ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED = {
    (1,1):240039, (3,3):705474, (4,4):507024,
    (5,5):105084, (6,6):1283436, (8,4):275520,
    (8,8):448224, (10,5):237216, (10,10):626136,
    (14,14):354816,
}

def parse_indegree(out):
    split = out.split('JOINT\n', 1)[1].split('CCA classes\n', 1)[0]
    return {(int(a), int(b)):int(c) for a,b,c in re.findall(r'(?m)^(\d+) (\d+) (\d+)$',split)}

def parse_paths(out):
    return {(int(a), int(b)):int(c) for a,b,c in re.findall(r'(?m)^pair (\d+):(\d+) = (\d+)$',out)}

def independent_witness(code, mode):
    # Third incidence representation: each line i contains points i, i+1, i+3 mod 7.
    lines = [[i,(i+1)%7,(i+3)%7] for i in range(7)]
    # Reindex a state encoded using the dot-product Fano presentation.
    dot_lines=[{p-1 for p in range(1,8) if ((p & normal).bit_count() % 2)==0} for normal in range(1,8)]
    cyclic_sets=[set(t) for t in lines]
    isos=[]
    for perm in itertools.permutations(range(7)):
        mapped=[{perm[p] for p in line} for line in dot_lines]
        if all(s in cyclic_sets for s in mapped):
            isos.append((perm,[cyclic_sets.index(s) for s in mapped]));break
    assert isos, 'Fano presentations not isomorphic'
    pm,lm=isos[0]
    from_digits=[(code // (3**i))%3 for i in range(14)]
    to_digits=[0]*14
    for p in range(7):to_digits[pm[p]]=from_digits[p]
    for j in range(7):to_digits[7+lm[j]]=from_digits[7+j]
    code=sum(c*(3**i) for i,c in enumerate(to_digits))
    adj = [[] for _ in range(14)]
    for i, pts in enumerate(lines):
        for p in pts:
            adj[p].append(7+i);adj[7+i].append(p)
    assert all(len(v)==3 for v in adj)
    seen = {}
    depth=0
    state = code
    while state not in seen:
        seen[state]=depth
        digits=[];temp=state
        for _ in range(14):digits.append(temp%3);temp//=3
        nxt=[]
        for v,c in enumerate(digits):
            if mode=='CCA':
                target=(c+1)%3
                nxt.append(target if any(digits[w]==target for w in adj[v]) else c)
            else:
                nxt.append(2 if c==1 else 0 if c==2 else 1 if any(digits[w]==1 for w in adj[v]) else 0)
        state=sum(c*(3**v) for v,c in enumerate(nxt))
        depth+=1
        assert depth < 1000
    return seen[state], depth-seen[state]

# Validate the explicit seven-line Fano presentation used by the first program.
from itertools import combinations
triples=[[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]]
pairs=[tuple(sorted(pair)) for line in triples for pair in combinations(line,2)]
assert len(pairs)==len(set(pairs))==21

with tempfile.TemporaryDirectory() as d:
    outputs=[]
    for stem in ['census_indegree', 'census_paths']:
        exe=pathlib.Path(d)/stem
        subprocess.run(['g++','-std=c++17','-O2',str(ROOT/(stem+'.cpp')),'-o',str(exe)],check=True)
        out=subprocess.run([str(exe)],check=True,capture_output=True,text=True).stdout
        assert out == (ROOT/(stem+'.out')).read_text(encoding='utf-8'), stem+' saved output mismatch'
        outputs.append(out)
    assert parse_indegree(outputs[0])==parse_paths(outputs[1])==EXPECTED
    assert sum(EXPECTED.values())==3**14
    ghm_periodic = {int(p):int(c) for p,c in re.findall(r'(?m)^(\d+):0 (\d+)$',outputs[0].split('GHM classes\n',1)[1].split('Discrepancy shells\n',1)[0])}
    assert {p:ghm_periodic[p]//p for p in ghm_periodic} == {1:1,3:5334,4:224,5:84,6:42,8:168,10:84,14:96}
    assert sum(v for (a,b),v in EXPECTED.items() if a!=b)==512736
    assert independent_witness(10976,'CCA')==(2,8)
    assert independent_witness(10976,'GHM')==(4,4)
    assert independent_witness(8885,'CCA')==(0,10)
    assert independent_witness(8885,'GHM')==(2,5)
    print('PASS two exhaustive finite-state methods: 4782969 states, 10 joint period classes')
    print('PASS discrepancy 512736 = 275520 (8 to 4) + 237216 (10 to 5)')
    print('PASS published GHM-only orbit marginal: 8 primitive-period classes')
    print('PASS two direct-trajectory witnesses with independent incidence presentation')
