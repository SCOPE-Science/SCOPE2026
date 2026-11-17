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

## Exact computation
`python verify_spectrum.py` traverses all 32768 binary cube corners, computes sixteen affine barycentric integer scores per corner, solves the active-set threshold in Python `Fraction` arithmetic, checks the KKT feasibility assertions, and compares the full thirteen-shell table and nearest-face support sizes. Execution result: `SIMPLEX15_EXACT_PASS inputs=32768 shells=13 max=16 next=240`.

## Independent numerical corroboration
`python verify_secondary.py` (NumPy and SciPy required) independently forms 15-dimensional codewords and optimizes the constrained squared Euclidean objective over sixteen nonnegative mixing coefficients. Execution result: `SIMPLEX15_QP_PASS samples=37`, each squared-distance discrepancy below `1e-8`.

## Scope and limitations
The exact finite enumeration, with the analytical Gram/KKT formula, proves the reported finite spectrum. The optional numerical test does not certify all possible code lengths or identify historical priority. No independent mathematical review has been performed.
