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

# Reproducible finite verification

Run `python3 check_grid46_homology.py` in a Python 3 environment. There are no nonstandard dependencies. The script reconstructs 38 square-grid edges and all 281 perfect-matching facets, deduplicates every nonempty subface, constructs the complete finite acyclic face matching, verifies the directed Hasse graph has all 511,338 faces in its topological sort, and calculates exact signed Morse differentials over the integers. It asserts 255,663 matched pairs, the exact critical-cell distribution and both displayed integer matrices. The actual included source ran to completion and satisfied all assertions.

The computation is a finite exhaustive certificate, not a general-grid theorem. Signed integral boundary calculations, not finite-field ranks alone, establish torsion-freeness. The proof invokes standard acyclic discrete Morse theory to identify a homotopy-equivalent CW complex; it does not conclude the existence of a wedge decomposition from the zero degree-five boundary.
