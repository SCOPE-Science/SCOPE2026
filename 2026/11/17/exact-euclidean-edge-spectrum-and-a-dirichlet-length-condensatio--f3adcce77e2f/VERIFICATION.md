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

For exact computation, run `python3 LODAY_EDGE_CHECK.py` from the same directory as this report. It uses Python 3's standard library only and enumerates each right-rotation edge directly from the binary-tree coordinate embedding. The checked leaf counts are N=3,4,5,6,7,8, with respectively 1,5,21,84,330,1287 edges and normalized total lengths 1,7,38,187,874,3958. The program checks per-rotation two-coordinate differences, every joint (a,c) count, the Catalan-binomial formula, total count and length, and maximal length.

Observed terminal message: `LODAY_EDGE_SPECTRUM_PASS`.

The analytic proof, not a finite experiment, establishes the formulas in all dimensions and the microscopic and macroscopic weak limits. The central-binomial coefficient expansion is exact; the Dirichlet limit uses a boundary uniform-integrability estimate on lattice sums. The original Loday local edge-length formula and the pre-existing numerical sequence OEIS A000531 are acknowledged. Independent audit has not been performed.
