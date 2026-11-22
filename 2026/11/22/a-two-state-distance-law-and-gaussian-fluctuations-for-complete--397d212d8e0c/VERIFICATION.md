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

# Verification details

Run \(`python3 verify.py`\) using Python 3 and only standard-library modules. The checker independently enumerates all path incidence edge sets and unordered edge symmetric differences for all \(\(4^m\)\) ordered vertex pairs with \(0\le m\le7\), and compares exact integer coefficient counts against the transfer recurrence. It verifies the first moment in rational arithmetic and the total mass \(\(4^m\)\); additional transfer computations check means through \(m=40\).

The checker printed `CRY_PATH_DISTANCE_EXACT_PASS m=0..7 exhaustive and m<=40 polynomial checks`. No stochastic simulation was treated as a proof. The general coefficient identity follows from the state-dependent shared-edge rule; the normal limit follows from the explicit analytic leading eigenvalue and spectral gap. These infinite arguments are mathematical proofs, not finite certificates.

Independent mathematical audit is not performed; the recorded review is same-model only. Historical uniqueness is not certified.
