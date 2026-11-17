#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify.py
binary="$(mktemp)"
output="$(mktemp)"
trap 'rm -f "$binary" "$output"' EXIT
c++ -std=c++17 -O2 enumerate.cpp -o "$binary"
"$binary" > "$output"
python3 verify.py --cpp "$output"
