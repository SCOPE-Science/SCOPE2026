#!/bin/sh
# Rebuild and compare the two finite, exhaustive majority-dynamics enumerations.
set -eu
cd "$(dirname "$0")"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
python3 check_majority_python.py > "$tmp/py.jsonl"
c++ -std=c++17 -O2 verify_paley_census.cpp -o "$tmp/verify"
"$tmp/verify" > "$tmp/cpp.txt"
python3 compare_census.py "$tmp/py.jsonl" "$tmp/cpp.txt"
diff -u census_python.jsonl "$tmp/py.jsonl"
diff -u census_cpp.txt "$tmp/cpp.txt"
