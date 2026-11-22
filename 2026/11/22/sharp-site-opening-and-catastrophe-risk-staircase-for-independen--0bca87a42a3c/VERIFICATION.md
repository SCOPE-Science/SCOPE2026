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

The analytic claim follows from the exact Poisson thinning identity, the strict concavity of \(g_c\), strict concavity of the continuously relaxed integer score, and the monotone likelihood-ratio comparison of the integrand \(v_r\). The proof includes all strict equality and endpoint arguments. Numerical tests only diagnose, and do not establish, these universal claims.

Run `python3 check_founder.py`. It uses Python 3 standard library only, does not access the network or proprietary services, and explicitly enumerates all admissible integer counts in finite examples. A successful diagnostic printout is not an independent mathematical audit. Large budgets and nearly degenerate site risks can incur floating-point conditioning limitations.

The independent audit status remains `not_performed`.
