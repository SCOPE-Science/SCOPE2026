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

Reconstruct the map in `RESULT.md` from its stated incremental-slope hypotheses and verify the two separate cases proving ordered-coordinate preservation. Substitute the ordered image twice to obtain the exact maximum-norm two-step identity. Confirm the inequalities \(h(y)+h(|y-h(x)|)\ge a(y+|y-h(x)|)\ge a h(x)\ge a^2x\) before iterating. Check the linear extremizer with exact rational arithmetic and the finite-iterate softplus small-state scaling, where the latter follows from \(h_*(t)=t/2+O(t^2)\).

The embedded `checker.py` uses only Python's standard library and can be executed with `python3 checker.py`; it supplies 126000 floating point finite-horizon checks, 70 exact rational equalities, and nine small-amplitude softplus comparisons. It is deliberately non-certifying: finite comparisons cannot prove a universal theorem, and their numerical tolerance does not change the analytic bounds. No independent audit has been performed.
