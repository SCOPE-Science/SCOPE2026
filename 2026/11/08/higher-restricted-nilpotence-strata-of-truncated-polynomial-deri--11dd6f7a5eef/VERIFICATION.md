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
# Verification of higher restricted-nilpotence strata

Run `python3 verify_derivation_height.py` from the directory containing the file. Compare its stdout byte-for-byte with `verify_derivation_height.log`; the last line is `DERIVATION_RESTRICTED_HEIGHT_DIRECT_MATRIX_CHECKS_OK`. It builds the original coefficient derivation matrices over \(\mathbb F_2\) and \(\mathbb F_4\) (irreducible polynomial \(z^2+z+1\) for the latter), raises those matrices to restricted powers by matrix multiplication, and calculates ranks through field Gaussian elimination. The exhaustive parameters are \(2\leq n\leq11\) over \(\mathbb F_2\), \(2\leq n\leq6\) over \(\mathbb F_4\), and heights \(2,4,8,16\). Additional direct checks enumerate all binary coordinate pairs for \(1\leq m\leq8\), heights \(4,8\), to test the proposed component cover against the original power equations.

These are exactly reproducible finite computations; the all-fields and all-dimensions claims rest on the written algebraic proof. Neither a finite search nor an absence of a contradictory sample establishes historical originality. The independent audit has not been performed.
