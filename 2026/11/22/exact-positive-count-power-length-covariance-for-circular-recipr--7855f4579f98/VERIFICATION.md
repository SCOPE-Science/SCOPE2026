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

# Verification notes

Run the adjacent `verify.py` with Python 3 and no third-party libraries. The checker independently enumerates every circular rank arrangement for \(n=5,6,7,8\), conditions on exponential order statistics and uses the independent-exponential-increment identity to compute exact integer-power conditional moments. It verifies 69 exact rational equalities for count means, weighted-length means, and mixed covariances at powers \(\alpha=0,1,2,3\), along with five half-plane integration identities and specializations.

The claim for all real \(\alpha>0\) and every \(n\ge5\) is proved by the explicit exponential mixed-moment integral and gamma–Dirichlet independence in `RESULT.md`; exhaustive finite ranks cannot replace this proof. Numerical experiments are not needed. The checker does not verify prior-work novelty and does not confer independent certification. Source-access and historical-priority limitations are described in `REVIEW.md` and `AUDIT.json`.
