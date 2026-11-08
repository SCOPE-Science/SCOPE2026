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

# Verification instructions and limits

Run `python3 check.py` beside the other files. The standalone script uses only the Python standard library. It must print `CHECK_OK 204` and the two explanatory lines if its 204 finite checks succeed.

Verified exactly: low-degree rational Legendre recurrences, odd/even reflection, strict finite-degree mirror amplification, and polynomial integral norm identities. Verified numerically: exterior asymptotic coefficient ratios and midpoint discretization; checked one deterministic-seed Gaussian bulk-concentration instance. The probability limit is not established by these finite tests; its proof is the explicit midpoint discrepancy/variance calculation and classical exterior asymptotics in RESULT.md.

Scope restrictions: \(0<a<b<c\), one fixed outlier, midpoint-spaced deterministic bulk, isotropic independent Gaussian starting coordinates, exact Legendre residuals, and \(d_n/n^4\to\infty\). Historical precedence is qualified in REVIEW.md; no independent audit is claimed.
