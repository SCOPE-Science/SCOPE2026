#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 checker.py
c++ -O3 -std=c++17 -o /tmp/phylo_dlx_verify_$$ dlx.cpp
c++ -O3 -std=c++17 -o /tmp/phylo_branch_verify_$$ branch.cpp
trap 'rm -f /tmp/phylo_dlx_verify_$$ /tmp/phylo_branch_verify_$$' EXIT HUP INT TERM
/tmp/phylo_dlx_verify_$$ < incidence7.txt > dlx_check.txt 2>&1
/tmp/phylo_branch_verify_$$ < incidence7.txt > branch_check.txt 2>&1
grep -q 'NO FOUND after calls=2561709' dlx_check.txt
grep -q 'UNSAT nodes=2561709' branch_check.txt
rm -f dlx_check.txt branch_check.txt
echo 'VERIFY_OK'
