#!/usr/bin/env python3
"""Independent verifier for DCLS(10) emptiness census (lane-10).

Re-runs the normalized a-vector enumeration with an implementation
independent of run_enumeration.py (set-based, no bitmask), reloads
output/artifacts/dcls10_squares.csv, checks SHA256, and asserts the
transversal/mate stages are vacuously complete because F is empty.
Runs in <5 s.
"""
import csv
import hashlib
import itertools
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "dcls10_squares.csv")
EXPECTED_CSV_SHA256 = "b1d83639e7c4fcd57fb2865cd71b255b85f80d1ab8c9ae7f0736ae96727fa61e"

def is_dcls(a):
    # a: tuple length 10, a[0]==0; row-Latin <=> a perm; col-Latin <=> b perm
    if set(a) != set(range(10)):
        return False
    b = [(a[k] - k) % 10 for k in range(10)]
    return set(b) == set(range(10))

def main():
    t0 = time.time()
    # 1. CSV checksum + content check
    with open(CSV, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print(f"CSV sha256: {digest}")
    assert digest == EXPECTED_CSV_SHA256, f"checksum mismatch: {digest}"
    with open(CSV, newline="") as f:
        rows = list(csv.DictReader(f))
    print(f"CSV data rows: {len(rows)}")
    for r in rows:
        a = tuple(int(r[f"a{i}"]) for i in range(10))
        assert is_dcls(a), f"CSV row fails DCLS check: {a}"
    assert len(rows) == 0, "expected empty census"

    # 2. Independent full re-enumeration over 9! normalized a-vectors
    total = 0
    n_pass = 0
    for perm in itertools.permutations(range(1, 10)):
        total += 1
        a = (0,) + perm
        # independent set-based column check
        if set((a[k] - k) % 10 for k in range(10)) == set(range(10)):
            n_pass += 1
            print("UNEXPECTED PASS:", a)
    print(f"re-scan: total={total} passes={n_pass}")
    assert total == 362880, total
    assert n_pass == 0, n_pass

    # 3. Algebraic certificate (sum invariant)
    assert sum(range(10)) % 10 == 5
    # sum of b over any a-vectors is 0 mod 10, never 5 -> no b can be a permutation
    print("sum invariant: sum(perm)=45=5 mod10; sum(a-k)=0 mod10 -> contradiction OK")

    # 4. Transversal/mate stage vacuous
    print("F empty -> no tau/DLX decomposition inputs; transversal & mate census vacuously complete.")

    print(f"VERIFIED in {time.time()-t0:.2f}s")

if __name__ == "__main__":
    main()
