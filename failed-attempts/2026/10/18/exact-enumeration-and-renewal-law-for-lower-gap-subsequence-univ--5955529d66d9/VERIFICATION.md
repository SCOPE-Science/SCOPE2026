---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the shortest full-alphabet prefix ending at r, its last letter has no earlier occurrence. Patterns beginning with that letter force their remaining positions into the suffix starting at r+g+1; conversely every first letter can be chosen at or before r and joined to a suffix embedding. Iteration, with no spacer after the kth required arch, proves the unique decomposition, including words with more than k arches. It makes spacer deletion and insertion mutually inverse with q^(g(k-1)) choices. Enumerating successive first arrivals gives arch series A_q. Multiplication gives the cumulative series; subtracting consecutive cumulative series yields the exact-index law, including the empty word. The coefficient one above minimum is obtained by extending exactly one arch or the arbitrary tail by one letter. On an i.i.d. uniform source, stopping at each arch and skipping a deterministic g letters leaves fresh i.i.d. input. Thus completion times are sums of independent coupon-collector lengths plus g(k-1), and inverse strong law gives the stated limit. The limit is for the length guaranteed for all patterns, not the achievable length of a single favored pattern.

## originality

FAIL

A distinct indexed theorem gives the same positive-minimum-spacing arch classification and full exact-index law for the same alphabet and all parameters. The additional bijection, one-extra-position count, and renewal limit follow directly from its proof and formula. Its catalogue date is later than the frozen source date; this establishes coverage, not priority or dependence.

## value

FAIL

The fixed-gap tractability and exact index law would be useful as mathematical content, but the matching record already gives its complete structural route. The remaining refinements are direct consequences of that route and do not establish a separate worthwhile invariant or mechanism. No distinct repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
