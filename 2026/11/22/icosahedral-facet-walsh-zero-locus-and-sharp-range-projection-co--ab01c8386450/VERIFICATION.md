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

## Reproducible checks

Use `python3 verify.py` with Python 3.8+ and no additional dependencies. The checker derives the icosahedral facets from the pentagonal construction and separately as all triangles of an independently built graph. It checks vertex and edge incidence counts, each of the \(4096\) direct signed face sums, every value of the structural \(20-10|S|+8(e-t)\) formula, and the separate complete Walsh–Hadamard transform.

The checker verifies the six-set zero-count table \((72,260,180,120,80,12)\), the \(796\) total zeros, the complete signed eigenvalue histogram, the exact spectral gap \(2\), and the rank \(3300\). It then computes the integer projection-kernel histogram, verifies that the transform restores the frequency projection mask, and checks \(\sum_x|4096p(x)|=56232\), yielding \(7029/512\). These are exhaustive exact-integer checks for the stated finite object, not random tests or extrapolation.

## Limits

The script itself does not verify external bibliographic priority or an infinite family; the symbolic proof of projection optimality is given in `RESULT.md`. Independent audit: not performed.
