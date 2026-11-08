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

The exact claim is established analytically in RESULT.md, Sections A–E. The standalone `verify.py` (Python standard library, fixed random seed) was executed from its actual package source path before embedding; observed output: `VERIFY_OK equilateral_fraction=7-4sqrt3 right_3_4_5=65/864 random_interior_centers= 5261`. It checks exact special values, angle feasibility, direct quadratic circle-segment root counts, and every radius chamber determined by vertex and perpendicular-foot distances for the 5261 sampled centers. This is finite corroboration, not the proof for all triangles. The strict endpoint assertions follow from the proof, not floating-point tests.

The full journal article of Bárány and Roldán-Pensado and full public regular-polygon RESULT.md were inspected for overlap. The closely related minimax triangle classification was checked at the retrieved summary level only. Historical novelty is provisional and not independently certified.
