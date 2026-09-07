#!/bin/bash
# Single-command replay for D(C3xC3xC6)=10. Stdlib-only + gcc. Runs in <2 min on one core.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "== [1/3] witness + group + small-depth brute checks (Python stdlib) =="
python3 "$DIR/verify.py"
echo "== [2/3] compile enumerator (gcc -O2) =="
gcc -O2 -o "$DIR/enumerate" "$DIR/enumerate.c"
echo "== [3/3] exhaustive sorted-multiset search for length-10 zero-sum-free =="
"$DIR/enumerate" 600 | tee "$DIR/enum_log.txt"
echo "== replay complete: depth-10 count must be 0 with COMPLETE =="
grep -q "depth 10: 0" "$DIR/enum_log.txt" && grep -q "COMPLETE" "$DIR/enum_log.txt" && echo "REPLAY PASS: D<=10 certified; with witness D>=10 => D=10"
