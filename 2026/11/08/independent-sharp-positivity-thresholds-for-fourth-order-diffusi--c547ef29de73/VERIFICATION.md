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

The exact-rational standalone `verify.py` ran successfully from extracted package contents and printed `VERIFY_OK exact matrix instances: 3636`. It computes matrix rational functions by independent rational linear algebra, compares all off-diagonal entries to the displayed formulas, checks the stochastic row sums and strict positive diagonal, and checks positive signs at permitted parameter values for finite test families.

Proof scope is infinite over every finite block profile, real \(b>0\), real \(a_i\ge0\), and all \(h\ge0\). The projector argument and quadratic sign analysis in `RESULT.md`, not finite enumeration, prove these quantified conclusions. The one-positive-root statement follows from the polynomial coefficient signs; all singular and coincident eigenvalue cases are handled by orthogonal projectors. No independent assessment is asserted.
