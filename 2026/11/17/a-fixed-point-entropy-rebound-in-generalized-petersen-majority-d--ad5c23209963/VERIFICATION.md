---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The definition of \(GP(n,k)\), synchronous binary strict majority and labelled fixed-state count is in `RESULT.md`. `check_transfer.py` constructs shift-window digraphs for steps 1, 2 and 3, takes cyclic strongly connected components, computes exact symbolic characteristic polynomials, verifies both degree-32 and degree-33 factor coefficient arrays, and certifies spectral intervals using strict rational Collatz–Wielandt bounds. It also generates complete small-circumference counts from Newton power sums. Dependencies are pinned in `requirements.txt`.

Run `python check_transfer.py` and compare exactly with `transfer_output.txt`. Compile the separate direct simulator with `g++ -O3 -std=c++17 direct_check.cpp -o direct_check` and run `./direct_check`; compare with `direct_output.txt`. The latter checks all binary colorings of each \(GP(n,k)\) for \(7\le n\le11\), and uses direct original-state majority update, not the transfer graph. Both recorded outputs were reproduced from these current sources.

The symbolic directed-graph construction and its exact characteristic polynomials establish the infinite-family enumeration; the independent finite brute-force check is supporting cross-validation only. The strict asymptotic inequalities rely on positive integer matrix-vector witnesses, not floating-point root estimation. No claim concerns all temporal two-cycles, transient basins, or graph symmetries. A separate external mathematical audit has not been performed.
