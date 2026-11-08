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

All parameter and endpoint inequalities are written in `RESULT.md`. The two affine-iterate identities and the survivor threshold inequalities constitute the proof for all real admissible parameters. The exact-rational checker `capture_checker.py` independently verifies sample branch regimes, strict admissibility of each test tuple, and the singular family tail for six values, and returned `PIECEWISE_AFFINE_CAPTURE_RATIONAL_CHECKS_OK 431`.

The checker uses finite input grids for supplementary trajectory comparisons and exact rational evaluation of formula identities. The proof, not the grid, establishes the continuum result. First-entry distributions count all starts in the half-open domain under normalized Lebesgue measure. Independently authored or third-party mathematical audit has not been performed.
