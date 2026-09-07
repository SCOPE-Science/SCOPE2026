#!/bin/bash
# Deterministic rerun: enumeration -> torsion/square-cube -> bounded search (B=1e6, ~40s) -> tables -> Lutz -> verify
set -e
cd "$(dirname "$0")"
echo "== enumerate =="
python3 enumerate.py
echo "== torsion square/cube =="
python3 torsion_check.py
echo "== bounded search B=1e6 =="
python3 search_bounded.py
echo "== tables =="
python3 build_tables.py
echo "== lutz cross-check =="
python3 lutz_check.py
echo "== verify =="
python3 verify.py
