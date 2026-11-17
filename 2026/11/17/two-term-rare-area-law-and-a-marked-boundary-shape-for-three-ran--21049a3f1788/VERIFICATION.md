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

# Verification notes

The proof is self-contained in `RESULT.md`. Run `python verify.py` with a standard Python 3 interpreter from the extracted package. It checks the exact rational beta-integral coefficient, tests the trigonometric determinant identity for 1,500 independently generated triples of unit normals, and uses 90,000 importance samples at each of two cutoff values to corroborate the rare-tail density ratio. The expected string is `SPHERICAL_MAX_CELL_MARKED_TAIL_CHECKS_OK`. These finite random tests are not an infinite proof, and the total-variation rate comes from the uniform analytic expansion, not from the tests.

The original mathematical references state stronger general distributions but do not independently certify this endpoint consequence. Independent expert verification and historical priority review have not been performed.
