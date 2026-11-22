#!/bin/sh
set -eu
cxx=${CXX:-g++}
"$cxx" -std=c++17 -O3 exhaustive.cpp -o exhaustive
"$cxx" -std=c++17 -O3 weighted.cpp -o weighted
./exhaustive > exhaustive.out
./weighted > weighted.out
python3 invariants.py > invariants.out
python3 symmetry.py > symmetry.out
python3 - <<'PY'
import re
from pathlib import Path
ex=Path('exhaustive.out').read_text().splitlines()
w=Path('weighted.out').read_text().splitlines()
assert ex[0]=='Rook' and ex[6]=='Shrikhande'
counts={}
for ix,name in [(1,'Rook'),(7,'Shrikhande')]:
    hist={int(a):int(b) for a,b,c in (line.split(',') for line in ex[ix:ix+5 if ix==1 else len(ex)])}
    counts[name]=hist
for i,name in [(1,'Rook'),(3,'Shrikhande')]:
    got={int(a):int(b) for a,b in re.findall(r'(\d+):(\d+)',w[i])}
    assert counts[name]==got, (name,counts[name],got)
assert counts['Rook']=={0:1,1:65535,2:10600327,3:30077258,4:2303600}
assert counts['Shrikhande']=={0:1,1:65535,2:10643847,3:30230026,4:2106224,5:1088}
assert sum(counts['Rook'].values())==3**16
assert sum(counts['Shrikhande'].values())==3**16
assert 'INVARIANTS_OK' in Path('invariants.out').read_text()
assert 'SYMMETRY_OK' in Path('symmetry.out').read_text()
print('VERIFICATION_OK')
PY
