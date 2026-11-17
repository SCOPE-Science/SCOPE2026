#!/bin/sh
set -eu
TMPDIR_CHECK=$(mktemp -d)
trap 'rm -rf "$TMPDIR_CHECK"' EXIT HUP INT TERM
c++ -std=c++17 -O3 checks/verify_direct.cpp -o "$TMPDIR_CHECK/direct"
"$TMPDIR_CHECK/direct" > "$TMPDIR_CHECK/direct.out"
diff -u checks/direct.out "$TMPDIR_CHECK/direct.out"
c++ -std=c++17 -O3 checks/verify_transfer.cpp -o "$TMPDIR_CHECK/transfer"
"$TMPDIR_CHECK/transfer" > "$TMPDIR_CHECK/transfer.out"
diff -u checks/transfer.out "$TMPDIR_CHECK/transfer.out"
python3 checks/verify_formula.py > "$TMPDIR_CHECK/formula.out"
diff -u checks/formula.out "$TMPDIR_CHECK/formula.out"
python3 - "$TMPDIR_CHECK/direct.out" "$TMPDIR_CHECK/formula.out" <<'PY'
import sys
A=open(sys.argv[1],encoding='utf-8').read().splitlines()
B=open(sys.argv[2],encoding='utf-8').read().splitlines()
for n in (2,3):
    aa=next(i for i,line in enumerate(A) if line.startswith(f'n={n} '))
    bb=next(i for i,line in enumerate(B) if line.startswith(f'n={n} '))
    ae=next((i for i in range(aa+1,len(A)) if A[i].startswith('n=')),len(A))
    be=next((i for i in range(bb+1,len(B)) if B[i].startswith('n=')),len(B))
    assert A[aa+1:ae]==B[bb+1:be],f'weighted mismatch for n={n}'
print('Independent direct and exact-polynomial histograms agree at n=2,3')
PY
python3 - "$TMPDIR_CHECK/transfer.out" "$TMPDIR_CHECK/formula.out" <<'PY'
import sys
A=open(sys.argv[1],encoding='utf-8').read().splitlines()
B=open(sys.argv[2],encoding='utf-8').read().splitlines()
aa=next(i for i,line in enumerate(A) if line.startswith('n=4 fixed='))
bb=next(i for i,line in enumerate(B) if line.startswith('n=4 total='))
ae=next((i for i in range(aa+1,len(A)) if A[i].startswith('n=')),len(A))
be=next((i for i in range(bb+1,len(B)) if B[i].startswith('n=')),len(B))
assert A[aa+1:ae]==B[bb+1:be],'transfer/formula weighted discrepancy for n=4'
print('Independent local transfer and polynomial histograms agree at n=4')
PY
echo 'All checks passed'
