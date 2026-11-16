#!/bin/sh
set -eu
cd "$(dirname "$0")"
build_dir="$(mktemp -d)"
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
for src in cograph_fourier cograph_recursive cograph_mod32; do
    g++ -std=c++17 -O2 "$src.cpp" -o "$build_dir/$src"
done
for n in 4 5 6 7; do
    "$build_dir/cograph_fourier" "$n"
    "$build_dir/cograph_recursive" "$n"
done
"$build_dir/cograph_mod32"
