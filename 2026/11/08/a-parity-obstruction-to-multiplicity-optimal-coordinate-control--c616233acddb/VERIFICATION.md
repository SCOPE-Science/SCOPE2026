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

# Verification

The public checker `checker.py` uses Python 3 standard-library integer arithmetic only. Execute `python3 checker.py` alongside this document after extracting all files from the same finding package.

It checks the 44 exact weighted-subset-sum eigenspace labels, the 20 double fibers and their six difference masks, the odd XOR identity for the five selected masks, all 4096 pointwise Walsh-eigenvector Laplacian identities, all 2016 unordered two-vertex choices, and the full-rank three-site coordinate restriction. It additionally checks the exact finite instances with superincreasing extra directions in dimensions 7, 8 and 9.

The universal extrapolation for all finite dimensions is an algebraic highest-differing-coordinate separation argument in the proof, not an experimental assertion. The script checks neither literature novelty nor control energy, numerical robustness, or an independent mathematical audit. Those omissions do not alter the exact statement's narrowly specified scope.
