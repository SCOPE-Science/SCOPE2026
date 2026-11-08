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

From this directory run `python3 verify.py`. The checker needs only the Python 3 standard library. Actual replay returned `VERIFY_OK 75 exact assertions; exhaustive matchings through seven chords; polynomial integrals exact`.

It independently enumerates all unlabelled perfect matchings on \(2n\) points for \(2\le n\le7\), builds the three two-chord pair counts from the endpoint order, checks exact first and second moments, and performs rational polynomial integration of the anchor-chord projections.

Analytic all-size proof: the iid chord representation, exact projection integrals and independent or shared-label indicator decomposition yield finite mixed moments. The standard iid multivariate CLT and bounded degenerate-kernel remainder give joint Gaussian independence. Enumeration is finite corroboration only; no independent audit or external certification has been performed. Literature priority remains a separate limitation.
