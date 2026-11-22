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

The script `verify_weighted_bras.py` runs with the Python standard library. It independently assembles two consistent P1 local mass blocks and their exact inverses; for a fixed deterministic family of 956 positive rational mesh and weighting ratios, it checks exact matrix entries, the trace, determinant, and the second characteristic-polynomial coefficient against the predicted eigenvalues, plus the Jacobi comparator and the minimizer identity. Running `python verify_weighted_bras.py` returned `PASS: 8618 exact-rational identities; independent two-cell local assembly`.

The finite checks do not certify statements for all positive real ratios or all real exponents; those are proved by the rank-one Gram identity and exact asymptotic algebra in RESULT.md. This is not a floating-point error bound, and no independent mathematical audit has been performed.
