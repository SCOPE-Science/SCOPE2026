#!/bin/sh
set -eu
python3 verify_bitset.py
c++ -O2 -std=c++17 -Wall -Wextra verify_group.cpp -o ./verify_group
./verify_group
python3 verify_orbits.py
