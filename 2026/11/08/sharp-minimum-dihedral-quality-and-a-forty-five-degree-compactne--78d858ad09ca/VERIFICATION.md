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

Run `python3 check_path_tetra.py` with Python 3 using only its standard library. Expected deterministic output: `PATH_TETRA_DIHEDRAL_CHECKS_OK 9506`.

The program calculates all six dihedral angles directly from outward oriented face normals and compares them to the stated three-angle formula over 2500 positive triples; it separately checks the exact quality-feasibility predicate, the golden-ratio maximizing shape, and the coordinate bounds and sharpness constructions. The numerical tests use deterministic seeds and tolerances, and are finite corroboration only. All-parameter correctness follows from the independent analytic argument in `RESULT.md`.

The source was first posted 2026-01-13 (arXiv:2601.08304v1). Earlier specialist priority remains provisional. No external validation is claimed.
