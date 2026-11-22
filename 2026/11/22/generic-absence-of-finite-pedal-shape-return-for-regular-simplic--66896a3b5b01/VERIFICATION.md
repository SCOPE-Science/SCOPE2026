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

The analytical proof, not a finite computation, establishes the universal dimensions and infinitely many iterate counts. It uses an explicit perpendicular-foot calculation, exact invariance of a two-variable positive domain, a symbolic Jacobian, the algebraic-integer root-of-unity obstruction, and real-analytic isolated zeros.

Run `python3 verify.py` in this directory with Python 3 and no additional packages. It checks exact rational fixed points and Jacobians in dimensions 2 through 15, matrix-power identities through 25 positive iterates, and the published dimension-three fourth-iterate squared-edge ratio \(57/121\). An observed run returned `PASS: 411 exact arithmetic checks; benchmark 57/121`.

The finite checker cannot certify all dimensions, all positive iterate counts, or originality. The main proof supplies the infinite argument. The statement concerns projections onto full supporting hyperplanes, which need not always be points of the bounded facets. Independent verification has not occurred.
