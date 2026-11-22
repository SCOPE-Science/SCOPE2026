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

# Reproducibility and verified scope

The package includes a pure Python 3 standard-library script, `verify.py`. Run `python3 verify.py`; successful completion ends with `VERIFY_OK`. The checker uses independent matching enumeration, exact integer column-lattice reduction, Bareiss determinants and gcds of minors rather than floating-point Smith calculations.

It verified the theorem on all 772 labelled connected simple graphs through five vertices and enumerated all 306 labelled partial Steiner triple systems through six vertices. For each of the latter it formed the leave, computed the exact Gram-lattice Smith factors and checked the connected-case formula when applicable; for bases of at most four vertices it also constructed the full finite monomer-overlap matrix and compared its exact Smith factors. The named \(K_{3,3}\) and \(K_{1,7}\) examples were explicitly checked, including 34 and eight labelled extension diagrams, respectively.

The all-parameter theorem relies on the separate integral proof in RESULT.md; exhaustive tests through finite bounds alone cannot establish it. The matrix is a vacancy-overlap kernel, not a simultaneous two-point realization matrix, and neither existence of a universal homogeneous partial-Steiner relational structure nor full historical priority is asserted.
