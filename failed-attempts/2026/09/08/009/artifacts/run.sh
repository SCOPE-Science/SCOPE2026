#!/bin/sh
# Lane-70 replay: integral homology census of flag 2-skeleta on 7 vertices.
# Requirements: python3 + sympy + networkx (any recent versions).
# Reproduces census.csv (1044 rows), distribution, RP2 witness, collapse logs in seconds.
set -e
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$SCRIPT_DIR"
python3 census.py
