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
The formula \(S(t)=sG(A(t))\), exact prevalence identity and peak equation are derived in RESULT.md from compartment conservation; they are not inferred from simulations. The peak-location error is proved from least-positive-exponential dominance. The integral comparison uses \(H_R\ge i>0\) up to the peak; the asymptotic tail is exponentially integrable. The limiting constant is therefore well defined and the displayed asymptotic is proven under finite support.

`check_peak.py` independently performs selected high-precision numerical quadrature and root calculations for the same explicit equations, including high-transmission approximation errors and a finite-transmission timing ordering. It is a diagnostic only: even a successful run does not certify the universal theorem, its historical priority or any external review.

Independent review and independent validation have not been performed.
