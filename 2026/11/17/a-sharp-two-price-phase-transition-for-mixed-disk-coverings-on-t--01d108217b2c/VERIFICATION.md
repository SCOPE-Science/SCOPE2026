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

## Reproduction

Run `python3 checker.py` with Python 3.9 or newer; no third-party packages are required. A successful run prints `TWO_RADIUS_TRIANGULAR_WEIGHTED_COVERING_OK`.

The checker independently determines distances to type-B sites in a finite lattice patch, validates the six-vertex reduction on random points of a hexagon, tests coverage and near-sharp geometric witnesses, and compares branch optima with an unconstrained grid minimization of the full profile. The finite tests do not establish plane-wide coverage or the uniqueness assertions; those follow from the geometric and derivative calculations in the proof.

## Mathematical validation boundaries

The verification is a self-review of algebra, geometry, limit cases, and actual code execution. No independent audit, peer review, or formal mathematical certificate has been performed. The price theorem applies only to the specified fixed periodic design with positive price and squared-radius expense.
