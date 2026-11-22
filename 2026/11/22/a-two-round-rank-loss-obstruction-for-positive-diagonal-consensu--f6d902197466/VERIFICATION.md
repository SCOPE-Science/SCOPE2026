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
The universal lower bound is established in RESULT.md by an explicit, nonzero left-null/right-null pairing and a rank-drop counting argument, with no computational assumptions. Running `python3 verify_star.py` uses only Python's standard library and rational arithmetic. It proves directly for the supplied three matrices that their product is the rank-one average-consensus matrix and checks the transversality formulas on 25 singular-factor pairs. These illustrative checks do not certify all dimensions or replace the proof.

Scientific limitations: nonnegative row-stochastic factors; positive diagonals; bidirectional star support; exact linear matrix products; no achievability for stars with more than two leaves. Independent audit is unperformed.
