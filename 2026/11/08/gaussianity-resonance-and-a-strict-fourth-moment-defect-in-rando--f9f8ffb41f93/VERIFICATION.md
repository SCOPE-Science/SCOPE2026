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

# Verification record

The exact-rational program `verify_random_batch.py` was executed using Python 3. It checked orthogonal-projector identities, permutation-average and pair-occupancy formulas, stability-polynomial factorization and the reflection-update identity for the nontrivial batch configurations \((N,p)=(4,2),(6,2),(6,3),(8,2),(8,4)\). It reported 504 partition cases and confirmed the rational example \(\rho=11/48\), \(v=12/37\), the fourth-defect lower bound \(24/1369\), the reflection step \(h_*=1/2\) and the stability endpoint \(h_{\max}=14/19\).

The proof in RESULT.md supplies all-size generality, the stationary perpetuity and the conditional-mixture argument. Finite enumeration is not an infinite proof. Outside the second-moment stability range no finite-second-moment invariant can exist; no conclusion is made about all possible infinite-moment stationary laws. The positive fourth-moment defect is interpreted in the extended sense if the fourth moment is infinite.
