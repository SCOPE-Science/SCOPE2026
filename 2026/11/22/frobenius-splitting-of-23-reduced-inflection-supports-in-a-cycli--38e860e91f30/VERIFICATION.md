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

The uniform theorem is proved by the homogeneous Hessian identity, the cubic discriminant and resultant identities, and the splitting behavior of cubic roots over finite fields. The standalone `verify_flex.py` uses exact finite-field polynomial division and separate direct curve-Hessian enumeration for \(r=3,4\) over the first three extensions of \(\mathbb F_7\).

Execute `python verify_flex.py` with a standard Python 3 interpreter. The output must be `CYCLIC_SIX_QUARTIC_FLEX_FROBENIUS_VERIFIED`. This tests finite instances and the \(\mathbb F_7\) table, not an infinite range. Excluded boundary parameters and independent mathematical auditing remain unverified here.
