#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify_bitset.py
BIN="$(mktemp)"
trap 'rm -f "$BIN"' EXIT HUP INT TERM
c++ -std=c++17 -O2 -Wall -Wextra verify_independent.cpp -o "$BIN"
"$BIN"
