"""Reproduce the exact finite functional-graph census with C++17 and Python 3."""
from pathlib import Path
import csv
import itertools
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
# Verify that the two independent line labellings present the same Fano plane.
cyclic = {frozenset((j, (j + 1) % 7, (j + 3) % 7)) for j in range(7)}
explicit = {frozenset(line) for line in [
    (0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5),
    (1, 4, 6), (2, 3, 6), (2, 4, 5)]}
assert any({frozenset(perm[i] for i in line) for line in cyclic} == explicit
           for perm in itertools.permutations(range(7)))
EXPECTED = HERE / 'census.csv'
with EXPECTED.open(newline='',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = [(int(r['entry_time']),int(r['least_period']),int(r['configurations'])) for r in reader]
assert len(rows)==55 and len(set((a,b) for a,b,c in rows))==55
assert sum(c for a,b,c in rows)==3**14
assert max(a for a,b,c in rows)==10
assert {b for a,b,c in rows}=={1,3,4,5,6,8,10,14}
with tempfile.TemporaryDirectory() as tmp:
    for src, expected_out in [('census_indegree.cpp','census_indegree.out'), ('census_paths.cpp','census_paths.out')]:
        exe=Path(tmp) / src.replace('.cpp','')
        subprocess.run(['g++','-std=c++17','-O3','-Wall','-Wextra','-Werror',str(HERE/src),'-o',str(exe)],check=True)
        result=subprocess.run([str(exe)],check=True,capture_output=True,text=True).stdout
        assert result==(HERE/expected_out).read_text(encoding='utf-8'), src+' captured output mismatch'
        if src=='census_indegree.cpp':
            parsed=[tuple(map(int,m)) for m in re.findall(r'T=(\d+) P=(\d+) count=(\d+)',result)]
        else:
            parsed=[tuple(map(int,m)) for m in re.findall(r'^(\d+),(\d+),(\d+)$',result,re.M)]
        assert parsed==rows,src+' census does not match table'
    before=(HERE/'witnesses.json').read_bytes()
    check=subprocess.run(['python3',str(HERE/'witness_check.py')],check=True,capture_output=True,text=True).stdout
    assert check==(HERE/'witness_check.out').read_text(encoding='utf-8')
    assert (HERE/'witnesses.json').read_bytes()==before
print('REPLAY_PASS 4782969 states, 55 entrance classes, 8 periods, maximum entry 10')
