#!/bin/bash
# Deterministic replay: triple census to n<=9. Stdlib only.
# Usage: bash replay.sh [--nmax 9] [--workers N]
set -e
cd "$(dirname "$0")"
NMAX=9
WORKERS=32
if [ "$1" = "--nmax" ]; then NMAX="$2"; shift 2; fi
if [ "$1" = "--workers" ]; then WORKERS="$2"; shift 2; fi
if command -v nproc >/dev/null 2>&1; then
  NCPU=$(nproc)
  if [ "$NCPU" -lt "$WORKERS" ]; then WORKERS="$NCPU"; fi
fi
echo "replay: nmax=$NMAX workers=$WORKERS seed=55"
python3 census_all.py --nmax "$NMAX" --workers "$WORKERS"
echo "--- counts.csv sha256 ---"
sha256sum counts.csv
echo "--- target check ---"
python3 -c "
import csv
rows=list(csv.DictReader(open('counts.csv')))
cols=[c for c in rows[0].keys() if c.startswith('a')]
ns=sorted(int(c[1:]) for c in cols)
def vec(p,q):
    for r in rows:
        if (r['rep_p'],r['rep_q'])== (p,q): return [int(r[f'a{n}']) for n in ns]
print('1342_2143:',vec('1342','2143'))
print('1432_2413 (=canon of 3142_2341):',vec('1432','2413'))
assert vec('1342','2143')==vec('1432','2413'), 'target mismatch'
print(f'TARGET EQUINUMEROSITY to n={ns[-1]}: OK')
print('1243_2134:',vec('1243','2134'))
print('1342_3124:',vec('1342','3124'))
assert vec('1243','2134')==vec('1342','3124'), 'Le second mismatch'
print(f'LE SECOND EQUINUMEROSITY to n={ns[-1]}: OK')
"
echo "replay OK"
