#!/bin/sh
set -eu
cd "$(dirname "$0")"
g++ -O3 -std=c++17 checker_rgs.cpp -o checker_rgs.bin
g++ -O3 -std=c++17 checker_subsets.cpp -o checker_subsets.bin
./checker_rgs.bin 0 > rgs_cubo.txt
./checker_rgs.bin 1 > rgs_trunc.txt
./checker_subsets.bin 0 > opt_cubo.txt
./checker_subsets.bin 1 > opt_trunc.txt
python3 orbits.py > orbit_summary.txt
grep -q 'graph=cuboctahedron n=12 partitions=4213597' rgs_cubo.txt
grep -q 'graph=truncated_tetrahedron n=12 partitions=4213597' rgs_trunc.txt
grep -q 'k=8 count=762' rgs_cubo.txt
grep -q 'k=8 count=93' rgs_trunc.txt
grep -q 'counts=2:24 3:10128 4:194733 5:582874 6:378855 7:47900 8:762' opt_cubo.txt
grep -q 'counts=2:171 3:24846 4:258625 5:441384 6:153715 7:7422 8:93' opt_trunc.txt
grep -q 'mode 0 automorphisms 48 orbits 23' orbit_summary.txt
grep -q 'mode 1 automorphisms 24 orbits 7' orbit_summary.txt
echo COALITION_PAIR_VERIFY_OK
