#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify.py
build_dir="$(mktemp -d)"
trap 'rm -rf "$build_dir"' EXIT
g++ -std=c++17 -O2 -Wall -Wextra crosscheck.cpp -o "$build_dir/crosscheck"
"$build_dir/crosscheck"
