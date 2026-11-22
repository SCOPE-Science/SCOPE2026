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

The theorem is proved by an ideal/graph parametrization, tensor-support dimension calculation, subspace-lattice Möbius inversion, and an exact central Gaussian/lift count. No finite computation is substituted for that proof.

Reproduce the direct small-field checks with `python3 verify_ideals.py`. The script enumerates row-reduced vector subspaces and multiplies each basis element against matrix-unit generators on both sides; the formula side uses independent integer Gaussian recurrences. All binary cases through ambient dimension five and all displayed ternary cases match by dimension, including the middle-size-two case. The supplied `verification_output.txt` records exact observed coefficient vectors. Predicted larger-shape values, including \((2,2,1)\), are formula evaluations only.

No independent audit has been performed, and no claims of machine-checked infinite correctness or historical uniqueness are made.
