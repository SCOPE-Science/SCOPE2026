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
The proof is analytical and uses exact identities in the rotated coordinates. The standalone `verify.py` requires Python with NumPy, SciPy, and SymPy. It tests symbolic radial and Jacobian formulas, neutrality of the first integral, 27 exact-versus-quadrature Floquet comparisons, two original-flow monodromy matrices, and four neutral near-circle returns. The script's finite tests are corroboration, not an infinite proof. In particular, the all-parameter regular first integral follows from the analytic removable-singularity argument in the proof, not from numerical orbit closure.
