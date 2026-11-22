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

# Verification scope

The associated script `verify_descents.py` was executed from the supplied complete file. It returned PASS for all 47 semigroups with \(2\le n\le48\), the predicted 17,296 strict descents, every actual descent position and drop size in the checked ranges, and every tested \(\nu_n\) value against the closed-form count. It uses semigroup reachability and direct ordered-pair counting, distinct from the carry-case proof.

The infinitely quantified statement relies on the written normal-form and finite-difference proof, not on the finite checker. The checker reaches past twice the conductor, but such a cutoff is not by itself an infinite proof. No independent audit or external certification was performed.
