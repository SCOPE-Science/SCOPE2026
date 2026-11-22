#!/bin/sh
set -eu
cd "$(dirname "$0")"
CXX=${CXX:-c++}
"$CXX" -std=c++17 -O2 -Wall -Wextra check_supports.cpp -o /tmp/hopkg3_verify_$$
trap 'rm -f /tmp/hopkg3_verify_$$' EXIT
/tmp/hopkg3_verify_$$
python3 check_formula.py
python3 check_constructions.py
