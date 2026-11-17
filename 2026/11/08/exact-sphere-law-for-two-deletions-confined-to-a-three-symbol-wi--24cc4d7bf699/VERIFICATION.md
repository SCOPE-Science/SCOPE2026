---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For exact deletion of i<j with j-i<=2, adjacent-pair output A_i matches A_(i+1) precisely when x_i=x_(i+2); equivalence classes form path components. A skipped-middle pair D_i contributes a genuinely new output precisely when x_(i+1) differs from both neighbors, and those new D_i outputs are distinct. Their indicator difference is +1 on all-distinct triples, -1 on equal triples, zero otherwise, proving B(x)=n-1+sum d. Ordered-pair transfer gives the all-n enumerator; extrema follow from forbidden equal triples or proper 3-color walks. Stationary two-dependent triple scores have covariance gamma0=(q-1)(3q^2-5q+1)/q^4, gamma1=(q-1)^3/q^4, gamma2=0, giving the finite variance and positive-variance m-dependent CLT. Independent direct enumerations for q=2,3 and n=3..7 confirmed volumes and rational variances.

## originality

PASS

The exact center-dependent three-window two-deletion sphere volume, full distribution/variance, extrema and CLT are not furnished by the closely related available localized-deletion correction-code constructions. A 2025 primary article full relevant text was inspected; 2026 successor full text unavailable and residual risk retained. Unrestricted two-deletion sphere laws concern a different deletion channel.

## value

PASS

Exact deletion-output neighborhoods are natural coding-theoretic combinatorial invariants; the local identity and complete alphabet-uniform sphere law provide useful finite counts and fluctuations for localized channels. This is a genuinely motivated classification, not an arbitrary small-length experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
