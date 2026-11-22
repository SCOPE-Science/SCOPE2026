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

# Reproduction and verification

The proof is analytic and applies for every integer \(n\ge4\) and \(2\le k\le n-2\). In `verify_two_erasure.py`, vertices of \(P_{n,k}\) are generated directly as zero-one incidence vectors. The actual retained-vertex hull is constructed and its intrinsic normalized volume computed via SciPy's convex-hull routine; the results are compared with the closed formula for every possible overlap size and rank through \(n=8\). Explicit orthogonal-foot coordinates and both forbidden-hyperplane constraints are independently checked. SymPy computes **exact integer determinants** of 28 proposed cap-overlap simplices through \(n=10\), verifying unimodularity in the finite sample.

To reproduce, run `python verify_two_erasure.py` with Python 3, NumPy, SciPy and SymPy. The completed run reported `PASS: 37 rank/intersection profiles; volume and Euclidean nearest-foot identities; 28 exact unimodular determinant tests` (plus progress messages). The exact determinant checks are finite, not an infinite proof; the unimodular variable-change proof and all-parameter hyperplane argument are in `RESULT.md`.

Caution: direct floating-point hull volumes have numerical tolerance; no numerical result is treated as proof for arbitrary dimensions. The original papers are cited for the already-known hypersimplex volume identity, sparse-paving cases, general alcoved triangulations, and the motivating extremal configuration. Independent audit remains unperformed.
