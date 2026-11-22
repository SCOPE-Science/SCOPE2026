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

The standalone `verify.py` uses exact finite-field arithmetic and no external Python packages. Execute `python verify.py` in the same directory as this document. It enumerates all admissible profiles and canonical two-sided ideal supports; directly enumerates all RREF subspaces of selected small incidence algebras and tests right multiplication by every matrix unit; and compares Hom dimensions with explicit linear intertwiner calculations.

Observed outputs: chain of three vertices, 14 types and 40 right ideals over F2; three-vertex root fork, 13 types and 29 right ideals over F2 and 40 over F3; four-vertex star, 35 types and 133 right ideals over F2; two disjoint two-vertex chains, 25 types and 49 right ideals over F2; chain of four, 42 types and 362 right ideals over F2. Final marker: `ROOTED_FOREST_ISO_MULTIPLICATION_CHECKS_OK`.

The proof in `RESULT.md` rather than these finite computations establishes all-field, all-rooted-forest universality. No assertion is made for posets with merging branches. Historical priority and independent mathematical audit remain unverified.
