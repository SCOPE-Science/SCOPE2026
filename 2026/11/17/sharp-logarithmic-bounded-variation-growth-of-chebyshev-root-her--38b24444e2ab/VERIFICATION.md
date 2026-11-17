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

The claim is an asymptotic theorem about real bounded-variation functions for all integers \(n\ge2\), with a proof by exact polynomial zero counting and angular kernel estimates. Its leading constant is \(4/\pi^2\); the additive \(O(1)\) is uniform in degree.

Checks carried out: direct derivation of the positive Hermite–Fejér cardinal functions, step-data decomposition, exact number of nodal and interstitial derivative zeros, uniformly summable endpoint-reflection corrections, and harmonic-sum estimates for both the upper and lower bounds. The program `checker.py` was run on the contents of this package; it verified low-degree cardinal identities, partition of unity, and finite-degree variation calculations.

Finite tests are corroborative, not a proof of the asymptotic claim. No exact finite-degree formula or central-step extremizer at every degree is asserted. Historical priority has not been independently certified.
